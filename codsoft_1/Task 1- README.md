
# 🎬 Movie Genre Classification using Machine Learning

This project is part of my CodSoft Machine Learning Internship. It predicts the genre of a movie based on its plot summary using TF-IDF and a Logistic Regression model.

---

## 🚀 Project Overview

- **Task**: Predict movie genres from plot descriptions
- **Techniques Used**: NLP, TF-IDF Vectorization, Logistic Regression
- **Dataset**: Provided as 4 `.txt` files
- **Language**: Python (Jupyter Notebook)

---

## 🧾 Dataset Files

- `train_data.txt`: Contains movie plot + genre info used for training
- `test_data.txt`: Contains plots for prediction
- `test_data_solution.txt`: Actual genres (used for evaluation)
- `README.md`: This file!

> 🔗 Due to large size, datasets are available via this Google Drive link:  
[📂 Click Here to Access Dataset](https://drive.google.com/drive/folders/1xoanx2O3gVN5pFr-g9V6CbZ5-g-w3-6T?usp=drive_link)

---

## ⚙️ Technologies Used

- Python 3.12+
- NLTK
- scikit-learn
- Pandas / NumPy
- Jupyter Notebook or VS Code

---

## 📊 Model Workflow

1. **Text Preprocessing**: Lowercasing, punctuation removal, stopword removal
2. **TF-IDF Vectorization**: Convert text to numeric features
3. **Label Encoding**: Transform genres into numeric labels
4. **Model Training**: Logistic Regression classifier
5. **Evaluation**: Accuracy, classification report
6. **Custom Prediction**: User can input a plot and get predicted genre

---

## ✅ Sample Output

```
🎯 Accuracy on Test Data: 0.76

📝 Classification Report:
              precision    recall  f1-score   support
     action       0.72      0.75      0.73     1300
     comedy       0.79      0.78      0.78     1500
     drama        0.76      0.74      0.75     1700
     ...
```

---

## ✍️ Predict Your Own Plot

```
Enter a movie plot to predict genre:
→ "A young man learns he is a wizard and goes to a magical school."

🎬 Predicted Genre: drama
```

---

## 🧠 Learnings

- Working with unstructured text data
- Natural Language Processing (NLP) pipeline
- Dealing with multi-class classification
- Handling data mismatches and cleaning

---

## 📌 Author

👨‍💻 **HARINARAYANAN V**  
🎓 BE - CSE(AIML), K RAMAKRISHNAN COLLEGE OF TECHNOLOGY 
🏆 CodSoft Machine Learning Intern (Task 1)

---

## 🏁 Final Note

This project demonstrates how simple machine learning techniques can be applied to natural language problems. Check out the notebook for code and results!
