from web_crawler import RufusCrawler
from extractor import RufusExtractor
from output import RufusDocument

class RufusClient:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.crawler = RufusCrawler()
        self.extractor = RufusExtractor()
        self.document = RufusDocument()

    def scrape(self, url, prompt, max_depth=1, dynamic=True, output_format="json"):
        print(f"Scraping: {url} with prompt: '{prompt}'")
        soup, links = self.crawler.crawl(url, max_depth=max_depth, dynamic=dynamic)
        if not soup:
            return {"error": "Failed to fetch content."}

        relevant_data = self.extractor.extract_relevant_data(soup, prompt)
        if not relevant_data:
            return {"error": "No relevant data found."}

        output_data = {"prompt": prompt, "content": relevant_data}
        if output_format == "json":
            self.document.save_to_json(output_data, filename="output.json")

        if links:
            self.document.save_links_to_json(links)

        print("Scraping completed successfully.")
        return output_data
