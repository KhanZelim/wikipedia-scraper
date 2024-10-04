import requests
from requests import Session
from bs4 import BeautifulSoup
import json
import re

class WikipediaScraper:
    """Class representing a Wikipedia scraper"""
    def __init__(self) -> None:
        """Constructor of the class WikipediaScraper"""
        self.base_url: str = "https://country-leaders.onrender.com"
        self.country_endpoint: str  = "/countries"
        self.leaders_endpoint: str = "/leaders"
        self.cookies_endpoint: str = "/cookie"
        self.leaders_data: dict = {}
        self.session: Session = requests.Session()
        self.cookie: object = self.refresh_cookies()

    def refresh_cookies(self) -> object:
        """
        Function to refresh the cookies from the API.
        
        :return: Cookie object.
        """
        self.cookie = self.session.get(f"{self.base_url}{self.cookies_endpoint}").cookies
        return self.cookie

    def get_countries(self) -> list:
        """
        Function to get the list of countries from the API.
        
        :return: List of countries.
        """
        countries = self.session.get(f"{self.base_url}{self.country_endpoint}", cookies=self.cookie).json()
        return countries

    def get_leaders(self, country: str) -> None:
        """
        Function to get the leaders for each country and to add the first paragraph from Wikipedia.
        
        :param country: String representation of the country.
        """
        try:
            leaders = self.session.get(f"{self.base_url}{self.leaders_endpoint}", cookies=self.cookie, params={"country": country}).json()
            for leader in leaders:
                wikipedia_url = leader["wikipedia_url"]
                leader["first_paragraph"] = self.get_first_paragraph(wikipedia_url)
            self.leaders_data[country] = leaders
        except ConnectionError:
            self.refresh_cookies()
            self.get_leaders()
        except TypeError as e:
            print(f"TypeError encountered: {e}")

    def get_first_paragraph(self, wikipedia_url: str) -> str:
        """
        Function to get the first paragraph from the Wikipedia page.
        
        :param wikipedia_url: String representation of the wikipedia url.
        :return: String representation of the first paragraph.
        """
        wiki = self.session.get(wikipedia_url)
        soup = BeautifulSoup(wiki.content, "html.parser")
        paragraphs = soup.find_all("p")
        for paragraph in paragraphs:
            for bold in soup.find_all("b"):
                if bold in paragraph:
                    first_paragraph = paragraph.text
                    break
            else:
                continue
            break
        pattern = r"\[.*\]|\(.*ⓘ\)|\n"
        return re.sub(pattern, "", first_paragraph)

    def to_json_file(self, filepath: str) -> None:
        """
        Function to save the scraped leaders data to a JSON file.
        
        :param filepath: String representation of the filepath.
        """
        with open(f"{filepath}.json", "w", encoding="utf-8") as json_file:
            json.dump(self.leaders_data, json_file, ensure_ascii=False, indent=4)

    def __str__(self) -> str:
        """String representation of the scraper object."""
        return f"WikipediaScraper with base URL: {self.base_url}"