def DisplayStar (Freq):
  for i in range(Freq):
    print("*",end=" ")

def main():
  count = int(input("Enter the count of star to be diplayed : "))
  DisplayStar(count)

if __name__=="__main__":
  main()
