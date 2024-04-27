def displayPattern(Nu):
    for i in range(Nu,0,-1):
        for j in range(i):
            print("*",end=" ")
        print()

def main():
    print("Enter the number for pattern start: ")
    No = int(input())
    displayPattern(No)

if __name__=="__main__":
    main()
