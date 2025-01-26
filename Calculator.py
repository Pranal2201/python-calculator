def main():
     print("Choose Operation : \n1. Addition\n2.Subtraction\n3.Multiply\n4.Division")
     c = int(input())
     
     
     if c == 1:
          print("Enter the values:")
          a = int(input())
          b = int(input())
          print(Sum(a, b))
          
     elif c == 2:
          print("Enter the values:")
          a = int(input())
          b = int(input())
          print(Subtract(a,b))
          
     elif c == 3:
          print("Enter the values:")
          a = int(input())
          b = int(input())
          print(multiply(a,b))
          
     elif c == 4:
          print("Enter the values:")
          a = int(input())
          b = int(input())
          #r = Division(a,b)
          #print(f"{r:.2f}")
          print(f"{Division(a,b):.2f}")
          
     else:
          print("Enter a valid option!")


def Sum(x, y):
     return x + y

def Subtract(x,y):
     return x - y

def multiply(x,y):
     return (x*y)

def Division(x,y):
     return  x/y

main()



     
