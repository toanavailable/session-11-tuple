# Bài 6 - [Bài tập tổng hợp] Ứng dụng quản lý kho hàng (Mini Inventory Management)

## Đề bài

**Mục tiêu:** thành thạo thao tác **CRUD** phần tử với List và Dictionary; vận dụng linh hoạt **List**, **Dictionary** và **Tuple** để tổ chức dữ liệu chuẩn hóa; rèn luyện tư duy logic khi xây dựng menu tương tác console và xử lý luồng dữ liệu.

**Mô tả:** viết chương trình Python quản lý kho hàng, trong đó:
- Mỗi sản phẩm là một **dictionary**.
- Thông tin sản phẩm gồm: `id` (chuỗi), `name` (chuỗi) và `info` là một **tuple** chứa `(giá_bán, số_lượng)`.
- Danh sách kho hàng là một **list** chứa các dictionary sản phẩm.

```python
inventory = [
    {"id": "P01", "name": "Laptop", "info": (15000000, 10)},
    {"id": "P02", "name": "Mouse", "info": (25000000, 50)}
]
```

```
=== HỆ THỐNG QUẢN LÝ KHO HÀNG ===
1. Xem danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật số lượng sản phẩm
4. Xóa sản phẩm
5. Thoát
Chọn chức năng (1-5):
```

- **Xem danh sách:** hiển thị toàn bộ sản phẩm dạng bảng `Mã SP | Tên Sản Phẩm | Giá Bán | Số Lượng`.
- **Thêm sản phẩm mới:** nhập ID, tên, giá, số lượng. ID không được trùng với ID đã có (`Lỗi: Mã sản phẩm P01 đã tồn tại!` rồi hỏi lại mã). Thành công: `Thành công: Đã thêm sản phẩm P03 vào kho!`
- **Cập nhật số lượng:** nhập ID và số lượng mới để cập nhật lại tuple `info`. Thành công: `Thành công: Đã cập nhật số lượng cho sản phẩm P01!`
- **Xóa sản phẩm:** nhập ID để xóa khỏi kho. Thành công: `Thành công: Đã xóa sản phẩm P02 khỏi hệ thống!`
- **Thoát:** `Cảm ơn bạn đã sử dụng hệ thống. Hẹn gặp lại!`

## Phân tích

| Cấu trúc | Vai trò | Lý do chọn |
|---|---|---|
| **List** `inventory` | Chứa nhiều sản phẩm theo thứ tự | Thêm (`append`), xóa (`pop`), duyệt (`for`) |
| **Dict** sản phẩm | Mô tả 1 sản phẩm bằng các key `id`, `name`, `info` | Truy cập thuộc tính bằng tên, rõ ràng |
| **Tuple** `info` | Gom cặp `(giá_bán, số_lượng)` | Dữ liệu đi theo cặp, không bị sửa lẻ tẻ từng phần |

Điểm mấu chốt: **cập nhật số lượng**. Tuple bất biến nên **không** viết được `product["info"][1] = 15`. Phải **tạo tuple mới** giữ giá cũ và thay số lượng mới, rồi gán lại cho key `info` của dict (dict thì sửa được):

```python
old_price = inventory[found_index]["info"][0]
inventory[found_index]["info"] = (old_price, int(quantity_text))
```

Khi hiển thị, dùng **tuple unpacking** `price, quantity = product["info"]` để lấy 2 giá trị gọn gàng.

Các kiểm tra thêm để chương trình không crash: mã nhập vào được `strip().upper()`; mã rỗng hoặc trùng thì hỏi lại; giá, số lượng phải là số nguyên không âm (`isdigit()`); cập nhật / xóa mã không có thì báo `Lỗi: Không tìm thấy sản phẩm ...!`; sai menu thì báo lỗi và hiện lại menu.

## Lời giải

File: [`quan_ly_kho.py`](quan_ly_kho.py)

```python
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
```

## Kết quả

Chạy theo đúng kịch bản mẫu của đề, thêm các trường hợp lỗi *(ẩn menu lặp lại cho gọn)*:

```
Chọn chức năng (1-5): 1
--- DANH SÁCH SẢN PHẨM ---
Mã SP | Tên Sản Phẩm     | Giá Bán   | Số Lượng
------------------------------------------------
P01   | Laptop           | 15000000  | 10
P02   | Mouse            | 25000000  | 50
------------------------------------------------

Chọn chức năng (1-5): 2
Nhập mã sản phẩm mới: P01
Lỗi: Mã sản phẩm P01 đã tồn tại!
Nhập mã sản phẩm mới: P03
Nhập tên sản phẩm: Keyboard
Nhập giá bán: 350000
Nhập số lượng: 20
Thành công: Đã thêm sản phẩm P03 vào kho!

Chọn chức năng (1-5): 3
Nhập mã sản phẩm cần cập nhật: P01
Nhập số lượng mới: 15
Thành công: Đã cập nhật số lượng cho sản phẩm P01!

Chọn chức năng (1-5): 4
Nhập mã sản phẩm cần xóa: P02
Thành công: Đã xóa sản phẩm P02 khỏi hệ thống!

Chọn chức năng (1-5): 3
Nhập mã sản phẩm cần cập nhật: P99
Lỗi: Không tìm thấy sản phẩm P99!

Chọn chức năng (1-5): 2
Nhập mã sản phẩm mới: p04
Nhập tên sản phẩm: Màn hình
Nhập giá bán: abc
Nhập số lượng: 5
Lỗi: Tên không được trống, giá và số lượng phải là số nguyên không âm!

Chọn chức năng (1-5): 1
--- DANH SÁCH SẢN PHẨM ---
Mã SP | Tên Sản Phẩm     | Giá Bán   | Số Lượng
------------------------------------------------
P01   | Laptop           | 15000000  | 15
P03   | Keyboard         | 350000    | 20
------------------------------------------------

Chọn chức năng (1-5): 9
Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 5!

Chọn chức năng (1-5): 5
Cảm ơn bạn đã sử dụng hệ thống. Hẹn gặp lại!
```
