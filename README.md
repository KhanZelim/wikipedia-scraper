# Wikipedia Scraper
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


## 🏢 Description

In this project we will query an API to obtain a list of countries and their past political leaders. We then extract and sanitize their short bio from Wikipedia. Finally, we save the data to a file.

![scraping](https://media4.giphy.com/media/Xe02toxlUsztG7iQgb/giphy.gif?cid=ecf05e47lixeo6qe5y4ooabkh0hfdz0t1pio4h0qgbngjq0n&ep=v1_gifs_search&rid=giphy.gif&ct=g)

## 📦 Repo structure

```
.
├── src/
│   ├── scraper.py
├── .gitignore
├── leaders_data.json
├── leaders.json
├── main.py
├── README.md
├── requirements.txt
└── wikipedia_scraper.ipynb
```

## 🛎️ Usage

1. Clone the repository to your local machine.

2. To run the script, you can execute the `main.py` file from your command line:

    ```
    python main.py
    ```

3. The script creates a Wikipedia scraper, gets a list of countries and their leaders from an API, gets the first paragrah for each leader fom Wikipedia, and saves it all in a dictionary. The resulting dictionary is saved to a "leaders_data.json" file in your root directory. 

```python
# Create a WikipediaScraper object
scraper = WikipediaScraper()

# Get list of countries from API
countries = scraper.get_countries()

# Loop through the list and get the leaders for each country
for country in countries:
    scraper.get_leaders(country)

# Saving dictionary to a json file
scraper.to_json_file("leaders_data")
```
## ⏱️ Timeline

This project took three days for completion.

## 📌 Personal Situation
This project was done as part of the AI Boocamp at BeCode.org. 

Connect with me on [LinkedIn](https://www.linkedin.com/in/zelimkhan-jachichanov/).