# Functional Approach -> lambda

# def CheckEven(No):
#     return (No % 2 == 0)

CheckEven = lambda No : (No % 2 == 0)

def main():
    value = 0
    Ret = False

    print("Enter number : ")
    value = int(input())
    
    Ret = CheckEven(value)
    
    if(Ret == True):
        print("it is Even")
    else:
        print("it is Odd")

if __name__ == "__main__":
    main()