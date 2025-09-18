import math

def tinh_S(x, n):
    S = 0
    for k in range(1, n+1):
        S += x**k / math.factorial(k)
    return S

# Nhập dữ liệu
x = float(input("Nhập x: "))
n = int(input("Nhập n: "))

print("Kết quả S(x, n) =", tinh_S(x, n))
