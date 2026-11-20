"""Hệ thống quản lý sản phẩm Yody - mỗi sản phẩm là một dictionary."""

# ========== KHỞI TẠO ==========
product_list = [
    {"product_id": "SP001", "product_name": "Áo polo nam", "price": 299000, "quantity": 20},
    {"product_id": "SP002", "product_name": "Quần kaki nam", "price": 399000, "quantity": 15},
    {"product_id": "SP003", "product_name": "Váy công sở nữ", "price": 459000, "quantity": 10},
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật thông tin sản phẩm")
    print("4. Xóa sản phẩm theo mã")
    print("5. Thoát chương trình")
    choice = input("Nhập lựa chọn (1-5): ").strip()

    # ----- Chức năng 1: Hiển thị -----
    if choice == "1":
        if len(product_list) == 0:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            print("Danh sách sản phẩm hiện tại:")
            for stt, product in enumerate(product_list, start=1):
                print(f"{stt}. Mã SP: {product['product_id']} | Tên: {product['product_name']} | "
                      f"Giá: {product['price']} | Số lượng: {product['quantity']}")

    # ----- Chức năng 2, 3, 4: bắt đầu bằng nhập mã sản phẩm -----
    elif choice == "2" or choice == "3" or choice == "4":
        if choice == "2":
            prompt = "Nhập mã sản phẩm: "
        elif choice == "3":
            prompt = "Nhập mã sản phẩm cần cập nhật: "
        else:
            prompt = "Nhập mã sản phẩm cần xóa: "
        product_id = input(prompt).strip().upper()          # Bẫy 1: chuẩn hóa mã

        # Tìm sản phẩm theo mã (-1 nếu không có)
        found_index = -1
        for index, product in enumerate(product_list):
            if product["product_id"] == product_id:
                found_index = index
                break

        # ---------- Thêm mới ----------
        if choice == "2":
            if product_id == "":
                print("Mã sản phẩm không được để trống!")
                continue
            if found_index != -1:
                print("Mã sản phẩm bị trùng")                 # Bẫy 2
                continue
            product_name = input("Nhập tên sản phẩm: ").strip()
            price_text = input("Nhập giá sản phẩm: ").strip()
            quantity_text = input("Nhập số lượng sản phẩm: ").strip()
            if product_name == "":
                print("Tên sản phẩm không được để trống!")
                continue
            # Bẫy 4: giá và số lượng phải là số nguyên dương
            if not price_text.isdigit() or not quantity_text.isdigit() \
                    or int(price_text) == 0 or int(quantity_text) == 0:
                print("Giá/Số lượng không hợp lệ")
                continue
            product_list.append({
                "product_id": product_id,
                "product_name": product_name,
                "price": int(price_text),
                "quantity": int(quantity_text),
            })
            print("Thêm sản phẩm thành công")

        # ---------- Cập nhật ----------
        elif choice == "3":
            if found_index == -1:
                print("Không tìm thấy mã sản phẩm cần cập nhật!")      # Bẫy 3
                continue
            product = product_list[found_index]
            print(f"Thông tin hiện tại: {product['product_name']} | Giá: {product['price']} | "
                  f"Số lượng: {product['quantity']}")
            product_name = input("Nhập tên sản phẩm mới: ").strip()
            price_text = input("Nhập giá sản phẩm mới: ").strip()
            quantity_text = input("Nhập số lượng tồn kho mới: ").strip()
            if product_name == "":
                print("Tên sản phẩm không được để trống!")
                continue
            if not price_text.isdigit() or not quantity_text.isdigit() \
                    or int(price_text) == 0 or int(quantity_text) == 0:
                print("Giá/Số lượng không hợp lệ")                       # Bẫy 4
                continue
            product["product_name"] = product_name
            product["price"] = int(price_text)
            product["quantity"] = int(quantity_text)
            print(f"Cập nhật sản phẩm {product_id} thành công")

        # ---------- Xóa ----------
        else:
            if found_index == -1:
                print("Không tìm thấy mã sản phẩm cần xoá!")             # Bẫy 3
                continue
            removed_product = product_list.pop(found_index)
            print(f"Đã xóa sản phẩm {removed_product['product_id']} - {removed_product['product_name']}")

    # ----- Chức năng 5: Thoát -----
    elif choice == "5":
        print("Thoát chương trình.")
        break

    # ----- Bẫy 5: sai lựa chọn menu -----
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
