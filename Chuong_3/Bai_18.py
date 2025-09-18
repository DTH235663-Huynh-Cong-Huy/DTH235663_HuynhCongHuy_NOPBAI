# Vẽ 3 hình bằng dấu * (hình 3 giống ảnh bạn gửi)

n = int(input("Nhập chiều cao n (thường chọn số lẻ như 7): "))
mid = n // 2

print("\nHình 1: Hình vuông rỗng")
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("\nHình 2: Hình tam giác vuông (ngược bên phải)")
for i in range(1, n+1):
    for _ in range(n - i):
        print(" ", end=" ")
    for _ in range(i):
        print("*", end=" ")
    print()

print("\nHình 3: Hình 3 theo ảnh (cột trái lên đến giữa, đường chéo, hàng giữa, cột phải từ giữa xuống)")
for i in range(n):
    for j in range(n):
        if (i == j) or (i == mid) or (j == 0 and i <= mid) or (j == n - 1 and i >= mid):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
