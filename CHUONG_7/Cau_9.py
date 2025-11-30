import os
import json

# --------------------------
# Hàm lưu dữ liệu vào file
def luu_file(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Hàm đọc dữ liệu từ file
def doc_file(filename):
    if not os.path.exists(filename):
        return {}  # Nếu file chưa tồn tại, trả về dict rỗng
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

# --------------------------
# Thêm danh mục mới
def them_danh_muc(data):
    ma_dm = input("Nhập mã danh mục: ")
    ten_dm = input("Nhập tên danh mục: ")
    if ma_dm in data:
        print("Danh mục đã tồn tại!")
    else:
        data[ma_dm] = {
            "ten": ten_dm,
            "san_pham": []
        }
        print("Thêm danh mục thành công.")

# Thêm sản phẩm cho danh mục
def them_san_pham(data):
    ma_dm = input("Nhập mã danh mục cần thêm sản phẩm: ")
    if ma_dm not in data:
        print("Danh mục không tồn tại!")
        return
    ma_sp = input("Nhập mã sản phẩm: ")
    ten_sp = input("Nhập tên sản phẩm: ")
    don_gia = float(input("Nhập đơn giá: "))
    # Kiểm tra trùng mã sản phẩm
    for sp in data[ma_dm]["san_pham"]:
        if sp["ma"] == ma_sp:
            print("Mã sản phẩm đã tồn tại!")
            return
    data[ma_dm]["san_pham"].append({
        "ma": ma_sp,
        "ten": ten_sp,
        "don_gia": don_gia
    })
    print("Thêm sản phẩm thành công.")

# Sửa sản phẩm
def sua_san_pham(data):
    ma_dm = input("Nhập mã danh mục: ")
    if ma_dm not in data:
        print("Danh mục không tồn tại!")
        return
    ma_sp = input("Nhập mã sản phẩm cần sửa: ")
    for sp in data[ma_dm]["san_pham"]:
        if sp["ma"] == ma_sp:
            sp["ten"] = input("Nhập tên sản phẩm mới: ")
            sp["don_gia"] = float(input("Nhập đơn giá mới: "))
            print("Sửa sản phẩm thành công.")
            return
    print("Sản phẩm không tồn tại!")

# Xóa sản phẩm
def xoa_san_pham(data):
    ma_dm = input("Nhập mã danh mục: ")
    if ma_dm not in data:
        print("Danh mục không tồn tại!")
        return
    ma_sp = input("Nhập mã sản phẩm cần xóa: ")
    for i, sp in enumerate(data[ma_dm]["san_pham"]):
        if sp["ma"] == ma_sp:
            del data[ma_dm]["san_pham"][i]
            print("Xóa sản phẩm thành công.")
            return
    print("Sản phẩm không tồn tại!")

# Tìm kiếm sản phẩm theo tên
def tim_kiem_san_pham(data):
    ten_sp = input("Nhập tên sản phẩm cần tìm: ")
    ket_qua = []
    for ma_dm, dm in data.items():
        for sp in dm["san_pham"]:
            if ten_sp.lower() in sp["ten"].lower():
                ket_qua.append((ma_dm, dm["ten"], sp))
    if ket_qua:
        print("Kết quả tìm kiếm:")
        for ma_dm, ten_dm, sp in ket_qua:
            print(f"Danh mục {ten_dm} ({ma_dm}): {sp['ten']} - Mã: {sp['ma']}, Giá: {sp['don_gia']}")
    else:
        print("Không tìm thấy sản phẩm.")

# Sắp xếp sản phẩm theo giá giảm dần
def sap_xep_san_pham(data):
    for dm in data.values():
        dm["san_pham"].sort(key=lambda sp: sp["don_gia"], reverse=True)
    print("Sắp xếp sản phẩm theo giá giảm dần thành công.")

# Hiển thị toàn bộ dữ liệu
def hien_thi(data):
    for ma_dm, dm in data.items():
        print(f"\nDanh mục: {dm['ten']} ({ma_dm})")
        for sp in dm["san_pham"]:
            print(f"  Mã: {sp['ma']}, Tên: {sp['ten']}, Giá: {sp['don_gia']}")

# --------------------------
# Chương trình chính
def main():
    filename = "products.txt"
    data = doc_file(filename)

    while True:
        print("\n===== QUẢN LÝ SẢN PHẨM =====")
        print("1. Thêm danh mục")
        print("2. Thêm sản phẩm")
        print("3. Sửa sản phẩm")
        print("4. Xóa sản phẩm")
        print("5. Tìm kiếm sản phẩm")
        print("6. Sắp xếp sản phẩm theo giá giảm dần")
        print("7. Hiển thị dữ liệu")
        print("8. Lưu dữ liệu và thoát")
        choice = input("Chọn chức năng (1-8): ")

        if choice == "1":
            them_danh_muc(data)
        elif choice == "2":
            them_san_pham(data)
        elif choice == "3":
            sua_san_pham(data)
        elif choice == "4":
            xoa_san_pham(data)
        elif choice == "5":
            tim_kiem_san_pham(data)
        elif choice == "6":
            sap_xep_san_pham(data)
        elif choice == "7":
            hien_thi(data)
        elif choice == "8":
            luu_file(filename, data)
            print("Đã lưu dữ liệu. Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")

# Gọi chương trình chính
if __name__ == "__main__":
    main()
