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
