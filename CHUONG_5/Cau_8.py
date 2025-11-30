# Hàm lấy tên file + phần mở rộng
def LayTenFile(dayduongdan):
    # Tách theo ký tự '\' hoặc '/'
    # Lấy phần cuối cùng chính là tên file
    ten_file = dayduongdan.replace("\\", "/").split("/")[-1]
    return ten_file


# Hàm lấy tên file không có đuôi mở rộng (mp3, mp4,...)
def LayTenKhongMoRong(dayduongdan):
    ten_file = LayTenFile(dayduongdan)   # gọi lại hàm 1
    # Tách theo dấu chấm và bỏ phần mở rộng
    ten_khong_duoi = ten_file.rsplit(".", 1)[0]
    return ten_khong_duoi


# ---------------------------
# Chương trình thử nghiệm
duongdan = "d:\\music\\muabui.mp3"

print("Tên file + mở rộng:", LayTenFile(duongdan))
print("Tên file không mở rộng:", LayTenKhongMoRong(duongdan))
