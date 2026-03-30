import pickle
from config import MODEL_PATHS, CONFIDENCE_THRESHOLD


class Classifier:
    def __init__(self):
        self.models = {
            disease: self.load(path)
            for disease, path in MODEL_PATHS.items()
        }

    def load(self, path):
        with open(path, "rb") as f:
            return pickle.load(f)

    def predict(self, symptoms):
        text = " ".join(symptoms)

        scores = {}

        for disease, (model, vectorizer) in self.models.items():
            X = vectorizer.transform([text])
            prob = model.predict_proba(X)[0][1]
            scores[disease] = prob

        final_disease = max(scores, key=scores.get)

        if scores[final_disease] < CONFIDENCE_THRESHOLD:
            return "General Condition"

        # better naming
        return {
            "heart": "Heart Disease",
            "asthma": "Asthma",
            "cancer": "Cancer",
            "abdominal": "Abdominal Issue"
        }[final_disease]
