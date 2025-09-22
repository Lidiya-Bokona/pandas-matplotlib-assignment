# ----------------------------------------
# analysis.py
# Analyzing Data with Pandas and Visualizing Results with Matplotlib
# ----------------------------------------

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style for better-looking plots
sns.set(style="whitegrid", palette="muted")

# -------------------------------
# Task 1: Load and Explore Dataset
# -------------------------------

# Load Iris dataset directly from seaborn (no download needed)
df = sns.load_dataset("iris")

print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

# Dataset is already clean (no missing values)

# -------------------------------
# Task 2: Basic Data Analysis
# -------------------------------

print("\nBasic statistics:")
print(df.describe())

# Group by species and compute mean values
grouped = df.groupby("species").mean()
print("\nMean values per species:")
print(grouped)

# Interesting observation: average petal length by species
print("\nAverage Petal Length by Species:")
print(df.groupby("species")["petal_length"].mean())

# -------------------------------
# Task 3: Data Visualization
# -------------------------------

# 1. Line Chart - petal length trend for first 30 samples
plt.figure(figsize=(8,5))
plt.plot(df.index[:30], df["petal_length"][:30], marker="o", label="Petal Length")
plt.title("Petal Length Trend (first 30 samples)")
plt.xlabel("Sample Index")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()

# 2. Bar Chart - average sepal length per species
plt.figure(figsize=(7,5))
sns.barplot(x="species", y="sepal_length", data=df, ci=None)
plt.title("Average Sepal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Sepal Length (cm)")
plt.show()

# 3. Histogram - distribution of petal width
plt.figure(figsize=(7,5))
plt.hist(df["petal_width"], bins=15, color="skyblue", edgecolor="black")
plt.title("Distribution of Petal Width")
plt.xlabel("Petal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot - sepal length vs petal length
plt.figure(figsize=(7,5))
sns.scatterplot(
    x="sepal_length",
    y="petal_length",
    hue="species",
    data=df,
    palette="deep"
)
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

# -------------------------------
# Findings Summary
# -------------------------------
print("\nFindings:")
print("1. The dataset has no missing values and is clean.")
print("2. Setosa species has the smallest petal lengths compared to others.")
print("3. Virginica species generally has the largest sepal lengths.")
print("4. Scatter plot shows that petal length separates Setosa clearly from other species.")
