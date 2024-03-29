import numpy as np
import pandas as pd
import spacy
import re
import nltk
import spacy
import string
pd.options.mode.chained_assignment = None

from textblob import TextBlob
nlp = spacy.load('en_core_web_md')

# Import the data
amazon = pd.read_csv("amazon_product_reviews.csv")
df = amazon[["reviews.text"]]
df["reviews.text"] = df["reviews.text"].astype(str)

df["text_lower"] = df["reviews.text"].str.lower()
#df.head()

#Remove punctuation

PUNCT_TO_REMOVE = string.punctuation
def remove_punctuation(text):
    #custom function to remove the punctuation
    return text.translate(str.maketrans('', '', PUNCT_TO_REMOVE))

df["text_wo_punct"] = df["text_lower"].apply(lambda text: remove_punctuation(text))
#df.head()

from nltk.corpus import stopwords
", ".join(stopwords.words('english'))

# Remove stopwords
STOPWORDS = set(stopwords.words('english'))
def remove_stopwords(text):
    """custom function to remove the stopwords"""
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])

df["text_wo_stop"] = df["text_wo_punct"].apply(lambda text: remove_stopwords(text))
#df.head()

text = df["text_wo_stop"]
#text

text.isnull().sum()

# Remove upper cases; removes any leading, and trailing whitespaces; remove stop wards and punctuation
nlp = spacy.load('en_core_web_md')
def preprocess(text):
  doc = nlp(text)
  #doc = nlp.pipe(text, n_process=4, batch_size=3)[0] does not work
  processed = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
  print(processed)
  return ' '.join(processed)

text.apply(preprocess)

data = text.values
#data

def analyze_polarity(data):
# Preprocess the text with spaCy
    doc = nlp(data)
    # nlp.pipe(data, n_process=4, batch_size=3)[0] does not work

  # Analyze sentiment with TextBlob
    blob = TextBlob(data)
    polarity = blob.sentiment.polarity
    return polarity

# Create a list to store sentiments for each review
sentiments = []

for item in data:
    polarity_score = analyze_polarity(item) 

    if polarity_score > 0:
        sentiment = 'positive'
    elif polarity_score < 0:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'

    sentiments.append(sentiment)

sentiments

positive_count = sentiments.count('positive')
negative_count = sentiments.count('negative')
neutral_count = sentiments.count('neutral')

total = len(sentiments)

positive_perc = (positive_count)/total *100
negative_perc = (negative_count)/total *100
neutral_perc = (neutral_count)/total *100

print(f"Positive percentage: {positive_perc: .2f}%")
print(f"Negative percentage: {negative_perc: .2f}%")
print(f"Neutral percentage: {neutral_perc: .2f}%")

#Test the model on sample product reviews: Test the sentiment analysis function on a few sample product reviews
#to verify its accuracy in predicting sentiment.
test1 = data[2]
print(test1)
print(analyze_polarity(data[2]))
print(f"The sentiment prediction is: {sentiment}")

test2 = data[10]
print(test2)
print(analyze_polarity(data[10]))
print(f"The sentiment prediction is: {sentiment}")