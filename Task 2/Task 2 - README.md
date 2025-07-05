# 💳 CodSoft Internship - Task 2: Credit Card Fraud Detection

This project is the second task of my Machine Learning Internship with **CodSoft**. The objective is to build a classification model that detects fraudulent credit card transactions using a real-world dataset.

---

## 📁 Dataset

- **Click Here to Access Dataset:**`(https://drive.google.com/file/d/1sKHwjh40iIeHrZ_PeD_cOiKQwKjYIfYy/view?usp=sharing)
- **Source:** Provided for the internship (similar to Kaggle datasets)
- **Records:** ~550,000 transactions
- **Target column:** `is_fraud` (0 = Legit, 1 = Fraud)

---

## 🔧 Technologies Used

- Python 3.11
- pandas, numpy
- matplotlib, seaborn
- scikit-learn
- Jupyter Notebook / VS Code

---

## 🚀 Steps Followed

1. **Data Extraction & Loading**
   - Extracted ZIP file and loaded CSV using pandas

2. **Data Exploration**
   - Checked shape, columns, null values, and class imbalance
   - Visualized class distribution using pie chart and bar chart

3. **Preprocessing**
   - Dropped irrelevant columns (e.g. card number, timestamp, etc.)
   - Encoded categorical columns using LabelEncoder

4. **Model Training**
   - Logistic Regression with `class_weight='balanced'`
   - Random Forest Classifier for comparison

5. **Evaluation**
   - Accuracy, Precision, Recall, F1-score
   - Confusion matrix & classification report
   - ROC Curve with AUC score

---

## 📊 Results

- **Random Forest** performed best with high recall and AUC score.
- Logistic Regression provided baseline performance.
- ROC Curve helped visualize trade-off.

---

## 📌 Folder Structure

```
Task-2/
├── Task 2.ipynb
└── README.md

---

## 👨‍💻 Developed By

**HARINARAYANAN V**  
3rd Year – CSE(AIML)  
K RAMAKRISHNAN COLLEGE OF TECHNOLOGY

---

## 🔗 Internship Details

- **Organization:** CodSoft
- **Track:** Machine Learning Internship
- **Task:** Credit Card Fraud Detection