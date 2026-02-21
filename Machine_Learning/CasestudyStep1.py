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
print("Step 1 - Load the Dataset")
print(Border)

Dataset = "iris.csv"

df = pd.read_csv(Dataset)

print("Dataset gets loaded succesfully...")
print("Initial entries from dataset :")
print(df.head())



