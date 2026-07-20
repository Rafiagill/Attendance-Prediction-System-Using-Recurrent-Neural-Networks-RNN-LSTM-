# 📚 Student Attendance Prediction Using RNN (LSTM)

A deep learning project that predicts whether a student is likely to be **Present** or **Absent** in the next class based on historical attendance records.

This project uses a **Recurrent Neural Network (RNN)** with **Long Short-Term Memory (LSTM)** architecture to learn attendance patterns from sequential data and forecast future attendance.

---

## 📌 Project Overview

Educational institutions often need to identify students who may become irregular in attendance. This project applies deep learning techniques to analyze historical attendance data and predict future attendance, enabling early intervention and improved student monitoring.

The model is trained using previous attendance records where:

- **Present (P) = 1**
- **Absent (A) = 0**

The trained model predicts the attendance status for the upcoming class.

---

## 🚀 Features

- Predicts a student's next-day attendance
- Deep Learning model using LSTM
- Attendance data preprocessing
- Sequence generation for time-series learning
- Binary classification (Present/Absent)
- Model training and evaluation
- Future attendance prediction

---

## 🛠 Technologies Used

- Python
- TensorFlow
- Keras
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Jupyter Notebook

---

## 📂 Project Structure

```
Attendance-Prediction-RNN/
│
├── attendance_dataset.xlsx
├── RNN.ipynb
├── model/
├── results/
├── images/
├── README.md
└── requirements.txt
```

---

## ⚙️ How It Works

1. Load the attendance dataset.
2. Convert attendance values:
   - Present → 1
   - Absent → 0
3. Clean and preprocess the data.
4. Convert attendance records into sequential data.
5. Train an LSTM-based Recurrent Neural Network.
6. Evaluate model performance.
7. Predict the student's attendance for the next lecture.

---

## 📊 Workflow

```
Attendance Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Sequence Generation
        │
        ▼
LSTM Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Next-Day Attendance Prediction
```

---

## 💡 Applications

- Educational Analytics
- Student Performance Monitoring
- Attendance Forecasting
- Early Identification of At-Risk Students
- Academic Decision Support Systems

---

## 📈 Future Improvements

- Web-based prediction dashboard using Streamlit
- Support for multiple attendance prediction horizons
- Integration with real-time student databases
- Improved prediction using Bidirectional LSTM
- Hyperparameter optimization
- Model deployment using Flask or FastAPI

---

## 👩‍💻 Author

**Rafia Gill**

BS Cyber Security  
The Islamia University of Bahawalpur

---

## ⭐ Acknowledgements

This project was developed as part of academic learning to demonstrate the application of Deep Learning and Recurrent Neural Networks for educational data analysis and attendance prediction.
