def ChkNum(No):
    if No%2==0:
        print("Even Number")
    else:
        print("Odd number")

def main():
    print("Please input a number to check odd or even")
    N1 = int(input())
    ChkNum(N1)

if __name__=="__main__":
    main()
