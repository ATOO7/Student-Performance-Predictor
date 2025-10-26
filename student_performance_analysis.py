# Step 2: Data Analysis & Visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("data.csv")

# Compute average score
data['Average'] = data[['Math','Science','English']].mean(axis=1)

# Assign grades based on average
def assign_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

data['Grade'] = data['Average'].apply(assign_grade)

# Display dataset head
print("Dataset Head:")
print(data.head(), "\n")

# Pass/Fail summary
print("Pass/Fail Summary:")
print(data['Passed'].value_counts(), "\n")

# Grade distribution
print("Grade Distribution:")
print(data['Grade'].value_counts(), "\n")

# Visualization 1: Average Scores per Student
plt.figure(figsize=(10,5))
sns.barplot(x='Student', y='Average', data=data, palette='cool')
plt.xticks(rotation=45)
plt.title("Average Scores per Student")
plt.tight_layout()
plt.show()

# Visualization 2: Grade Distribution
plt.figure(figsize=(6,4))
sns.countplot(x='Grade', data=data, palette='viridis')
plt.title("Grade Distribution")
plt.show()

# Visualization 3: Feature Correlation Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(data[['Math','Science','English','Attendance','Study_Hours']].corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correlation")
plt.show()
