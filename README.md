# 🏥 Healthcare Disease Risk Factor Analysis

An interactive data analytics dashboard for exploring relationships between patient health factors and observed stroke outcomes using statistical analysis and visualization.

## 🚀 Live Demo

**Streamlit Application:**  
https://healthcare-disease-risk-analysis-kcusu45hsafib8vtmqzaka.streamlit.app/

**GitHub Repository:**  
https://github.com/rohithasanapathi/Healthcare-Disease-Risk-Analysis

---

## 📌 Project Overview

Healthcare Disease Risk Factor Analysis is a data analytics project that investigates the relationships between selected patient health characteristics and stroke outcomes.

The project uses statistical techniques such as **Pearson correlation** and **covariance analysis**, supported by interactive visualizations through a Streamlit dashboard.

The objective is to identify and understand patterns in the dataset rather than provide medical diagnosis or individual clinical predictions.

---

## 🎯 Objectives

- Analyze a healthcare stroke dataset.
- Perform data cleaning and preprocessing.
- Identify missing values and potential outliers.
- Study relationships between health-related variables.
- Calculate correlation between selected factors and stroke.
- Perform covariance analysis.
- Visualize relationships using statistical plots and heatmaps.
- Provide an interactive dashboard for data exploration.
- Compare an entered patient profile with dataset-level statistics.

---

## 📊 Dataset

The project uses the **Healthcare Stroke Dataset**, containing:

- **5,110 patient records**
- **12 attributes**

### Main attributes

| Attribute | Description |
|---|---|
| `id` | Unique patient identifier |
| `gender` | Patient gender |
| `age` | Patient age |
| `hypertension` | Presence of hypertension |
| `heart_disease` | Presence of heart disease |
| `ever_married` | Marital status |
| `work_type` | Type of employment |
| `Residence_type` | Urban or rural residence |
| `avg_glucose_level` | Average glucose level |
| `bmi` | Body Mass Index |
| `smoking_status` | Smoking category |
| `stroke` | Observed stroke outcome |

---

## 🧹 Data Preprocessing

The dataset was examined and cleaned before statistical analysis.

The preprocessing stage included:

- Inspecting dataset structure
- Checking data types
- Identifying missing values
- Checking duplicate records
- Examining categorical variables
- Checking numerical ranges
- Detecting potential outliers
- Handling missing BMI values
- Creating a cleaned dataset for analysis

The cleaned dataset contains **5,110 records and 12 attributes**.

---

## 📈 Statistical Analysis

The project focuses on six selected health-related variables:

- Age
- BMI
- Average Glucose Level
- Hypertension
- Heart Disease
- Stroke

### Correlation Analysis

Pearson correlation is used to measure the strength and direction of linear relationships between variables.

The correlation coefficient ranges from:

- `-1` → Strong negative relationship
- `0` → No linear relationship
- `+1` → Strong positive relationship

The dashboard provides:

- Correlation matrix
- Correlation heatmap
- Stroke correlation ranking
- Interactive variable comparison

### Covariance Analysis

Covariance is used to examine how two variables vary together.

The dashboard provides:

- Covariance matrix
- Covariance heatmap
- Statistical interpretation

Unlike correlation, covariance is not standardized and its magnitude depends on the scale of the variables.

---

## 📊 Dashboard Features

The Streamlit dashboard contains the following sections:

### 1. 📋 Overview

Provides:

- Total patient count
- Stroke cases
- Non-stroke cases
- Observed stroke rate
- Dataset preview
- Stroke outcome distribution
- Data quality summary
- Cleaned dataset download

### 2. 🔗 Correlation Analysis

Provides:

- Correlation matrix
- Interactive heatmap
- Correlation of selected factors with stroke
- Strongest observed correlation

### 3. 📊 Covariance Analysis

Provides:

- Covariance matrix
- Covariance heatmap
- Interpretation of covariance values

### 4. 🔍 Risk Factor Explorer

Allows users to select two variables and automatically generates an appropriate visualization.

Depending on the selected variables, the dashboard displays:

- Bar plots
- Box plots
- Scatter plots

It also displays:

- Pearson correlation
- Correlation strength
- Correlation direction

### 5. 🧑‍⚕️ Patient Risk Profile

Allows users to enter:

- Age
- BMI
- Average glucose level
- Hypertension
- Heart disease

The dashboard compares the entered values with dataset-level statistics.

**Important:** This section is an exploratory statistical comparison and does not calculate an individual's probability of stroke.

### 6. 📌 Key Findings

Provides:

- Ranking of observed correlations
- Positive associations
- Statistical interpretation
- Correlation visualization

### 7. 📚 Methodology

Documents:

- Dataset
- Data preprocessing
- Selected variables
- Correlation analysis
- Covariance analysis
- Visualization techniques
- Key analytical result
- Limitations

---

## 🖼️ Project Visualizations

The project includes generated analytical figures:

- Age vs Stroke
- BMI vs Stroke
- Glucose vs Stroke
- Correlation Heatmap
- Covariance Heatmap

These visualizations are available in:

```text
outputs/figures/
🛠️ Technologies Used
Programming Language
Python
Data Analysis
Pandas
NumPy
Visualization
Matplotlib
Seaborn
Dashboard
Streamlit
Development Tools
Visual Studio Code
Git
GitHub
📁 Project Structure
Healthcare-Disease-Risk-Analysis/
│
├── data/
│   ├── cleaned/
│   │   └── healthcare_stroke_cleaned.csv
│   │
│   └── original/
│       └── healthcare-dataset-stroke-data.csv
│
├── outputs/
│   └── figures/
│       ├── age_vs_stroke.png
│       ├── bmi_vs_stroke.png
│       ├── correlation_heatmap.png
│       ├── covariance_heatmap.png
│       └── glucose_vs_stroke.png
│
├── src/
│   ├── analysis.py
│   ├── app.py
│   ├── app_backup.py
│   ├── clean_data.py
│   ├── eda_initial.py
│   ├── inspect_data.py
│   └── outlier_analysis.py
│
├── .gitignore
├── README.md
└── requirements.txt
▶️ Run the Project Locally
1. Clone the repository
git clone https://github.com/rohithasanapathi/Healthcare-Disease-Risk-Analysis.git
2. Navigate into the project
cd Healthcare-Disease-Risk-Analysis
3. Create a virtual environment
python -m venv .venv
4. Activate the virtual environment
Windows PowerShell
.venv\Scripts\Activate.ps1
5. Install dependencies
pip install -r requirements.txt
6. Run the Streamlit dashboard
streamlit run src/app.py

The dashboard will open in your browser.

📦 Requirements

The required Python packages are listed in:

requirements.txt

Main libraries include:

pandas
numpy
matplotlib
seaborn
streamlit
⚠️ Limitations

The analysis is based on statistical relationships within the available dataset.

Correlation and covariance describe associations and do not establish causation.

The dashboard should not be used as a medical diagnostic system or as a tool for making individual clinical decisions.

🔮 Future Enhancements

Possible future improvements include:

Machine learning-based stroke classification
Model performance comparison
Feature importance analysis
Interactive ROC and precision-recall curves
Model explainability using SHAP
Improved patient-level risk modeling
Additional demographic analysis
Advanced dashboard filtering
Deployment of a trained predictive model
👩‍💻 Author

Rohitha Sanapathi

B.Tech – Computer Science and Engineering (Data Science)

GitHub:
https://github.com/rohithasanapathi