'''Các toán tử trong Python
🔹 1. Toán tử / → Chia thực

Dùng để chia hai số và luôn trả về số thực (float), kể cả khi chia hết.

📌 Ví dụ:

print(7 / 2)   # 3.5
print(8 / 4)   # 2.0

🔹 2. Toán tử // → Chia lấy phần nguyên (Floor division)

Trả về phần nguyên của phép chia.

Nếu là số âm thì sẽ làm tròn xuống (floor).

📌 Ví dụ:

print(7 // 2)    # 3
print(-7 // 2)   # -4  (làm tròn xuống, không phải -3)

🔹 3. Toán tử % → Lấy phần dư (Modulo)

Trả về số dư của phép chia.

📌 Ví dụ:

print(7 % 2)   # 1
print(8 % 3)   # 2
print(-7 % 3)  # 2  (vì -7 = -3*3 + 2)

🔹 4. Toán tử ** → Lũy thừa (Exponentiation)

Dùng để tính số mũ (power).

📌 Ví dụ:

print(2 ** 3)   # 8  (2 mũ 3)
print(5 ** 2)   # 25
print(9 ** 0.5) # 3.0 (căn bậc hai)

🔹 5. Toán tử and → Logic AND

Trả về True nếu cả hai vế đều đúng.

Nếu không, trả về False.

📌 Ví dụ:

print(True and True)   # True
print(True and False)  # False
print(5 > 3 and 10 > 2)  # True

🔹 6. Toán tử or → Logic OR

Trả về True nếu ít nhất một trong hai vế đúng.

📌 Ví dụ:

print(True or False)   # True
print(False or False)  # False
print(5 > 10 or 3 < 8)  # True

🔹 7. Toán tử is → So sánh danh tính đối tượng

Dùng để kiểm tra hai biến có trỏ đến cùng một đối tượng trong bộ nhớ hay không.

Khác với == (so sánh giá trị).

📌 Ví dụ:

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True  (giá trị giống nhau)
print(a is b)   # False (khác đối tượng trong bộ nhớ)
print(a is c)   # True  (cùng một đối tượng)

✅ Tóm tắt

/ → chia thực.

// → chia lấy phần nguyên (floor).

% → lấy phần dư.

** → lũy thừa.

and → logic AND (đúng khi cả hai đều đúng).

or → logic OR (đúng khi ít nhất một đúng).

is → so sánh danh tính đối tượng (có phải cùng đối tượng không).'''