import math

def tinh_log(x, a):
    return math.log(x, a)

# Chạy thử
x = float(input("Nhập x: "))
a = float(input("Nhập cơ số a: "))

if x > 0 and a > 0 and a != 1:
    print(f"log_{a}({x}) = {tinh_log(x, a)}")
else:
    print("Giá trị x > 0, a > 0 và a ≠ 1")
