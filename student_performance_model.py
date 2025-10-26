# Step 3: Predictive Model – Student Pass/Fail Prediction
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("data.csv")

# Encode categorical columns
le = LabelEncoder()
data['Extracurriculars'] = le.fit_transform(data['Extracurriculars'])
data['Passed_Label'] = le.fit_transform(data['Passed'])

# Features and target
X = data[['Math', 'Science', 'English', 'Attendance', 'Study_Hours', 'Extracurriculars']]
y = data['Passed_Label']

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy*100:.2f}%")

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# Optional: Visualize confusion matrix
plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Fail','Pass'], yticklabels=['Fail','Pass'])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

# Optional: Predict for a new student
# Format: [Math, Science, English, Attendance, Study_Hours, Extracurriculars (1=Yes,0=No)]
new_student = [[85, 80, 88, 90, 10, 1]] 
prediction = model.predict(new_student)
print("New Student Prediction:", "Pass" if prediction[0] == 1 else "Fail")
