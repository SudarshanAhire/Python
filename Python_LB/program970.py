def small(st):
    st = ""

    for ch in st:
        if ord(ch) >= 65 and ord(ch) <= 90:
            st.append(ch)

    return st

def main():
    st = input()

    ret = small(st)

    print(ret)

main()