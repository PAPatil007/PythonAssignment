#Specific job handling function
def PatternDisp(No):
    No=No+1
    for i in range(1,No,1):
        i = i +1
        for j in range(1,i):
            print(j,end=" ")
        print()

#Main function
def main():
    Nu = int(input("Enter a number for pattern generation:"))
    PatternDisp(Nu)

#Starter
if __name__=="__main__":
    main()
