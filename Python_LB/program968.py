def CountCapital(Arr):
    count = 0
    for ch in Arr:
        if ch >= 65 and ch <= 90:  # Issue
            count = count + 1

    return count

def main():
    Arr = input()

    count = CountCapital(Arr)

    print(count)

main()