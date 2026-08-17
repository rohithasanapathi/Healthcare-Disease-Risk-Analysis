import pandas as pd

# Load original dataset
file_path = "data/original/healthcare-dataset-stroke-data.csv"
df = pd.read_csv(file_path)


def analyze_outliers(column):
    data = df[column].dropna()

    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = data[
        (data < lower_bound) |
        (data > upper_bound)
    ]

    print(f"\n===== {column.upper()} =====")
    print(f"Q1: {Q1:.2f}")
    print(f"Q3: {Q3:.2f}")
    print(f"IQR: {IQR:.2f}")
    print(f"Lower bound: {lower_bound:.2f}")
    print(f"Upper bound: {upper_bound:.2f}")
    print(f"Number of outliers: {len(outliers)}")
    print(f"Percentage of outliers: {len(outliers) / len(data) * 100:.2f}%")


analyze_outliers("bmi")
analyze_outliers("avg_glucose_level")
