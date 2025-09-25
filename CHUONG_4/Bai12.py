def oscillate(start, count):
    val = start
    for i in range(count):
        yield val        # xuất giá trị hiện tại
        yield -val       # xuất giá trị đối xứng qua 0
        val += 1

# --- Chạy kiểm tra ---
for n in oscillate(-3, 5):
    print(n, end=' ')
print()
