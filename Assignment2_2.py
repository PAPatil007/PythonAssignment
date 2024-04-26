def StarPattern(Freq):
    for i in range(Freq):
        for i in range(Freq):
            print("*",end="  ")
        print()

def main():
    Count = int(input("Please enter your secret number:"))
    StarPattern(Count)

if __name__=="__main__":
    main()
