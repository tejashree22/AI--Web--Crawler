class RufusExtractor:
    def extract_relevant_data(self, soup, prompt):
        """
        Extract FAQ-style questions and answers based on the prompt.
        """
        relevant_content = []
        questions = []
        answers = []

        # Debug: Print all extracted tags
        print("Extracted Tags and Text:")
        for tag in soup.find_all(["p", "h2", "h3"]):
            text = tag.get_text(strip=True)
            print(f"Tag: {tag.name}, Text: {text}")

            if not text:
                continue

            # Detect questions
            if text.endswith("?") or text.lower().startswith(("what", "how", "why", "when", "can", "do", "does")):
                questions.append(text)
            else:
                answers.append(text)

        # Pair questions with potential answers
        for idx, question in enumerate(questions):
            try:
                relevant_content.append({
                    "question": question,
                    "answer": answers[idx] if idx < len(answers) else "Answer not found."
                })
            except IndexError:
                relevant_content.append({"question": question, "answer": "Answer not found."})

        return relevant_content if relevant_content else ["No FAQs found."]
