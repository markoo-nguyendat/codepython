n = int(input("Nhập số phần tử của mảng: ")) # Biến để nhập tổng các phần tử
arr = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i + 1}: ")) # Nhập từng các phần tử
    arr.append(x) # append là thêm vào

print("Mảng ban đầu:", arr)

for i in range(n - 1):
    min_index = i # Min index chạy từ nhỏ nhất đến lớn
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]: # Đi từ nhỏ tới lớn
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]
    print(f"Bước {i + 1}: {arr}")
print("Mảng sau khi được sắp xếp:", arr)
