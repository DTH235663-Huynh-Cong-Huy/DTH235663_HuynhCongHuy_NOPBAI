# Hàm nhập chuỗi
def NhapChuoi():
    s = input("Nhập chuỗi bất kỳ: ")
    return s


# Hàm trích lọc số âm trong chuỗi
def NegativeNumberInStrings(s):
    result = []     # danh sách chứa các số âm tìm được
    i = 0

    while i < len(s):
        # Kiểm tra nếu gặp dấu "-" và sau đó là chữ số
        if s[i] == '-' and i + 1 < len(s) and s[i+1].isdigit():
            j = i + 1

            # Duyệt qua toàn bộ phần số phía sau
            while j < len(s) and s[j].isdigit():
                j += 1

            # Lấy số âm và đưa vào danh sách
            result.append(int(s[i:j]))

            # Nhảy đến vị trí sau số đã tách
            i = j
        else:
            i += 1

    return result


# Hàm chính để chạy chương trình
def main():
    chuoi = NhapChuoi()             # nhập chuỗi
    nums = NegativeNumberInStrings(chuoi)     # lấy số âm

    print("Các số nguyên âm trong chuỗi là:")
    for n in nums:
        print(n)


# Gọi hàm main
main()
