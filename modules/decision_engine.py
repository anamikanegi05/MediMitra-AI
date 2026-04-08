class DecisionEngine:
    def __init__(self):
        self.hospitals = {
            "heart": ("City Heart Hospital", "1234567890"),
            "asthma": ("Breathe Well Clinic", "9876543210"),
            "cancer": ("Cancer Care Center", "111222333"),
            "abdominal": ("Digestive Health Hospital", "444555666")
        }
        self.emoji = {
            "heart": "❤️",
            "asthma": "🌬️",
            "cancer": "🎗️",
            "abdominal": "🫀"
        }
        self.emergency_keywords = ["chest pain", "severe pain", "difficulty breathing"]
        self.advisory = {
            "heart": "Avoid heavy exertion, track BP, consult a cardiologist.",
            "asthma": "Use inhalers, avoid allergens, stay hydrated.",
            "cancer": "Monitor symptoms, maintain healthy diet, consult oncologist.",
            "abdominal": "Eat light meals, avoid spicy food, consult gastroenterologist."
        }

    def make_decision(self, symptoms, probs):
        top_disease = max(probs, key=probs.get)
        top_prob = int(probs[top_disease] * 100)
        
        output = f"Health Suggestion\n"
        output += f"{self.emoji[top_disease]} {top_disease.capitalize()} probability: {top_prob}%\n"

        if any(word in symptoms.lower() for word in self.emergency_keywords):
            hospital, number = self.hospitals["heart"]
            output += f"\nEmergency detected!\nNearest hospital: {hospital}\nContact: {number}\n"
        else:
            output += f"\nAdvisory: {self.advisory[top_disease]}"

        return output
