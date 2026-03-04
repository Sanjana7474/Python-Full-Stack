'''
n=int(input("enter value:"))
for row in range(n):
      for col in range(n):
          print(col,end='')
      print()



n=int(input("enter value:"))
for row in range(n):
      for col in range(n):
          print(row+col,end='')
      print()



n=int(input("enter value:"))
for row in range(n):
      for col in range(row+1):
          print("*",end='')
      print()


n=int(input("enter value:"))
for row in range(n):
      for col in range(n-row):
          print("*",end='')
      print()



n=int(input("enter value:"))
for row in range(n):
    for spaces in range(n-row-1):
        print(' ',end=' ')
    for col in range(row+1):
        print("*",end=' ')
    print()


n=int(input("enter value:"))
for row in range(n):
    for spaces in range(row+1):
        print(' ',end=' ')
    for col in range(n-row):
        print("*",end=' ')
    print()

'''

