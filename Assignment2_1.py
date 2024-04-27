## All import
import Arithmetic

def main():
    print("Please enter 2 numberss: ")
    No1 = int(input())
    No2 = int(input())

    Res = Arithmetic.Add(No1,No2)
    print("Addition is :",Res)

    Res = Arithmetic.Sub(No1,No2)
    print("Substraction = ",Res)

    Res = Arithmetic.Multi(No1,No2)
    print("Multiplication: ",Res)

    Res = Arithmetic.Div(No1,No2)
    print("Division : ",Res)

if __name__=="__main__":
    main()
