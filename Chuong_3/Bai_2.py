print("Chương Trình Điếm Số Ngày Trong Tháng")
month = int(input("Nhập tháng (1-12): "))
if month in [1, 3, 5, 7, 8, 10, 12]:
    print(f"Tháng {month} có 31 ngày")  
elif month in [4, 6, 9, 11]:
    print(f"Tháng {month} có 30 ngày")
elif month == 2:
    year = int(input("Nhập năm để kiểm tra năm nhuần: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"Tháng {month} của năm {year} có 29 ngày")
    else:
        print(f"Tháng {month} của năm {year} có 28 ngày")
else:
    print("Tháng không hợp lệ. Vui lòng nhập tháng từ 1 đến 12.")