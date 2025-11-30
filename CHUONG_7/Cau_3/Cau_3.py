from xml.dom.minidom import parse

def main():
    # Đọc file XML
    dom_tree = parse("Cau_3\employees.xml")
    
    # Lấy phần tử gốc <employees>
    employees = dom_tree.documentElement
    
    # Lấy danh sách tất cả <employee>
    employee_list = employees.getElementsByTagName("employee")
    
    print("Danh sách nhân viên:")
    for emp in employee_list:
        # Lấy id
        emp_id = emp.getElementsByTagName("id")[0].firstChild.data
        # Lấy tên
        emp_name = emp.getElementsByTagName("name")[0].firstChild.data
        
        print(f"ID: {emp_id}, Name: {emp_name}")

# Gọi hàm main
if __name__ == "__main__":
    main()
