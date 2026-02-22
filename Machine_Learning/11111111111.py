##########################################################################################
# Histogram
##########################################################################################

# import pandas as pd
# import matplotlib.pyplot as plt 

# def main():
#     df = pd.read_csv("iris.csv")

#     plt.figure(figsize=(8, 5))
#     plt.hist(df["sepal length (cm)"], bins=10, color="skyblue", edgecolor="black")

#     plt.xlabel("Sepal Length")
#     plt.ylabel("Frequency")
#     plt.title("Marvellous Histogram - Sepal Length Distribution")

#     plt.grid(alpha=0.3)
#     plt.show()

# if __name__ == "__main__":
#     main()



##########################################################################################
# Boxplot
##########################################################################################

# import pandas as pd
# import seaborn as sns 
# import matplotlib.pyplot as plt 

# def main():
#     df = pd.read_csv("iris.csv")

#     plt.figure(figsize=(8, 5))
#     sns.boxplot(x="species", y="petal length (cm)", data=df)

#     plt.title("Marvellous Boxplot - Peatl Legnth by Variety")
#     plt.show()

# if __name__ == "__main__":
#     main()


##########################################################################################
# Pairplot
##########################################################################################

# import pandas as pd 
# import seaborn as sns 
# import matplotlib.pyplot as plt

# def main():
#     df = pd.read_csv("iris.csv")

#     sns.pairplot(df, hue="species")
#     plt.show()

# if __name__ == "__main__":
#     main()

##########################################################################################
# 3D Scatter plot
##########################################################################################

# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt 
# from sklearn.datasets import load_iris 

# def main():
#     iris = load_iris()
#     X = iris.data
#     y = iris.target

#     fig = plt.figure(figsize=(8, 5))
#     ax = fig.add_subplot(111, projection="3d")

#     ax.scatter(X[:, 2], X[:, 3], X[:, 0], c=y, cmap="viridis", edgecolor='k')

#     ax.set_xlabel("Peatl Length")
#     ax.set_ylabel("Peatl Width")
#     ax.set_zlabel("Sepal Length")

#     plt.title("Marvellous 3D Visualization - IRIS")
#     plt.show()

# if __name__ == "__main__":
#     main()


##########################################################################################
# Scatter Plot
##########################################################################################

# import matplotlib.pyplot as plt 
# import pandas as pd

# df = pd.read_csv("iris.csv")

# plt.scatter(df["sepal length (cm)"], df["petal length (cm)"])
# plt.xlabel("Sepal Length")
# plt.ylabel("Petal Length")
# plt.title("Scatter Plot")
# plt.show()


##########################################################################################
# Correlation Heatmap
##########################################################################################

# import seaborn as sns 
# import matplotlib.pyplot as plt 
# import pandas as pd

# df = pd.read_csv("iris.csv")

# corr = df.corr()

# plt.figure(figsize=(8, 5))
# sns.heatmap(corr, annot=True, cmap="coolwarm")
# plt.title("Correlation Matrix")
# plt.show()


##########################################################################################
# Countplot
##########################################################################################

import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")

sns.countplot(x="species", data=df)
plt.title("Count of Each Species")
plt.show()
