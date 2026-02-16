# Procedural 

def CheckEven(no):
    if(no % 2  == 0):
        print("it is Even")
    else:
        print("it is Odd")

def main():
    value = 0

    print("Enter number : ")
    value = int(input())

    CheckEven(value)

if __name__ == "__main__":
    main()