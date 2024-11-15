def get_user_input():
    """
    Prompt the user to enter the website URL and prompt for data extraction.
    """
    url = input("Enter the website URL to scrape: ").strip()
    prompt = input("Enter the prompt (e.g., 'extract industry reports'): ").strip()
    return url, prompt
