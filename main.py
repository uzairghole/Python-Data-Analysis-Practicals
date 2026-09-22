import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. NUMPY BASE-PRACTICE
# ==========================================

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
m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nElement at (1,2):", m[1, 2])
print("Second column:", m[:, 1])
print("First two rows:\n", m[0:2, :])

# Boolean masking & Fancy indexing
scores = np.array([85, 42, 91, 67, 73])
passed = scores[scores >= 70]
print("\nPassed Scores:", passed)
print("Fancy Indexing:", arr[[0, 3, 4]])


# ==========================================
# 2. PANDAS BASE-PRACTICE
# ==========================================

# Create DataFrame & inspect structure
df_demo = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Dept": ["IT", "HR", "IT", "HR"],
    "Salary": [70000, 65000, 80000, 72000]
})

# Filtering & Sorting
it_team = df_demo[df_demo["Dept"] == "IT"]
high_pay = df_demo[df_demo["Salary"] > 70000]
sorted_df = df_demo.sort_values("Salary", ascending=False)

# New Column & Aggregation
df_demo["Bonus"] = df_demo["Salary"] * 0.1
dept_avg = df_demo.groupby("Dept")["Salary"].mean()

print("\n--- Department Average Salary ---")
print(dept_avg)

# Clean up DataFrame columns
df_demo = df_demo.drop(columns=["Bonus"]).rename(columns={"Dept": "Department"})


# ==========================================
# 3. DATA CLEANING & ANALYSIS WORKFLOW
# ==========================================

# Load retail sales dataset
file_path = "retail_store_sales.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    
    # Standardize column headers to lower_snake_case
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    
    print("\n--- Dataset Summary ---")
    df.info()
    print("\n--- Statistical Overview ---")
    print(df.describe())

    # Missing values check
    missing_pct = df.isnull().mean() * 100
    print("\n--- Missing Value Percentage ---")
    print(missing_pct)

    # Check duplicated rows
    duplicates = df[df.duplicated()]
    print(f"\nDuplicate Rows Found: {len(duplicates)}")

    # Data Cleaning Ops
    df_cleaned = df.drop(columns=["transaction_id"], errors="ignore")

    # Conditionally fill missing items
    condition = (
        (df_cleaned["item"].isna()) & 
        (df_cleaned["price_per_unit"] == 33.5) & 
        (df_cleaned["category"] == "Furniture")
    )
    df_cleaned.loc[condition, "item"] = "Item_20_FUR"

    # View updated record subset
    target_items = df_cleaned[
        (df_cleaned["price_per_unit"] == 33.5) & 
        (df_cleaned["category"] == "Furniture")
    ]
    print("\n--- Updated Targeted Records ---")
    print(target_items)
else:
    print(f"\nNote: '{file_path}' not found. Skipping file read steps.")


# ==========================================
# 4. VISUALIZATIONS
# ==========================================

# Chart 1: Exam Score Distribution
plt.figure(figsize=(8, 4))
data = np.random.normal(70, 10, 1000)

plt.hist(data, bins=17, edgecolor="#4A5568", alpha=0.7, color="#4FD1C5")
plt.axvline(data.mean(), color="#E53E3E", linestyle="--", linewidth=2, label=f"Mean: {data.mean():.2f}")
plt.title("Exam Score Distribution", fontsize=12, pad=10)
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.show()

# Chart 2: Trigonometric Functions
plt.figure(figsize=(8, 4))
x = np.linspace(0, 10, 100)

plt.plot(x, np.sin(x), label="sin(x)", linewidth=2)
plt.plot(x, np.cos(x), label="cos(x)", linewidth=2, linestyle="--")
plt.title("Trigonometric Functions", fontsize=12, pad=10)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()


# ==========================================
# . DATA SCIENCE AND MACHING LEARNING
# ==========================================

import pandas as pd
data = {
    "Product": ["A", "B", "A", "C"],
    "Sales": [100, 200, 150, 120]
}
df = pd.DataFrame(data)
print(df)
print("Total sales:", df["Sales"].sum())


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


from sklearn.linear_model import LinearRegression
X = [[500], [800], [1000], [1200]]
y = [100000, 160000, 200000, 240000]
model = LinearRegression()
model.fit(X, y)
prediction = model.predict([[900]])
print("Predicted price:", prediction[0])


from sklearn.linear_model import LinearRegression
X = [[1], [2], [3]]
y = [2, 4, 6]
model = LinearRegression()
model.fit(X, y)
print(model.predict([[4]]))


from sklearn.cluster import KMeans
X = [[1, 1], [1, 2], [8, 8], [9, 8]]
clusters = KMeans(n_clusters=2, random_state=42, n_init=10)
clusters.fit(X)
print(clusters.labels_)


applications = {
    "Healthcare": "Disease-risk prediction",
    "Finance": "Fraud detection",
    "Retail": "Recommendation systems",
    "Education": "Personalized learning",
    "Transport": "Route and traffic prediction"
}
for field, example in applications.items():
    print(field, ":", example)


import pandas as pd
df = pd.DataFrame({
    "Area": [500, 800, 1000],
    "Bedrooms": [1, 2, 3],
    "Price": [100000, 160000, 200000]
})
X = df[["Area", "Bedrooms"]]
y = df["Price"]
print("Features:")
print(X)
print("Label:")
print(y)


from sklearn.model_selection import train_test_split
X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print("Training rows:", len(X_train))
print("Testing rows:", len(X_test))


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = {
    "Age": [18, 19, 20, 18, 21, 22, 19, 20, 21, 22],
    "StudyHours": [2, 3, 4, 5, 6, 7, 3, 5, 6, 8],
    "Attendance": [70, 75, 80, 85, 90, 95, 72, 88, 92, 96],
    "Gender": [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    "Marks": [45, 52, 60, 68, 75, 85, 50, 72, 80, 90]
}

df = pd.DataFrame(data)

X = df[["Age", "StudyHours", "Attendance", "Gender"]]
y = df["Marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Features:")
print(X)
print("Label:")
print(y)
print("Training rows:", len(X_train))
print("Testing rows:", len(X_test))
print("Predicted Marks:")
print(y_pred)
print("Mean Squared Error:", mse)
print("R2 Score:", r2)
