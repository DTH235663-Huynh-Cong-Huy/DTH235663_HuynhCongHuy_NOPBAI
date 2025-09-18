#Câu 6: Nhập một số n có tối đa 2 chữ số. Hãy cho biết cách đọc ra dạng chữ.
#(vd: n=35 => Ba mươi lăm, n=5 => năm). 

print("Chương Trình Đọc Số Có Tối Đa 2 Chữ Số")
num = int(input("Nhập một số có tối đa 2 chữ số (0-99): "))
if num < 0 or num > 99:
    print("Số không hợp lệ. Vui lòng nhập số từ 0 đến 99.")
else:
    units = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    tens = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", 
            "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    
    if num < 10:
        print(f"Số {num} đọc là: {units[num]}")
    elif num < 20:
        if num == 10:
            print("Số 10 đọc là: mười")
        else:
            print(f"Số {num} đọc là: mười {units[num % 10]}")
    else:
        ten_part = tens[num // 10]
        unit_part = units[num % 10]
        if num % 10 == 0:
            print(f"Số {num} đọc là: {ten_part}")
        else:
            print(f"Số {num} đọc là: {ten_part} {unit_part}")