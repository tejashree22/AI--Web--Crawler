from rufus_client import RufusClient

# Initialize RufusClient
client = RufusClient(api_key="your_api_key_here")  # API key is optional for now

# Define the website URL and prompt
url = 'https://www.sf.gov/information/sf-erap-frequently-asked-questions'  # Replace with a real URL for testing
instructions = "SF ERAP Frequently Asked Questions"

# Call the API
result = client.scrape(url, prompt=instructions)

# Output the results
print("Scraped Content:", result)
