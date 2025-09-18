#Câu 8: Nhập vào 2 giá trị a, b và phép toán ‘+’, ‘-’, ‘*’, ‘/’ . Hãy xuất kết quả theo
#đúng phép toán đã nhập.

print("Chương Trình Máy Tính Đơn Giản")
a = float(input("Nhập số thứ nhất (a): "))
b = float(input("Nhập số thứ hai (b): "))
operation = input("Nhập phép toán (+, -, *, /): ")
if operation == '+':
    result = a + b
    print(f"Kết quả: {a} + {b} = {result}")
elif operation == '-':
    result = a - b
    print(f"Kết quả: {a} - {b} = {result}")
elif operation == '*':
    result = a * b
    print(f"Kết quả: {a} * {b} = {result}")
elif operation == '/':
    if b != 0:
        result = a / b
        print(f"Kết quả: {a} / {b} = {result}")
    else:
        print("Lỗi: Không thể chia cho 0.")
else:
    print("Phép toán không hợp lệ. Vui lòng nhập một trong các phép toán: +, -, *, /.")
