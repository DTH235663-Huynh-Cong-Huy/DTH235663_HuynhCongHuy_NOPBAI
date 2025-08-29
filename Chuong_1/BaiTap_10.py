# Cây thông theo mẫu trong sách

# tầng 1
for i in range(1, 6, 2):
    print(" " * (5 - i//2 - 1) + "*" * i)

# tầng 2
for i in range(3, 8, 2):
    print(" " * (5 - i//2 - 1) + "*" * i)

# thân cây
for i in range(2):
    print(" " * 3 + "* *")
