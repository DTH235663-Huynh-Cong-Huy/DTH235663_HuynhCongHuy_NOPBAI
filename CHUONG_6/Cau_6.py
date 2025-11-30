import random

def main():
    N = int(input("Nhập số lượng phần tử N: "))

    # Tạo list ngẫu nhiên không trùng nhau trong khoảng 0..100*N (để đảm bảo đủ số lượng)
    lst = random.sample(range(0, 100*N), N)

    print("List ngẫu nhiên không trùng nhau:", lst)


# Gọi hàm main
main()
