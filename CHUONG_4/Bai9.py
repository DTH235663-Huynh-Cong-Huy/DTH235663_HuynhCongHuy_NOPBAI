import math

def can_bac_2_long(n):
    result = 0
    for i in range(1, n + 1):
        result = math.sqrt(i + result)
    return result

# Chạy thử
n = int(input("Nhập n: "))
print(f"Căn bậc 2 lồng nhau của {n} là: {can_bac_2_long(n)}")
