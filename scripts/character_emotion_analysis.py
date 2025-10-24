from faction_emotion_analysis import analyse_text_emotion
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/cleaned_character_data.csv')

df['emotion'] = df['Text'].apply(analyse_text_emotion)

fig, ax = plt.subplots(figsize = (12, 6))

bar_width = 0.25
index = range(len(df))
entry_labels = df['Title']

# Extract data for plotting
positive_emotions = [entry['standard_positive_emotion'] for entry in df['emotion']]
negative_emotions = [entry['standard_negative_emotion'] for entry in df['emotion']]
objective_emotions = [entry['standard_objective_emotion'] for entry in df['emotion']]

ax.bar(index, positive_emotions, bar_width, label='Positive', color="green")
ax.bar([i + bar_width for i in index], negative_emotions, bar_width, label='Negative', color='red')
ax.bar([i + 2 * bar_width for i in index], objective_emotions, bar_width, label='Objective', color='blue')

# Setup plot settings
ax.set_xlabel('Character')
ax.set_ylabel('Standardised Sentiment')
ax.set_xticklabels(entry_labels)
ax.set_title('Emotion Distribution per Text Entry')
ax.set_xticks([i + bar_width for i in index])
ax.legend(title='Emotion Type')
plt.savefig('visualisations/character_emotion_visualisation.png')

plt.show()