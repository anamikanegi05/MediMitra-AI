from modules.llm_handler import LLMHandler
from modules.ocr_server import OCRHandler
from modules.classifier import Classifier
from modules.decision_engine import DecisionEngine
from database import save_chat

class MCPServer:
    def __init__(self):
        self.llm = LLMHandler()
        self.ocr = OCRHandler()
        self.classifier = Classifier()
        self.decision_engine = DecisionEngine()

    def process(self, user_input):
        self.llm.store_input(user_input)

        self.ocr.process_text(user_input)

        probs = self.classifier.predict(user_input)

        suggestion = self.decision_engine.make_decision(user_input, probs)

        save_chat(user_input, suggestion)

        return suggestion
