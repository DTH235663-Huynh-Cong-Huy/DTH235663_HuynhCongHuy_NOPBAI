import time
import os
import sys

# Hình 1 (bên trái)
hinh1 = (
"      *\n"
"      * *\n"
"      * * *\n"
"* * * * * * *\n"
"* * *\n"
"* *\n"
"*\n"
)

# Hình 2 (kế bên phải H1)
hinh2 = (
"      *\n"
"      * *\n"
"      *   *\n"
"* * * * * * *\n"
"*   *\n"
"* *\n"
"*\n"
)

# Hình 3 (kế bên phải H2)
hinh3 = (
"      * * * *\n"
"      * * *\n"
"      * *\n"
"      *\n"
"    * *\n"
"  * * *\n"
"* * * *\n"
)

# Hình 4 (bên phải cùng)
hinh4 = (
"      * * * *\n"
"      *   *\n"
"      * *\n"
"      *\n"
"    * *\n"
"  *   *\n"
"* * * *\n"
)

ds_hinh = [hinh1, hinh2, hinh3, hinh4]

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Hiển thị lần lượt, mỗi hình giữ 5 giây
for h in ds_hinh:
    clear()
    print(h)
    sys.stdout.flush()
    time.sleep(5)

# Kết thúc: xoá màn hình và báo xong
clear()
print("Đã hiển thị xong 4 hình (mỗi hình 5 giây).")
