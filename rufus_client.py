from web_crawler import RufusCrawler
from extractor import RufusExtractor
from output import RufusDocument


class RufusClient:
    def __init__(self, api_key=None):
        """
        Initialize the RufusClient.
        The API key is optional for now (reserved for future enhancements).
        """
        self.api_key = api_key
        self.crawler = RufusCrawler()
        self.extractor = RufusExtractor()
        self.document = RufusDocument()

    def scrape(self, url, prompt, max_depth=1, dynamic=True, output_format="json"):
        """
        Scrape the provided URL and extract content based on the prompt.

        Args:
            url (str): The website URL to scrape.
            prompt (str): Instructions for the type of data to extract.
            max_depth (int): Maximum depth for crawling links.
            dynamic (bool): Whether to use dynamic fetching (Selenium).
            output_format (str): Format for the output file ('json' or 'csv').

        Returns:
            dict: Extracted data ready for use in downstream applications.
        """
        print(f"Scraping: {url} with prompt: '{prompt}'")

        # Step 1: Crawl the website
        soup, links = self.crawler.crawl(url, max_depth=max_depth, dynamic=dynamic)
        if not soup:
            print("Failed to fetch content. Exiting...")
            return {"error": "Failed to fetch content."}

        # Step 2: Extract relevant data
        relevant_data = self.extractor.extract_relevant_data(soup, prompt)
        if not relevant_data or relevant_data == ["No relevant data found."]:
            print("No relevant data found.")
            return {"error": "No relevant data found."}

        # Step 3: Save the output
        output_data = {"prompt": prompt, "content": relevant_data}
        if output_format == "json":
            self.document.save_to_json(output_data, filename="output.json")
        elif output_format == "csv":
            # Convert to CSV format if requested (optional future enhancement)
            print("CSV format not yet implemented.")
        else:
            print(f"Unsupported output format: {output_format}")

        # Step 4: Save links (optional)
        if links:
            self.document.save_links_to_json(links)

        print("Scraping completed successfully.")
        return output_data
