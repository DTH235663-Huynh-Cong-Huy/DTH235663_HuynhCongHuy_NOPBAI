# Giới thiệu Python và Các Câu Lệnh Cơ Bản

## 1. Giới thiệu Python
Python là một ngôn ngữ lập trình bậc cao, thông dịch, dễ học và mạnh mẽ.  
Một số đặc điểm nổi bật:
- Cú pháp đơn giản, dễ đọc.
- Hỗ trợ lập trình hướng đối tượng, hàm, thủ tục.
- Có thư viện phong phú.
- Được sử dụng nhiều trong: phát triển web, khoa học dữ liệu, trí tuệ nhân tạo, tự động hóa,...

---

## 2. Câu lệnh cơ bản trong Python

### 2.1. In ra màn hình (`print`)

print("Xin chào Python!")

**Kết quả:**

### 2.2. Khai báo biến và kiểu dữ liệu

x = 10        # số nguyên
y = 3.14      # số thực
name = "An"   # chuỗi
is_ok = True  # boolean

print(x, y, name, is_ok)

**Kết quả:**

10 3.14 An True
### 2.3. Nhập dữ liệu từ bàn phím (`input`)

name = input("Nhập tên của bạn: ")
print("Xin chào,", name)

**Kết quả (ví dụ nhập "An"):**

##Nhập tên của bạn: An
Xin chào, An

### 2.4. Cấu trúc điều kiện (`if`, `elif`, `else`)
n = 5
if n > 0:
    print("Số dương")
elif n == 0:
    print("Số 0")
else:
    print("Số âm")
**Kết quả:**
Số dương

### 2.5. Vòng lặp `for`
for i in range(1, 6):
    print("i =", i)

**Kết quả:**

i = 1
i = 2
i = 3
i = 4
i = 5

### 2.6. Vòng lặp `while`
count = 0
while count < 3:
    print("Lặp lần", count)
    count += 1
**Kết quả:**
Lặp lần 0
Lặp lần 1
Lặp lần 2

### 2.7. Hàm trong Python (`def`)
def tong(a, b):
    return a + b

print("Tổng 3 + 4 =", tong(3, 4))
**Kết quả:**
Tổng 3 + 4 = 7
### 2.8. Danh sách (List)
fruits = ["Táo", "Cam", "Xoài"]
print(fruits[0])   # Truy cập phần tử đầu tiên
fruits.append("Chuối")  # Thêm phần tử
print(fruits)

**Kết quả:**
Táo
['Táo', 'Cam', 'Xoài', 'Chuối']

### 2.9. Vòng lặp với danh sách
for fruit in ["Táo", "Cam", "Xoài"]:
    print("Tôi thích", fruit)
**Kết quả:**
Tôi thích Táo
Tôi thích Cam
Tôi thích Xoài

### 2.10. Thư viện chuẩn (`import`)
import math

print("Căn bậc hai của 16 là:", math.sqrt(16))
**Kết quả:**
Căn bậc hai của 16 là: 4.0

## 3. Kết luận
Python rất dễ tiếp cận cho người mới bắt đầu, đồng thời đủ mạnh để giải quyết các bài toán phức tạp.  
Nắm vững các câu lệnh cơ bản trên sẽ giúp bạn nhanh chóng bắt đầu lập trình với Python.
