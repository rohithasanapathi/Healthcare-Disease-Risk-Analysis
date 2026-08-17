import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. Load cleaned dataset
# ==========================================

file_path = "data/cleaned/healthcare_stroke_cleaned.csv"

df = pd.read_csv(file_path)

print("Cleaned dataset shape:", df.shape)


# ==========================================
# 2. Select health-related features
# ==========================================

health_features = [
    "age",
    "bmi",
    "avg_glucose_level",
    "hypertension",
    "heart_disease",
    "stroke"
]

health_df = df[health_features]

print("\n===== HEALTH FEATURES =====")
print(health_df.head())


# ==========================================
# 3. Descriptive statistics
# ==========================================

print("\n===== DESCRIPTIVE STATISTICS =====")
print(health_df.describe())


# ==========================================
# 4. Covariance matrix
# ==========================================

covariance_matrix = health_df.cov()

print("\n===== COVARIANCE MATRIX =====")
print(covariance_matrix)


# ==========================================
# 5. Correlation matrix
# ==========================================

correlation_matrix = health_df.corr()

print("\n===== CORRELATION MATRIX =====")
print(correlation_matrix)


# ==========================================
# 6. Save covariance heatmap
# ==========================================

plt.figure(figsize=(10, 7))

sns.heatmap(
    covariance_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm"
)

plt.title("Healthcare Risk Factor Covariance Matrix")
plt.tight_layout()

plt.savefig(
    "outputs/figures/covariance_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ==========================================
# 7. Save correlation heatmap
# ==========================================

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)

plt.title("Healthcare Risk Factor Correlation Matrix")
plt.tight_layout()

plt.savefig(
    "outputs/figures/correlation_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ==========================================
# 8. Age vs Stroke
# ==========================================

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="stroke",
    y="age"
)

plt.title("Age Distribution by Stroke Status")
plt.xlabel("Stroke (0 = No, 1 = Yes)")
plt.ylabel("Age")

plt.tight_layout()

plt.savefig(
    "outputs/figures/age_vs_stroke.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ==========================================
# 9. BMI vs Stroke
# ==========================================

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="stroke",
    y="bmi"
)

plt.title("BMI Distribution by Stroke Status")
plt.xlabel("Stroke (0 = No, 1 = Yes)")
plt.ylabel("BMI")

plt.tight_layout()

plt.savefig(
    "outputs/figures/bmi_vs_stroke.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ==========================================
# 10. Glucose vs Stroke
# ==========================================

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="stroke",
    y="avg_glucose_level"
)

plt.title("Average Glucose Level by Stroke Status")
plt.xlabel("Stroke (0 = No, 1 = Yes)")
plt.ylabel("Average Glucose Level")

plt.tight_layout()

plt.savefig(
    "outputs/figures/glucose_vs_stroke.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


print("\n===== ANALYSIS COMPLETE =====")
print("Figures saved in: outputs/figures/")
# ==========================================
# 11. Rank risk factors by correlation with stroke
# ==========================================

stroke_correlations = correlation_matrix["stroke"].drop("stroke")

stroke_correlations = stroke_correlations.abs().sort_values(
    ascending=False
)

print("\n===== RISK FACTORS RANKED BY CORRELATION WITH STROKE =====")

for factor, value in stroke_correlations.items():
    original_value = correlation_matrix.loc[factor, "stroke"]
    print(f"{factor}: {original_value:.4f}")