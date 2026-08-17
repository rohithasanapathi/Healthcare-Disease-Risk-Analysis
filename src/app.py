import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Healthcare Risk Analytics",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PROFESSIONAL UI STYLING
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #f5f8fb;
    }

    .main .block-container {
        max-width: 1500px;
        padding-top: 2rem;
        padding-bottom: 3rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }

    section[data-testid="stSidebar"] {
        background-color: #102a43;
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }

    h1 {
        color: #12344d;
        font-weight: 700;
    }

    h2 {
        color: #12344d;
        font-weight: 650;
    }

    h3 {
        color: #1f4e6d;
        font-weight: 600;
    }

    div[data-testid="stMetric"] {
        background-color: white;
        border: 1px solid #d9e2ec;
        border-radius: 12px;
        padding: 18px 20px;
        box-shadow: 0 2px 8px rgba(16, 42, 67, 0.06);
    }

    div[data-testid="stMetricLabel"] {
        color: #627d98;
        font-weight: 600;
    }

    div[data-testid="stMetricValue"] {
        color: #12344d;
        font-weight: 700;
    }

    div[data-testid="stDataFrame"] {
        border: 1px solid #d9e2ec;
        border-radius: 10px;
        overflow: hidden;
    }

    .stDownloadButton button {
        background-color: #1677a8;
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 600;
    }

    .stDownloadButton button:hover {
        background-color: #125f86;
        color: white;
    }

    div[data-testid="stAlert"] {
        border-radius: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD DATA
# ============================================================

file_path = "data/cleaned/healthcare_stroke_cleaned.csv"

try:

    df = pd.read_csv(file_path)

except FileNotFoundError:

    st.error(
        "Dataset not found. Please check that the file exists at: "
        "data/cleaned/healthcare_stroke_cleaned.csv"
    )

    st.stop()


# ============================================================
# COMMON HEALTH DATA
# ============================================================

health_features = [
    "age",
    "bmi",
    "avg_glucose_level",
    "hypertension",
    "heart_disease",
    "stroke"
]

health_df = df[health_features]

correlation_matrix = health_df.corr()

covariance_matrix = health_df.cov()

stroke_correlations = (
    correlation_matrix["stroke"]
    .drop("stroke")
    .sort_values(ascending=False)
)


# ============================================================
# COMMON VALUES
# ============================================================

total_patients = len(df)

stroke_cases = int(
    df["stroke"].sum()
)

non_stroke_cases = int(
    (df["stroke"] == 0).sum()
)

stroke_rate = (
    df["stroke"].mean() * 100
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🏥 Healthcare Analytics")

st.sidebar.caption(
    "Stroke Risk Factor Analysis"
)

st.sidebar.divider()

st.sidebar.subheader("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Overview",
        "Correlation Analysis",
        "Covariance Analysis",
        "Risk Factor Explorer",
        "Patient Risk Profile",
        "Key Findings",
        "Methodology"
    ],
    label_visibility="collapsed"
)

st.sidebar.divider()

st.sidebar.subheader("Dataset Summary")

st.sidebar.write(
    f"**Patients:** {total_patients:,}"
)

st.sidebar.write(
    f"**Attributes:** {len(df.columns)}"
)

st.sidebar.write(
    f"**Stroke Cases:** {stroke_cases:,}"
)

st.sidebar.divider()

st.sidebar.warning(
    "Statistical analysis only — "
    "not a medical diagnosis."
)


# ============================================================
# MAIN HEADER
# ============================================================

st.title(
    "🏥 Healthcare Disease Risk Factor Analysis"
)

st.caption(
    "Interactive statistical exploration of patient health "
    "factors and observed stroke outcomes."
)

st.divider()


# ============================================================
# OVERVIEW
# ============================================================

if page == "Overview":

    st.header("📋 Dataset Overview")

    st.write(
        "This dashboard explores relationships between "
        "selected health-related factors and stroke using "
        "statistical analysis and interactive visualization."
    )

    st.divider()

    # --------------------------------------------------------
    # KPI CARDS
    # --------------------------------------------------------

    st.subheader("Dashboard Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Total Patients",
            f"{total_patients:,}"
        )

    with col2:

        st.metric(
            "Stroke Cases",
            f"{stroke_cases:,}"
        )

    with col3:

        st.metric(
            "Non-Stroke Cases",
            f"{non_stroke_cases:,}"
        )

    with col4:

        st.metric(
            "Observed Stroke Rate",
            f"{stroke_rate:.2f}%"
        )

    st.write("")

    # --------------------------------------------------------
    # DATASET PREVIEW
    # --------------------------------------------------------

    st.subheader("📄 Dataset Preview")

    st.dataframe(
        df.head(10),
        use_container_width=True,
        height=350
    )

    # --------------------------------------------------------
    # STROKE DISTRIBUTION
    # --------------------------------------------------------

    st.subheader(
        "🩺 Stroke Outcome Distribution"
    )

    stroke_counts = (
        df["stroke"]
        .value_counts()
        .sort_index()
    )

    stroke_labels = [
        "No Stroke",
        "Stroke"
    ]

    stroke_values = [
        stroke_counts.get(0, 0),
        stroke_counts.get(1, 0)
    ]

    fig, ax = plt.subplots(
        figsize=(9, 5)
    )

    sns.barplot(
        x=stroke_labels,
        y=stroke_values,
        ax=ax
    )

    ax.set_title(
        "Distribution of Stroke Outcomes",
        fontsize=14,
        fontweight="bold"
    )

    ax.set_xlabel(
        "Stroke Outcome"
    )

    ax.set_ylabel(
        "Number of Patients"
    )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    for i, value in enumerate(stroke_values):

        ax.text(
            i,
            value,
            f"{value:,}",
            ha="center",
            va="bottom",
            fontweight="bold"
        )

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)

    st.info(
        f"The dataset contains {stroke_cases:,} stroke cases "
        f"out of {total_patients:,} patients, corresponding "
        f"to an observed stroke rate of {stroke_rate:.2f}%."
    )

    # --------------------------------------------------------
    # DATA QUALITY
    # --------------------------------------------------------

    st.subheader(
        "🔎 Data Quality Summary"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Missing Values",
            int(df.isnull().sum().sum())
        )

    with col2:

        st.metric(
            "Duplicate Rows",
            int(df.duplicated().sum())
        )

    with col3:

        st.metric(
            "Total Columns",
            len(df.columns)
        )

    # --------------------------------------------------------
    # DOWNLOAD
    # --------------------------------------------------------

    st.subheader(
        "⬇️ Download Cleaned Dataset"
    )

    st.write(
        "Download the cleaned dataset used for the analysis."
    )

    csv_data = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="Download Cleaned CSV",
        data=csv_data,
        file_name="healthcare_stroke_cleaned.csv",
        mime="text/csv"
    )


# ============================================================
# CORRELATION ANALYSIS
# ============================================================

elif page == "Correlation Analysis":

    st.header(
        "🔗 Correlation Analysis"
    )

    st.write(
        "Correlation measures the strength and direction "
        "of a linear relationship between two variables. "
        "The Pearson correlation coefficient ranges from "
        "-1 to +1."
    )

    st.divider()

    st.subheader(
        "Correlation Matrix"
    )

    st.dataframe(
        correlation_matrix.round(4),
        use_container_width=True
    )

    st.subheader(
        "Correlation Heatmap"
    )

    fig, ax = plt.subplots(
        figsize=(10, 7)
    )

    sns.heatmap(
        correlation_matrix,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        vmin=-1,
        vmax=1,
        linewidths=0.5,
        ax=ax
    )

    ax.set_title(
        "Healthcare Risk Factor Correlation Matrix",
        fontsize=14,
        fontweight="bold"
    )

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)

    st.subheader(
        "Observed Correlation with Stroke"
    )

    st.dataframe(
        stroke_correlations.round(4).to_frame(
            name="Correlation with Stroke"
        ),
        use_container_width=True
    )

    strongest_factor = (
        stroke_correlations.idxmax()
    )

    strongest_value = (
        stroke_correlations.max()
    )

    st.success(
        f"🏆 Strongest observed linear correlation with "
        f"stroke: **{strongest_factor}** "
        f"(r = {strongest_value:.4f})"
    )

    st.info(
        "Correlation indicates statistical association, "
        "not causation or clinical risk."
    )


# ============================================================
# COVARIANCE ANALYSIS
# ============================================================

elif page == "Covariance Analysis":

    st.header(
        "📊 Covariance Analysis"
    )

    st.write(
        "Covariance measures how two variables vary "
        "together. A positive value indicates that the "
        "variables tend to increase together, while a "
        "negative value indicates an opposite tendency."
    )

    st.divider()

    st.subheader(
        "Covariance Matrix"
    )

    st.dataframe(
        covariance_matrix.round(4),
        use_container_width=True
    )

    st.subheader(
        "Covariance Heatmap"
    )

    fig, ax = plt.subplots(
        figsize=(10, 7)
    )

    sns.heatmap(
        covariance_matrix,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        linewidths=0.5,
        ax=ax
    )

    ax.set_title(
        "Healthcare Risk Factor Covariance Matrix",
        fontsize=14,
        fontweight="bold"
    )

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)

    st.info(
        "Unlike correlation, covariance is not standardized. "
        "Its magnitude depends on the units and scales of "
        "the variables."
    )


# ============================================================
# RISK FACTOR EXPLORER
# ============================================================

elif page == "Risk Factor Explorer":

    st.header(
        "🔍 Interactive Risk Factor Explorer"
    )

    st.write(
        "Select two health-related variables to explore "
        "their relationship. The dashboard automatically "
        "selects a suitable visualization."
    )

    st.divider()

    explorer_features = [
        "age",
        "bmi",
        "avg_glucose_level",
        "hypertension",
        "heart_disease",
        "stroke"
    ]

    st.subheader(
        "Select Variables"
    )

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

    selected_correlation = (
        df[x_variable].corr(
            df[y_variable]
        )
    )

    absolute_correlation = abs(
        selected_correlation
    )

    if absolute_correlation < 0.10:
        correlation_strength = "Very Weak"

    elif absolute_correlation < 0.30:
        correlation_strength = "Weak"

    elif absolute_correlation < 0.50:
        correlation_strength = "Moderate"

    elif absolute_correlation < 0.70:
        correlation_strength = "Strong"

    else:
        correlation_strength = "Very Strong"

    if selected_correlation > 0:
        correlation_direction = "Positive"

    elif selected_correlation < 0:
        correlation_direction = "Negative"

    else:
        correlation_direction = "No Linear"

    st.subheader(
        "Relationship Summary"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Pearson Correlation",
            f"{selected_correlation:.4f}"
        )

    with col2:

        st.metric(
            "Strength",
            correlation_strength
        )

    with col3:

        st.metric(
            "Direction",
            correlation_direction
        )

    st.info(
        f"The selected variables show a "
        f"**{correlation_strength.lower()} "
        f"{correlation_direction.lower()} linear relationship** "
        f"(r = {selected_correlation:.4f})."
    )

    binary_features = [
        "hypertension",
        "heart_disease",
        "stroke"
    ]

    # --------------------------------------------------------
    # BOTH BINARY
    # --------------------------------------------------------

    if (
        x_variable in binary_features
        and y_variable in binary_features
    ):

        st.subheader(
            f"{x_variable} vs {y_variable}"
        )

        grouped_data = (
            df.groupby(
                [x_variable, y_variable]
            )
            .size()
            .reset_index(
                name="count"
            )
        )

        fig, ax = plt.subplots(
            figsize=(8, 5)
        )

        sns.barplot(
            data=grouped_data,
            x=x_variable,
            y="count",
            hue=y_variable,
            ax=ax
        )

        ax.set_title(
            f"{x_variable} vs {y_variable}",
            fontweight="bold"
        )

        ax.set_ylabel(
            "Number of Patients"
        )

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        plt.tight_layout()

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)

    # --------------------------------------------------------
    # ONE BINARY
    # --------------------------------------------------------

    elif (
        x_variable in binary_features
        or y_variable in binary_features
    ):

        st.subheader(
            f"{x_variable} vs {y_variable}"
        )

        if x_variable in binary_features:

            binary_variable = x_variable
            numerical_variable = y_variable

        else:

            binary_variable = y_variable
            numerical_variable = x_variable

        fig, ax = plt.subplots(
            figsize=(9, 5)
        )

        sns.boxplot(
            data=df,
            x=binary_variable,
            y=numerical_variable,
            ax=ax
        )

        ax.set_title(
            f"{numerical_variable} by "
            f"{binary_variable}",
            fontweight="bold"
        )

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        plt.tight_layout()

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)

    # --------------------------------------------------------
    # BOTH CONTINUOUS
    # --------------------------------------------------------

    else:

        st.subheader(
            f"{x_variable} vs {y_variable}"
        )

        fig, ax = plt.subplots(
            figsize=(9, 5)
        )

        sns.scatterplot(
            data=df,
            x=x_variable,
            y=y_variable,
            alpha=0.5,
            ax=ax
        )

        ax.set_title(
            f"{x_variable} vs {y_variable}",
            fontweight="bold"
        )

        ax.set_xlabel(
            x_variable
        )

        ax.set_ylabel(
            y_variable
        )

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        plt.tight_layout()

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)


# ============================================================
# PATIENT RISK PROFILE
# ============================================================

elif page == "Patient Risk Profile":

    st.header(
        "🧑‍⚕️ Patient Risk Profile"
    )

    st.write(
        "Enter patient health characteristics to explore "
        "how the selected profile compares with observed "
        "patterns in the dataset."
    )

    st.warning(
        "⚠️ Exploratory statistical profile only. "
        "It does not provide a medical diagnosis or "
        "individual stroke prediction."
    )

    st.divider()

    st.subheader(
        "Patient Information"
    )

    col1, col2 = st.columns(2)

    with col1:

        patient_age = st.number_input(
            "Age",
            min_value=0.0,
            max_value=100.0,
            value=45.0,
            step=1.0
        )

        patient_bmi = st.number_input(
            "BMI",
            min_value=5.0,
            max_value=100.0,
            value=28.1,
            step=0.1
        )

        patient_glucose = st.number_input(
            "Average Glucose Level",
            min_value=40.0,
            max_value=300.0,
            value=100.0,
            step=0.1
        )

    with col2:

        patient_hypertension = st.selectbox(
            "Hypertension",
            ["No", "Yes"]
        )

        patient_heart_disease = st.selectbox(
            "Heart Disease",
            ["No", "Yes"]
        )

    hypertension_value = (
        1
        if patient_hypertension == "Yes"
        else 0
    )

    heart_disease_value = (
        1
        if patient_heart_disease == "Yes"
        else 0
    )

    st.subheader(
        "Patient Profile"
    )

    profile_data = pd.DataFrame({

        "Feature": [
            "Age",
            "BMI",
            "Average Glucose Level",
            "Hypertension",
            "Heart Disease"
        ],

        "Patient Value": [
            patient_age,
            patient_bmi,
            patient_glucose,
            hypertension_value,
            heart_disease_value
        ],

        "Dataset Mean": [
            df["age"].mean(),
            df["bmi"].mean(),
            df["avg_glucose_level"].mean(),
            df["hypertension"].mean(),
            df["heart_disease"].mean()
        ]
    })

    st.dataframe(
        profile_data.round(2),
        use_container_width=True
    )

    st.subheader(
        "Patient Values vs Dataset Mean"
    )

    comparison_data = pd.DataFrame({

        "Feature": [
            "Age",
            "BMI",
            "Average Glucose Level"
        ],

        "Patient": [
            patient_age,
            patient_bmi,
            patient_glucose
        ],

        "Dataset Mean": [
            df["age"].mean(),
            df["bmi"].mean(),
            df["avg_glucose_level"].mean()
        ]
    })

    fig, ax = plt.subplots(
        figsize=(9, 5)
    )

    comparison_data.set_index(
        "Feature"
    ).plot(
        kind="bar",
        ax=ax
    )

    ax.set_title(
        "Patient Values Compared with Dataset Mean",
        fontweight="bold"
    )

    ax.set_ylabel(
        "Value"
    )

    ax.tick_params(
        axis="x",
        rotation=0
    )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)

    st.subheader(
        "Observed Stroke Associations"
    )

    association_data = (
        stroke_correlations
        .round(4)
        .to_frame(
            name="Correlation with Stroke"
        )
    )

    st.dataframe(
        association_data,
        use_container_width=True
    )

    st.info(
        "These correlation values describe relationships "
        "observed across the dataset. They do not calculate "
        "the individual patient's probability of stroke."
    )


# ============================================================
# KEY FINDINGS
# ============================================================

elif page == "Key Findings":

    st.header(
        "📌 Key Findings"
    )

    st.write(
        "The following findings summarize the observed "
        "statistical relationships between selected health "
        "factors and stroke."
    )

    st.divider()

    strongest_factor = (
        stroke_correlations.index[0]
    )

    strongest_correlation = (
        stroke_correlations.iloc[0]
    )

    st.success(
        f"🏆 Strongest observed correlation with stroke: "
        f"**{strongest_factor}** "
        f"(r = {strongest_correlation:.4f})"
    )

    st.subheader(
        "Risk Factors Ranked by Correlation with Stroke"
    )

    ranking_data = (
        stroke_correlations
        .sort_values()
    )

    fig, ax = plt.subplots(
        figsize=(9, 5)
    )

    sns.barplot(
        x=ranking_data.values,
        y=ranking_data.index,
        ax=ax
    )

    ax.set_title(
        "Observed Correlation of Health Factors with Stroke",
        fontweight="bold"
    )

    ax.set_xlabel(
        "Correlation with Stroke"
    )

    ax.set_ylabel(
        "Health Factor"
    )

    ax.axvline(
        0,
        linewidth=1
    )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "Positive Associations"
        )

        for factor, value in (
            stroke_correlations.items()
        ):

            if value > 0:

                st.write(
                    f"• **{factor}**: "
                    f"r = {value:.4f}"
                )

    with col2:

        st.subheader(
            "Statistical Interpretation"
        )

        st.write(
            f"**Age** shows the strongest observed "
            f"linear correlation with stroke "
            f"(r = {stroke_correlations['age']:.4f})."
        )

        st.write(
            f"**Heart disease** has a weaker positive "
            f"association with stroke "
            f"(r = {stroke_correlations['heart_disease']:.4f})."
        )

        st.write(
            f"**Average glucose level** shows a weak "
            f"positive association with stroke "
            f"(r = {stroke_correlations['avg_glucose_level']:.4f})."
        )

        st.write(
            f"**Hypertension** also has a weak positive "
            f"correlation with stroke "
            f"(r = {stroke_correlations['hypertension']:.4f})."
        )

        st.write(
            f"**BMI** has a very weak linear correlation "
            f"with stroke "
            f"(r = {stroke_correlations['bmi']:.4f})."
        )

    st.warning(
        "⚠️ These are statistical associations observed "
        "in this dataset. They should not be interpreted "
        "as proof that a particular factor directly causes "
        "stroke or as an individual's medical risk."
    )


# ============================================================
# METHODOLOGY
# ============================================================

elif page == "Methodology":

    st.header(
        "📚 Methodology"
    )

    st.write(
        "This project analyzes relationships between selected "
        "health-related factors and stroke using statistical "
        "correlation and covariance analysis."
    )

    st.divider()

    st.subheader(
        "1. Dataset"
    )

    st.write(
        "The analysis uses a healthcare stroke dataset "
        "containing 5,110 patient records and 12 attributes."
    )

    st.write(
        "The dataset contains demographic information, "
        "health conditions, lifestyle-related information, "
        "and stroke outcomes."
    )

    st.subheader(
        "2. Data Preprocessing"
    )

    st.write(
        "The dataset was inspected for missing values, "
        "duplicate records, data types, categorical values, "
        "numerical ranges, and potential outliers."
    )

    st.write(
        "Missing BMI values were handled during the data "
        "cleaning stage, and the cleaned dataset was used "
        "for subsequent analysis."
    )

    st.write(
        "The cleaned dataset contains 5,110 records and "
        "12 attributes."
    )

    st.subheader(
        "3. Selected Health Features"
    )

    st.markdown(
        """
        The statistical analysis focuses on:

        - **Age**
        - **BMI**
        - **Average Glucose Level**
        - **Hypertension**
        - **Heart Disease**
        - **Stroke**
        """
    )

    st.subheader(
        "4. Correlation Analysis"
    )

    st.write(
        "Pearson correlation was used to measure the "
        "strength and direction of linear relationships "
        "between the selected numerical variables."
    )

    st.latex(
        r"r = \frac{cov(X,Y)}{\sigma_X\sigma_Y}"
    )

    st.write(
        "The correlation coefficient ranges from -1 to +1. "
        "A positive value indicates a positive linear "
        "association, while a negative value indicates "
        "a negative linear association."
    )

    st.subheader(
        "5. Covariance Analysis"
    )

    st.write(
        "Covariance was calculated to determine how pairs "
        "of variables vary together."
    )

    st.latex(
        r"Cov(X,Y) = \frac{\sum (X_i-\bar X)(Y_i-\bar Y)}{n-1}"
    )

    st.write(
        "Unlike correlation, covariance is not standardized. "
        "Its magnitude therefore depends on the scale and "
        "units of the variables."
    )

    st.subheader(
        "6. Visualization"
    )

    st.write(
        "Correlation and covariance heatmaps are used to "
        "visualize relationships between variables. The "
        "Risk Factor Explorer provides interactive "
        "visualizations for selected variable pairs."
    )

    st.subheader(
        "7. Key Analytical Result"
    )

    strongest_factor = (
        stroke_correlations.index[0]
    )

    strongest_value = (
        stroke_correlations.iloc[0]
    )

    st.success(
        f"The strongest observed linear correlation "
        f"with stroke among the selected factors is "
        f"**{strongest_factor}** with "
        f"r = {strongest_value:.4f}."
    )

    st.subheader(
        "8. Limitation"
    )

    st.warning(
        "Correlation represents statistical association "
        "and does not establish causation. The analysis "
        "should therefore not be interpreted as proving "
        "that any individual factor directly causes stroke."
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Healthcare Disease Risk Factor Analysis • "
    "Statistical Analytics Dashboard • "
    "Not a Medical Diagnostic Tool"
)