import random

# -------------------------
# Hàm kiểm tra list có đối xứng không
def isSymmetry(lst):
    return lst == lst[::-1]


# -------------------------
# Chương trình chính
def main():
    # Nhập số lượng phần tử
    n = int(input("Nhập số lượng phần tử n: "))

    # 1. Khởi tạo list n phần tử ngẫu nhiên trong khoảng 0..100
    lst = [random.randint(0, 100) for _ in range(n)]
    print("List ngẫu nhiên:", lst)

    # 2. Nhập k và xóa tất cả phần tử có giá trị k
    k = int(input("\nNhập k: "))

    # Xóa bằng list comprehension
    lst = [x for x in lst if x != k]
    print("List sau khi xóa tất cả", k, ":", lst)

    # 3. Kiểm tra đối xứng
    if isSymmetry(lst):
        print("List đối xứng.")
    else:
        print("List không đối xứng.")

# Gọi hàm main
main()
