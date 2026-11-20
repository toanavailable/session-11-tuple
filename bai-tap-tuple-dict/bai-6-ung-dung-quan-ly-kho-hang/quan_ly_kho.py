"""Mini Inventory Management - List of Dictionary, thông tin giá / số lượng lưu bằng Tuple."""

# ========== KHỞI TẠO: mỗi sản phẩm là dict; "info" là tuple (giá_bán, số_lượng) ==========
inventory = [
    {"id": "P01", "name": "Laptop", "info": (15000000, 10)},
    {"id": "P02", "name": "Mouse", "info": (25000000, 50)},
]
line_width = 48

while True:
    print("\n=== HỆ THỐNG QUẢN LÝ KHO HÀNG ===")
    print("1. Xem danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật số lượng sản phẩm")
    print("4. Xóa sản phẩm")
    print("5. Thoát")
    choice = input("Chọn chức năng (1-5): ").strip()

    # ----- 1. Xem danh sách (Read) -----
    if choice == "1":
        print("--- DANH SÁCH SẢN PHẨM ---")
        if len(inventory) == 0:
            print("Kho hàng hiện đang trống.")
            continue
        print(f"{'Mã SP':<6}| {'Tên Sản Phẩm':<17}| {'Giá Bán':<10}| Số Lượng")
        print("-" * line_width)
        for product in inventory:
            price, quantity = product["info"]          # tuple unpacking
            print(f"{product['id']:<6}| {product['name']:<17}| {price:<10}| {quantity}")
        print("-" * line_width)

    # ----- 2. Thêm sản phẩm (Create) -----
    elif choice == "2":
        # Hỏi lại đến khi mã không rỗng và không trùng
        while True:
            new_id = input("Nhập mã sản phẩm mới: ").strip().upper()
            if new_id == "":
                print("Lỗi: Mã sản phẩm không được để trống!")
                continue
            is_duplicate = False
            for product in inventory:
                if product["id"] == new_id:
                    is_duplicate = True
                    break
            if is_duplicate:
                print(f"Lỗi: Mã sản phẩm {new_id} đã tồn tại!")
            else:
                break

        new_name = input("Nhập tên sản phẩm: ").strip()
        price_text = input("Nhập giá bán: ").strip()
        quantity_text = input("Nhập số lượng: ").strip()
        if new_name == "" or not price_text.isdigit() or not quantity_text.isdigit():
            print("Lỗi: Tên không được trống, giá và số lượng phải là số nguyên không âm!")
            continue
        inventory.append({"id": new_id, "name": new_name,
                          "info": (int(price_text), int(quantity_text))})
        print(f"Thành công: Đã thêm sản phẩm {new_id} vào kho!")

    # ----- 3. Cập nhật số lượng (Update) & 4. Xóa (Delete) -----
    elif choice == "3" or choice == "4":
        prompt = "Nhập mã sản phẩm cần cập nhật: " if choice == "3" else "Nhập mã sản phẩm cần xóa: "
        product_id = input(prompt).strip().upper()

        found_index = -1
        for index, product in enumerate(inventory):
            if product["id"] == product_id:
                found_index = index
                break
        if found_index == -1:
            print(f"Lỗi: Không tìm thấy sản phẩm {product_id}!")
            continue

        if choice == "3":
            quantity_text = input("Nhập số lượng mới: ").strip()
            if not quantity_text.isdigit():
                print("Lỗi: Số lượng phải là số nguyên không âm!")
                continue
            # Tuple bất biến -> tạo tuple mới (giá cũ, số lượng mới) rồi gán lại
            old_price = inventory[found_index]["info"][0]
            inventory[found_index]["info"] = (old_price, int(quantity_text))
            print(f"Thành công: Đã cập nhật số lượng cho sản phẩm {product_id}!")
        else:
            inventory.pop(found_index)
            print(f"Thành công: Đã xóa sản phẩm {product_id} khỏi hệ thống!")

    # ----- 5. Thoát -----
    elif choice == "5":
        print("Cảm ơn bạn đã sử dụng hệ thống. Hẹn gặp lại!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 5!")
