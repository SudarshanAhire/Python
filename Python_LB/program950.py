def Sum(no):
    sum = 0
    while no > 0:
        dig = no % 10
        sum = sum + dig
        no = no / 10   # issue

    return sum

def main():
    no = int(input())

    sum = Sum(no)

    print(sum)

main()