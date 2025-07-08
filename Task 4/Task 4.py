import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

# Step 1: Load and clean data
df = pd.read_csv(r"C:\Users\Admin\OneDrive\Documents\ML-INTERNSHIP\Task 4\spam.csv", encoding='latin-1')[['v1', 'v2']]
df.columns = ['label', 'message']
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Step 2: Split data
X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.2, random_state=42)

# Step 3: TF-IDF Vectorization
tfidf = TfidfVectorizer(max_features=5000)
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

# Step 4: Train model
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Step 5: Evaluate
y_pred = model.predict(X_test_tfidf)
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("📊 Report:\n", classification_report(y_test, y_pred))

# Step 6: Save model and vectorizer
model_dir = r"C:\Users\Admin\OneDrive\Documents\ML-INTERNSHIP\model"
os.makedirs(model_dir, exist_ok=True)

joblib.dump(model, os.path.join(model_dir, "spam_classifier_model.pkl"))
joblib.dump(tfidf, os.path.join(model_dir, "tfidf_vectorizer.pkl"))

print("🎉 Model and Vectorizer saved successfully!")