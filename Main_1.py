def Multiplication(Value1, Value2):
    Ans = 0       # Local Variable
    Ans = Value1 * Value2
    return Ans

def main():
    No1 = 0
    No2 = 0
    Result = 0

    No1 = int(input("Enter fisrt number :"))
    No2 = int(input("Enter second number :"))

    Result = Multiplication(No1, No2)
    print("Multiplication is :", Result)

main()