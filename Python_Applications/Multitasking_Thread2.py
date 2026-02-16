import threading

def Display():
    print("Inside display function :", threading.get_ident())

def main():
    print("Inside Main :", threading.get_ident())
    t = threading.Thread(target=Display)
    t.start()
    
    print("End of main ")

if __name__ == "__main__":
    main()