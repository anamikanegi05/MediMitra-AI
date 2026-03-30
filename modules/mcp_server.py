from modules.llm_handler import LLMHandler
from modules.classifier import Classifier
from modules.decision_engine import DecisionEngine
from utils.hospital_finder import get_nearby_hospital
from modules.ocr_server import extract_text


class MCPServer:
    def __init__(self):
        self.llm = LLMHandler()
        self.classifier = Classifier()
        self.decision_engine = DecisionEngine()

    def process(self, user_input):

        # Step 0: OCR layer
        text = extract_text(user_input, is_image=False)

        # Step 1: Extract symptoms
        symptoms = self.llm.extract_symptoms(text)

        # (Optional safety)
        if not symptoms:
            return "Could not detect symptoms. Please describe clearly."

        # Step 2: Classify disease
        disease = self.classifier.predict(symptoms)

        # Step 3: Decision
        is_serious = self.decision_engine.is_serious(symptoms)

        # Step 4: Hospital if serious
        hospital_info = None
        if is_serious:
            hospital_info = get_nearby_hospital()

        # Step 5: Generate response
        response = self.llm.generate_response(
            symptoms, disease, is_serious, hospital_info
        )

        return response