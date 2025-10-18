import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define your factions and URLs
factions = {
    "Imperium of Man": "https://warhammer40k.fandom.com/wiki/Imperium_of_Man",
    "Chaos": "https://warhammer40k.fandom.com/wiki/Chaos",
    "Eldar": "https://warhammer40k.fandom.com/wiki/Aeldari",
    "Orks": "https://warhammer40k.fandom.com/wiki/Orks",
    "Tyranids": "https://warhammer40k.fandom.com/wiki/Tyranids",
    "Necrons": "https://warhammer40k.fandom.com/wiki/Necrons"
}

test_urls = {
    "Roboute Guilliman": "https://warhammer40k.fandom.com/wiki/Roboute_Guilliman",
    "Abaddon the Despoiler": "https://warhammer40k.fandom.com/wiki/Abaddon",
    "Eldrad Ulthran": "https://warhammer40k.fandom.com/wiki/Eldrad_Ulthran",
    "Ghazghkull Mag Uruk Thraka": "https://warhammer40k.fandom.com/wiki/Ghazghkull_Mag_Uruk_Thraka",
    "Hive Tyrant": "https://warhammer40k.fandom.com/wiki/Hive_Tyrant",
    "Imotekh": "https://warhammer40k.fandom.com/wiki/Imotekh"   
}

def scraping(lore_urls):
    
    # Empty table where the lore will go
    data = []
    
    # Iterate over the URLs dictionary
    for faction, url in lore_urls.items():
        page = requests.get(url, verify=False)
        soup = BeautifulSoup(page.content, "html.parser")

        # Extract all paragraphs from the article body
        paragraphs = soup.select("div.mw-parser-output > p")
        text = " ".join([p.get_text() for p in paragraphs])

        data.append({"Title": faction, "Text": text})
        
    return data

data_table = scraping(test_urls)

# Save to CSV
df = pd.DataFrame(data_table)
df.to_csv("data/raw_test_data_texts.csv", index=False)

print("Scraping complete. Data saved to data/raw_test_data_texts.csv")
