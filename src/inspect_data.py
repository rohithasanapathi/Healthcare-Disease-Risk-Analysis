import pandas as pd

# Path to the organization's dataset copy
file_path = "data/original/healthcare-dataset-stroke-data.csv"

# Read dataset
df = pd.read_csv(file_path)

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATASET SHAPE =====")
print(df.shape)

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())

print("\n===== BASIC STATISTICS =====")
print(df.describe(include="all"))
print("\n===== UNIQUE VALUES =====")

categorical_columns = [
    "gender",
    "ever_married",
    "work_type",
    "Residence_type",
    "smoking_status"
]

for column in categorical_columns:
    print(f"\n{column}:")
    print(df[column].unique())


print("\n===== VALUE COUNTS =====")

for column in categorical_columns:
    print(f"\n{column}:")
    print(df[column].value_counts(dropna=False))


print("\n===== NUMERICAL RANGES =====")

numerical_columns = [
    "age",
    "avg_glucose_level",
    "bmi"
]

for column in numerical_columns:
    print(
        f"{column}: "
        f"min={df[column].min()}, "
        f"max={df[column].max()}"
    )


print("\n===== HEALTH INDICATOR COUNTS =====")

health_columns = [
    "hypertension",
    "heart_disease",
    "stroke"
]

for column in health_columns:
    print(f"\n{column}:")
    print(df[column].value_counts())