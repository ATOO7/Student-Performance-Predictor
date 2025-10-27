import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load trained model
model = joblib.load("student_model.pkl")

# Define feature names (same order as training)
features = ['Math', 'Science', 'English', 'Attendance', 'Study_Hours', 'Extracurriculars']

# Get feature importances from the Random Forest model
importances = model.feature_importances_

# Create a DataFrame for better visualization
importance_df = pd.DataFrame({
    'Feature': features,
    'Importance': importances
}).sort_values(by='Importance', ascending=False)

# Print importance values
print("📊 Feature Importance:\n")
print(importance_df, "\n")

# Visualize using Seaborn
plt.figure(figsize=(8,5))
sns.barplot(x='Importance', y='Feature', data=importance_df, palette='viridis')
plt.title('Feature Importance in Student Performance Prediction', fontsize=13)
plt.xlabel('Importance Score')
plt.ylabel('Feature')
plt.tight_layout()
plt.show()
