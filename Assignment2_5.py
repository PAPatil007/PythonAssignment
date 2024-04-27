def CheckPrime(No1):
    Div = list()
    for i in range(1,No1,1):
        if No1%i==0:
            Div.append(i)

    if len(Div)>1:
        print("Not prime number")
    else:
        print("Its Prime number")

def main():
    Nu = int(input("Enter a number: "))
    CheckPrime(Nu)

if __name__=="__main__":
    main()
