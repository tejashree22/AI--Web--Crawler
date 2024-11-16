class RufusExtractor:
    def extract_relevant_data(self, soup, prompt):
        """
        Extract FAQs systematically: questions and answers.
        """
        extracted_data = []

        # Target tags commonly used for FAQs
        question_tags = ["h4", "strong"]  # Headers or bold text often indicate questions
        answer_tags = ["p", "ul", "li"]  # Answers are typically in paragraphs or lists

        # Extract and pair questions with their answers
        questions = soup.find_all(question_tags)
        for question in questions:
            question_text = question.get_text(strip=True)
            answer_elements = question.find_next_siblings(answer_tags)

            # Gather all answer text for the question
            answer_text = "\n".join(
                element.get_text(strip=True) for element in answer_elements
            )

            # Add to the extracted data
            if question_text and answer_text:
                extracted_data.append({
                    "question": question_text,
                    "answer": answer_text
                })

        # Return extracted data or a message if none found
        return extracted_data if extracted_data else [{"question": "No relevant data found.", "answer": ""}]
