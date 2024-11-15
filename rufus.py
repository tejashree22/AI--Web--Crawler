from crawler import RufusCrawler
from extractor import RufusExtractor
from output import RufusDocument
from user_input import get_user_input


def main():
    # Step 1: Get user input
    url, prompt = get_user_input()

    # Step 2: Crawl the website
    crawler = RufusCrawler()
    soup, links = crawler.crawl(url, max_depth=1, dynamic=True)

    if not soup:
        print("Failed to fetch content. Exiting...")
        return

    # Step 3: Extract relevant data
    extractor = RufusExtractor()
    relevant_data = extractor.extract_relevant_data(soup, prompt)

    if not relevant_data or relevant_data == ["No FAQs found."]:
        print("No FAQs found.")
        return

    # Step 4: Save the output
    document = RufusDocument()
    document.save_to_json({"prompt": prompt, "content": relevant_data})

    # Step 5: Save extracted links (optional)
    if links:
        document.save_links_to_json(links)

    print("Process completed successfully!")


if __name__ == "__main__":
    main()
