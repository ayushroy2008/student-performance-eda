# Student Performance — Exploratory Data Analysis (EDA)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?logo=numpy)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-4C72B0)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C)
![Status](https://img.shields.io/badge/Project-Completed-success)

A Python-based Exploratory Data Analysis project investigating student academic performance using statistical descriptions, data visualisation and correlation analysis.

---

## 📌 Project Overview

Educational institutions collect large amounts of student data, but extracting meaningful insights from this information is an important challenge.

This project performs Exploratory Data Analysis (EDA) on the **Student Performance dataset** from the UCI Machine Learning Repository.

The primary objective is to understand the distribution of student-related variables and investigate how different academic, personal and lifestyle factors are associated with students' final Mathematics grades.

The project focuses on three major stages:

- Univariate Analysis
- Bivariate Analysis
- Multivariate Analysis

The project uses Python libraries to inspect, process, analyse and visualise the dataset, followed by interpretation of the observed patterns.

## 📊 Dataset Information

**Dataset:** Student Performance  
**Source:** UCI Machine Learning Repository  
**File used:** `student-mat.csv`  
**Total Records:** 395 students  
**Total Features:** 33 columns  
**Subject:** Mathematics

The dataset contains information about students' academic performance, personal backgrounds, family circumstances, study habits and lifestyle.

### Important Variables

| Variable | Description |
|---|---|
| G1 | First-period grade |
| G2 | Second-period grade |
| G3 | Final grade |
| age | Age of the student |
| studytime | Weekly study-time category |
| failures | Number of previous class failures |
| absences | Number of school absences |
| Medu | Mother's education level |
| Dalc | Weekday alcohol consumption |
| famsup | Family educational support |

## 🛠️ Technologies and Libraries

The following technologies and Python libraries were used:

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualisation |
| Seaborn | Statistical visualisation |
| Scikit-learn | Label encoding of categorical variables |

## 🔍 Analysis Performed

### 1. Data Understanding and Preprocessing

- Inspected the dataset structure and dimensions.
- Examined column names and data types using Pandas.
- Checked for missing values.
- Converted categorical variables into numerical representations using Label Encoding and binary encoding.
- Retained outliers to avoid removing potentially useful observations.

### 2. Univariate Analysis

Individual variables were analysed to understand their distributions and characteristics.

**Variables examined:**

- First-period grade (G1)
- Second-period grade (G2)
- Final grade (G3)
- Age
- Absences
- Study time
- Previous failures

**Visualisation techniques:**

- Histograms
- Boxplots
- Countplots

Statistical measures such as mean, median, minimum, maximum and standard deviation were also calculated for selected numerical variables.

### 3. Bivariate Analysis

Relationships between two variables were investigated to identify patterns and differences in student performance.

| Analysis | Visualisation |
|---|---|
| Study time vs Final grade | Boxplot |
| Previous failures vs Final grade | Boxplot |
| Absences vs Final grade | Scatterplot |
| G1 vs G3 | Scatterplot |
| G2 vs G3 | Scatterplot |
| Mother's education vs Final grade | Boxplot |
| Weekday alcohol consumption vs Final grade | Boxplot |
| Family educational support vs Final grade | Boxplot |

### 4. Multivariate Analysis

Three-variable relationships and correlations were explored using multiple visualisation techniques.

**Analyses performed:**

- Study time, previous failures and final grade using a grouped boxplot.
- Absences, previous failures and final grade using a scatterplot with categorical hue.
- G1, G2 and G3 using a correlation heatmap.

## 💡 Key Findings

Some of the important observations from the analysis include:

**1. Earlier Academic Performance**

G1 and G2 show strong positive correlations with G3.

- G1 and G2: 0.85
- G1 and G3: 0.80
- G2 and G3: 0.90

G2 shows the strongest correlation with the final grade.

**2. Previous Failures**

Students with more previous class failures generally show lower median final grades. The median decreases across failure categories.

**3. Study Time**

Students with greater study time generally tend to have higher median final grades, although the trend is not consistent across all categories.

**4. Absences**

Most students have fewer than 20 absences. The scatterplot does not show a clear relationship between absences and final grades.

**5. Other Factors**

Mother's education, weekday alcohol consumption and family educational support show comparatively weaker or less consistent patterns in relation to final grades.

## 📈 Visualisations

The project generates multiple visualisations, including:

- Grade distribution histograms.
- Age and absences boxplots.
- Study-time and previous-failure countplots.
- Academic performance comparison boxplots.
- Grade relationship scatterplots.
- Multivariate grouped visualisations.
- Correlation heatmap.

All generated graphs are available in the `plots/` directory.

## 📁 Project Structure

```text
student-performance-eda/
│
├── student_performance_eda.py
├── README.md
├── requirements.txt
│
├── plots/
│   ├── DalcVsG3.png
│   ├── Heatmap.png
│   ├── absencesVsG3.png
│   ├── absencesVsPrevfailVsFinal.png
│   ├── absences_boxplot.png
│   ├── absences_hist.png
│   ├── age_boxplot.png
│   ├── age_hist.png
│   ├── failuresVsG3.png
│   ├── failures_bar.png
│   ├── famsupVsG3.png
│   ├── g1VsG3.png
│   ├── g1_hist.png
│   ├── g2VsG3.png
│   ├── g2_hist.png
│   ├── g3_hist.png
│   ├── meduVsG3.png
│   ├── studytimeVsG3.png
│   ├── studytimeVsPrevfailVsFinalgrade.png
│   └── studytime_bar.png
│
└── report/
    └── Student_Performance_EDA_Completed.pdf
```

## ⚙️ Installation and Execution

Follow these steps to run the project locally.

### Prerequisites

- Python 3.x
- pip package manager

### 1. Clone the repository

```bash
git clone https://github.com/ayushroy2008/student-performance-eda.git
```

### 2. Navigate to the project directory

```bash
cd student-performance-eda
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Prepare the dataset

Download the `student-mat.csv` file from the UCI Machine Learning Repository and place it in the root project directory, alongside the Python script.

The script uses a semicolon (`;`) as the CSV delimiter.

### 5. Execute the Python script

```bash
python student_performance_eda.py
```

The script performs the analysis and generates the corresponding visualisations.

## ⚠️ Limitations

- The dataset contains 395 students and represents only the Mathematics course.
- Findings may not generalise to other educational institutions or student populations.
- Observed correlations and associations do not establish causation.
- The analysis primarily uses descriptive statistics and visualisation.
- No statistical hypothesis testing or predictive modelling was performed.
- Some categories contain relatively few observations and should be interpreted cautiously.
- Outliers were retained and may influence certain observations.
- G1, G2 and G3 are strongly correlated, making it difficult to separate their individual contributions.

## 🎯 Project Objectives Achieved

- Understanding and inspecting a real-world dataset.
- Performing data preprocessing and categorical encoding.
- Applying univariate, bivariate and multivariate analysis.
- Creating statistical visualisations using Python.
- Identifying and interpreting patterns in student performance.
- Documenting analytical findings in a structured report.

## 📄 Project Report

The complete project report, containing the methodology, visualisations, observations, key insights, limitations and conclusion, is available in the `report/` directory.

## 📚 References

Cortez, P. and Silva, A. (2008). *Using Data Mining to Predict Secondary School Student Performance.*

Student Performance Dataset — UCI Machine Learning Repository.

## 👨‍💻 Author

**Ayush Roy**

B.Tech Computer Science and Engineering Student

**Project Type:** Minor Project  
**Domain:** Data Science  
**Institution:** Skillairo Edutech Pvt. Ltd.

---

*This project was developed as part of my learning journey in Python, Data Science and Exploratory Data Analysis.*
