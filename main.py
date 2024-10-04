from src.scraper import WikipediaScraper

# Initializing WikipediaScraper object
scraper = WikipediaScraper()

# Get list of countries from API
countries = scraper.get_countries()

# Loop through the list and get the leaders for each country
for country in countries:
    scraper.get_leaders(country)

# Saving dictionary to a json file
scraper.to_json_file("leaders_data")