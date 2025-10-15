import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define your factions and URLs
factions = {
    "Imperium of Man": "https://warhammer40k.fandom.com/wiki/Imperium_of_Man",
    "Chaos": "https://warhammer40k.fandom.com/wiki/Chaos_(Warhammer_40,000)",
    "Eldar": "https://warhammer40k.fandom.com/wiki/Aeldari",
    "Orks": "https://warhammer40k.fandom.com/wiki/Orks",
    "Tyranids": "https://warhammer40k.fandom.com/wiki/Tyranids",
    "Necrons": "https://warhammer40k.fandom.com/wiki/Necrons"
}

data = []

for faction, url in factions.items():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # Extract all paragraphs from the article body
    paragraphs = soup.select("div.mw-parser-output > p")
    text = " ".join([p.get_text() for p in paragraphs])

    data.append({"Faction": faction, "Text": text})

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("raw_lore_texts.csv", index=False)

print("Scraping complete. Data saved to data/raw_lore_texts.csv")
