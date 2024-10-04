import requests
from requests import Session
from bs4 import BeautifulSoup
import json
import re

class WikipediaScraper:
    def __init__(self) -> None:
        self.base_url: str = "https://country-leaders.onrender.com"
        self.country_endpoint: str  = "/countries"
        self.leaders_endpoint: str = "/leaders"
        self.cookies_endpoint: str = "/cookie"
        self.leaders_data: dict = {}
        self.cookie: object = self.refresh_cookies()
        self.session: Session = requests.Session()

    def refresh_cookies(self) -> object:
        self.cookie = self.session.get(f"{self.base_url}{self.cookies_endpoint}").cookies
        return self.cookie

    def get_countries(self) -> list:
        countries = self.session.get(f"{self.base_url}{self.country_endpoint}", cookies=self.cookie).json()
        return countries

    def get_leaders(self, country: str) -> None:
        try:
            countries = self.get_countries
            for country in countries:
                leaders = self.session.get(f"{self.base_url}{self.leaders_endpoint}", cookies=self.cookie, params={"country": country}).json()
                for leader in leaders:
                    wikipedia_url = leader["wikipedia_url"]
                    leader["first_paragraph"] = self.get_first_paragraph(wikipedia_url)
                self.leaders_data[country] = leaders
        except ConnectionError:
            self.refresh_cookies()
            self.get_leaders()
        except TypeError as e:
            print(f"TypeError encountered: {e}, leader content: {leader}")

    def get_first_paragraph(self, wikipedia_url: str) -> str:
        wiki = self.session.get(wikipedia_url)
        soup = BeautifulSoup(wiki.content, "html.parser")
        paragraphs = soup.find_all("p")
        for paragraph in paragraphs:
            if paragraph.find("b"):
                first_paragraph = paragraph.text
                break
        pattern = r"\[\d\]|\(.*ⓘ\)|\n"
        return re.sub(pattern, "", first_paragraph)

    def to_json_file(self, filepath: str) -> None:
        with open(filepath, "w") as json_file:
            json_file.write(json.dumps(self.leaders_data))

    def __str__(self) -> str:
        return f"WikipediaScraper with base URL: {self.base_url}, Number of countries scraped: {len()}"