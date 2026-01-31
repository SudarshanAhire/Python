import os 

def main():
    FileName = input("Enter the name of the file : ")

    Ret = os.path.exists(FileName)

    if (Ret == True):
        fobj = open(FileName, "r")
        print("File gets succesfully opened")

    else:
        print("There is no such files")


    

if __name__ == "__main__":
    main()