# Bài 1 - [Vận dụng cơ bản] Lỗi xử lý thông tin sản phẩm tại hệ thống bán hàng Yody

## Đề bài

Hệ thống quản lý thông tin sản phẩm cho chuỗi cửa hàng thời trang **Yody**. Mỗi sản phẩm được lưu bằng **tuple** vì thông tin cơ bản của sản phẩm không nên bị thay đổi trực tiếp trong quá trình xử lý:

```python
product_info = ("SP001", "Áo polo nam", "Size L", 299000)
# ("Mã sản phẩm", "Tên sản phẩm", "Kích cỡ", "Giá bán")
```

Hệ thống cần: lấy mã sản phẩm; lấy tên sản phẩm; kiểm tra số lượng thông tin trong tuple; cập nhật giá bán từ `299000` thành `279000`; tạo tuple mới khi cập nhật vì tuple không cho phép sửa trực tiếp.

**Kết quả đúng cần hiển thị:**

```
Mã sản phẩm: SP001
Tên sản phẩm: Áo polo nam
Số lượng thông tin sản phẩm: 4
Thông tin sản phẩm sau cập nhật: ('SP001', 'Áo polo nam', 'Size L', 279000)
```

## Mã nguồn hiện tại (legacy)

File: [`script_legacy.py`](script_legacy.py)

```python
# Thông tin sản phẩm ban đầu
product_info = ("SP001", "Áo polo nam", "Size L", 299000)

# Lấy mã sản phẩm
product_code = product_info[1]

# Lấy tên sản phẩm
product_name = product_info[2]

# Đếm số lượng thông tin sản phẩm
product_length = product_info.length()

# Cập nhật giá bán
product_info[3] = 279000

print("Mã sản phẩm:", product_code)
print("Tên sản phẩm:", product_name)
print("Số lượng thông tin sản phẩm:", product_length)
print("Thông tin sản phẩm sau cập nhật:", product_info)
```

Kết quả khi chạy:

```
Traceback (most recent call last):
  File "script_legacy.py", line 11, in <module>
    product_length = product_info.length()
                     ^^^^^^^^^^^^^^^^^^^
AttributeError: 'tuple' object has no attribute 'length'
```

## (1) Phân tích lỗi

| Index | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Giá trị | `"SP001"` | `"Áo polo nam"` | `"Size L"` | `299000` |

**Tuple `product_info` ban đầu có bao nhiêu phần tử?** **4** phần tử.

**Phần tử `"SP001"` đang nằm ở index nào?** Index **0**.

**Vì sao `product_code = product_info[1]` lấy sai mã sản phẩm?** Index bắt đầu từ 0, nên index 1 là phần tử **thứ hai** (`"Áo polo nam"`), không phải mã sản phẩm. Phải dùng `product_info[0]`.

**Phần tử `"Áo polo nam"` đang nằm ở index nào?** Index **1**.

**Vì sao `product_name = product_info[2]` lấy sai tên sản phẩm?** Index 2 là `"Size L"` (kích cỡ). Tên sản phẩm ở index 1.

**Muốn đếm số phần tử trong tuple, cần dùng hàm nào?** Hàm có sẵn **`len(product_info)`**. Tuple (và list, chuỗi) không có phương thức `.length()`, nên `product_info.length()` báo `AttributeError: 'tuple' object has no attribute 'length'`. Đây là dòng làm chương trình dừng.

**Vì sao `product_info[3] = 279000` không hợp lệ?** Tuple là kiểu **bất biến (immutable)**: sau khi tạo thì không gán lại được từng phần tử. Dòng này báo `TypeError: 'tuple' object does not support item assignment`. Lỗi này chưa kịp hiện ra vì chương trình đã dừng ở `.length()` trước đó.

**Tuple có cho phép sửa trực tiếp phần tử không?** **Không.** Tuple không sửa, không thêm, không xóa phần tử được.

**Muốn cập nhật giá bán từ 299000 thành 279000, cần xử lý như thế nào?** **Tạo một tuple mới** rồi gán lại cho biến, ví dụ ghép 3 phần tử đầu (slicing) với tuple chứa giá mới:

```python
product_info = product_info[:3] + (279000,)   # (279000,) có dấu phẩy mới là tuple 1 phần tử
```

Cách khác: chuyển sang list, sửa, rồi chuyển lại tuple: `temp = list(product_info); temp[3] = 279000; product_info = tuple(temp)`.

## (2) Sửa lỗi

File: [`script.py`](script.py)

```python
# Thông tin sản phẩm ban đầu: (Mã, Tên, Kích cỡ, Giá bán) -> index 0, 1, 2, 3
product_info = ("SP001", "Áo polo nam", "Size L", 299000)

# Lấy mã sản phẩm: index 0
product_code = product_info[0]

# Lấy tên sản phẩm: index 1
product_name = product_info[1]

# Đếm số phần tử của tuple: dùng hàm len() (tuple không có phương thức length())
product_length = len(product_info)

# Tuple bất biến -> không sửa trực tiếp được; tạo TUPLE MỚI gồm 3 phần tử đầu + giá mới
product_info = product_info[:3] + (279000,)

print("Mã sản phẩm:", product_code)
print("Tên sản phẩm:", product_name)
print("Số lượng thông tin sản phẩm:", product_length)
print("Thông tin sản phẩm sau cập nhật:", product_info)
```

## Kết quả

```
Mã sản phẩm: SP001
Tên sản phẩm: Áo polo nam
Số lượng thông tin sản phẩm: 4
Thông tin sản phẩm sau cập nhật: ('SP001', 'Áo polo nam', 'Size L', 279000)
```
