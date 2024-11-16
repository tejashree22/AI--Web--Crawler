import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class RufusCrawler:
    def __init__(self):
        self.visited = set()

    def fetch_dynamic_content(self, url):
        print(f"Fetching dynamic content for {url}")
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            driver.quit()
            return soup
        except Exception as e:
            print(f"Error fetching dynamic content: {e}")
            return None

    def fetch_static_content(self, url):
        print(f"Fetching static content for {url}")
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup
        except Exception as e:
            print(f"Error fetching static content: {e}")
            return None

    def crawl(self, url, dynamic=False):
        print(f"Crawling: {url}")
        return self.fetch_dynamic_content(url) if dynamic else self.fetch_static_content(url)
