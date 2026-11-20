# Bài 2 - [Vận dụng cơ bản] Lỗi xử lý thông tin nhân viên

## Đề bài

Hệ thống quản lý nhân sự cho hệ thống bán hàng **Yody**. Mỗi nhân viên được lưu bằng **dictionary** gồm các cặp `key - value`:

```python
employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}
```

Hệ thống cần: lấy mã nhân viên; lấy họ tên; cập nhật trạng thái từ `"probation"` thành `"official"`; thêm thông tin lương cơ bản; xóa thông tin phòng ban khi nhân viên được chuyển sang hệ thống phân quyền nội bộ.

**Kết quả đúng cần hiển thị:**

```
Mã nhân viên: NV001
Họ tên nhân viên: Nguyễn Văn An
Thông tin nhân viên sau xử lý: {'employee_id': 'NV001', 'full_name': 'Nguyễn Văn An', 'status': 'official', 'base_salary': 15000000}
```

## Mã nguồn hiện tại (legacy)

File: [`script_legacy.py`](script_legacy.py)

```python
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
```

Kết quả khi chạy:

```
Traceback (most recent call last):
  File "script_legacy.py", line 10, in <module>
    employee_id = employee[0]
                  ~~~~~~~~^^^
KeyError: 0
```

## (1) Phân tích lỗi

**Dictionary `employee` gồm những key nào?** `"employee_id"`, `"full_name"`, `"department"`, `"status"`.

**Vì sao `employee_id = employee[0]` gây lỗi?** Python hiểu `0` là **một key** và đi tìm key có giá trị số `0`. Dict này không có key `0`, nên báo `KeyError: 0`. Đây là dòng làm chương trình dừng.

**Dictionary có truy cập phần tử bằng index giống list không?** **Không.** Dict truy cập value **bằng key**, không có khái niệm vị trí 0, 1, 2 như list.

**Muốn lấy mã nhân viên `"NV001"`, cần viết lệnh như thế nào?** `employee_id = employee["employee_id"]`

**Vì sao `full_name = employee["name"]` gây lỗi?** Dict không có key `"name"`, nên báo `KeyError: 'name'`.

**Key đúng để lấy họ tên nhân viên là gì?** `"full_name"`.

**Vì sao `employee["employee_status"] = "official"` chưa cập nhật đúng trạng thái?** Phép gán `d[key] = value` với key **chưa tồn tại** sẽ **thêm key mới**. Kết quả là dict có thêm key thừa `"employee_status"`, còn key `"status"` vẫn là `"probation"`. Python không báo lỗi nên đây là lỗi logic.

**Muốn cập nhật trạng thái nhân viên, cần dùng key nào?** Key đã có sẵn **`"status"`**: `employee["status"] = "official"`.

**Vì sao `employee.append("base_salary", 15000000)` gây lỗi?** `append()` là phương thức của **list**. Dict không có `append`, nên báo `AttributeError: 'dict' object has no attribute 'append'`.

**Dictionary có phương thức `append()` không?** **Không.**

**Muốn thêm lương cơ bản `base_salary` bằng 15000000, cần viết lệnh như thế nào?** Gán cho key mới: `employee["base_salary"] = 15000000` (hoặc `employee.update({"base_salary": 15000000})`).

**Vì sao `del employee["team"]` gây lỗi?** Không có key `"team"`, nên `del` báo `KeyError: 'team'`.

**Muốn xóa thông tin phòng ban, cần dùng key nào?** `"department"`: `del employee["department"]` (hoặc `employee.pop("department")`).

## (2) Sửa lỗi

File: [`script.py`](script.py)

```python
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
```

## Kết quả

```
Mã nhân viên: NV001
Họ tên nhân viên: Nguyễn Văn An
Thông tin nhân viên sau xử lý: {'employee_id': 'NV001', 'full_name': 'Nguyễn Văn An', 'status': 'official', 'base_salary': 15000000}
```
