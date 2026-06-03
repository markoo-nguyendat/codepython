n = int(input("Nhập số phần tử của mảng: "))
arr = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i + 1}: "))
    arr.append(x)

print("Mảng ban đầu:", arr)

for i in range(n - 1):
    max_index = i
    for j in range(i + 1, n):
        if arr[j] > arr[max_index]:
            max_index = j
    arr[i], arr[max_index] = arr[max_index], arr[i]
    print(f"Bước {i + 1}: {arr}")

print("Mảng sau khi sắp xếp giảm dần:", arr)
