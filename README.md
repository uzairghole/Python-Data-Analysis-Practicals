# 🐍 Python Data Science & Machine Learning

A practical Python project created to learn and practice the fundamentals of **Data Science and Machine Learning** using popular Python libraries.

## 📖 Project Introduction

This project brings together my practice in **NumPy, Pandas, Data Cleaning, Data Analysis, Data Visualization, and Machine Learning**.

It starts with basic numerical operations using NumPy and data manipulation using Pandas. It then covers working with CSV datasets, checking missing values and duplicates, cleaning data, and creating visualizations.

The project also introduces Machine Learning using **Scikit-learn**, including Linear Regression, K-Means Clustering, train-test splitting, prediction, and model evaluation.

This repository represents my learning journey from **Python programming to practical Data Science and Machine Learning**.

---

## 🛠️ Technologies Used

* **Python** — Programming language
* **NumPy** — Numerical computing
* **Pandas** — Data manipulation and analysis
* **Matplotlib** — Data visualization
* **Seaborn** — Statistical visualization
* **Scikit-learn** — Machine Learning

---

## 📚 Topics Covered

### 🔢 NumPy

* Creating arrays
* Array properties
* Reshaping
* Indexing and slicing
* 2D arrays
* Boolean masking
* Fancy indexing
* `arange()`
* `linspace()`

Example:

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])
```

---

### 🐼 Pandas

* Creating DataFrames
* Filtering data
* Sorting data
* Creating new columns
* GroupBy
* Aggregation
* Renaming columns
* Working with CSV files

Example:

```python
import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob"],
    "Salary": [70000, 65000]
})

print(df)
```

---

### 🧹 Data Cleaning

The project includes basic data cleaning operations such as:

* Loading CSV datasets
* Standardizing column names
* Checking missing values
* Finding duplicate rows
* Removing unnecessary columns
* Updating missing values
* Selecting specific records

Example:

```python
df.columns = df.columns.str.lower()

print(df.isnull().sum())
print(df.duplicated().sum())
```

---

### 📊 Data Visualization

The project includes basic visualizations using Matplotlib:

* Histogram
* Score distribution
* Mean line
* Sine graph
* Cosine graph
* Labels and legends
* Grid

Example:

```python
import matplotlib.pyplot as plt

plt.hist([60, 70, 75, 80, 90])
plt.title("Score Distribution")
plt.show()
```

---

## 🤖 Machine Learning

Basic Machine Learning concepts are practiced using Scikit-learn.

### Linear Regression

Used for simple prediction problems such as house price and student marks prediction.

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[900]])
print(prediction)
```

### K-Means Clustering

Used to understand basic unsupervised learning and grouping of data points.

```python
from sklearn.cluster import KMeans

model = KMeans(n_clusters=2, random_state=42)
model.fit(X)

print(model.labels_)
```

### Train-Test Split

The dataset is divided into training and testing data.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

### Model Evaluation

The project uses:

* Mean Squared Error (MSE)
* R² Score

to evaluate the Linear Regression model.

---

## 🔄 Data Science Workflow

```text
Problem Definition
        ↓
Data Collection
        ↓
Data Cleaning
        ↓
Data Analysis
        ↓
Data Visualization
        ↓
Feature Selection
        ↓
Modeling
        ↓
Evaluation
        ↓
Deployment
        ↓
Monitoring
```

---

## 📂 Project Structure

```text
python-data-science-machine-learning/
│
├── data_science_machine_learning.py
├── retail_store_sales.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Install the required libraries:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

---

## ▶️ Run the Project

```bash
python data_science_machine_learning.py
```

> Make sure `retail_store_sales.csv` is placed in the same folder as the Python file.

---

## 🎯 Learning Objectives

Through this project, I am practicing how to:

* Work with NumPy arrays
* Manipulate data using Pandas
* Clean and inspect datasets
* Handle missing values
* Detect duplicate records
* Create data visualizations
* Understand the Data Science lifecycle
* Prepare data for Machine Learning
* Build Linear Regression models
* Apply K-Means clustering
* Split datasets into training and testing sets
* Evaluate Machine Learning models

---

## 🚀 Future Learning

* Advanced Pandas
* Exploratory Data Analysis
* Feature Engineering
* Statistical Analysis
* Classification
* Decision Trees
* Random Forest
* Advanced Machine Learning
* Real-world Data Science Projects

---

## 👨‍💻 Author

**Uzair Ghole**

BSc IT Student | Aspiring Data Science Professional

[GitHub](https://github.com/uzairghole)

---

<p align="center">

**Python → NumPy → Pandas → Data Analysis → Machine Learning → Data Science**

</p>
