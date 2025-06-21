# core/nlp.py

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load fallback responses
with open("resources/data.txt", "r") as f:
    output_list = f.read().split(",")


def get_output(text, fallback_data):
    text = text.lower()
    fallback_data.append(text)
    cm = CountVectorizer().fit_transform(fallback_data)
    similarity = cosine_similarity(cm[-1], cm)
    fallback_data.pop()
    return similarity[0]


def classify(text):
    sims = get_output(text, output_list)
    max_val = max(sims[:-1])
    best_index = np.argmax(sims[:-1])
    if max_val >= 0.6:
        return output_list[best_index]
    else:
        return "sorry"
