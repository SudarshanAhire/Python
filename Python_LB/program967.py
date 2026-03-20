def CountCapital(Arr):
    count = 0
    for ch in Arr:
        if ch >= 'A' and ch <= 'Z':
            count = count + 1

    return count

def main():
    Arr = input()

    count = CountCapital(Arr)

    print(count)

main()