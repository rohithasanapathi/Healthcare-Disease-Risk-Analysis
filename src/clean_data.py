import pandas as pd

# -----------------------------------------
# 1. Load original dataset
# -----------------------------------------

input_file = "data/original/healthcare-dataset-stroke-data.csv"

df = pd.read_csv(input_file)

print("Original dataset shape:", df.shape)


# -----------------------------------------
# 2. Check duplicate records
# -----------------------------------------

duplicates = df.duplicated().sum()

print("Duplicate rows:", duplicates)


# -----------------------------------------
# 3. Handle missing BMI values
# -----------------------------------------

missing_bmi_before = df["bmi"].isna().sum()

bmi_median = df["bmi"].median()

df["bmi"] = df["bmi"].fillna(bmi_median)

missing_bmi_after = df["bmi"].isna().sum()

print("Missing BMI before cleaning:", missing_bmi_before)
print("BMI median used:", bmi_median)
print("Missing BMI after cleaning:", missing_bmi_after)


# -----------------------------------------
# 4. Save cleaned dataset
# -----------------------------------------

output_file = "data/cleaned/healthcare_stroke_cleaned.csv"

df.to_csv(output_file, index=False)

print("\nCleaned dataset saved successfully.")
print("Output file:", output_file)
print("Cleaned dataset shape:", df.shape)