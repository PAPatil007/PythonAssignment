def numberType(No):
    if No>0:
        print("Number is positive")
    elif No<0:
        print("Number is negative")
    else :
        print("Number is Zero")
    
def main():
    Nu=float(input("Please enter a number:"))
    numberType(Nu)

if __name__=="__main__":
    main()
