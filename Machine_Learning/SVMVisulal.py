import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.svm import SVC
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load Dataset
data = load_breast_cancer()

# Take onlu first 2 features for 2D visualization
X = data.data[:, :2]
Y = data.target

print("Selected Features :")
print(data.feature_names[:2])

# split dataset
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
 
# Create SVM model 
model = SVC(kernel="linear", C=1.0)

# Train Model 
model.fit(X_train, Y_train)

# Prediction 
Y_pred = model.predict(X_test)

# Accuracy 
print("Accuarcy :", accuracy_score(Y_test, Y_pred))

# Function to plot decision boundary
def plot_svm_boundary(model, X, Y):
    plt.figure(figsize=(10, 7))

    # Plot data points 
    plt.scatter(X[:, 0], X[:, 1], c=Y, s=80, edgecolors='k')

    # Highlight support vectors 
    plt.scatter(
        model.support_vectors_[:, 0],
        model.support_vectors_[:, 1],
        s=200,
        facecolors='none',
        edgecolors='k',
        linewidths=2,
        label='Support Vectors'
    )

    # Create grid
    ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    xx = np.linspace(xlim[0], xlim[1], 300)
    yy = np.linspace(ylim[0], ylim[1], 300)

    YY, XX = np.meshgrid(yy, xx)
    xy = np.vstack([XX.ravel(), YY.ravel()]).T

    # Decision function values 
    Z = model.decision_function(xy).reshape(XX.shape)

    # Plot decision boundary and margins 
    ax.contour(
        XX, YY, Z,
        colors = 'k',
        levels = [-1, 0, 1],
        alpha=0.8,
        linestyles=['--', '--', '--']
    )

    plt.xlabel(data.feature_names[0])
    plt.ylabel(data.feature_names[1])
    plt.title("SVM Decision Boundary with Supposrt Vectors")
    plt.legend()
    plt.show()

# Visualize
plot_svm_boundary(model, X_train, Y_train)

