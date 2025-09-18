print("Kiểm tra Năm Nhuần")
year = int(input("Nhập năm cần kiểm tra: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"Năm {year} là năm nhuần")
else:
    print(f"Năm {year} không phải là năm nhuần")