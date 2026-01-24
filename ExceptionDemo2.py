def main():
    Ans = 0
    
    try:
        print("Insdie try")
        print("Enter first number : ")
        No1 = int(input())

        print("Enter second number : ")
        No2 = int(input())

        Ans = No1 / No2

    except:
        print("Inside except")

    finally:
        print("Inside finally")
    


    print("Dividion is : ", Ans)

if __name__ == "__main__":
    main()