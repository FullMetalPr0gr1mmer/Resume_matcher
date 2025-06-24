'''import spacy

nlp = spacy.load("en_core_web_sm") #en_core_web_sm is a lightweight En lang processing model , works on cpu
# -> provides comprehensive nlp processing capabilities while maining a small footPrint

#lemmatization (e.g. running-> run) while stimming (changing->chang) the first gets words based on dictionary while the second depends on algos. to remove suffixes
# and may crete non-existent word .. first is accurate second is faster

#so this code runs over text and tokenize it using en core web sm returns lemmatized verision
# of tekens .. token.is_stop -> is - for -etc ... is_alpha -> words that not abbreviations nor numbers
def preprocess_text(text):
    doc=nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct and token.is_alpha]
    return " ".join(tokens) # returns a single sting of all the tokens'''
import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters

# ✅ Define temp path for nltk data
nltk_data_path = "/tmp/nltk_data"
nltk.data.path.append(nltk_data_path)

# ✅ Download if not found
if not os.path.exists(nltk_data_path):
    os.makedirs(nltk_data_path)

try:
    stop_words = set(stopwords.words("english"))
except LookupError:
    nltk.download("stopwords", download_dir=nltk_data_path)
    stop_words = set(stopwords.words("english"))

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt", download_dir=nltk_data_path)


def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)

    # Force tokenizer to use the local nltk_data path
    tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
    sentences = tokenizer.tokenize(text)
    words = []
    for sentence in sentences:
        words.extend(word_tokenize(sentence))

    words = [w for w in words if w not in stop_words]
    return " ".join(words)