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
import re

# Basic list of English stopwords (you can add more if needed)
stop_words = set([
    "the", "and", "is", "in", "it", "of", "to", "a", "for", "on", "with",
    "this", "that", "as", "an", "by", "be", "are", "from", "at", "or", "was",
    "i", "you", "your", "we", "our", "they", "their", "but", "have", "has"
])

def preprocess_text(text):
    # Lowercase + remove punctuation
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)

    # Basic whitespace tokenization
    words = text.split()

    # Remove stopwords
    words = [word for word in words if word not in stop_words]

    return " ".join(words)