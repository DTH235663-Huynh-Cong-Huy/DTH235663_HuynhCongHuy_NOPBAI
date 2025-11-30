def nhap_ma_tran(m, n, ten="Ma trận"):
    """Hàm nhập ma trận m x n từ bàn phím"""
    matrix = []
    print(f"Nhập các phần tử cho {ten}:")
    for i in range(m):
        row = []
        for j in range(n):
            x = float(input(f"{ten}[{i}][{j}]: "))
            row.append(x)
        matrix.append(row)
    return matrix

def xuat_ma_tran(matrix, ten="Ma trận"):
    """Hàm xuất ma trận ra màn hình"""
    print(f"{ten}:")
    for row in matrix:
        print(row)

def cong_ma_tran(A, B):
    """Hàm cộng 2 ma trận cùng kích thước"""
    m = len(A)
    n = len(A[0])
    C = []
    for i in range(m):
        row = [A[i][j] + B[i][j] for j in range(n)]
        C.append(row)
    return C

def hoan_vi(matrix):
    """Hàm tính ma trận hoán vị (transpose)"""
    m = len(matrix)
    n = len(matrix[0])
    return [[matrix[i][j] for i in range(m)] for j in range(n)]

# -----------------------------
# Chương trình chính
def main():
    m = int(input("Nhập số dòng của ma trận: "))
    n = int(input("Nhập số cột của ma trận: "))

    A = nhap_ma_tran(m, n, "Ma trận A")
    B = nhap_ma_tran(m, n, "Ma trận B")

    xuat_ma_tran(A, "Ma trận A")
    xuat_ma_tran(B, "Ma trận B")

    # Cộng 2 ma trận
    C = cong_ma_tran(A, B)
    xuat_ma_tran(C, "Ma trận A + B")

    # Ma trận hoán vị
    AT = hoan_vi(A)
    BT = hoan_vi(B)
    xuat_ma_tran(AT, "Ma trận A hoán vị")
    xuat_ma_tran(BT, "Ma trận B hoán vị")

# Gọi hàm main
main()
