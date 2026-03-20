def maximun(arr):
    maxi = 0
    for val in arr:
        if maxi < val:
            maxi = val

    return maxi

def main():
    size = int(input())
    arr = []

    for i in range(size):
        arr.append(int(input("Enter value ")))

    max = maximun(arr)
    print(max)

main()