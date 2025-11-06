# Sentiment Analysis with NLTK

## Project Overview
This project performs sentiment analysis on text data from Warhammer 40k's fandom page using the NLTK library's `SentiWordNet` module. The analysis calculates standardized positive, negative, and objective emotion scores for each text entry, and visualizes these results as bar graphs using Matplotlib.

## Folder Structure
- **`scripts`**: Contains Python scripts used for sentiment analysis and visualization.
- **`data`**: Holds raw and preprocessed text data files (e.g., `cleaned_lore.csv`).
- **`visualizations`**: Stores generated graph outputs showing sentiment distributions.

## Setup

### Prerequisites
- Python 3.x
- Pip package manager

### Required Python Packages
- `pandas`
- `matplotlib`
- `nltk`

To install the required packages, you can use:
```
pip install pandas matplotlib nltk
```

NLTK Setup
Ensure the necessary NLTK corpora are downloaded using the following commands within a Python environment:

```
import nltk
nltk.download('punkt')
nltk.download('sentiwordnet')
nltk.download('wordnet')
nltk.download('omw-1.4')
```
