#Câu 9: Nhập vào 1 tháng, xuất ra tháng đó thuộc quý mấy trong năm
print("Chương Trình Xác Định Quý Của Tháng")
month = int(input("Nhập tháng (1-12): "))
if month in [1, 2, 3]:
    print(f"Tháng {month} thuộc Quý 1")
elif month in [4, 5, 6]:
    print(f"Tháng {month} thuộc Quý 2")
elif month in [7, 8, 9]:
    print(f"Tháng {month} thuộc Quý 3")
elif month in [10, 11, 12]:
    print(f"Tháng {month} thuộc Quý 4")
else:
    print("Tháng không hợp lệ. Vui lòng nhập tháng từ 1 đến 12.")
