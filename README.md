# 🎓 Student Performance Predictor

A machine learning application that predicts student academic outcomes based on their performance metrics, attendance, and study habits.

## 📋 Overview

This project uses historical student data to predict whether a student will pass or fail their courses. It includes complete data preprocessing, exploratory analysis, model training, and a prediction interface for evaluating new student records.

**Key capabilities:**
- Data cleaning and validation
- Statistical analysis and visualization
- Random Forest classification model
- Feature importance analysis
- Real-time student outcome prediction

## 🛠️ Tech Stack

- **Python 3.x**
- **Data Processing:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn (Random Forest Classifier)
- **Model Persistence:** Joblib

## 📁 Project Structure

```
Student-Performance-Predictor/
├── student_performance_analysis.py    # Data cleaning & EDA
├── student_performance_model.py       # Model training & evaluation
├── new_student.py                     # Prediction interface
├── feature_importance.py              # Feature analysis
├── fix_datasets.py                    # Dataset utilities
├── requirements.txt                   # Python dependencies
├── student_model.pkl                  # Trained model (generated)
└── plots/                             # Generated visualizations
```

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.x installed on your system.

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ATOO7/Student-Performance-Predictor.git
   cd Student-Performance-Predictor
   ```

2. **Set up virtual environment**
   
   *Windows:*
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   
   *macOS/Linux:*
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

### 1. Data Analysis & Visualization

Run exploratory data analysis to understand patterns in student performance:

```bash
python student_performance_analysis.py
```

This generates:
- Grade distribution charts
- Correlation heatmaps
- Average performance metrics
- Cleaned dataset ready for modeling

### 2. Train the Model

Train and evaluate the Random Forest classifier:

```bash
python student_performance_model.py
```

**Output includes:**
- Model accuracy score
- Confusion matrix
- Saved model file (`student_model.pkl`)

### 3. Make Predictions

Predict outcomes for new students:

```bash
python new_student.py
```

**Sample input format:**
```python
{
    'Math': 85, 
    'Science': 78, 
    'English': 80, 
    'Attendance': 92, 
    'StudyHours': 5, 
    'Extracurricular': 1
}
```

**Sample output:**
```
✅ Prediction: Pass
```

### 4. Analyze Feature Importance

Understand which factors most influence student success:

```bash
python feature_importance.py
```

This visualizes the relative importance of each feature in the prediction model.

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| Algorithm | Random Forest Classifier |
| Accuracy | ~91% |
| Key Features | Math Score, Study Hours, Attendance |
| Target Variable | Binary (Pass/Fail) |

## 🔍 Features Analyzed

The model considers the following student attributes:

- **Academic Scores:** Math, Science, English
- **Attendance Rate:** Percentage of classes attended
- **Study Hours:** Average daily study time
- **Extracurricular Participation:** Binary indicator (Yes/No)

## 📈 Sample Visualizations

The project generates several plots saved in the `/plots/` directory:

- Grade distribution histograms
- Feature correlation heatmap
- Confusion matrix
- Feature importance bar chart

## 🔧 Utility Scripts

- **`fix_datasets.py`** - Handles missing values and data inconsistencies
- **`feature_importance.py`** - Ranks features by prediction impact

## 🎯 Future Roadmap

- [ ] Add support for additional ML algorithms (SVM, XGBoost)
- [ ] Build web interface using Flask or Streamlit
- [ ] Implement real-time dashboard for monitoring student performance
- [ ] Add hyperparameter tuning capabilities
- [ ] Include more demographic and behavioral features

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - feel free to use it for learning or commercial purposes with attribution.

## 👤 Author

**Aksh Thada**

Machine Learning Enthusiast | Data Science Developer

- GitHub: [@ATOO7](https://github.com/ATOO7)
- Project Link: [Student Performance Predictor](https://github.com/ATOO7/Student-Performance-Predictor)

## 🙏 Acknowledgments

This project was developed as a complete demonstration of the ML pipeline - from raw data to deployment-ready predictions. It's designed to help students and professionals understand practical machine learning implementation in education analytics.

---

⭐ If you find this project helpful, please consider giving it a star!