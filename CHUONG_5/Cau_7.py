def ToiUuDanhTu(s):
    # Bước 1: Xóa khoảng trắng dư thừa đầu và cuối
    s = s.strip()
    
    # Bước 2: Tách các từ dựa trên khoảng trắng (tự loại bỏ khoảng trắng dư thừa)
    words = s.split()
    
    # Bước 3: Viết hoa chữ cái đầu mỗi từ
    # Hàm title() tự chuyển: "tÊn" → "Tên"
    words = [w.title() for w in words]
    
    # Bước 4: Ghép lại thành chuỗi tối ưu
    return " ".join(words)


# Chương trình chính
def main():
    s = input("Nhập chuỗi danh từ: ")
    print("Chuỗi tối ưu:", ToiUuDanhTu(s))


# Gọi hàm main
main()
