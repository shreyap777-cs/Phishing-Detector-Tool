import pandas as pd
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


# -------------------------------
# 1. Text Cleaning Function
# -------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+', '', text)  # remove links
    text = re.sub(r'[^a-zA-Z]', ' ', text)  # remove special characters
    return text


# -------------------------------
# 2. Load Dataset
# -------------------------------
df = pd.read_csv("dataset.csv", encoding='latin-1')

# Keep only required columns
df = df[['v1', 'v2']]
df.columns = ['label', 'text']

# Remove missing values (safety)
df.dropna(inplace=True)

# Apply text cleaning
df['text'] = df['text'].apply(clean_text)

# Convert labels to numeric
df['label'] = df['label'].map({'spam': 1, 'ham': 0})


# -------------------------------
# 3. Feature Extraction (TF-IDF)
# -------------------------------
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['text'])

y = df['label']


# -------------------------------
# 4. Train-Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# -------------------------------
# 5. Train Model
# -------------------------------
model = MultinomialNB()
model.fit(X_train, y_train)


# -------------------------------
# 6. Evaluate Model
# -------------------------------
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)


# -------------------------------
# 7. Suspicious Keyword Detection
# -------------------------------
def find_suspicious_words(text):
    keywords = ["free", "win", "urgent", "money", "offer", "click"]
    found = []

    text = text.lower()
    for word in keywords:
        if word in text:
            found.append(word)

    return found


# -------------------------------
# 8. Email Prediction Function
# -------------------------------
def predict_email(text):
    cleaned = clean_text(text)
    transformed = vectorizer.transform([cleaned])

    prediction = model.predict(transformed)[0]
    probability = model.predict_proba(transformed)[0]
    confidence = max(probability) * 100

    if prediction == 1:
        return f"Phishing Email 🚨 ({confidence:.2f}%)"
    else:
        return f"Safe Email ✅ ({confidence:.2f}%)"