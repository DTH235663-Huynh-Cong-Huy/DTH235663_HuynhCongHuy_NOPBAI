# Nhập chiều dài và chiều rộng của hình chữ nhật
length = int(input("Nhập chiều dài của hình chữ nhật: "))
width = int(input("Nhập chiều rộng của hình chữ nhật: "))

# Sử dụng vòng lặp để in hình chữ nhật
for i in range(width):
    for j in range(length):
        print("*", end=" ")  # In dấu * với khoảng cách
    print()  # Chuyển dòng sau khi in xong một hàng
