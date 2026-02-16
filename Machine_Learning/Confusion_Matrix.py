from sklearn.datasets import load_iris
from sklearn.metrics import confusion_metrix

def main():
    # 1 : Positive
    # 0 : Negative

    Actual = [1, 0, 1, 1, 1, 0, 1, 0, 0, 1]
    Predicted = [1, 0, 0, 1, 1, 1, 1, 1, 0, 1]

    print("Actual Data : ", Actual)
    print("Predicted Data :", Predicted)

    con_mat = confusion_metrix(Actual, Predicted)

    print(con_mat)


if __name__ == "__main__":
    main()


