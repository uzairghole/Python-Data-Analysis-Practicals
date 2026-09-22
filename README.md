# 🤖 AI Course Daily Coursework

> **Python • Data Science • Machine Learning**

This repository contains my **daily practical work, coding exercises, and learning notes** from my AI course at **Hirwal Education Trust**.

The coursework focuses on building a foundation in Python-based Data Science and Machine Learning through hands-on programs and examples.

---

## 📖 About

The course work starts with fundamental Python libraries used in Data Science and gradually introduces Machine Learning concepts.

The programs in this repository cover:

* Numerical operations with **NumPy**
* Data manipulation with **Pandas**
* Basic **data cleaning**
* Working with **CSV datasets**
* Data analysis
* Data visualization
* Data Science lifecycle
* Linear Regression
* K-Means Clustering
* Train-Test Split
* Model prediction
* Model evaluation

This repository is mainly maintained as a **record of my regular AI course practice and progress**.

---

## 🧠 What I Practiced

### 🔢 NumPy

Practiced basic array operations and numerical computing.

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr.shape)
print(arr[1:4])
```

**Concepts:**

* Arrays
* Array properties
* Reshaping
* Indexing
* Slicing
* Boolean masking
* Fancy indexing
* `arange()`
* `linspace()`

---

### 🐼 Pandas

Practiced working with structured data using DataFrames.

```python
import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob"],
    "Salary": [70000, 65000]
})

print(df)
```

**Concepts:**

* DataFrames
* Filtering
* Sorting
* GroupBy
* Aggregation
* Creating columns
* Renaming columns
* CSV files

---

### 🧹 Data Cleaning

Practiced preparing raw data before analysis.

```python
df = pd.read_csv("retail_store_sales.csv")

print(df.isnull().sum())
print(df.duplicated().sum())
```

**Concepts:**

* Loading datasets
* Column standardization
* Missing values
* Duplicate records
* Removing unnecessary columns
* Conditional data updates

---

### 📊 Data Visualization

Practiced representing data using graphs.

```python
import matplotlib.pyplot as plt

plt.hist([60, 70, 75, 80, 90])
plt.title("Score Distribution")
plt.show()
```

**Visualizations practiced:**

* Histogram
* Score distribution
* Mean line
* Sine graph
* Cosine graph
* Labels
* Legends
* Grid

---

## 🤖 Machine Learning

The coursework introduces basic Machine Learning using **Scikit-learn**.

### Linear Regression

Used to understand numerical prediction.

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)

print(model.predict([[900]]))
```

Practiced examples include:

* House price prediction
* Simple numerical prediction
* Student marks prediction

---

### K-Means Clustering

Practiced basic unsupervised learning.

```python
from sklearn.cluster import KMeans

model = KMeans(n_clusters=2, random_state=42)
model.fit(X)

print(model.labels_)
```

This demonstrates how data points can be grouped into clusters.

---

### Train-Test Split

Practiced dividing data into training and testing sets.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

The training data is used to build the model, while the testing data is used to check its performance.

---

### Model Evaluation

Practiced evaluating regression models using:

* **Mean Squared Error (MSE)**
* **R² Score**

```python
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
```

---

## 🔄 Data Science Lifecycle

The coursework also covers the basic Data Science process:

```text
Problem Definition
        ↓
Data Collection
        ↓
Data Cleaning
        ↓
EDA
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

## 🛠️ Tools & Libraries

| Tool / Library | Used For                  |
| -------------- | ------------------------- |
| Python         | Programming               |
| NumPy          | Numerical Computing       |
| Pandas         | Data Analysis             |
| Matplotlib     | Visualization             |
| Seaborn        | Statistical Visualization |
| Scikit-learn   | Machine Learning          |

---

## 📁 Repository Structure

```text
AI-Course-Daily-Work/
│
├── data_science_machine_learning.py
├── retail_store_sales.csv
├── requirements.txt
└── README.md
```

---

## 📦 Requirements

```text
numpy
pandas
matplotlib
seaborn
scikit-learn
```

Install the required libraries:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

---

## 📈 Learning Progress

```text
Python
  ↓
NumPy
  ↓
Pandas
  ↓
Data Cleaning
  ↓
Data Analysis
  ↓
Visualization
  ↓
Machine Learning
  ↓
Model Evaluation
```

---

## 🎓 Course Information

**Course:** Artificial Intelligence
**Institute:** Hirwal Education Trust
**Student:** Uzair Ghole
**Program:** BSc IT

---

## 📝 Note

This repository represents **coursework and daily practical learning**, not a standalone personal project. The programs are developed and maintained as part of my ongoing AI course practice.

---

<p align="center">

**Learn • Practice • Understand • Improve**

</p>
