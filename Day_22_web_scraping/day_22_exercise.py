#Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
import requests
from bs4 import BeautifulSoup
import json

url = "http://www.bu.edu/president/boston-university-facts-stats/"
response = requests.get(url)
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
#print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
#print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
#print(soup.body) # gives the whole page on the website
print('---------------------------------------------------------------------------')
li_items = soup.select("li")

print("Total <li> found:", len(li_items))
facts_dict = {}

for item in li_items:
    text = item.get_text(" ", strip=True)

    # If the line contains a colon, split into key/value
    if ":" in text:
        key, value = text.split(":", 1)
        facts_dict[key.strip()] = value.strip()
    else:
        # Otherwise store as key with null value
        facts_dict[text] = None


# Save to JSON file
with open("bu_facts.json", "w", encoding="utf-8") as f:
    json.dump(facts_dict, f, indent=4)

print("Saved successfully to bu_facts.json")

#Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file

url1 = "https://archive.ics.uci.edu/ml/datasets.php"
response1 = requests.get(url1)
content1 = response1.content # we get all the content from the website
soup1 = BeautifulSoup(content1, 'html.parser')
print("response of url1 ",response1.status_code)

#Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.
"""url2 = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
response2 = requests.get(url2)
content2 = response2.content # we get all the content from the website
soup2 = BeautifulSoup(content2, 'html.parser')
print("response of url2 ",response2.status_code)
"""
import re

url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Select the big Presidents table
table = soup.find("table", {"class": "wikitable"})

presidents = []

# Remove reference numbers like [1], [a]
def clean(text):
    return re.sub(r"\[.*?\]", "", text).strip()

# Process rows
rows = table.find_all("tr")

# Skip header row
for row in rows[1:]:
    cols = row.find_all(["td", "th"])
    if len(cols) < 5:
        continue  # skip spacing rows

    number = clean(cols[0].get_text(" ", strip=True))
    name = clean(cols[1].get_text(" ", strip=True))
    term = clean(cols[2].get_text(" ", strip=True))
    party = clean(cols[3].get_text(" ", strip=True))
    vice_president = clean(cols[4].get_text(" ", strip=True))

    presidents.append({
        "number": number,
        "name": name,
        "term": term,
        "party": party,
        "vice_president": vice_president
    })

# Save to JSON file
with open("us_presidents.json", "w", encoding="utf-8") as f:
    json.dump(presidents, f, indent=4)

print("Scraping complete! Saved as us_presidents.json")