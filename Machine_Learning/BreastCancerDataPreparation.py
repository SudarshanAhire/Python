import pandas as pd
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()

df = pd.DataFrame(data.data, columns=data.feature_names)
df["target"] = data.target

df.to_csv("Breast_Cancer.csv", index=False)

print("Breast_Cancer.csv file gets created succesfully")