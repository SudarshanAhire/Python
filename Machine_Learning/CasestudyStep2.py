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