def AddDigits(Nu):
    Nu = str(Nu)
    Ans = 0
    for i in list(Nu):
        Ans = Ans + int(i)

    print("Addition is : ",Ans)

def main():
    No=int(input("Enter number for addtion of digits: "))
    AddDigits(No)

if __name__=="__main__":
    main()
