"""Hệ thống quản lý giao dịch bán hàng Yody - bán, đổi trả, giảm giá, nhập kho."""

# ========== KHỞI TẠO ==========
product_list = [
    {"product_id": "SP001", "product_name": "Áo polo nam", "price": 299000,
     "quantity": 20, "sold": 5, "returned": 1, "discount": 0},
    {"product_id": "SP002", "product_name": "Quần kaki nam", "price": 399000,
     "quantity": 8, "sold": 3, "returned": 0, "discount": 10},
    {"product_id": "SP003", "product_name": "Váy công sở nữ", "price": 459000,
     "quantity": 3, "sold": 7, "returned": 1, "discount": 15},
]
low_stock_limit = 5
max_discount = 70

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ GIAO DỊCH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Xử lý đổi trả sản phẩm")
    print("4. Áp dụng giảm giá cho sản phẩm")
    print("5. Nhập thêm hàng vào kho cửa hàng")
    print("6. Thoát chương trình")
    choice = input("Nhập lựa chọn (1-6): ").strip()

    # =================================================================
    # Chức năng 1: Hiển thị danh sách
    # =================================================================
    if choice == "1":
        if len(product_list) == 0:
            print("Danh sách sản phẩm hiện đang trống.")
            continue
        print("Danh sách sản phẩm hiện tại:")
        for stt, product in enumerate(product_list, start=1):
            if product["quantity"] == 0:
                stock_status = "Hết hàng"
            elif product["quantity"] <= low_stock_limit:
                stock_status = "Sắp hết hàng"
            else:
                stock_status = "Còn hàng"
            print(f"{stt}. Mã SP: {product['product_id']} | Tên: {product['product_name']} | "
                  f"Giá: {product['price']} | Tồn kho: {product['quantity']} | "
                  f"Đã bán: {product['sold']} | Đổi trả: {product['returned']} | "
                  f"Giảm giá: {product['discount']}% | Trạng thái: {stock_status}")

    # =================================================================
    # Chức năng 2 - 5: đều nhập mã sản phẩm + một con số
    # =================================================================
    elif choice in ["2", "3", "4", "5"]:
        if choice == "2":
            product_id = input("Nhập mã sản phẩm khách muốn mua: ")
            number_text = input("Nhập số lượng khách mua: ")
            not_found_message = "Không tìm thấy sản phẩm cần bán"
        elif choice == "3":
            product_id = input("Nhập mã sản phẩm khách muốn đổi/trả: ")
            number_text = input("Nhập số lượng đổi/trả: ")
            not_found_message = "Không tìm thấy sản phẩm cần đổi trả"
        elif choice == "4":
            product_id = input("Nhập mã sản phẩm cần áp dụng giảm giá: ")
            number_text = input("Nhập phần trăm giảm giá: ")
            not_found_message = "Không tìm thấy sản phẩm cần áp dụng giảm giá"
        else:
            product_id = input("Nhập mã sản phẩm cần nhập thêm: ")
            number_text = input("Nhập số lượng nhập thêm: ")
            not_found_message = "Không tìm thấy sản phẩm cần nhập kho"

        product_id = product_id.strip().upper()          # Bẫy 1: chuẩn hóa mã
        number_text = number_text.strip()

        found_product = None
        for product in product_list:
            if product["product_id"] == product_id:
                found_product = product
                break
        if found_product is None:
            print(not_found_message)                      # Bẫy 2, Bẫy 4
            continue

        # ---------- Chức năng 4: giảm giá 0 - 70 ----------
        if choice == "4":
            if not number_text.isdigit() or int(number_text) > max_discount:
                print("Phần trăm giảm giá không hợp lệ")  # Bẫy 6
                continue
            found_product["discount"] = int(number_text)
            print(f"Đã áp dụng giảm giá {found_product['discount']}% cho {found_product['product_name']}")
            continue

        # ---------- Chức năng 2, 3, 5: số lượng nguyên dương ----------
        if not number_text.isdigit() or int(number_text) == 0:
            print("Số lượng không hợp lệ (phải là số nguyên dương)")
            continue
        quantity = int(number_text)
        # Giá sau giảm (VND là số nguyên -> dùng chia lấy phần nguyên)
        discounted_price = found_product["price"] * (100 - found_product["discount"]) // 100

        if choice == "2":
            if quantity > found_product["quantity"]:
                print("Số lượng trong kho không đủ để bán")          # Bẫy 3
                continue
            found_product["quantity"] -= quantity
            found_product["sold"] += quantity
            total_payment = discounted_price * quantity
            print(f"Giá sau giảm: {discounted_price:,} VND (giảm {found_product['discount']}%)")
            print(f"Tổng tiền khách cần thanh toán: {total_payment:,} VND")

        elif choice == "3":
            if quantity > found_product["sold"]:
                print("Số lượng đổi/trả không được vượt quá số lượng đã bán")   # Bẫy 5
                continue
            found_product["sold"] -= quantity
            found_product["quantity"] += quantity
            found_product["returned"] += quantity
            refund_amount = discounted_price * quantity
            print(f"Đổi trả thành công {quantity} x {found_product['product_name']}.")
            print(f"Số tiền hoàn lại: {refund_amount:,} VND")

        else:
            found_product["quantity"] += quantity
            print(f"Nhập kho thành công. Tồn kho mới của {found_product['product_name']}: "
                  f"{found_product['quantity']}")

    # =================================================================
    # Chức năng 6: Thoát
    # =================================================================
    elif choice == "6":
        print("Thoát chương trình.")
        break

    # Bẫy 7: sai lựa chọn menu
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
