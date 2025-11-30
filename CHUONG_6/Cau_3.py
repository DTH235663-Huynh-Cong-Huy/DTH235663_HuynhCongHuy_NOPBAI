import random

def main():
    # Nhập số dòng và số cột
    M = int(input("Nhập số dòng (M): "))
    N = int(input("Nhập số cột (N): "))

    # -----------------------------------------
    # 1. Khởi tạo và nhập ma trận MxN ngẫu nhiên
    matrix = [[random.randint(0, 100) for _ in range(N)] for _ in range(M)]

    print("\nMa trận ngẫu nhiên:")
    for row in matrix:
        print(row)

    # -----------------------------------------
    # 2. Xuất dòng bất kỳ
    d = int(input("\nNhập số dòng muốn xuất (0 đến {}): ".format(M - 1)))
    if 0 <= d < M:
        print("Dòng", d, ":", matrix[d])
    else:
        print("Dòng không hợp lệ!")

    # -----------------------------------------
    # 3. Xuất cột bất kỳ
    c = int(input("\nNhập số cột muốn xuất (0 đến {}): ".format(N - 1)))
    if 0 <= c < N:
        print("Cột", c, ": ", end="")
        for i in range(M):
            print(matrix[i][c], end=" ")
        print()
    else:
        print("Cột không hợp lệ!")

    # -----------------------------------------
    # 4. Xuất số MAX trong ma trận
    max_value = max(max(row) for row in matrix)
    print("\nGiá trị lớn nhất trong ma trận là:", max_value)


# Gọi hàm main
main()
