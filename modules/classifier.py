import pickle

class Classifier:
    def __init__(self):
        self.models = {}
        for disease in ["heart", "asthma", "cancer", "abdominal"]:
            with open(f"models/{disease}_model.pkl", "rb") as f:
                self.models[disease] = pickle.load(f)

    def predict(self, symptoms):
        probs = {}
        for disease, (vectorizer, model) in self.models.items():
            X = vectorizer.transform([symptoms])
            probs[disease] = model.predict_proba(X)[0][1]
        return probs
