# 🖋️ Task 5 – Handwritten Text Generation using RNN

🎯 **Final Task** from my Machine Learning Internship at **CodSoft**

This project builds a character-level Recurrent Neural Network (RNN) that learns patterns from poetic text and generates handwritten-style text — one character at a time ✍️

---

## 📌 Objective

- Use deep learning to generate new poetic lines.
- Train a GRU-based RNN on the **Gutenberg Poetry Corpus**.
- Generate text using learned patterns in character sequences.

---

## 💻 Technologies Used

- Python 🐍
- TensorFlow / Keras 🧠
- NumPy 🔢
- NDJSON Preprocessing 📄
- GRU (Gated Recurrent Unit)

---

## 📂 Project Structure

```
Task 5/
├── extract_text.py          # Extracts poems from NDJSON into plain text
├── train_rnn_textgen.py     # Trains the RNN model
├── generate.py              # Generates text using trained model
├── char2idx.npy             # Character-to-index mapping
├── idx2char.npy             # Index-to-character mapping
├── README.md                # You're reading this!
```

> ⚠️ Note: The following large files are not included in this repo due to size:
> - `gutenberg-poetry-v001.ndjson`  
> - `data.txt`  

📥 You can download them from the link below:

### 🔗 [Google Drive – Download Dataset & Model]
1) https://drive.google.com/file/d/11cWVOL4-7QwQskj9jFHhKzXtEKjX4HD4/view?usp=sharing 
2) https://drive.google.com/file/d/1okggbCv5OiprYl0FS5ifi83dUQOMoKLn/view?usp=sharing

---

## 🚀 How to Run

### 1️⃣ Extract Poems
```bash
python extract_text.py
```

### 2️⃣ Train the Model
```bash
python train_rnn_textgen.py
```

### 3️⃣ Generate New Text
```bash
python generate.py
```

---

## 📝 Sample Output

```
The sky was full of stars and fire,
A song beneath the winds’ desire.
With silver threads, the night was spun,
Until the rise of morning sun...

---
