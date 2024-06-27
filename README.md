# Cross-platform comparison of social media data in natural disaster management

This repository contains a geoparsed cross-platform social media dataset created for my thesis. It includes a Python class for geoparsing and notebooks with detailed analysis.

## Link to thesis
The full thesis is available [here](link_to_thesis).

## Data Availability Statement

The datasets included in this repository within `dataset` folder are:
1. Boundaries for different administrative levels

    1.1 Florida boundary - [source](https://www.esri.com/)

    1.2 Counties - [source](https://www.esri.com/)

    1.3 County subdivisions - [source](https://www.census.gov/) 

    1.4 Census tracts - [source](https://www.atsdr.cdc.gov/)

2. Geoparsed posts - without any reference to the original posts, as some platforms prohibit sharing retrieved posts publicly.


Query parameters available [here](link_to_thesis), and respective crawlers: [Telegram Crawler](https://github.com/vraikonen/telegram-crawler), [Reddit Crawler](https://github.com/vraikonen/reddit-crawler), [Tiktok Crawler](https://github.com/vraikonen/tiktok-crawler) and [Mastodon Crawler](https://github.com/vraikonen/mastodon-crawler). Twitter dataset was obtained by querying private Twitter archive obtained via Twitter Streaming API and owned by [Geosocial Analytics Lab](https://geosocial.at/). 


**__Note:__** Due to privacy and ethical considerations, the raw data from social media cannot be shared publicly. However, anonymized datasets or post IDs used in the analysis can be provided in accordance with the terms and conditions specific for each of the social media platforms.


## Code

### Geoparser class 

A class to extract and geocode location entities using spaCy and Nominatim from social media posts.

### Notebook 1: 1_geoparse_timeseries
A notebook with geoparsing indices and time series of filtered and geoparsed posts.

### Notebook 2: 2_distance_based 
A notebook with code to calcualte Pariwise Distances ECDF, Ripley's K function and Monte Carlo simulation for nearest neighbor analysis.

### Notebook 3: 3_distribution_clustering 
A notebook with code to calculate Pearson's r, KDE, SDE and ECDF of x and y coordinates. 

### Notebook 4: query_database 
A notebook with querying database and text editing separately for each dataset.

### Notebook 5: tiktok_comments
A notebook exploring comment counts of TikTok posts. 




