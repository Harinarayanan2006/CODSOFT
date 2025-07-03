# 💳 Credit Card Fraud Detection – CodSoft Internship Task 2

This project is part of my Machine Learning internship with **CodSoft**. It involves building a machine learning model to detect fraudulent transactions in a real-world credit card dataset.

---

## 📁 Dataset Used

- **Name:** `fraudTest.csv`
- **Source:** Provided via Kaggle-style dataset
- **Format:** Extracted from a ZIP file (`fraudTest.csv.zip`)
- **Rows:** ~550,000+
- **Target column:** `is_fraud` (0 = Legitimate, 1 = Fraud)

---

## 🚀 Project Workflow

1. **File Upload and Extraction**  
   - The dataset is uploaded as a ZIP and extracted using Python in Google Colab.

2. **Data Exploration**  
   - Dataset summary, column types, missing values
   - Class imbalance analysis with pie and bar charts

3. **Preprocessing**  
   - Dropping irrelevant or sensitive columns
   - Label Encoding for categorical fields

4. **Model Training**  
   - Logistic Regression with `class_weight='balanced'`
   - Random Forest Classifier for better performance

5. **Evaluation**  
   - Accuracy, Precision, Recall, F1-score
   - Confusion Matrix
   - ROC Curve with AUC

---

## 📊 Results

- Logistic Regression struggled slightly due to class imbalance.
- Random Forest performed well with higher Recall and AUC.
- ROC Curve added for visual confidence in fraud detection.

---

## 🛠️ Technologies Used

- Python
- Google Colab
- pandas, seaborn, matplotlib
- scikit-learn (LogisticRegression, RandomForestClassifier)

---

## 📌 Key Learnings

- How to handle class imbalance with `class_weight='balanced'`
- Encoding and cleaning real-world data
- Model evaluation beyond just accuracy
- Visualization of fraud distribution

---

## 🧑‍💻 Author

**HARINARAYANAN V**  
3rd Year, CSE(AIML)  
K RAMAKRISHNAN COLLEGE OF TECHNOLOGY

---

## 🔗 Internship

**Organization:** CodSoft  
**Task:** Machine Learning – Task 2  
**Title:** Credit Card Fraud Detection

---
