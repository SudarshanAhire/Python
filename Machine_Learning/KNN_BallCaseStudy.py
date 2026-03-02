# Not coded in class its a homework

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

def main():

    X = [[35, 1], [47, 1], [90,0], [95, 0], [35, 1], [110, 0], [43, 1], [96, 0], [92, 0], [48, 1]]

    Y = [1, 1, 2, 2, 1, 2, 1, 2, 2, 1]

    model = KNeighborsClassifier(n_neighbors=3)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    model.fit(X_train, Y_train)

    Y_pred = model.predict([[52, 1]])[0]

    print(Y_pred)

    if Y_pred == 2:
        print("It is cricket ball")
    else:
        print("it is tennis ball")


if __name__ == "__main__":
    main()