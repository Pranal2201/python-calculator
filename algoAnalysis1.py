def main():
     num = int(input())
     print(fun1(num))


#algorithm 1
def fun1(n):
     return int(n*(n+1)/2)


#algorithm 2
def fun2(n):
     sum = 0
     for i in range(1,n+1):
          sum = sum + i
     return sum


#algorithm 3
def fun3(n):
     sum = 0
     for i in range(1,n+1):
          for j in range(1,i+1):
               sum = sum + 1
     return sum

main()
