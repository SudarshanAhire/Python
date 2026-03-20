def small(st):
    st = ""

    for ch in st:
        if (ch >= 'a' and ch <= 'z'):
            st = st + ch

    print(st)

    return st

def main():
    st = input()

    ret = small(st)

    print(ret)

main()