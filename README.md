\# 🏥 Healthcare Disease Risk Factor Analysis



An interactive healthcare analytics dashboard for exploring statistical relationships between patient health factors and stroke outcomes.



\## 📌 Project Overview



Healthcare Disease Risk Factor Analysis is a data analytics project developed to explore relationships between selected patient health characteristics and stroke outcomes.



The project uses a cleaned healthcare stroke dataset and applies data preprocessing, exploratory data analysis, correlation analysis, covariance analysis, and interactive visualization.



A Streamlit dashboard provides an easy-to-use interface for exploring the results.



> \*\*Important:\*\* This project is intended for statistical and educational analysis only. It is not a medical diagnostic system and does not provide individual clinical predictions.



\---



\## 🎯 Objectives



The main objectives of this project are:



\- Analyze a healthcare stroke dataset.

\- Clean and preprocess healthcare data.

\- Identify missing values and potential outliers.

\- Explore relationships between health-related variables.

\- Calculate Pearson correlation coefficients.

\- Calculate covariance between selected variables.

\- Visualize statistical relationships using charts and heatmaps.

\- Provide an interactive Risk Factor Explorer.

\- Provide a Patient Risk Profile for exploratory comparison.

\- Present analytical findings through a professional Streamlit dashboard.



\---



\## 📊 Dataset



The project uses the \*\*Healthcare Stroke Dataset\*\*, containing:



\- \*\*5,110 patient records\*\*

\- \*\*12 attributes\*\*



\### Important Attributes



| Attribute | Description |

|---|---|

| `id` | Unique patient identifier |

| `gender` | Patient gender |

| `age` | Patient age |

| `hypertension` | Hypertension indicator |

| `heart\_disease` | Heart disease indicator |

| `ever\_married` | Marital status |

| `work\_type` | Type of employment |

| `Residence\_type` | Urban or rural residence |

| `avg\_glucose\_level` | Average glucose level |

| `bmi` | Body Mass Index |

| `smoking\_status` | Smoking status |

| `stroke` | Stroke outcome |



\---



\## 🧹 Data Preprocessing



The dataset was examined and cleaned before performing the statistical analysis.



The preprocessing workflow included:



1\. Inspecting the dataset structure.

2\. Checking data types.

3\. Identifying missing values.

4\. Checking duplicate records.

5\. Examining categorical variables.

6\. Checking numerical ranges.

7\. Detecting potential outliers.

8\. Handling missing BMI values.

9\. Saving the cleaned dataset for analysis.



The cleaned dataset is stored in:



```text

data/cleaned/healthcare\_stroke\_cleaned.csv

🔎 Exploratory Data Analysis



Exploratory analysis was performed to understand the distribution and relationships within the dataset.



The project includes visualizations such as:



Age vs Stroke

BMI vs Stroke

Glucose Level vs Stroke

Correlation Heatmap

Covariance Heatmap



Generated figures are stored in:



outputs/figures/

🔗 Correlation Analysis



Pearson correlation was used to measure the strength and direction of linear relationships between selected health variables.



The selected variables are:



Age

BMI

Average Glucose Level

Hypertension

Heart Disease

Stroke



The Pearson correlation coefficient is represented by:



r=

σ

X

&#x09;​



σ

Y

&#x09;​



cov(X,Y)

&#x09;​





The coefficient ranges from:



\-1 to +1



A positive value indicates a positive linear association, while a negative value indicates a negative linear association.



Correlation indicates statistical association and does not establish causation.



📊 Covariance Analysis



Covariance was calculated to determine how pairs of variables vary together.



The covariance formula is:



Cov(X,Y)=

n−1

∑(X

i

&#x09;​



−

X

ˉ

)(Y

i

&#x09;​



−

Y

ˉ

)

&#x09;​





Unlike correlation, covariance is not standardized. Its magnitude therefore depends on the scale and units of the variables.



🖥️ Interactive Streamlit Dashboard



The project includes a professional Streamlit dashboard with the following sections:



1\. 📋 Overview



Provides:



Total patient count

Stroke cases

Non-stroke cases

Observed stroke rate

Dataset preview

Stroke distribution

Data quality summary

Cleaned dataset download

2\. 🔗 Correlation Analysis



Provides:



Correlation matrix

Correlation heatmap

Correlation of selected factors with stroke

Strongest observed correlation

3\. 📊 Covariance Analysis



Provides:



Covariance matrix

Covariance heatmap

Explanation of covariance interpretation

4\. 🔍 Risk Factor Explorer



Allows users to select two variables and automatically displays an appropriate visualization.



Depending on the selected variables, the dashboard can display:



Scatter plots

Box plots

Bar charts



It also displays:



Pearson correlation

Correlation strength

Correlation direction

5\. 🧑‍⚕️ Patient Risk Profile



Allows users to enter:



Age

BMI

Average glucose level

Hypertension

Heart disease



The entered profile is compared with dataset averages.



This feature is an exploratory statistical comparison and does not calculate an individual's probability of stroke.



6\. 📌 Key Findings



Summarizes:



Strongest observed correlation with stroke

Correlation ranking

Positive associations

Statistical interpretation

Analytical limitations

7\. 📚 Methodology



Documents:



Dataset

Preprocessing

Selected features

Correlation methodology

Covariance methodology

Visualization methods

Key result

Limitations

🛠️ Technologies Used

Technology	Purpose

Python	Core programming language

Pandas	Data manipulation and analysis

NumPy	Numerical operations

Matplotlib	Data visualization

Seaborn	Statistical visualization

Streamlit	Interactive dashboard

Git	Version control

GitHub	Source code management

📁 Project Structure

Healthcare-Disease-Risk-Analysis/

│

├── data/

│   ├── cleaned/

│   │   └── healthcare\_stroke\_cleaned.csv

│   │

│   └── original/

│       └── healthcare-dataset-stroke-data.csv

│

├── outputs/

│   └── figures/

│       ├── age\_vs\_stroke.png

│       ├── bmi\_vs\_stroke.png

│       ├── correlation\_heatmap.png

│       ├── covariance\_heatmap.png

│       └── glucose\_vs\_stroke.png

│

├── src/

│   ├── analysis.py

│   ├── app.py

│   ├── app\_backup.py

│   ├── clean\_data.py

│   ├── eda\_initial.py

│   ├── inspect\_data.py

│   └── outlier\_analysis.py

│

├── .gitignore

├── requirements.txt

└── README.md

⚙️ Installation



Clone the repository:



git clone https://github.com/rohithasanapathi/Healthcare-Disease-Risk-Analysis.git



Navigate into the project:



cd Healthcare-Disease-Risk-Analysis



Create a virtual environment:



python -m venv .venv



Activate the virtual environment on Windows PowerShell:



.venv\\Scripts\\Activate.ps1



Install the required packages:



pip install -r requirements.txt

▶️ Running the Dashboard



From the project root directory, run:



streamlit run src/app.py



The Streamlit application will open in your browser.

\## 📊 Visualizations



The project includes several visualizations to explore relationships between healthcare factors and stroke outcomes.



\### Age vs Stroke



!\[Age vs Stroke](outputs/figures/age\_vs\_stroke.png)



\### BMI vs Stroke



!\[BMI vs Stroke](outputs/figures/bmi\_vs\_stroke.png)



\### Average Glucose Level vs Stroke



!\[Glucose vs Stroke](outputs/figures/glucose\_vs\_stroke.png)



\### Correlation Heatmap



!\[Correlation Heatmap](outputs/figures/correlation\_heatmap.png)



\### Covariance Heatmap



!\[Covariance Heatmap](outputs/figures/covariance\_heatmap.png)





📈 Key Analytical Findings



The analysis identifies the relationships between selected health-related variables and stroke outcomes using Pearson correlation.



Among the selected variables, age shows the strongest observed linear correlation with stroke in the dataset.



Other variables, including:



Heart disease

Average glucose level

Hypertension

BMI



show varying degrees of statistical association with stroke.



These findings describe patterns present in the dataset and should not be interpreted as medical conclusions.



⚠️ Limitations



This project has several limitations:



Correlation does not establish causation.

The analysis focuses primarily on linear relationships.

Binary variables are treated numerically for correlation analysis.

The dataset may not represent all populations.

Statistical relationships in the dataset should not be interpreted as individual medical risk.

The Patient Risk Profile is not a machine-learning prediction model.

Clinical decisions should never be based on this dashboard.

🔐 Medical Disclaimer



This application is developed for educational, statistical, and data analytics purposes.



It is not intended to diagnose, treat, prevent, or predict any medical condition.



The results represent statistical relationships observed in the dataset and should not replace professional medical advice.



🚀 Future Enhancements



Possible future improvements include:



Machine learning-based stroke prediction.

Model performance evaluation.

Feature importance analysis.

Interactive filtering.

Advanced statistical testing.

ROC-AUC analysis.

Model explainability using SHAP.

Cloud deployment.

Improved accessibility and responsive design.

\## 👩‍💻 Author



\*\*Rohitha Sanapathi\*\*



B.Tech – Computer Science and Engineering (Data Science)



GitHub:



https://github.com/rohithasanapathi

