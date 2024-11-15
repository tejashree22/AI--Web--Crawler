import json


class RufusDocument:
    @staticmethod
    def save_to_json(data, filename="output.json"):
        """
        Save extracted data to a JSON file.
        """
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"Data saved to {filename}")
        except Exception as e:
            print(f"Error saving data: {e}")

    @staticmethod
    def save_links_to_json(links, filename="links.json"):
        """
        Save extracted links to a JSON file.
        """
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump({"links": links}, f, indent=4, ensure_ascii=False)
            print(f"Links saved to {filename}")
        except Exception as e:
            print(f"Error saving links: {e}")
