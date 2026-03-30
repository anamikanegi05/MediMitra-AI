import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import random

heart_symptoms = [
    "chest pain", "heart attack", "high blood pressure", "left arm pain",
    "tight chest", "pain in chest", "pressure in chest", "rapid heartbeat",
    "irregular heartbeat", "shortness of breath with chest pain",
    "sweating with chest pain", "dizziness", "nausea with chest pain",
    "fatigue", "weakness", "palpitations", "pain spreading to jaw",
    "pain spreading to back", "cold sweat", "lightheadedness"
]

asthma_symptoms = [
    "shortness of breath", "breathing problem", "wheezing", "cough at night",
    "tight chest", "difficulty breathing", "rapid breathing",
    "chest tightness", "dry cough", "coughing after exercise",
    "breathing difficulty in cold air", "whistling sound breathing",
    "frequent coughing", "sleep disturbance due to breathing",
    "fatigue due to breathing", "shallow breathing", "labored breathing"
]

cancer_symptoms = [
    "unexplained weight loss", "tumor", "fatigue", "blood in stool",
    "persistent cough", "lump in body", "unusual bleeding",
    "skin changes", "difficulty swallowing", "chronic pain",
    "night sweats", "loss of appetite", "persistent fever",
    "change in bowel habits", "chronic fatigue", "hoarseness",
    "swelling", "pain without reason"
]

abdominal_symptoms = [
    "abdominal pain", "stomach ache", "vomiting", "gas problem",
    "bloating", "diarrhea", "constipation", "nausea",
    "cramps", "indigestion", "burning stomach",
    "food intolerance", "loss of appetite", "acid reflux",
    "stomach discomfort", "pain after eating",
    "sharp abdominal pain", "lower belly pain"
]


def generate_data(symptom_list, label, count=80):
    data = []
    for _ in range(count):
        sample = random.sample(symptom_list, k=2)
        sentence = " and ".join(sample)
        data.append((sentence, label))
    return data


data = []
data += generate_data(heart_symptoms, "heart")
data += generate_data(asthma_symptoms, "asthma")
data += generate_data(cancer_symptoms, "cancer")
data += generate_data(abdominal_symptoms, "abdominal")

df = pd.DataFrame(data, columns=["symptoms", "disease"])
