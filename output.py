import json

class RufusDocument:
    def save_to_json(self, data, filename="output.json"):
        """
        Save any given data to a JSON file.

        Parameters:
        - data (dict or list): The data to save.
        - filename (str): The name of the output JSON file.
        """
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Data successfully saved to {filename}")
        except Exception as e:
            print(f"Error saving data to {filename}: {e}")

    def save_links_to_json(self, links, filename="links.json"):
        """
        Save extracted links to a JSON file in a standardized format.

        Parameters:
        - links (list): A list of links to save.
        - filename (str): The name of the output JSON file.
        """
        try:
            with open(filename, 'w') as f:
                json.dump({"links": links}, f, indent=4)
            print(f"Links successfully saved to {filename}")
        except Exception as e:
            print(f"Error saving links to {filename}: {e}")
