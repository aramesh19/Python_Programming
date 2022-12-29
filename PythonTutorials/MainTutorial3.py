print("First module's name: {}".format(__name__))

def main():
    print("inside main module in maintut3")

if __name__ == "__main__":
    main()
    print("Run directly")
else:
    print("Run from import")