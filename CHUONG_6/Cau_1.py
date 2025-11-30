# ---------------------------
# Hàm kiểm tra số nguyên tố
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# ---------------------------
# Chương trình chính
def main():
    lst = []   # Khởi tạo list rỗng
    
    # Nhập số lượng phần tử
    n = int(input("Nhập số lượng phần tử của list: "))
    
    # Thêm phần tử vào list
    for i in range(n):
        x = int(input(f"Nhập phần tử thứ {i+1}: "))
        lst.append(x)

    print("\nList hiện tại:", lst)

    # Nhập k và kiểm tra số lần xuất hiện
    k = int(input("\nNhập k: "))
    dem = lst.count(k)
    print(f"Số lần xuất hiện của {k} trong list là: {dem}")

    # Tính tổng số nguyên tố
    tong_nt = sum(x for x in lst if isPrime(x))
    print("Tổng các số nguyên tố trong list là:", tong_nt)

    # Sắp xếp list
    lst.sort()
    print("List sau khi sắp xếp tăng dần:", lst)

    # Xóa list
    lst.clear()
    print("List sau khi xóa:", lst)


# Gọi hàm main
main()
