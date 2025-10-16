import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

df = pd.read_csv("data/raw_lore_texts.csv")

def clean_text(text):
    # if text is missing or not a string, return empty string
    if not isinstance(text, str):
        return ""
    
    text = re.sub(r'\[.*?\]', '', text)      # remove references like [1]
    text = re.sub(r'[^A-Za-z\s]', '', text)  # remove punctuation/numbers
    text = text.lower()                      # lowercase
    words = [w for w in text.split() if w not in stop_words]
    return " ".join(words)

df["Cleaned_Text"] = df["Text"].apply(clean_text)
df.to_csv("cleaned_lore.csv", index=False)
