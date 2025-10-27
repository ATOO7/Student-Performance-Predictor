import pandas as pd
import joblib

# Load the trained model
model = joblib.load("student_model.pkl")

# Load existing dataset
data = pd.read_csv("data.csv")

print("\n🎓 Add a New Student Record")
print("----------------------------")

# Take user input
student_name = input("Enter Student Name: ").strip()
math = int(input("Enter Math marks (0–100): "))
science = int(input("Enter Science marks (0–100): "))
english = int(input("Enter English marks (0–100): "))
attendance = int(input("Enter Attendance percentage (0–100): "))
study_hours = float(input("Enter average Study Hours per week: "))
extra = input("Did the student participate in Extracurriculars? (Yes/No): ").capitalize()

# Convert extracurriculars to numeric
extra_encoded = 1 if extra == "Yes" else 0

# Predict
new_data = [[math, science, english, attendance, study_hours, extra_encoded]]
prediction = model.predict(new_data)[0]

# Decode prediction
result = "Pass" if prediction == 1 else "Fail"

# Show result
print(f"\n✅ Prediction complete! {student_name} is likely to: {result}")

# Append new record
new_row = {
    "Student": student_name,
    "Math": math,
    "Science": science,
    "English": english,
    "Attendance": attendance,
    "Study_Hours": study_hours,
    "Extracurriculars": extra,
    "Result": result
}

data = pd.concat([data, pd.DataFrame([new_row])], ignore_index=True)
data.to_csv("data.csv", index=False)

print("📁 Student record saved successfully in data.csv\n")
