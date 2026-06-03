n = int(input("Nhap n: "))

print("Hinh 1")
for i in range(n):
    for j in range(n):
        print(1, end=" ")
    print()

print("Hinh 2")
for i in range(n):
    for j in range(1, n+1):
        print(j, end=" ")
    print()

print("Hinh 3")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print("Hinh 4")
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print("Hinh 5")
for i in range(1, n+1):
    for s in range(n-i):
        print(" ", end=" ")
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print("Hinh 6")
for i in range(n, 0, -1):
    for s in range(n-i):
        print(" ", end=" ")
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print("Hinh 7")
for i in range(1, n+1):
    for s in range(n-i):
        print(" ", end=" ")
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print("Hinh 8")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    for j in range(i-1, 0, -1):
        print(j, end=" ")
    print()

print("Hinh 9")
for i in range(1, n+1):
    for s in range(n-i):
        print(" ", end=" ")
    for j in range(1, i+1):
        print(j, end=" ")
    for j in range(i-1, 0, -1):
        print(j, end=" ")
    print()
