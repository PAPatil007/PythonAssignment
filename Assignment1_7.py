def divBy5(No):
    if No%5==0:
        print("True")
    else:
        print("False")

def main():
    Nu = int(input("Enter a number to check if divisible by 5 or not"))
    divBy5(Nu)
    
if __name__=="__main__":
    main()
