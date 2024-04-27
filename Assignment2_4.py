def factorAdd(No1):
    Ans=0
    
    for i in range (1,No1,1):
        if No1%i==0:
            Ans=Ans+i

    return Ans

def main():
    print("Enter the numbe: ")
    Nu = int(input())
    Res = factorAdd(Nu)
    print("Addition of factorial: ",Res)

if __name__=="__main__":
    main()
