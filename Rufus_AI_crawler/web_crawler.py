from web_crawler import fetch_content
from extractor import extract_relevant_data
from output import save_to_json
from user_input import get_user_input

def main():
    # Step 1: Get user input
    url, prompt = get_user_input()

    # Step 2: Fetch content (static or dynamic)
    print("Fetching content...")
    soup = fetch_content(url)

    if not soup:
        print("Failed to fetch content. Exiting...")
        return

    # Step 3: Extract relevant data based on prompt
    print("Extracting relevant data...")
    relevant_data = extract_relevant_data(soup, prompt)

    if not relevant_data:
        print("No relevant data found based on the prompt. Exiting...")
        return

    # Step 4: Save structured data to JSON
    print("Saving data to output.json...")
    save_to_json(relevant_data)
    print("Process complete. Data saved successfully!")

if __name__ == "__main__":
    main()
