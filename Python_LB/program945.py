def CheckEven(No):
    return No % 2 == 0

def main():
    No = 0

    No = int(input())

    ret = CheckEven(No)

    if ret == 1:
        print("It is even")
    else:
        print("It is odd")

main()