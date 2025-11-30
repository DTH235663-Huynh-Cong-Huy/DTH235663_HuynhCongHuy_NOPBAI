def main():
    n = int(input("Nhập số lượng phần tử của dãy: "))
    lst = []

    print("Nhập các số theo thứ tự tăng dần:")

    for i in range(n):
        while True:
            x = int(input(f"Nhập phần tử thứ {i+1}: "))
            
            # Nếu là phần tử đầu tiên hoặc lớn hơn phần tử trước
            if i == 0 or x > lst[i-1]:
                lst.append(x)
                break
            else:
                print("Sai quy tắc! Phải lớn hơn phần tử trước. Nhập lại.")

    print("\nDãy số sau khi nhập xong:", lst)


# Gọi hàm main
main()
