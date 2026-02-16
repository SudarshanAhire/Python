def CheckEven(no):
    if(no % 2  == 0):
        print("it is Even")
    else:
        print("it is Odd")

def main():
    CheckEven(21)        # Positional Argument
    CheckEven(no = 22)   # Keyword Argument

if __name__ == "__main__":
    main()