from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests


class RufusCrawler:
    def __init__(self):
        self.visited = set()

    def fetch_static_content(self, url):
        try:
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            response.raise_for_status()
            return BeautifulSoup(response.text, "html.parser")
        except Exception as e:
            print(f"Error fetching static content: {e}")
            return None

    def fetch_dynamic_content(self, url):
        try:
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, "html.parser")
            driver.quit()
            return soup
        except Exception as e:
            print(f"Error fetching dynamic content: {e}")
            return None

    def crawl(self, url, max_depth=1, dynamic=False):
        if url in self.visited or max_depth == 0:
            return None, []

        self.visited.add(url)
        print(f"Crawling: {url}")

        soup = self.fetch_dynamic_content(url) if dynamic else self.fetch_static_content(url)
        if not soup:
            print(f"Failed to fetch content for {url}")
            return None, []

        # Extract links
        links = [a["href"] for a in soup.find_all("a", href=True) if a["href"].startswith("http")]
        return soup, links
