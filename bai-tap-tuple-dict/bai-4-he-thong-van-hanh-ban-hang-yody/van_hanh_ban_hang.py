"""Hệ thống vận hành bán hàng Yody - list of dict, có số lượng đã bán."""

# ========== KHỞI TẠO ==========
product_list = [
    {"product_id": "SP001", "product_name": "Áo polo nam", "price": 299000, "quantity": 20, "sold": 5},
    {"product_id": "SP002", "product_name": "Quần kaki nam", "price": 399000, "quantity": 8, "sold": 3},
    {"product_id": "SP003", "product_name": "Váy công sở nữ", "price": 459000, "quantity": 3, "sold": 7},
]
low_stock_limit = 5

while True:
    print("\n===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Nhập thêm hàng vào kho")
    print("4. Xem báo cáo doanh thu")
    print("5. Thoát chương trình")
    choice = input("Nhập lựa chọn (1-5): ").strip()

    # ----- Chức năng 1: Danh sách + trạng thái tồn kho -----
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
                  f"Đã bán: {product['sold']} | Trạng thái: {stock_status}")

    # ----- Chức năng 2, 3: bán / nhập kho -----
    elif choice == "2" or choice == "3":
        if choice == "2":
            product_id = input("Nhập mã sản phẩm khách muốn mua: ").strip().upper()   # Bẫy 1
            quantity_text = input("Nhập số lượng khách mua: ").strip()
        else:
            product_id = input("Nhập mã sản phẩm cần nhập thêm: ").strip().upper()
            quantity_text = input("Nhập số lượng nhập thêm: ").strip()

        found_product = None
        for product in product_list:
            if product["product_id"] == product_id:
                found_product = product
                break

        if found_product is None:
            print("Không tìm thấy sản phẩm cần bán/Nhập kho")                      # Bẫy 2
            continue
        # Bẫy 3: số lượng phải là số nguyên dương (isdigit chặn chữ, số âm)
        if not quantity_text.isdigit() or int(quantity_text) == 0:
            print("Số lượng mua/Nhập kho không hợp lệ")
            continue
        quantity = int(quantity_text)

        if choice == "2":
            if quantity > found_product["quantity"]:
                print("Số lượng trong kho không đủ để bán")                        # Bẫy 4
                continue
            found_product["quantity"] -= quantity
            found_product["sold"] += quantity
            total_payment = found_product["price"] * quantity
            print(f"Bán thành công {quantity} x {found_product['product_name']}. "
                  f"Khách cần thanh toán: {total_payment} VND")
        else:
            found_product["quantity"] += quantity
            print(f"Nhập kho thành công. Tồn kho mới của {found_product['product_name']}: "
                  f"{found_product['quantity']}")

    # ----- Chức năng 4: Báo cáo doanh thu -----
    elif choice == "4":
        total_revenue = 0
        best_seller = None
        for product in product_list:
            total_revenue += product["price"] * product["sold"]
            if best_seller is None or product["sold"] > best_seller["sold"]:
                best_seller = product

        if total_revenue == 0:
            print("Chưa có doanh thu phát sinh.")
            continue

        print("===== BÁO CÁO DOANH THU CỬA HÀNG YODY =====")
        for stt, product in enumerate(product_list, start=1):
            revenue = product["price"] * product["sold"]
            print(f"{stt}. {product['product_name']} | Đã bán: {product['sold']} | Doanh thu: {revenue}")
        print(f"\nTổng doanh thu: {total_revenue}")
        print(f"Sản phẩm bán chạy nhất: {best_seller['product_name']}")

    # ----- Chức năng 5: Thoát -----
    elif choice == "5":
        print("Thoát chương trình.")
        break

    # ----- Bẫy 5 -----
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
