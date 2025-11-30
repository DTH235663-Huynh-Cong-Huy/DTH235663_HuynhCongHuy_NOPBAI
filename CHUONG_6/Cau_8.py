def main():
    n = int(input("Nhập số lượng phần tử n: "))
    M = []

    # Nhập dãy số thực
    for i in range(n):
        x = float(input(f"Nhập phần tử thứ {i}: "))
        M.append(x)

    # Sắp xếp giảm dần
    M.sort(reverse=True)

    # Xuất dãy số sau khi sắp xếp
    print("\nDãy số sau khi sắp xếp giảm dần:", M)


# Gọi hàm main
main()
