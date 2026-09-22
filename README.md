# 🐍 Python Data Science & Machine Learning

A practical Python project for learning and practicing **Data Science and Machine Learning** concepts using NumPy, Pandas, Matplotlib, Seaborn, and Scikit-learn.

## 📖 Project Introduction

This project contains my practical Python programs covering the basic workflow of Data Science.

The code starts with **NumPy** for numerical operations and array handling, followed by **Pandas** for creating, filtering, sorting, and analyzing data. It also includes basic **data cleaning**, **CSV dataset handling**, and **data visualization** using Matplotlib.

The project then moves into basic **Machine Learning** concepts using Scikit-learn, including Linear Regression, K-Means Clustering, train-test splitting, prediction, and model evaluation.

---

## 🧩 Code Explanation

### 1. NumPy

NumPy is used for working with numerical data and arrays.

The code demonstrates:

* Creating NumPy arrays
* Creating zeros and ones
* `arange()` and `linspace()`
* Checking array shape and dimensions
* Reshaping arrays
* Indexing and slicing
* Boolean masking
* Fancy indexing

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr.shape)
print(arr[1:4])
```

Here, the array is created using NumPy. The code then checks its shape and extracts values using slicing.

---

### 2. Pandas

Pandas is used for working with structured data in the form of DataFrames.

The code demonstrates:

* Creating DataFrames
* Filtering rows
* Sorting data
* Creating new columns
* Grouping data
* Calculating averages
* Renaming columns

```python
import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob"],
    "Salary": [70000, 65000]
})

print(df)
```

The code creates a simple DataFrame containing names and salaries. Pandas is then used to perform different data operations.

---

### 3. Data Cleaning

The project uses a **retail store sales CSV dataset** for basic data cleaning and analysis.

The code performs:

* CSV file loading
* Column name standardization
* Dataset information checking
* Statistical summary
* Missing-value checking
* Duplicate checking
* Removing unnecessary columns
* Updating missing values based on conditions

```python
df = pd.read_csv("retail_store_sales.csv")

print(df.isnull().sum())
print(df.duplicated().sum())
```

This helps identify missing and duplicate data before further analysis.

---

### 4. Data Visualization

Matplotlib is used to create simple graphs and understand data visually.

The project includes:

* Histogram
* Exam score distribution
* Mean value line
* Sine graph
* Cosine graph

```python
import matplotlib.pyplot as plt

plt.hist([60, 70, 75, 80, 90])
plt.title("Score Distribution")
plt.show()
```

The histogram shows how values are distributed across different score ranges.

---

### 5. Data Science Lifecycle

The project also demonstrates the basic Data Science lifecycle:

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

This represents the general process followed when solving a Data Science problem.

---

## 🤖 Machine Learning

The project includes basic Machine Learning examples using **Scikit-learn**.

### Linear Regression

Linear Regression is used to predict a numerical value based on input data.

The project includes examples such as:

* House price prediction
* Simple numerical prediction
* Student marks prediction

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[900]])
print(prediction)
```

The model learns the relationship between `X` and `y` and then predicts a value for new input data.

---

### K-Means Clustering

K-Means is used for basic **unsupervised learning**.

```python
from sklearn.cluster import KMeans

model = KMeans(n_clusters=2, random_state=42)
model.fit(X)

print(model.labels_)
```

The algorithm groups similar data points into clusters.

---

### Train-Test Split

The project divides data into training and testing sets.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

The training data is used to build the model, while the testing data is used to check its performance.

---

### Model Evaluation

The student marks prediction example evaluates the model using:

* **Mean Squared Error (MSE)** — measures prediction error.
* **R² Score** — shows how well the model explains the variation in the target values.

```python
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MSE:", mse)
print("R2 Score:", r2)
```

---

## 🛠️ Technologies Used

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python       | Programming          |
| NumPy        | Numerical operations |
| Pandas       | Data analysis        |
| Matplotlib   | Visualization        |
| Seaborn      | Data visualization   |
| Scikit-learn | Machine Learning     |

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

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

Run the program:

```bash
python data_science_machine_learning.py
```

---

## 🎯 Learning Outcome

By completing this project, I practiced the basic workflow of:

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

## 👨‍💻 Author

**Uzair Ghole**

BSc IT Student | Aspiring Data Science Professional

[GitHub](https://github.com/uzairghole)
