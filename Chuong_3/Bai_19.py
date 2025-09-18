import math

x = float(input("Nhập x: "))
n = int(input("Nhập n: "))

S = 0
for k in range(n+1):
    S += x**(2*k+1) / math.factorial(2*k+1)

print("Giá trị S =", S)
