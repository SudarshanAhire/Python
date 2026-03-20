def maximun(arr):
    mini = float('inf')
    for val in arr:
        if mini > val:
            mini = val

    return mini

def main():
    size = int(input())
    arr = []

    for i in range(size):
        arr.append(int(input("Enter value ")))

    mini = maximun(arr)
    print(mini)

main()