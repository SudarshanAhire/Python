def checkPerfect(No, iSum):
    if iSum == No:
        return True
    else: 
        return False

def isum(ret):
    sum = 0

    for val in ret:
        sum = sum + val

    return sum


def DisplayFactores(value):
    fact = []
    for i in range(1, (value//2) + 1):
        if value % i == 0:
            fact.append(i)

    return fact

def main():
    value = 0

    value = int(input())

    ret = DisplayFactores(value)

    iSum = isum(ret)

    isPefect = checkPerfect(value, iSum)

    if isPefect == True:
        print("it is perfect")
    else:
        print("Not perfect number")
    
    
main()