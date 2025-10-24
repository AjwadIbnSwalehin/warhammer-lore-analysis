import pandas as pd
from nltk.corpus import sentiwordnet as swn
from nltk.tokenize import word_tokenize
import nltk
import matplotlib.pyplot as plt

# Download necessary NLTK data files
# nltk.download('sentiwordnet')
# nltk.download('punkt')
# nltk.download('punkt_tab')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

# Assuming df is your DataFrame with a 'Text' column
df = pd.read_csv('data/cleaned_lore.csv')  # Your cleaned text

def analyse_text_emotion(text):
    tokens = word_tokenize(text)
    # Check word count
    word_count = 0

    # Iterate over each token in the tokens list
    for token in tokens:
        # Check if the token consists only of alphabetic characters
        if token.isalpha():
            # Increment the counter for each alphabetic token
            word_count += 1
    emotions = {'standard_positive_emotion': 0, 'standard_negative_emotion': 0, 'standard_objective_emotion': 0}
    for word in tokens:
        synsets = list(swn.senti_synsets(word)) # Finds emotions
        if synsets:
            sentiment = synsets[0]
            emotions['standard_positive_emotion'] += (sentiment.pos_score() / word_count) # Dividing by word count to standardise it
            emotions['standard_negative_emotion'] += (sentiment.neg_score() / word_count)
            emotions['standard_objective_emotion'] += (sentiment.obj_score() / word_count)
    return emotions

df['emotion'] = df['Text'].apply(analyse_text_emotion)
# print(df['emotion'])

fig, ax = plt.subplots(figsize = (12, 6))

bar_width = 0.25
index = range(len(df))
entry_labels = df['Faction']
print(entry_labels)

# Extract data for plotting
positive_emotions = [entry['standard_positive_emotion'] for entry in df['emotion']]
negative_emotions = [entry['standard_negative_emotion'] for entry in df['emotion']]
objective_emotions = [entry['standard_objective_emotion'] for entry in df['emotion']]

ax.bar(index, positive_emotions, bar_width, label='Positive', color="green")
ax.bar([i + bar_width for i in index], negative_emotions, bar_width, label='Negative', color='red')
ax.bar([i + 2 * bar_width for i in index], objective_emotions, bar_width, label='Objective', color='blue')

# Setup plot settings
ax.set_xlabel('Faction')
ax.set_ylabel('Standardised Sentiment')
ax.set_xticklabels(entry_labels)
ax.set_title('Emotion Distribution per Text Entry')
ax.set_xticks([i + bar_width for i in index])
ax.legend(title='Emotion Type')
plt.savefig('emotional_analysis.png')

plt.show()