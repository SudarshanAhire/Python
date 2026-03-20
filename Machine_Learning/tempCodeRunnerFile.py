import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

#--------------------------------------------------------
#   Function name : LoadPreservedModel
#   Description :   It is used to load preserved model
#   Parameters :    filename
#   Return :        model
#   Date :          14/03/2026
#   Author :        Sudarshan Gokul Ahire
#--------------------------------------------------------

def LoadPreservedModel(filename):
    
    loaded_model = joblib.load(filename)

    print("Model Succesfully loaded")

    return loaded_model

#-----------------------------------------------------------------------------
# Function Name : TrainTitanicMOdel
# Description :   It does split X, Y, Trainind data , testin data
# Parameters :    Title (str)
# Return :        None
# Date :          14/03/2026
# Author :        Sudarshan Gokul Ahire
#----------------------------------------------------------------------------

def PreserveModel(model, filename):
    joblib.dump(model, filename)

    print("Model preserved succesfully with name : ", filename)


#-----------------------------------------------------------------------------
# Function Name : TrainTitanicMOdel
# Description :   It does split X, Y, Trainind data , testin data
# Parameters :    Title (str)
# Return :        None
# Date :          14/03/2026
# Author :        Sudarshan Gokul Ahire
#----------------------------------------------------------------------------

def TrainTitanicModel(df):
    # split features and labels
    X = df.drop("Survived", axis = 1)
    Y = df["Survived"]

    print("\nFeatures :", X.head())
    print("\nLabels :", Y.head())

    print("Shape of X :", X.shape)
    print("Shape of Y :", Y.shape)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    print("X_train shape :", X_train.shape)
    print("X_test shape :", X_test.shape)
    print("Y_train shape :", Y_train.shape)
    print("Y_test shape :", Y_test.shape)

    model = LogisticRegression(max_iter=1000)

    model.fit(X_train, Y_train)

    print("Model trained succesfully")

    print("\nIntercept of model :")
    print(model.intercept_)

    print("Coefficient of model")
    for feature, coefficient in zip(X.columns, model.coef_[0]):
        print(feature, " : ", coefficient)

    PreserveModel(model, "MarvellousTitanic.pkl")

    loaded_model = LoadPreservedModel("MarvellousTitanic.pkl")

    Y_pred = loaded_model.predict(X_test)

    accuracy = accuracy_score(Y_pred, Y_test)

    print("Accuracy is :", accuracy*100)

    cm = confusion_matrix(Y_pred, Y_test)

    print("Confusion matrix :")
    print(cm)

#-----------------------------------------------------------------------------
# Function Name : DisplayInfo
# Description :   It diaplays the formated title
# Parameters :    Title (str)
# Return :        None
# Date :          14/03/2026
# Author :        Sudarshan Gokul Ahire
#-----------------------------------------------------------------------------

def DisplayInfo(Title):
    print("\n" + "="*70)
    print(Title)
    print("="*70)

#-----------------------------------------------------------------------------
# Function Name : ShowData
# Description :   it shows the basic information about dataset
# Parameters :    df
#                 df -> pandas dataframe object
#                 message
#                 message -> Heading text to display
# Return :        None
# Date :          14/03/2026
# Author :        Sudarshan Gokul Ahire
#-----------------------------------------------------------------------------

def ShowData(df, message):
    DisplayInfo("message")

    print("\nFirst five rows of dataset :")
    print(df.head())

    print("\nShape of dataset :")
    print(df.shape)

    print("\nColumn names :")
    print(df.columns.tolist())

    print("\nMissing values in each column :")
    print(df.isnull().sum())

#-----------------------------------------------------------------------------
# Function Name : CleanTitanicData
# Description :   it does preprocessing 
#                 it removes unnecessory columns
#                 it handles missing values
#                 it convert text data to numeric format
#                 it does encoding to categorica columns 
# Parameters :    df -> Pandas dataframe
# Return :        df -> clean dataframe
# Date :          14/03/2026
# Author :        Sudarshan Gokul Ahire
#-----------------------------------------------------------------------------

def CleanTitanicData(df):
    DisplayInfo("Step 2 - Oroginal data")
    print(df.head())

    # Remove nuneccesary columns
    drop_columns = ["Passengerid", "zero", "Name", "Cabin"]
    existing_columns = [col for col in drop_columns if col in df.columns]

    print("\nColumns to dropped : ")
    print(existing_columns)

    # Drop the unwanted columns
    df.drop(columns=existing_columns)

    DisplayInfo("Step 2 - Data after column removel")
    print(df.head())

    # Handled age columns
    if "Age" in df.columns:
        print("Age column before filling missing values")
        print(df["Age"].head(10))

        # Invalid value gets converted as NaN
        df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
        age_median = df["Age"].median()

        # replace missing values with median
        df["Age"] = df["Age"].fillna(age_median)

        print("\nAge colummn after preprocessing :")
        print(df["Age"].head(10))

    # Handled fare column
    if "Fare" in df.columns:
        print("Fare column before preprocessing")
        print(df["Fare"].head(10))

        df["Fare"] = pd.to_numeric(df["Fare"], errors="coerce")

        fare_median = df["Fare"].median()
        print("Meadian of fare column is :", fare_median)

        # replace missing values with median
        df["Fare"] = df["Fare"].fillna(fare_median)

        print("\nFare column after preprocessing")
        print(df.head(10))

    # Handled embarked column
    if "Embarked" in df.columns:
        print("\nEmbarked column befor preprocessing")
        print(df["Embarked"].head(10))

        # Convert the data into string
        df["Embarked"] = df["Embarked"].astype(str).str.strip()

        # remove missing values
        df["Embarked"] = df["Embarked"].replace(('nan', 'None', ' '), np.nan)

        # get mor frequent value
        embarked_mode = df["Embarked"].mode()[0]
        print("mode of embarked column :", embarked_mode)
        df["Embarked"] = df["Embarked"].fillna(embarked_mode)

        print("\nEmbarked column after preprocessing :")
        print(df["Embarked"].head(10))

    # Handled sex column
    if "Sex" in df.columns:
        print("Sex column before preprocessing")
        print(df["Sex"].head(10))

        df["Sex"] = pd.to_numeric(df["Sex"], errors="coerce")

        print("\nSex column after preprocessing :")
        print(df["Sex"].head(10))

    DisplayInfo("Data after preprocessing")
    print(df.head(5))

    print("\nMissing values after preprocessing")
    print(df.isnull().sum())

    # Encode embarked columns
    df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)
    print("\nData after encoding")

    print(df.head())

    print("Shape of dataset : ", df.shape)

    # Convert boolean columns into integer
    for col in df.columns:
        if df[col].dtype == bool:
            df[col] = df[col].astype(int)

    print("\nData after encoding")

    print(df.head())

    return df


#-----------------------------------------------------------------------------
# Function Name : MarvellousTitanicLogistic
# Description :   this is main pipeline controller 
#                 it loads the dataset , shows raw data, it preprocess the dataset, 
#                 and train the model
# Parameters :    Data Path of of dataset file
# Return :        None
# Date :          14/03/2026
# Author :        Sudarshan Gokul Ahire
#-----------------------------------------------------------------------------

def MarvellousTitanicLogistic(DataPath):
    DisplayInfo("Step 1 - Loading the dataset")

    df = pd.read_csv(DataPath)

    ShowData(df, "Initial dataset")

    df = CleanTitanicData(df)

    TrainTitanicModel(df)


#-----------------------------------------------------------------------------
# Function Name : main
# Description :   Starting point of the application
# Parameters :    None
# Return :        None
# Date :          14/03/2026
# Author :        Sudarshan Gokul Ahire
#-----------------------------------------------------------------------------

def main():
    MarvellousTitanicLogistic("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()