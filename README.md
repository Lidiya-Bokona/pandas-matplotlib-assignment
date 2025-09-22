# 📊 Analyzing Data with Pandas and Visualizing Results with Matplotlib

## 🎯 Objective
This assignment demonstrates how to:
- Load and explore a dataset using **pandas**.
- Perform basic data analysis.
- Visualize data using **matplotlib** and **seaborn**.

Dataset: **Iris dataset**.

---

## ✅ Tasks Completed

### 1. Load and Explore Dataset
- Loaded Iris dataset using `sns.load_dataset("iris")`.
- Displayed first rows with `.head()`.
- Checked dataset structure with `.info()` and missing values.
- Dataset is clean with no missing values.

### 2. Basic Data Analysis
- Computed basic statistics with `.describe()`.
- Grouped data by species to calculate mean values.
- Observed that **Setosa species has the smallest petal lengths**, while Virginica generally has the largest sepals.

### 3. Data Visualization
Created 4 types of plots:

1. **Line chart** – Petal length trend for the first 30 samples.  
2. **Bar chart** – Average sepal length per species.  
3. **Histogram** – Distribution of petal width.  
4. **Scatter plot** – Sepal length vs petal length, color-coded by species.  

Each plot is properly labeled with titles, axes, and legends.

---

## 📈 Key Findings
- **Setosa** is clearly separated by smaller petal lengths.  
- **Virginica** generally has the largest sepal lengths.  
- Petal length is a strong feature to distinguish Setosa from other species.  
- Overall, the dataset is clean and easy to analyze.

---

## 🛠️ Requirements
Install dependencies if not already installed:
```bash
pip install pandas matplotlib seaborn
