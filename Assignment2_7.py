def PatternDisp(No):
    No = No+1
    for i in range (1,No,1):
        for j in range(1,No,1):
            print(j,end=" ")
        print()
    
def main():
    Nu=int(input("Enter a number for pattern generation: "))
    PatternDisp(Nu)

if __name__=="__main__":
    main()
