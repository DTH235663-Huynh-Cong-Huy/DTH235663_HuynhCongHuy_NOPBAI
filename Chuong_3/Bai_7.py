#Câu 7: Nhập vào một ngày (ngày, tháng, năm). Tìm ngày kế sau ngày
#vừa nhập (ngày/tháng/năm).

print("Chương Trình Tìm Ngày Kế Tiếp")
day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))
# Kiểm tra tính hợp lệ của ngày tháng năm
if month < 1 or month > 12 or day < 1 or day > 31:
    print("Ngày tháng không hợp lệ.")
else:
    # Xác định số ngày trong tháng
    if month in [1, 3, 5, 7, 8, 10, 12]:
        days_in_month = 31
    elif month in [4, 6, 9, 11]:
        days_in_month = 30
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_month = 29
        else:
            days_in_month = 28
    else:
        print("Tháng không hợp lệ.")
        days_in_month = 0
    # Tính ngày kế tiếp
    if days_in_month > 0:
        if day < days_in_month:
            next_day = day + 1
            next_month = month
            next_year = year
        else:
            next_day = 1
            if month == 12:
                next_month = 1
                next_year = year + 1
            else:
                next_month = month + 1
                next_year = year
        print(f"Ngày kế tiếp là: {next_day}/{next_month}/{next_year}")  