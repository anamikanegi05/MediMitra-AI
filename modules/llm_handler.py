class LLMHandler:

    def extract_symptoms(self, text):
        # simple keyword extraction
        keywords = [
            "chest pain", "breathing", "cough", "fever",
            "weight loss", "abdominal pain", "vomiting"
        ]

        found = []
        for word in keywords:
            if word in text.lower():
                found.append(word)

        return found

    def generate_response(self, symptoms, disease, is_serious, hospital_info):
        response = f"Detected possible condition: {disease}\n"
        response += f"Symptoms: {', '.join(symptoms)}\n"

        if is_serious:
            response += "\nThis may be serious. Seek medical help immediately.\n"
            response += f"Nearby Hospital: {hospital_info}\n"
        else:
            response += "\nCondition seems mild. Monitor symptoms.\n"

        response += "\n(Note: This is not a medical diagnosis.)"

        return response