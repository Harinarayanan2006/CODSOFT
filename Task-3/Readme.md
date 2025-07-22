
# 📊 Customer Churn Prediction - Task 3 (CodSoft Internship)

This repository contains the implementation of **Customer Churn Prediction** developed by me as part of **Task 3** in the CodSoft Machine Learning Internship.

---

## ✅ Objective

To predict which customers are likely to churn in a subscription-based service and identify the key factors contributing to churn.

---

## 📁 Dataset

- Dataset is provided in ZIP format containing a CSV file with customer data.
- The data includes features such as:
  - CreditScore, Age, Gender, Geography
  - Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary

- **Target Variable**: `Exited` (1 = Churned, 0 = Retained)

---

## ⚙️ Tools & Libraries Used

- Python
- Pandas, NumPy
- Matplotlib, Seaborn (Visualization)
- Scikit-learn (ML modeling and evaluation)
- Jupyter Notebook

---

## 🧠 Project Workflow Summary

1. **Extract & Load ZIP File** – Used `zipfile` module to extract dataset.
2. **Preprocessing**
   - Dropped non-informative columns: `RowNumber`, `CustomerId`, `Surname`
   - Encoded `Gender` with LabelEncoder and `Geography` with One-Hot Encoding
   - Scaled numeric columns using `StandardScaler`
3. **Train-Test Split** – Split data 80% train / 20% test.
4. **Model Training** – Trained a `RandomForestClassifier`.
5. **Model Evaluation**
   - Accuracy Score
   - Classification Report
   - Confusion Matrix (Plotted)
6. **Feature Importance Plot** – Visualized which features impact churn most.

---

## 🔍 Sample Code Snippets

```python
# Sample: Encoding Gender and Geography
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])
df = pd.get_dummies(df, columns=['Geography'], drop_first=True)
```

```python
# Sample: Model Training & Evaluation
model = RandomForestClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
```

---

## 📈 Visual Outputs

- Confusion Matrix (Heatmap using Seaborn)
- Feature Importance (Barplot of top features)

---

## 🧑‍💻 Developed By

**HARINARAYANAN V**  
CodSoft ML Intern  
📅 Task 3 – Customer Churn Prediction

---

## ▶️ How to Run

1. Clone this repo or download the notebook.
2. Ensure your ZIP file is correctly placed and path updated.
3. Run the Jupyter Notebook: `Task-3.ipynb`
---
