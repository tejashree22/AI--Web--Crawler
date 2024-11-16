from web_crawler import RufusCrawler
from extractor import RufusExtractor
from output import RufusDocument
from user_input import get_user_input

def main():
    url, prompt = get_user_input()

    crawler = RufusCrawler()
    extractor = RufusExtractor()
    document = RufusDocument()

    print(f"Scraping: {url} with prompt: '{prompt}'")
    soup = crawler.crawl(url, dynamic=True)
    if not soup:
        print("Failed to fetch content. Exiting...")
        return

    with open("fetched_content_debug.html", "w", encoding="utf-8") as file:
        file.write(str(soup.prettify()))
    print("Fetched content saved to fetched_content_debug.html for debugging.")

    relevant_data = extractor.extract_relevant_data(soup, prompt)
    if not relevant_data:
        print("No relevant data found. Exiting...")
        return

    output_data = {"prompt": prompt, "content": relevant_data}
    document.save_to_json(output_data)
    print("Data saved to output.json")

if __name__ == "__main__":
    main()
