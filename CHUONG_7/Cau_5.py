import json

# Python Object
pythonObject = {
    "ten": "Trần Duy Thanh",
    "tuoi": 50,
    "ma": "nv1"
}

# Chuyển đổi Python Object sang JSON String
json_string = json.dumps(pythonObject, ensure_ascii=False)  # ensure_ascii=False để giữ ký tự Unicode

# Xuất kết quả
print("Chuỗi JSON:")
print(json_string)
