# Hàm tính tổng ước số (không kể chính nó)
def tong_uoc_so(n):
    tong = 1  # luôn có ước số 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            tong += i
            if i != n // i:  # tránh cộng trùng khi i*i = n
                tong += n // i
    return tong if n != 1 else 0

# a) Kiểm tra số hoàn thiện
def so_hoan_thien(n):
    return tong_uoc_so(n) == n

# b) Kiểm tra số thịnh vượng
def so_thinh_vuong(n):
    return tong_uoc_so(n) > n

# Chạy thử
n = int(input("Nhập số nguyên dương n: "))

if so_hoan_thien(n):
    print(f"{n} là số hoàn thiện")
elif so_thinh_vuong(n):
    print(f"{n} là số thịnh vượng")
else:
    print(f"{n} không phải số hoàn thiện cũng không phải số thịnh vượng")
