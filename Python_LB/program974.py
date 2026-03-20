def LowerCase(string):

    result = ""
    
    for val in string:
        if val >= 'A' and val <= 'Z':
            result = result + chr(ord(val) + 32)
        else:
            result = result + chr(ord(val) - 32)

    return result

def main():
    string = input()

    ret = LowerCase(string)

    print(ret)


main()