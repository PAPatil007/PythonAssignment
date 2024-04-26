def display_descend(No1):
    for i in range(No1,0,-1):
        print(i,end=" ")

def main():
    N1 = int(input("Please enter a number to see in descending order:"))
    display_descend(N1)

if __name__=="__main__":
    main()
