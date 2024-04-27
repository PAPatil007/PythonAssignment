def factorial(No1):
    Ans = 1
    No2=No1+1
    for i in range(1,No2,1):
        Ans=Ans*i

    return Ans

def main():
    Nu=int(input("Please enter number: "))
    Res = factorial(Nu)
    print("Factorial = ",Res)

if __name__=="__main__":
    main()
