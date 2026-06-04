import spacy
import nltk
from nltk.tokenize import word_tokenize
from textblob import TextBlob

# pip install spacy nltk
# python -m spacy download en_core_web_sm
# pip install textblob


def nlp_spacy():
    nlp = spacy.load('en_core_web_sm')
    text = "Hello! How are you? I hope all is great"
    doc = nlp(text)
    for token in doc:
        print(token.text)

def nlp_():
    text = "Hello! How are you? I hope all is great"
    tokens = word_tokenize(text)
    print(tokens)


def nlp_exercise():
    nlp = spacy.load('en_core_web_sm')
    feedback = ["Product amazing, I'm really happy with the quality",
                "Terrible service, I will never buy from here again",
                "The delivery was on time, and the product is ok"]
    for text in feedback:
        doc = nlp(text.lower())
        tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
        print(f"Tokens: {tokens}")
