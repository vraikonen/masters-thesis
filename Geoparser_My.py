import pandas as pd
import torch
import torch.nn.functional as F
import logging
# from transformers import BertTokenizer, BertForTokenClassification
from geopy.geocoders import Nominatim 
from utils.text_editing import edit_text
import time
import spacy
import os
import sys

from utils.logging import logging_parser, custom_exception_hook



class Geoparser:
    def __init__(self,df, spacy_model, text_column, output_path_ler = None, output_path_geocode = None):
        self.df = df
        self.text_column = text_column
        self.output_path_ler = output_path_ler
        self.output_path_geocode = output_path_geocode
        self.geolocator = Nominatim(user_agent="geo_coder")
        self.nlp = spacy.load(spacy_model)

    def preprocess_data(self):
        # Edit text 
        self.df['edited_text'] = self.df[self.text_column].apply(lambda x: edit_text(str(x), stoplist=[], min_length_word=0, remove_links=True, remove_user_names=True, remove_emojis=True, letters_only=True))

    def extract_locations(self, text):
        # Function to extract location entities from text using spaCy
        doc = self.nlp(text)
        entities = doc.ents
        locations = []
        locations1 = []
        locations2 = []
        locations3 = []
        for entity in entities:
            if entity.label_ == 'GPE':
                locations.append(entity.text)
            if entity.label_ == 'FAC':
                locations1.append(entity.text)
            if entity.label_ == 'LOC':
                locations2.append(entity.text)
            if entity.label_ == 'ORG':
                locations3.append(entity.text)
        return pd.Series((locations, locations1, locations2, locations3), index=['GPE', 'FAC', 'LOC', 'ORG'])
    
    
    def combine_values(self, row):
        # Helper function to combine location values into a single string
        order = ['FAC', 'LOC', 'GPE', 'ORG']
        combined_values = [row[col] for col in order if row[col]]
        return ', '.join(combined_values)
    
    def process_data(self):
        if "edited_text" in self.df.columns and self.df["edited_text"].any():
            pass
        else:
            self.preprocess_data()
            
        if "locations" in self.df.columns and self.df["locations"].any():
            pass
        
        else:
            # Extract location 
            self.df['edited_text'] = self.df['edited_text'].fillna('')

            self.df[['GPE', 'FAC', 'LOC', 'ORG']] = self.df['edited_text'].apply(self.extract_locations)
            logging.info("LER finished")
            # Remove brackets from location columns
            columns_to_clean = ['GPE', 'FAC', 'LOC', 'ORG']
            for col in columns_to_clean:
                self.df[col] = self.df[col].astype(str).str.replace('[', '').str.replace(']', '')

            # Combine location values into a new 'locations' column, remove '
            self.df['locations'] = self.df.apply(self.combine_values, axis=1)
            self.df['locations'] = self.df['locations'].str.replace("'", '')

            # Save processed data to CSV
            if self.output_path_ler:
                self.df.to_csv(self.output_path_ler, index=False)
        
        # Directory to save intermediate results
        os.makedirs("intermediate_results", exist_ok=True)

        # Geocoding
        dict_for_locs = {}
        self.df['latitude'] = None
        self.df['longitude'] = None
        unique_loc = 0
        total_rows = 0
        row_with_loc = 0
        total_requests = 0
        for index, row in self.df.iterrows():
            total_rows +=1
            if total_rows % 100 == 0:
                logging.info(f"Total rows: {total_rows}; Rows with loc: {row_with_loc}; Total requests: {total_requests}; Unique locs: {unique_loc}")
            if total_rows % 10000 == 0:
                self.df.to_csv(f"intermediate_results/result{total_rows}.csv")
            loc = row['locations']
            if loc and loc != "nan":
                row_with_loc +=1
                if loc in dict_for_locs:
                    self.df.loc[index, 'latitude'] = dict_for_locs[loc][0]
                    self.df.loc[index, 'longitude'] = dict_for_locs[loc][1]
                else:

                    try:
                        geocoded_loc = self.geolocator.geocode(loc)
                        total_requests += 1
                        if geocoded_loc:
                            self.df.loc[index, 'latitude'] = geocoded_loc.latitude
                            self.df.loc[index, 'longitude'] = geocoded_loc.longitude
                            dict_for_locs[loc] = [geocoded_loc.latitude, geocoded_loc.longitude]
                            unique_loc += 1
                        else:
                            dict_for_locs[loc] = ['','']
                    except Exception as e:
                        logging.info(f"Error geocoding location '{loc}': {str(e)}. Let's try again...")
                        self.df.loc[index, 'latitude'] = "error"
                        self.df.loc[index, 'longitude'] = "error"
                        time.sleep(2)

        # Save processed data to CSV
        if self.output_path_geocode:
            self.df.to_csv(self.output_path_geocode, index=False)

        return self.df

if __name__ == "__main__":


    path_to_csv = "dataset.csv" # Link to csv file with all the posts
    output_path = "geoparsed.csv" # Save final geoparsed output
    text_column = "text"
    output_path_ler = "ler.csv" # Save spaCy output
    output_path_geocode = "geocoded.csv" # Save geocoded = save geoparsed
    spacy_model = "en_core_web_lg"

    logging_parser()
    sys.excepthook = custom_exception_hook
    # Geoparse
    df = pd.read_csv(path_to_csv, dtype={"id":str}) # TODO Change this
    Geoparser = Geoparser(df, spacy_model, text_column, output_path_ler, output_path_geocode)
    processed_df = Geoparser.process_data()

    print(processed_df.head())
    logging.info("Finished!")
    processed_df.to_csv(output_path)
