from config import SERIOUS_SYMPTOMS
class DecisionEngine:
    def __init__(self):
        self.serious_keywords = SERIOUS_SYMPTOMS

    def is_serious(self, symptoms):
        for s in symptoms:
            if s in self.serious_keywords:
                return True
        return False