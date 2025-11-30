# Nhập chuỗi từ người dùng
s = input("Nhập chuỗi: ")

# Khởi tạo biến đếm
hoa = thuong = so = dac_biet = khoang_trang = nguyen_am = phu_am = 0

# Tập các nguyên âm (cả hoa và thường)
nguyen_am_set = "aeiouAEIOU"

for ch in s:
    if ch.isupper():
        hoa += 1
    elif ch.islower():
        thuong += 1
    elif ch.isdigit():
        so += 1
    elif ch.isspace():
        khoang_trang += 1
    else:
        dac_biet += 1

    # Kiểm tra nguyên âm & phụ âm (chỉ xét chữ cái)
    if ch.isalpha():
        if ch in nguyen_am_set:
            nguyen_am += 1
        else:
            phu_am += 1

# Xuất kết quả
print("Số chữ IN HOA:", hoa)
print("Số chữ in thường:", thuong)
print("Số chữ số:", so)
print("Số ký tự đặc biệt:", dac_biet)
print("Số khoảng trắng:", khoang_trang)
print("Số nguyên âm:", nguyen_am)
print("Số phụ âm:", phu_am)
