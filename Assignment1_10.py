def AlphabetCount(Var):
    count = 0
    for i in Var:
        count = count + 1
        print(i)
    
    return count

def main():
    var = input("Please enter string to check count of alphabet : ")
    Res = AlphabetCount(var)
    print("Alphabet count is : ",Res)

if __name__=="__main__":
    main()
