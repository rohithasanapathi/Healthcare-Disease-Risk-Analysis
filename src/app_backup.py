import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Healthcare Disease Risk Analysis",
    page_icon="🏥",
    layout="wide"
)


# ==========================================
# LOAD DATA
# ==========================================

file_path = "data/cleaned/healthcare_stroke_cleaned.csv"

df = pd.read_csv(file_path)


# ==========================================
# TITLE
# ==========================================

st.title("🏥 Healthcare Disease Risk Factor Analysis")

st.write(
    "Interactive analysis of relationships between "
    "patient health factors and stroke."
)


# ==========================================
# DATASET OVERVIEW
# ==========================================

st.header("Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Patients",
        len(df)
    )

with col2:
    st.metric(
        "Stroke Cases",
        int(df["stroke"].sum())
    )

with col3:
    st.metric(
        "Stroke Rate",
        f"{df['stroke'].mean() * 100:.2f}%"
    )


# ==========================================
# DATA PREVIEW
# ==========================================

st.subheader("Dataset Preview")

st.dataframe(
    df.head(10),
    use_container_width=True
)
# ==========================================
# CORRELATION ANALYSIS
# ==========================================

st.header("🔗 Correlation Analysis")

st.write(
    "Correlation measures the strength and direction of the "
    "linear relationship between health-related variables. "
    "Values range from -1 to +1."
)


# Select health-related numerical features
health_features = [
    "age",
    "bmi",
    "avg_glucose_level",
    "hypertension",
    "heart_disease",
    "stroke"
]

health_df = df[health_features]


# Calculate correlation matrix
correlation_matrix = health_df.corr()


# Display correlation matrix
st.subheader("Correlation Matrix")

st.dataframe(
    correlation_matrix.round(4),
    use_container_width=True
)


# ==========================================
# CORRELATION HEATMAP
# ==========================================

st.subheader("Correlation Heatmap")

fig, ax = plt.subplots(figsize=(10, 7))

sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    ax=ax
)

ax.set_title("Healthcare Risk Factor Correlation Matrix")

st.pyplot(fig)


# ==========================================
# RISK FACTOR CORRELATION WITH STROKE
# ==========================================

st.subheader("Risk Factor Correlation with Stroke")

stroke_correlations = (
    correlation_matrix["stroke"]
    .drop("stroke")
    .sort_values(ascending=False)
)

st.dataframe(
    stroke_correlations.round(4).to_frame(
        name="Correlation with Stroke"
    ),
    use_container_width=True
)


# ==========================================
# STRONGEST CORRELATED RISK FACTOR
# ==========================================

strongest_factor = stroke_correlations.idxmax()
strongest_value = stroke_correlations.max()

st.success(
    f"Strongest observed correlation with stroke: "
    f"{strongest_factor} (r = {strongest_value:.4f})"
)
# ==========================================
# COVARIANCE ANALYSIS
# ==========================================

st.header("📊 Covariance Analysis")

st.write(
    "Covariance indicates how two numerical variables vary together. "
    "A positive value indicates that the variables tend to increase "
    "together, while a negative value indicates an opposite tendency."
)


# Calculate covariance matrix
covariance_matrix = health_df.cov()


# Display covariance matrix
st.subheader("Covariance Matrix")

st.dataframe(
    covariance_matrix.round(4),
    use_container_width=True
)


# ==========================================
# COVARIANCE HEATMAP
# ==========================================

st.subheader("Covariance Heatmap")

fig, ax = plt.subplots(figsize=(10, 7))

sns.heatmap(
    covariance_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    ax=ax
)

ax.set_title("Healthcare Risk Factor Covariance Matrix")

st.pyplot(fig)
# ==========================================
# INTERACTIVE RISK FACTOR EXPLORER
# ==========================================

st.header("🔍 Interactive Risk Factor Explorer")

st.write(
    "Select two health-related variables to explore their "
    "relationship. The prototype automatically selects an "
    "appropriate visualization based on the selected variables."
)


# Available variables
explorer_features = [
    "age",
    "bmi",
    "avg_glucose_level",
    "hypertension",
    "heart_disease",
    "stroke"
]


# User selections
col1, col2 = st.columns(2)

with col1:
    x_variable = st.selectbox(
        "Select X-axis variable",
        explorer_features,
        index=0
    )

with col2:
    y_variable = st.selectbox(
        "Select Y-axis variable",
        explorer_features,
        index=5
    )


# Calculate correlation
selected_correlation = df[x_variable].corr(df[y_variable])


# Display correlation
st.metric(
    "Correlation",
    f"{selected_correlation:.4f}"
)


# ==========================================
# VISUALIZATION
# ==========================================

binary_features = [
    "hypertension",
    "heart_disease",
    "stroke"
]


# Both variables are binary
if x_variable in binary_features and y_variable in binary_features:

    st.subheader(
        f"{x_variable} vs {y_variable}"
    )

    grouped_data = (
        df.groupby([x_variable, y_variable])
        .size()
        .reset_index(name="count")
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    sns.barplot(
        data=grouped_data,
        x=x_variable,
        y="count",
        hue=y_variable,
        ax=ax
    )

    ax.set_title(
        f"{x_variable} vs {y_variable}"
    )

    ax.set_ylabel("Number of Patients")

    st.pyplot(fig)

    plt.close(fig)


# One variable is binary
elif x_variable in binary_features or y_variable in binary_features:

    st.subheader(
        f"{x_variable} vs {y_variable}"
    )

    if x_variable in binary_features:
        binary_variable = x_variable
        numerical_variable = y_variable
    else:
        binary_variable = y_variable
        numerical_variable = x_variable

    fig, ax = plt.subplots(figsize=(9, 5))

    sns.boxplot(
        data=df,
        x=binary_variable,
        y=numerical_variable,
        ax=ax
    )

    ax.set_title(
        f"{numerical_variable} by {binary_variable}"
    )

    st.pyplot(fig)

    plt.close(fig)


# Both variables are continuous
else:

    st.subheader(
        f"{x_variable} vs {y_variable}"
    )

    fig, ax = plt.subplots(figsize=(9, 5))

    sns.scatterplot(
        data=df,
        x=x_variable,
        y=y_variable,
        alpha=0.5,
        ax=ax
    )

    ax.set_title(
        f"{x_variable} vs {y_variable}"
    )

    st.pyplot(fig)

    plt.close(fig)
    # ==========================================
# KEY FINDINGS
# ==========================================

st.header("📌 Key Findings")

st.write(
    "The following findings are based on the correlation analysis "
    "of the selected healthcare risk factors."
)


# Get correlations with stroke
stroke_correlations = (
    correlation_matrix["stroke"]
    .drop("stroke")
    .sort_values(ascending=False)
)


# Strongest factor
strongest_factor = stroke_correlations.index[0]
strongest_correlation = stroke_correlations.iloc[0]


# Display strongest factor
st.success(
    f"🏆 Strongest observed correlation with stroke: "
    f"{strongest_factor} (r = {strongest_correlation:.4f})"
)


# Findings in columns
col1, col2 = st.columns(2)

with col1:

    st.subheader("Positive Associations")

    for factor, value in stroke_correlations.items():

        if value > 0:
            st.write(
                f"• **{factor}**: r = {value:.4f}"
            )


with col2:

    st.subheader("Interpretation")

    st.write(
        f"**Age** shows the strongest observed linear "
        f"correlation with stroke (r = {stroke_correlations['age']:.4f})."
    )

    st.write(
        f"**Heart disease** has a weaker positive association "
        f"with stroke (r = {stroke_correlations['heart_disease']:.4f})."
    )

    st.write(
        f"**Average glucose level** also shows a weak positive "
        f"association with stroke (r = {stroke_correlations['avg_glucose_level']:.4f})."
    )

    st.write(
        f"**Hypertension** has a weak positive correlation "
        f"with stroke (r = {stroke_correlations['hypertension']:.4f})."
    )

    st.write(
        f"**BMI** has a very weak linear correlation "
        f"with stroke (r = {stroke_correlations['bmi']:.4f})."
    )


# ==========================================
# IMPORTANT INTERPRETATION
# ==========================================

st.info(
    "⚠️ Correlation indicates statistical association, "
    "not causation. These results do not prove that a risk "
    "factor directly causes stroke."
)
