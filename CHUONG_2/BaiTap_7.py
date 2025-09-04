'''Một số cách nhập dữ liệu từ bàn phím trong Python
🔹 1. Hàm input() – Nhập chuỗi

Mặc định dữ liệu nhập từ bàn phím sẽ có kiểu string (chuỗi).

📌 Ví dụ:

name = input("Nhập tên của bạn: ")
print("Xin chào,", name)

🔹 2. Ép kiểu dữ liệu khi nhập

Nếu muốn nhập số nguyên (int) hoặc số thực (float), ta cần ép kiểu.

📌 Ví dụ:

age = int(input("Nhập tuổi của bạn: "))      # ép sang int
height = float(input("Nhập chiều cao (m): "))  # ép sang float

print("Tuổi:", age)
print("Chiều cao:", height)

🔹 3. Nhập nhiều giá trị trên một dòng

Dùng split() để tách chuỗi thành danh sách, sau đó ép kiểu nếu cần.

📌 Ví dụ:

a, b = input("Nhập 2 số, cách nhau bằng dấu cách: ").split()
print("a =", a, ", b =", b)


👉 Nếu muốn 2 số nguyên:

a, b = map(int, input("Nhập 2 số nguyên: ").split())
print("Tổng =", a + b)

🔹 4. Nhập nhiều giá trị và lưu vào danh sách

Dùng list() + map() để ép kiểu và lưu vào list.

📌 Ví dụ:

numbers = list(map(int, input("Nhập các số nguyên: ").split()))
print("Danh sách số vừa nhập:", numbers)

🔹 5. Nhập nhiều dòng (dùng vòng lặp)

📌 Ví dụ:

print("Nhập các ghi chú (gõ 'exit' để thoát):")
notes = []
while True:
    line = input()
    if line.lower() == "exit":
        break
    notes.append(line)

print("Danh sách ghi chú:", notes)

✅ Tóm lại

input() → nhập chuỗi.

int(input()), float(input()) → nhập số.

split() + map() → nhập nhiều giá trị 1 dòng.

Vòng lặp while → nhập nhiều dòng'''