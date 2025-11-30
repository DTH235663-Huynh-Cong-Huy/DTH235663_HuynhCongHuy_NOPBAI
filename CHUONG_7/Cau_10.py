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
# Thêm lớp mới
def them_lop(data):
    ma_lop = input("Nhập mã lớp: ")
    ten_lop = input("Nhập tên lớp: ")
    if ma_lop in data:
        print("Lớp đã tồn tại!")
    else:
        data[ma_lop] = {
            "ten": ten_lop,
            "sinh_vien": []
        }
        print("Thêm lớp thành công.")

# Thêm sinh viên cho lớp
def them_sinh_vien(data):
    ma_lop = input("Nhập mã lớp cần thêm sinh viên: ")
    if ma_lop not in data:
        print("Lớp không tồn tại!")
        return
    ma_sv = input("Nhập mã sinh viên: ")
    ten_sv = input("Nhập tên sinh viên: ")
    nam_sinh = input("Nhập năm sinh: ")
    # Kiểm tra trùng mã sinh viên
    for sv in data[ma_lop]["sinh_vien"]:
        if sv["ma"] == ma_sv:
            print("Mã sinh viên đã tồn tại!")
            return
    data[ma_lop]["sinh_vien"].append({
        "ma": ma_sv,
        "ten": ten_sv,
        "nam_sinh": nam_sinh
    })
    print("Thêm sinh viên thành công.")

# Sửa thông tin sinh viên
def sua_sinh_vien(data):
    ma_lop = input("Nhập mã lớp: ")
    if ma_lop not in data:
        print("Lớp không tồn tại!")
        return
    ma_sv = input("Nhập mã sinh viên cần sửa: ")
    for sv in data[ma_lop]["sinh_vien"]:
        if sv["ma"] == ma_sv:
            sv["ten"] = input("Nhập tên mới: ")
            sv["nam_sinh"] = input("Nhập năm sinh mới: ")
            print("Sửa sinh viên thành công.")
            return
    print("Sinh viên không tồn tại!")

# Xóa sinh viên
def xoa_sinh_vien(data):
    ma_lop = input("Nhập mã lớp: ")
    if ma_lop not in data:
        print("Lớp không tồn tại!")
        return
    ma_sv = input("Nhập mã sinh viên cần xóa: ")
    for i, sv in enumerate(data[ma_lop]["sinh_vien"]):
        if sv["ma"] == ma_sv:
            del data[ma_lop]["sinh_vien"][i]
            print("Xóa sinh viên thành công.")
            return
    print("Sinh viên không tồn tại!")

# Tìm kiếm sinh viên theo tên
def tim_kiem_sinh_vien(data):
    ten_sv = input("Nhập tên sinh viên cần tìm: ")
    ket_qua = []
    for ma_lop, lop in data.items():
        for sv in lop["sinh_vien"]:
            if ten_sv.lower() in sv["ten"].lower():
                ket_qua.append((ma_lop, lop["ten"], sv))
    if ket_qua:
        print("Kết quả tìm kiếm:")
        for ma_lop, ten_lop, sv in ket_qua:
            print(f"Lớp {ten_lop} ({ma_lop}): {sv['ten']} - Mã: {sv['ma']}, Năm sinh: {sv['nam_sinh']}")
    else:
        print("Không tìm thấy sinh viên.")

# Sắp xếp sinh viên theo năm sinh tăng dần trong mỗi lớp
def sap_xep_sinh_vien(data):
    for lop in data.values():
        lop["sinh_vien"].sort(key=lambda sv: sv["nam_sinh"])
    print("Sắp xếp sinh viên theo năm sinh thành công.")

# Hiển thị toàn bộ dữ liệu
def hien_thi(data):
    for ma_lop, lop in data.items():
        print(f"\nLớp: {lop['ten']} ({ma_lop})")
        for sv in lop["sinh_vien"]:
            print(f"  Mã: {sv['ma']}, Tên: {sv['ten']}, Năm sinh: {sv['nam_sinh']}")

# --------------------------
# Chương trình chính
def main():
    filename = "students.json"
    data = doc_file(filename)

    while True:
        print("\n===== QUẢN LÝ SINH VIÊN =====")
        print("1. Thêm lớp")
        print("2. Thêm sinh viên")
        print("3. Sửa sinh viên")
        print("4. Xóa sinh viên")
        print("5. Tìm kiếm sinh viên")
        print("6. Sắp xếp sinh viên theo năm sinh")
        print("7. Hiển thị dữ liệu")
        print("8. Lưu dữ liệu và thoát")
        choice = input("Chọn chức năng (1-8): ")

        if choice == "1":
            them_lop(data)
        elif choice == "2":
            them_sinh_vien(data)
        elif choice == "3":
            sua_sinh_vien(data)
        elif choice == "4":
            xoa_sinh_vien(data)
        elif choice == "5":
            tim_kiem_sinh_vien(data)
        elif choice == "6":
            sap_xep_sinh_vien(data)
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
