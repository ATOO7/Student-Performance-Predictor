import pandas as pd

# Load your existing dataset
data = pd.read_csv("data.csv")

# 1️⃣ Rename 'Passed' column to 'Result'
data.rename(columns={'Passed': 'Result'}, inplace=True)

# 2️⃣ Replace 'Yes' with 'Pass' and 'No' with 'Fail' in the 'Result' column
data['Result'] = data['Result'].replace({'Yes': 'Pass', 'No': 'Fail'})

# 3️⃣ Save cleaned data back to the same CSV
data.to_csv("data.csv", index=False)

print("✅ Dataset cleaned successfully!")
print(data.head())
