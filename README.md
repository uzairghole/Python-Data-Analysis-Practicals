# 🤖 AI Course – Complete Python, Data Science & Machine Learning

> **Daily Coursework & Practical Learning at Hirwal Education Trust**

This repository contains my **daily practical programs and coding exercises** completed as part of my **AI Course at Hirwal Education Trust**.

The coursework covers Python programming for **NumPy, Pandas, Data Cleaning, Data Analysis, Data Visualization, Data Science, and Machine Learning**.

This repository is maintained as a **coursework and learning record**, not as a single standalone personal project.

---

# 📚 Topics Covered

```text
Python
  │
  ├── NumPy
  │    ├── Arrays
  │    ├── Array Properties
  │    ├── Reshaping
  │    ├── Indexing & Slicing
  │    ├── Boolean Masking
  │    └── Fancy Indexing
  │
  ├── Pandas
  │    ├── DataFrames
  │    ├── Filtering
  │    ├── Sorting
  │    ├── GroupBy
  │    ├── Aggregation
  │    └── Column Operations
  │
  ├── Data Cleaning
  │    ├── CSV Loading
  │    ├── Missing Values
  │    ├── Duplicate Rows
  │    └── Data Transformation
  │
  ├── Data Visualization
  │    ├── Histogram
  │    ├── Mean
  │    ├── Sine
  │    └── Cosine
  │
  └── Machine Learning
       ├── Linear Regression
       ├── K-Means Clustering
       ├── Features & Labels
       ├── Train-Test Split
       └── Model Evaluation
```

---

# 🛠️ Libraries Used

```python
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

| Library        | Purpose                        |
| -------------- | ------------------------------ |
| `os`           | File and directory operations  |
| `NumPy`        | Numerical computing and arrays |
| `Pandas`       | Data analysis and DataFrames   |
| `Matplotlib`   | Data visualization             |
| `Seaborn`      | Statistical visualization      |
| `Scikit-learn` | Machine Learning               |

---

# 🔢 1. NumPy Base Practice

NumPy is used for numerical computing and working with arrays.

## Complete NumPy Code

```python
import numpy as np

# Creating arrays
a = np.array([1, 2, 3, 4, 5])
b = np.zeros((3, 3))
c = np.ones((2, 4))
d = np.arange(0, 10, 2)
e = np.linspace(0, 1, 5)

# Array properties
print("Array A properties:", a.shape, a.dtype, a.ndim)

# Reshaping
matrix = np.arange(12).reshape(3, 4)
print("\nReshaped Matrix:\n", matrix)

# Indexing & Slicing
arr = np.array([10, 20, 30, 40, 50])
print("\nFirst & Last:", arr[0], arr[-1])
print("Slice [1:4]:", arr[1:4])

# 2D indexing
m = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\nElement at (1,2):", m[1, 2])
print("Second column:", m[:, 1])
print("First two rows:\n", m[0:2, :])

# Boolean masking & Fancy indexing
scores = np.array([85, 42, 91, 67, 73])

passed = scores[scores >= 70]

print("\nPassed Scores:", passed)
print("Fancy Indexing:", arr[[0, 3, 4]])
```

### Concepts Practiced

* `np.array()`
* `np.zeros()`
* `np.ones()`
* `np.arange()`
* `np.linspace()`
* `shape`
* `dtype`
* `ndim`
* `reshape()`
* Indexing
* Slicing
* 2D indexing
* Boolean masking
* Fancy indexing

---

# 🐼 2. Pandas Base Practice

Pandas is used for handling structured and tabular data.

## Complete Pandas Code

```python
import pandas as pd

# Create DataFrame
df_demo = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Dept": ["IT", "HR", "IT", "HR"],
    "Salary": [70000, 65000, 80000, 72000]
})

# Filtering
it_team = df_demo[df_demo["Dept"] == "IT"]

high_pay = df_demo[df_demo["Salary"] > 70000]

# Sorting
sorted_df = df_demo.sort_values(
    "Salary",
    ascending=False
)

# New Column
df_demo["Bonus"] = df_demo["Salary"] * 0.1

# Aggregation
dept_avg = df_demo.groupby("Dept")["Salary"].mean()

print("\n--- Department Average Salary ---")
print(dept_avg)

# Clean up DataFrame columns
df_demo = df_demo.drop(
    columns=["Bonus"]
).rename(
    columns={"Dept": "Department"}
)
```

### Concepts Practiced

* DataFrame creation
* Filtering
* Sorting
* Creating new columns
* GroupBy
* Mean/Average
* Dropping columns
* Renaming columns

---

# 🧹 3. Data Cleaning & Analysis

This section uses the `retail_store_sales.csv` dataset.

The program checks the dataset, finds missing values and duplicates, removes an unnecessary column, and conditionally fills missing item values.

## Complete Data Cleaning Code

```python
import os
import pandas as pd

file_path = "retail_store_sales.csv"

if os.path.exists(file_path):

    df = pd.read_csv(file_path)

    # Standardize column headers
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    print("\n--- Dataset Summary ---")
    df.info()

    print("\n--- Statistical Overview ---")
    print(df.describe())

    # Missing values
    missing_pct = df.isnull().mean() * 100

    print("\n--- Missing Value Percentage ---")
    print(missing_pct)

    # Duplicate rows
    duplicates = df[df.duplicated()]

    print(
        f"\nDuplicate Rows Found: {len(duplicates)}"
    )

    # Remove transaction ID
    df_cleaned = df.drop(
        columns=["transaction_id"],
        errors="ignore"
    )

    # Condition for missing item
    condition = (
        (df_cleaned["item"].isna()) &
        (df_cleaned["price_per_unit"] == 33.5) &
        (df_cleaned["category"] == "Furniture")
    )

    # Fill missing item
    df_cleaned.loc[
        condition,
        "item"
    ] = "Item_20_FUR"

    # View updated records
    target_items = df_cleaned[
        (df_cleaned["price_per_unit"] == 33.5) &
        (df_cleaned["category"] == "Furniture")
    ]

    print("\n--- Updated Targeted Records ---")
    print(target_items)

else:

    print(
        f"\nNote: '{file_path}' not found. "
        "Skipping file read steps."
    )
```

### Data Cleaning Workflow

```text
CSV File
   ↓
Load Dataset
   ↓
Clean Column Names
   ↓
Inspect Dataset
   ↓
Statistical Summary
   ↓
Check Missing Values
   ↓
Check Duplicates
   ↓
Remove Unnecessary Column
   ↓
Fill Required Missing Values
   ↓
Clean Dataset
```

---

# 📊 4. Data Visualization

The coursework includes two visualization exercises.

---

## 4.1 Exam Score Distribution

```python
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 4))

data = np.random.normal(
    70,
    10,
    1000
)

plt.hist(
    data,
    bins=17,
    edgecolor="#4A5568",
    alpha=0.7,
    color="#4FD1C5"
)

plt.axvline(
    data.mean(),
    color="#E53E3E",
    linestyle="--",
    linewidth=2,
    label=f"Mean: {data.mean():.2f}"
)

plt.title(
    "Exam Score Distribution",
    fontsize=12,
    pad=10
)

plt.xlabel("Score")
plt.ylabel("Frequency")

plt.legend()

plt.tight_layout()
plt.show()
```

### Concepts

* Random data generation
* Normal distribution
* Histogram
* Mean calculation
* Mean reference line
* X-axis and Y-axis
* Legend

---

## 4.2 Trigonometric Functions

```python
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 4))

x = np.linspace(0, 10, 100)

plt.plot(
    x,
    np.sin(x),
    label="sin(x)",
    linewidth=2
)

plt.plot(
    x,
    np.cos(x),
    label="cos(x)",
    linewidth=2,
    linestyle="--"
)

plt.title(
    "Trigonometric Functions",
    fontsize=12,
    pad=10
)

plt.xlabel("x")
plt.ylabel("y")

plt.grid(
    True,
    linestyle=":",
    alpha=0.6
)

plt.legend()

plt.tight_layout()
plt.show()
```

### Concepts

* `linspace()`
* `sin()`
* `cos()`
* Line plots
* Labels
* Grid
* Legend

---

# 📚 5. Data Science Basics

## 5.1 Sales Data Analysis

```python
import pandas as pd

data = {
    "Product": ["A", "B", "A", "C"],
    "Sales": [100, 200, 150, 120]
}

df = pd.DataFrame(data)

print(df)

print(
    "Total sales:",
    df["Sales"].sum()
)
```

### What it does

Creates a small sales dataset and calculates total sales.

```text
100 + 200 + 150 + 120 = 570
```

---

# 🔄 6. Data Science Lifecycle

```python
lifecycle = [
    "Problem Definition",
    "Data Collection",
    "Data Cleaning",
    "EDA",
    "Modeling",
    "Evaluation",
    "Deployment",
    "Monitoring"
]

for step in lifecycle:
    print(step)
```

### Lifecycle

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

**EDA = Exploratory Data Analysis**

---

# 📐 7. Linear Regression – House Price Prediction

```python
from sklearn.linear_model import LinearRegression

X = [
    [500],
    [800],
    [1000],
    [1200]
]

y = [
    100000,
    160000,
    200000,
    240000
]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[900]])

print(
    "Predicted price:",
    prediction[0]
)
```

### Concept

```text
Area
  ↓
Linear Regression
  ↓
Predicted Price
```

Here:

* `X` = Area
* `y` = Price
* `fit()` = Train the model
* `predict()` = Make prediction

---

# 📈 8. Simple Linear Regression

```python
from sklearn.linear_model import LinearRegression

X = [
    [1],
    [2],
    [3]
]

y = [
    2,
    4,
    6
]

model = LinearRegression()

model.fit(X, y)

print(
    model.predict([[4]])
)
```

The model learns the relationship:

```text
1 → 2
2 → 4
3 → 6
```

Therefore, the prediction for `4` is approximately:

```text
8
```

---

# 🔵 9. K-Means Clustering

K-Means is an example of **unsupervised Machine Learning**.

```python
from sklearn.cluster import KMeans

X = [
    [1, 1],
    [1, 2],
    [8, 8],
    [9, 8]
]

clusters = KMeans(
    n_clusters=2,
    random_state=42,
    n_init=10
)

clusters.fit(X)

print(
    clusters.labels_
)
```

### Concept

The points can be grouped into two clusters:

```text
Cluster 1
[1,1]
[1,2]

Cluster 2
[8,8]
[9,8]
```

---

# 🌍 10. Machine Learning Applications

```python
applications = {
    "Healthcare": "Disease-risk prediction",
    "Finance": "Fraud detection",
    "Retail": "Recommendation systems",
    "Education": "Personalized learning",
    "Transport": "Route and traffic prediction"
}

for field, example in applications.items():

    print(
        field,
        ":",
        example
    )
```

### Examples

| Field      | Application                  |
| ---------- | ---------------------------- |
| Healthcare | Disease-risk prediction      |
| Finance    | Fraud detection              |
| Retail     | Recommendation systems       |
| Education  | Personalized learning        |
| Transport  | Route and traffic prediction |

---

# 🎯 11. Features and Labels

```python
import pandas as pd

df = pd.DataFrame({
    "Area": [500, 800, 1000],
    "Bedrooms": [1, 2, 3],
    "Price": [100000, 160000, 200000]
})

X = df[
    ["Area", "Bedrooms"]
]

y = df["Price"]

print("Features:")
print(X)

print("Label:")
print(y)
```

### Machine Learning Structure

```text
Features (X)
     │
     ├── Area
     └── Bedrooms
          ↓
      ML Model
          ↓
     Price (y)
```

`X` represents the input features.

`y` represents the target/label.

---

# ✂️ 12. Train-Test Split

```python
from sklearn.model_selection import train_test_split

X = [
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8],
    [9],
    [10]
]

y = [
    2,
    4,
    6,
    8,
    10,
    12,
    14,
    16,
    18,
    20
]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print(
    "Training rows:",
    len(X_train)
)

print(
    "Testing rows:",
    len(X_test)
)
```

### Data Split

```text
Complete Dataset
       │
       ├──────────────┐
       ↓              ↓
   Training         Testing
     80%              20%
       │              │
       ↓              ↓
   Train Model     Evaluate Model
```

---

# 🎓 13. Student Marks Prediction

This is the complete Machine Learning exercise using multiple student features.

## Complete Code

```python
import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.metrics import (
    mean_squared_error,
    r2_score
)

data = {
    "Age": [
        18, 19, 20, 18, 21,
        22, 19, 20, 21, 22
    ],

    "StudyHours": [
        2, 3, 4, 5, 6,
        7, 3, 5, 6, 8
    ],

    "Attendance": [
        70, 75, 80, 85, 90,
        95, 72, 88, 92, 96
    ],

    "Gender": [
        0, 1, 0, 1, 0,
        1, 1, 0, 1, 0
    ],

    "Marks": [
        45, 52, 60, 68, 75,
        85, 50, 72, 80, 90
    ]
}

df = pd.DataFrame(data)

# Features
X = df[
    [
        "Age",
        "StudyHours",
        "Attendance",
        "Gender"
    ]
]

# Target
y = df["Marks"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(
    X_train,
    y_train
)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(
    y_test,
    y_pred
)

r2 = r2_score(
    y_test,
    y_pred
)

# Display results
print("Features:")
print(X)

print("Label:")
print(y)

print(
    "Training rows:",
    len(X_train)
)

print(
    "Testing rows:",
    len(X_test)
)

print("Predicted Marks:")
print(y_pred)

print(
    "Mean Squared Error:",
    mse
)

print(
    "R2 Score:",
    r2
)
```

---

# 🧠 Student Marks ML Workflow

```text
                 Student Dataset
                       │
                       ↓
        ┌────────────────────────────┐
        │ Features                   │
        │                            │
        │ Age                        │
        │ Study Hours                │
        │ Attendance                 │
        │ Gender                     │
        └────────────────────────────┘
                       │
                       ↓
                Train-Test Split
                       │
              ┌────────┴────────┐
              ↓                 ↓
          Training           Testing
              │                 │
              ↓                 │
       Linear Regression         │
              │                 │
              ↓                 ↓
           Prediction ←─────── X_test
              │
              ↓
       Model Evaluation
          │          │
          ↓          ↓
         MSE         R²
```

---

# 📏 14. Model Evaluation

Two metrics are used in the student marks prediction program.

## Mean Squared Error

```python
mse = mean_squared_error(
    y_test,
    y_pred
)
```

MSE measures the squared difference between actual and predicted values.

Generally:

```text
Lower MSE
    ↓
Smaller prediction error
```

---

## R² Score

```python
r2 = r2_score(
    y_test,
    y_pred
)
```

R² measures how well the model explains variation in the target values.

---

# 📦 Installation

Install all required libraries:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

---

# 📁 Repository Structure

```text
AI-Course-Daily-Work/
│
├── data_science_machine_learning.py
├── retail_store_sales.csv
├── requirements.txt
└── README.md
```

---

# 🔗 Complete Learning Flow

```text
                    AI COURSE
                        │
                        ↓
                    Python
                        │
          ┌─────────────┴─────────────┐
          ↓                           ↓
        NumPy                       Pandas
          │                           │
          ↓                           ↓
       Arrays                    DataFrames
          │                           │
          └─────────────┬─────────────┘
                        ↓
                  Data Cleaning
                        ↓
                   Data Analysis
                        ↓
                  Visualization
                        ↓
                  Data Science
                        ↓
               Machine Learning
                        │
             ┌──────────┴──────────┐
             ↓                     ↓
       Linear Regression       K-Means
             │                     │
             ↓                     ↓
        Prediction             Clustering
             │
             ↓
       Train-Test Split
             │
             ↓
       Model Evaluation
          │          │
          ↓          ↓
         MSE         R²
```

---

# 🎓 Course Information

**Student:** Uzair Ghole
**Program:** BSc IT
**Institute:** Hirwal Education Trust
**Course:** Artificial Intelligence

---

# 📝 Purpose of This Repository

This repository serves as a record of my **daily AI course practical work and programming practice**.

The main purpose is to learn and practice how Python is used for:

* Numerical computing
* Data manipulation
* Data cleaning
* Data analysis
* Data visualization
* Machine Learning
* Prediction
* Clustering
* Model evaluation

---

## 🚀 Learning Path

```text
Python
→ NumPy
→ Pandas
→ Data Cleaning
→ Data Analysis
→ Visualization
→ Data Science
→ Machine Learning
→ Model Evaluation
```

<p align="center">

**🤖 Learn • Practice • Analyze • Build**

</p>
