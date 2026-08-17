import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load original dataset
file_path = "data/original/healthcare-dataset-stroke-data.csv"
df = pd.read_csv(file_path)

# -----------------------------
# BMI Distribution
# -----------------------------

plt.figure(figsize=(8, 5))
sns.histplot(df["bmi"].dropna(), kde=True)
plt.title("Distribution of BMI")
plt.xlabel("BMI")
plt.ylabel("Number of Patients")
plt.tight_layout()
plt.show()

# -----------------------------
# BMI Box Plot
# -----------------------------

plt.figure(figsize=(8, 4))
sns.boxplot(x=df["bmi"].dropna())
plt.title("BMI Box Plot")
plt.xlabel("BMI")
plt.tight_layout()
plt.show()

# -----------------------------
# Glucose Distribution
# -----------------------------

plt.figure(figsize=(8, 5))
sns.histplot(df["avg_glucose_level"], kde=True)
plt.title("Distribution of Average Glucose Level")
plt.xlabel("Average Glucose Level")
plt.ylabel("Number of Patients")
plt.tight_layout()
plt.show()

# -----------------------------
# Glucose Box Plot
# -----------------------------

plt.figure(figsize=(8, 4))
sns.boxplot(x=df["avg_glucose_level"])
plt.title("Average Glucose Level Box Plot")
plt.xlabel("Average Glucose Level")
plt.tight_layout()
plt.show()