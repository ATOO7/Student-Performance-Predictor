# Step 3: Predictive Model – Student Pass/Fail Prediction
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# Load dataset
data = pd.read_csv("data.csv")

# Encode categorical columns (Yes/No → 1/0, Pass/Fail → 1/0)
le_extra = LabelEncoder()
le_result = LabelEncoder()

data['Extracurriculars'] = le_extra.fit_transform(data['Extracurriculars'])
data['Result_Label'] = le_result.fit_transform(data['Result'])

# Features and target
X = data[['Math', 'Science', 'English', 'Attendance', 'Study_Hours', 'Extracurriculars']]
y = data['Result_Label']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy*100:.2f}%")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Fail', 'Pass'], yticklabels=['Fail', 'Pass'])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

# Save model only
joblib.dump(model, "student_model.pkl")
print("💾 Model saved successfully as student_model.pkl")
