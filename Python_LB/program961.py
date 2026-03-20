def summetion(arr):
    sum = 0
    for val in arr:
        sum = sum + val

    return sum

def main():
    size = int(input())
    arr = []

    for i in range(size):
        arr.append(int(input("Enter value ")))

    sum = summetion(arr)
    print(sum)

main()