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
