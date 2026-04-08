import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

data = {
    "heart": [
        ("chest pain left arm", 1), ("shortness of breath", 1),
        ("headache", 0), ("cough", 0)
    ],
    "asthma": [
        ("wheezing", 1), ("cough at night", 1),
        ("chest pain", 0), ("stomach ache", 0)
    ],
    "cancer": [
        ("unexplained weight loss", 1), ("fatigue", 1),
        ("cough", 0), ("mild pain", 0)
    ],
    "abdominal": [
        ("stomach pain", 1), ("nausea", 1),
        ("chest pain", 0), ("cough", 0)
    ]
}

for disease, samples in data.items():
    texts, labels = zip(*samples)
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts)
    model = MultinomialNB()
    model.fit(X, labels)
    
    with open(f"models/{disease}_model.pkl", "wb") as f:
        pickle.dump((vectorizer, model), f)
    
    print(f"{disease}_model.pkl created")
