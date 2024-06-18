import re
import nltk
import emoji
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
from collections import defaultdict


def edit_text(tweet, stoplist, min_length_word, remove_links=False, remove_user_names=False, remove_emojis=False, replace_diacritics=False, filter_nsfw_words=False,
              letters_only=False, stemming=False, words_to_remove=None,  language="english"):
    """A function that pre-processes the tweet text.

    Args:
        tweet (str): tweet text
        stoplist (list): list of stopwords to be erased
        min_length_word (int): minimum number of characters per word
        remove_links (bool, optional): True: removes all links (URLs) from text. Defaults to False.
        remove_user_names (bool, optional): True: removes all usernames (@) from text. Defaults to False.
        remove_emojis (bool, optional): True: removes all emojis from text. Defaults to False.
        replace_diacritics (bool, optional): True: replaces all diacritical signs (i.e. accents, umlaut, e.g. é > e). Defaults to False.
        filter_nsfw_words (bool, optional):  True: deletes all NSFW words. Defaults to False.
        letters_only (bool, optional): True: only keep letters. Defaults to False.
        stemming (bool, optional): either: False, "Porter" or "Snowball". Defaults to False.
        language (str, optional): necessary for "Snowball" stemming and NSFW filtering. Defaults to "english".
        words_to_remove (list): A list of specific words to be removed from the text. Default is None.

    Returns:
        tweet (str): edited tweet text
    """

    tweet = str(tweet).lower()
     
    if remove_links == True:
        # remove URLs
        remove_url_regex = r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b'
        tweet = re.sub(remove_url_regex,'', str(tweet))
        
    # Remove all user names in the tweet text
    if remove_user_names == True:
        tweet = re.sub("@\S+", '', str(tweet))
        
    # only keep letters
    if letters_only:
        tweet = re.sub("[^a-zA-Z]", " ", tweet)
    
    # remove emojis
    if remove_emojis == True:
        tweet = emoji.replace_emoji(tweet, replace='')
        
    # remove diacritics
    if replace_diacritics == True:
        tweet = replace_diacritical_signs(str(tweet))

    # check if in NSFW word list
    if filter_nsfw_words == True:
        nsfw_words = get_nsfw_word_list(language=language, length=min_length_word)

        # delete NSFW words
        for word in nsfw_words:
            if word in tweet:
                tweet = tweet.replace(word, "")

    # stemming
    if stemming == 'Porter':
        stemmer = PorterStemmer()
        stoplist = stemm_stoplist(stoplist, stemming, min_length_word, language)

    if stemming == 'Snowball':
        stemmer = SnowballStemmer(language)
        stoplist = stemm_stoplist(stoplist, stemming, min_length_word, language)

    if stemming:
        try:
            # tokenization (also removes special characters, e.g. %&/?)
            tweet = nltk.word_tokenize(tweet)

            # join list to string
            tweet = ' '.join([str(elem) for elem in tweet])
        except Exception as e:
            print(e)

    # Remove short words and stopwords
    tweet_words = []
    for word in tweet.split(" "):
        # stemming
        if stemming != False:
            word = stemmer.stem(word)
        else:
            pass

        # only include words longer than minimum length
        if len(word) > min_length_word:
            # check if in stoplist
            if word not in stoplist: 
                tweet_words.append(word)

            else:
                pass

        else:
            pass
    
    # Remove specific words
    if words_to_remove:
        for word in words_to_remove:
            text = text.replace(word, '')
    # join list to string
    tweet = ' '.join([str(elem) for elem in tweet_words])

    return tweet


def replace_diacritical_signs(text):
    """A function that replaces common diacritics in indo-european languages so that text remains readable

    Args:
        text (str): text to be edited (e.g. tweet)

    Returns:
        text (str): edited ted
    """

    # accent aigu (French, Spanish, Portuguese)
    text = re.sub('ó','o', str(text))
    text = re.sub('é','e', str(text))
    text = re.sub('á','a', str(text))
    text = re.sub('í','i', str(text))
    text = re.sub('ú','u', str(text))

    # accent grave (French, Catalan)
    text = re.sub('ò','o', str(text))
    text = re.sub('è','e', str(text))
    text = re.sub('à','a', str(text))
    text = re.sub('ì','i', str(text))
    text = re.sub('ù','u', str(text))

    # accent circonflexe (French)
    text = re.sub('â','a', str(text))
    text = re.sub('ê','e', str(text))
    text = re.sub('î','i', str(text))
    text = re.sub('ô','o', str(text))
    text = re.sub('û','u', str(text))

    # tilde (Portuguese)
    text = re.sub('ã','a', str(text))
    text = re.sub('õ','o', str(text))
    
    # cédille (French, Portuguese)
    text = re.sub('ç','c', str(text))
    
    # eñe (Spanish)
    text = re.sub('ñ','n', str(text))
    
    # Eszett (German)
    text = re.sub('ß','ss', str(text))
    
    # tréma (French)
    text = re.sub('ä','a', str(text))
    text = re.sub('ë','e', str(text))
    text = re.sub('ï','i', str(text))
    text = re.sub('ö','o', str(text))
    text = re.sub('ü','u', str(text))
    
    # special characters in germanic languages (e.g. Swedish)
    text = re.sub('å','a', str(text))
    text = re.sub('æ','ae', str(text))
    text = re.sub('ø','oe', str(text))
    
    # special characters in slavic languages (e.g. Czech)
    text = re.sub('ą','a', str(text))
    text = re.sub('ć','c', str(text))
    text = re.sub('č','c', str(text))
    text = re.sub('ę','e', str(text))
    text = re.sub('ě','e', str(text))
    text = re.sub('ł','l', str(text))
    text = re.sub('ň','n', str(text))
    text = re.sub('ń','n', str(text))
    text = re.sub('ř','r', str(text))
    text = re.sub('š','s', str(text))
    text = re.sub('ś','s', str(text))
    text = re.sub('ů','u', str(text))
    text = re.sub('ý','y', str(text))
    text = re.sub('ž','z', str(text))
    text = re.sub('ź','z', str(text))
    text = re.sub('ż','z', str(text))

    return str(text)


def term_frequency(df, min_frequency_words, text_column="text_edit"):
    """A function that calculates term frequency and removes rare words.

    Args:
        df (pd.DataFrame): dataframe with tweets
        min_frequency_words (int): minimum word occurrence in corpus
        text_column (str, optional): name of text column to be edited. Defaults to 'text_edit'.

    Returns:
        df: dataframe with edited text column
    """

    # get term frequency
    tweets_list = df[text_column].to_list()

    frequency = defaultdict(int)
    for tweet in tweets_list:
        for word in tweet.split(" "):
            frequency[word] += 1

    # create new column with edited text
    df[text_column] = df[text_column].apply(lambda x: remove_rare_words(x, frequency, min_frequency_words))
    
    return df


def remove_rare_words(tweet, frequency, min_frequency_words=5):
    """A function that removes word that appear less than n times in the corpus

    Args:
        tweet (str): tweet text
        frequency (int): term frequency
        min_frequency_words (_type_): minimum word occurrence in corpus. Defaults to 5.

    Returns:
        tweet (str): edited tweet text
    """

    # Remove unique words that appear only once in the dataset
    tweet_words = []
    
    for word in tweet.split(" "):
        if frequency[word] > min_frequency_words:
            tweet_words.append(word)
        else:
            pass
    
    # join list to string
    tweet = ' '.join([str(elem) for elem in tweet_words])
        
    return tweet


def create_stoplist(languages, additional_stopwords=None, text_editing=True):
    """A function that creates a list of stopwords (based on nltk package)

    Args:
        languages (list): list of languages (e.g. ['english', 'spanish'])
        additional_stopwords (list): list of customised stopwords. Defaults to None.
        text editing (bool, optional): True: replace diacritics. Defaults to True.

    Returns:
        stoplist: list of stopwords
    """

    stoplist=[]
    # add stopwords from nltk for each defined language
    for language in languages:
        stopwords = nltk.corpus.stopwords.words(language)
        stoplist.extend(stopwords)
    # add additional, customised stopwords
    if additional_stopwords:
        stoplist.extend(additional_stopwords)

    if text_editing == True:
        stoplist_edit = []
        # apply same editing on stopwords as for text data
        for word in stoplist:
            word = replace_diacritical_signs(str(word))

            if len(word) > 1:
                stoplist_edit.append(word)
            else:
                pass

        return stoplist_edit
    
    else:
        return stoplist


def stemm_stoplist(stoplist, stemming="Porter", min_length_word=3, language="english"):
    """A function that stemms the stopwords.

    Args:
        stoplist (list): list of stop words
        stemming (str): "Porter" or "Snowball". Defaults to "Porter"
        min_length_word (int): minimum number of characters per word. Defaults to 3.
        language (str, optional): only necessary for "Snowball" stemming. Defaults to "english".

    Returns:
        stoplist_stemmed: stemmed version of stoplist
    """

    if stemming == "Porter":
        stemmer = PorterStemmer()

    if stemming == "Snowball":
        stemmer = SnowballStemmer(language)

    stoplist_stemmed = []
    for word in stoplist:
        # stemming
        if stemming != False:
            word = stemmer.stem(word)
            
            if len(word) > min_length_word:
                stoplist_stemmed.append(word)
            
            else:
                pass

    stoplist_stemmed = set(stoplist_stemmed)
    return stoplist_stemmed



def get_nsfw_word_list(language='english', length=None):
    """A function that loads a list of NSFW words for further processing.

    Args:
        language (str, optional): language of NSFW list. Defaults to 'english'.
        length (_type_, optional): minimum character limit of NSFW word. Defaults to None.

    Returns:
        nsfw_words: list of NSFW words
    """
    # NSFW word lists based on: https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words
    if language == "english":
        nsfw_words = ['apeshit', 'arsehole', 'asshole', 'autoerotic', 'bareback', 'bdsm', 'big breasts', 'big tits', 'bimbos', 'bitches', 'black cock', 'blowjob', 'blow job', 'blow your load', 'bondage', 'boner', 'boob', 'boobs', 'booty call', 'bullshit', 'buttcheeks', 'butthole', 'camgirl', 'camslut', 'camwhore', 'circlejerk', 'clitoris', 'cocks', 'cumming', 'cumshot', 'cunnilingus', 'cunt', 'date rape', 'daterape', 'deep throat', 'deepthroat', 'dildo', 'doggie style', 'doggiestyle', 'doggy style', 'doggystyle', 'dominatrix', 'ejaculation', 'erotic', 'erotism', 'escort', 'faggot', 'fellatio', 'fingering', 'fisting', 'foot fetish', 'fuck', 'fucker', 'fucking', 'gangbang', 'gang bang', 'gay sex', 'genitals', 'giant cock', 'group sex', 'g-spot', 'hand job', 'handjob', 'hentai', 'homoerotic', 'horny', 'hot chick', 'humping', 'intercourse', 'jack off', 'jerk off', 'jizz', 'livesex', 'masturbate', 'masturbating', 'masturbation', 'menage a trois', 'missionary position', 'motherfucker', 'neonazi', 'nigga', 'nigger', 'nsfw', 'nympho', 'nymphomania', 'orgasm', 'orgy', 'pedophile', 'penis', 'porn', 'porno', 'pornography', 'pussy', 'raping', 'rapist', 'rectum', 'sadism', 'sexcam', 'shemale', 'sodomy', 'strap on', 'strapon', 'strip club', 'threesome', 'tits', 'titties', 'titty', 'twink', 'upskirt', 'vagina', 'viagra', 'vibrator', 'voyeur', 'vulva', 'wet dream', 'whore', 'xxx']

    elif language == "german":
        nsfw_words = ['arschficker', 'arschlecker', 'arschloch', 'bimbo', 'bratze', 'bumsen', 'dödel', 'ficken', 'fotze', 'hurensohn', 'kackbratze', 'kampflesbe', 'kanake', 'MILF', 'möpse', 'morgenlatte', 'möse', 'muschi', 'neger', 'nigger', 'nutte', 'onanieren', 'orgasmus', 'penis', 'pimmel', 'pimpern', 'poppen', 'porno', 'rosette', 'schlampe', 'scheiss', 'scheiß', 'scheiße', 'scheisser', 'schwanzlutscher', 'schwuchtel', 'strap-on', 'titten', 'vögeln', 'wichsen', 'wichser']

    else:
        raise ValueError("No NSFW word list found. Specify language as 'english' or 'german'.")
 
    # only keep words longer than n
    if length:
        nsfw_words = list(filter(lambda i: len(i) >= length, nsfw_words))

    return nsfw_words


def check_nsfw_words(text, nsfw_words):
    """
    This function checks whether a word from a list of words is included in a string.

    Parameters:
    text (str): input string
    nsfw_words (list): list of NSFW words. Output of get_nsfw_word_list()

    Returns:
    True if NSFW word is included, False otherwise.
    """
    for word in nsfw_words:
        if word in text:
            return True
    return False
