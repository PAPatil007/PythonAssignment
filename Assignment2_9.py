def DigitCounter(No):
    count = 0
    for i in list(str(No)):
        count = count +1
    print("Count is :",count)
    
def main():
    Nu= int(input("Please enter integer number : "))
    DigitCounter(Nu)

if __name__=="__main__":
    main()
