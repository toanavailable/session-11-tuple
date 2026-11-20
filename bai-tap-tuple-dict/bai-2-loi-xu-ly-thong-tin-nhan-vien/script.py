# Thông tin nhân viên ban đầu
employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}

# Lấy mã nhân viên: dictionary truy cập bằng KEY, không bằng index
employee_id = employee["employee_id"]

# Lấy họ tên nhân viên: key đúng là "full_name"
full_name = employee["full_name"]

# Cập nhật trạng thái: gán lại cho key ĐÃ CÓ "status"
employee["status"] = "official"

# Thêm lương cơ bản: gán cho một key MỚI (dict không có append())
employee["base_salary"] = 15000000

# Xóa phòng ban: key đúng là "department"
del employee["department"]

print("Mã nhân viên:", employee_id)
print("Họ tên nhân viên:", full_name)
print("Thông tin nhân viên sau xử lý:", employee)
