def Add(No1,No2):
    Ans=0
    Ans=No1+No2
    print("Addition is : ", Ans)

def main():
    print("Please enter 2 numbers for addition:")
    N1 = int(input("Enter first number:"))
    N2 = int(input("Enter second number:"))

    Add(N1,N2)

if __name__=="__main__":
    main()
