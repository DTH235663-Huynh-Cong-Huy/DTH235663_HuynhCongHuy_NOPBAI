# Hàm kiểm tra số nguyên tố
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def main():
    # Nhập mảng M
    M = [3,6,7,8,11,17,2,90,2,5,4,5,8]

    # -------------------------
    # Dòng 1: các số lẻ
    le = [x for x in M if x % 2 != 0]
    print("Số lẻ:", le, "Tổng số lẻ:", len(le))

    # Dòng 2: các số chẵn
    chan = [x for x in M if x % 2 == 0]
    print("Số chẵn:", chan, "Tổng số chẵn:", len(chan))

    # Dòng 3: các số nguyên tố
    nguyen_to = [x for x in M if isPrime(x)]
    print("Số nguyên tố:", nguyen_to)

    # Dòng 4: các số không phải nguyên tố
    khong_nguyen_to = [x for x in M if not isPrime(x)]
    print("Số không phải nguyên tố:", khong_nguyen_to)


# Gọi hàm main
main()
