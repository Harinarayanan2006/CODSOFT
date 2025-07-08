
# 📩 SMS Spam Classifier - Task 4 ✅

This is **Task 4** of my Machine Learning Internship at **CodSoft**.  
I built an **SMS Spam Classifier** using **Logistic Regression** and **TF-IDF Vectorization**, and deployed it via **Streamlit Web App**.

---

## 🔍 Problem Statement
The goal is to automatically classify SMS messages as **Spam** or **Not Spam** using Natural Language Processing and Machine Learning techniques.

---

## 🚀 Project Highlights

- 📊 **TF-IDF Vectorization** for feature extraction
- 🧠 **Logistic Regression** & **Naive Bayes** models
- ✅ Achieved **96.6% accuracy**
- 🧪 Evaluation via **classification report** & **confusion matrix**
- 🌐 Built an **interactive web app** using **Streamlit**
- 💾 Saved trained model and vectorizer with **Joblib**

---

## 🛠️ Technologies Used

- Python
- Scikit-learn
- Pandas
- Joblib
- Streamlit
- Matplotlib & Seaborn (for visualization)

---

## 📁 Project Structure

```
├── spam.csv                       # Dataset
├── train_model.py                # Model training & saving
├── app.py                        # Streamlit UI code
├── model/
│   ├── spam_classifier_model.pkl     # Trained model
│   └── tfidf_vectorizer.pkl         # TF-IDF vectorizer
├── Task 4.ipynb                  # Notebook with full workflow
├── requirements.txt              # Dependencies
└── README.md                     # Project overview
```

---

## 📊 Model Performance

| Metric      | Score |
|-------------|-------|
| Accuracy    | 96.6% |
| Precision   | 1.00 (Spam) |
| Recall      | 0.75 (Spam) |
| F1-score    | 0.86 (Spam) |

---

## 🖥️ Web App Usage

1. Enter your SMS text in the input box.
2. Click **"Predict"**.
3. The app tells you if it's **SPAM** or **NOT SPAM**.

---

## 💡 Future Enhancements

- Add more classifiers like SVM, XGBoost
- Include real-time SMS input via API
- Improve UI design with custom CSS

---

## 📌 Internship: CodSoft
This project was completed as part of my internship at **CodSoft**, under **Task 4** – Machine Learning Projects.


---

> ✅ Task 4 Completed – Spam Detection Web App using Streamlit 🚀
