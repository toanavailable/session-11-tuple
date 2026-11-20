# Thông tin nhân viên ban đầu
employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}

# Lấy mã nhân viên
employee_id = employee[0]

# Lấy họ tên nhân viên
full_name = employee["name"]

# Cập nhật trạng thái nhân viên
employee["employee_status"] = "official"

# Thêm lương cơ bản
employee.append("base_salary", 15000000)

# Xóa phòng ban
del employee["team"]

print("Mã nhân viên:", employee_id)
print("Họ tên nhân viên:", full_name)
print("Thông tin nhân viên sau xử lý:", employee)
