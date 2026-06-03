m=int(input("nhập chiều rộng m:"))
n=int(input("nhập chiểu dài n:"))
for i in range(m):
    for j in range(n):
        print("*",end=" ")
    print()

a = int(input("cạnh tam giác a = "))
for i in range(a):
    for j in range(i+1):
        print("*",end=" ")
    print()

a = int(input("cạnh tam giác a = "))
for i in range(a):
    for j in range(a-i):
        print("*",end=" ")
    print()

print("\n")
a = int(input("cạnh tam giác a = "))
for i in range(a+1):
    for j in range(a):
        if j < a-i:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()

print("\n")
a = int(input("cạnh tam giác a = "))
for i in range(a+1):
    for j in range(1,i+1):
        if j==1 or j==i or i==a:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("\n")
a = int(input("cạnh tam giác a = "))
for i in range(1,a+1):
    for j in range(a):
        if j==a-i or j==a-1 or i==a:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("\n")

a = int(input("cạnh tam giác a = "))
