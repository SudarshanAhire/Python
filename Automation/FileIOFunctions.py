import os 

def main():
    FileName = input("Enter the name of the file : ")  # Demo.txt

    if(os.path.exists(FileName)):
       fobj = open(FileName, "r")

       print(fobj.name)    # Demo.txt
       print(fobj.mode)    # R
       print(fobj.closed)  # F

       fobj.close()
       print(fobj.closed)  # T

    else:
        print("There is no such file")
    

if __name__ == "__main__":
    main()