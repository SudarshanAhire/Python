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

    print(ret)
    
main()