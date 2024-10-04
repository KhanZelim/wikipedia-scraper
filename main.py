from src.scraper import WikipediaScraper

scraper = WikipediaScraper()

countries = scraper.get_countries()
for country in countries:
    scraper.get_leaders(country)

scraper.to_json_file("leaders_data")