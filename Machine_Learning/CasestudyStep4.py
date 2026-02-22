import pandas as pd 

import numpy as np 

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split 

from sklearn.tree import DecisionTreeClassifier, plot_tree 

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

Border = "-"*40

#################################################################################################
# Step 1 - Load the dataset
#################################################################################################

print(Border)
print("Step 1- Load the Dataset")
print(Border)

Dataset = "iris.csv"

df = pd.read_csv(Dataset)

print("Dataset gets loaded succesfully...")
print("Initial entries from dataset :")
print(df.head())

#################################################################################################
# Step 2 - Data Analysis (EDA)
#################################################################################################

print(Border)
print("Step 2 - Data Analysis")
print(Border)

print("Shape of dataset : ", df.shape)
print("Column Names :", list(df.columns))

print("Missing values (per Column)")
print(df.isnull().sum())

print("Class Distribution (Species count)")
print(df["species"].value_counts())

print("Statistical Report of Dataset")
print(df.describe())

#################################################################################################
# Step 3 - Decide Independent and Dependent Variables
#################################################################################################

print(Border)
print("Step 3 - Decide Independent and Dependent Variables")
print(Border)

# X : Independent Variables / Labels
# Y : Dependent Variables / Labels

feature_cols = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
]

X = df[feature_cols]
Y = df["species"]

print("X shape :", X.shape)
print("Y shape :", Y.shape)

#################################################################################################
# Step 4 - Visualisation of Dataset
#################################################################################################

print(Border)
print("Step 4 - Visualisation of Dataset")
print(Border)

# Scatter plot

plt.figure(figsize=(7, 5))

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"], temp["petal width (cm)"], label = sp)

plt.title("Iris : Petal Length vs Petal Width")

plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.legend()
plt.grid(True)
plt.show()
