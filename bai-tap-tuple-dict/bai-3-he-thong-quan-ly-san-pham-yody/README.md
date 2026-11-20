# Bài 3 - [Vận dụng chuyên sâu] Hệ thống quản lý sản phẩm Yody

## Đề bài

Tại bộ phận bán hàng của cửa hàng thời trang Yody, nhân viên cần quản lý danh sách các sản phẩm đang được bày bán. Mỗi sản phẩm được lưu dưới dạng **dictionary** gồm: mã sản phẩm, tên sản phẩm, giá bán, số lượng tồn kho. Danh sách ban đầu:

```python
product_list = [
    {"product_id": "SP001", "product_name": "Áo polo nam", "price": 299000, "quantity": 20},
    {"product_id": "SP002", "product_name": "Quần kaki nam", "price": 399000, "quantity": 15},
    {"product_id": "SP003", "product_name": "Váy công sở nữ", "price": 459000, "quantity": 10},
]
```

```
===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật thông tin sản phẩm
4. Xóa sản phẩm theo mã
5. Thoát chương trình
```

- **Chức năng 1:** in danh sách dạng `1. Mã SP: SP001 | Tên: Áo polo nam | Giá: 299000 | Số lượng: 20`; rỗng thì `Danh sách sản phẩm hiện đang trống.`
- **Chức năng 2:** nhập mã, tên, giá, số lượng; xóa khoảng trắng hai đầu của mã, chuyển chữ hoa; kiểm tra mã có trùng không; giá và số lượng phải là số nguyên dương; hợp lệ thì thêm vào cuối danh sách và thông báo `Thêm sản phẩm thành công`.
- **Chức năng 3:** nhập mã cần cập nhật (chuẩn hóa); nếu có thì cho cập nhật tên, giá, số lượng tồn kho; nếu không: `Không tìm thấy mã sản phẩm cần cập nhật!`
- **Chức năng 4:** nhập mã cần xóa (chuẩn hóa); có thì xóa, không thì `Không tìm thấy mã sản phẩm cần xoá!`
- **Chức năng 5:** `Thoát chương trình.` rồi dừng.

**Edge cases:** Bẫy 1 mã thừa khoảng trắng / viết thường → chuẩn hóa; Bẫy 2 thêm mã trùng → `Mã sản phẩm bị trùng`; Bẫy 3 cập nhật / xóa mã không tồn tại; Bẫy 4 giá / số lượng là chữ, số âm hoặc 0 → `Giá/Số lượng không hợp lệ`; Bẫy 5 sai lựa chọn menu → `Lựa chọn không hợp lệ, vui lòng nhập lại!`

## (1) Phân tích và thiết kế giải pháp

### Phân tích Input / Output

| Dữ liệu | Biến | Kiểu | Xử lý |
|---|---|---|---|
| Danh sách sản phẩm | `product_list` | `list[dict]` | Mỗi dict có 4 key: product_id, product_name, price, quantity |
| Lựa chọn menu | `choice` | `str` | So sánh "1"…"5" |
| Mã sản phẩm | `product_id` | `str` | strip().upper() |
| Giá, số lượng | `price_text, quantity_text` | `str → int` | isdigit() và khác 0 |
| Vị trí tìm thấy | `found_index` | `int` | -1 nếu không có |

### Đề xuất giải pháp

- Dữ liệu là **list of dict**: duyệt list bằng `for`, truy cập thông tin bằng key `product['price']`.
- Chức năng 2, 3, 4 dùng chung bước tìm sản phẩm theo mã: duyệt `enumerate(product_list)`, so `product['product_id']` với mã đã chuẩn hóa, lưu `found_index`.
- Thêm: chỉ thêm khi `found_index == -1` (không trùng); tạo dict mới rồi `append()` vào list.
- Cập nhật: dict là kiểu có thể thay đổi, nên gán trực tiếp `product['price'] = ...` là danh sách được cập nhật ngay.
- Xóa: `pop(found_index)` để lấy lại thông tin sản phẩm vừa xóa và in ra.
- Kiểm tra số bằng `isdigit()` trước khi `int()`: chặn chữ, số âm, số thập phân, ô trống mà không crash; thêm điều kiện khác 0 để bảo đảm số nguyên dương.

### Thiết kế thuật toán (Pseudocode)

```
LẶP MÃI:
    IN menu; NHẬP choice
    NẾU "1": danh sách rỗng → "Danh sách sản phẩm hiện đang trống."; ngược lại in từng sản phẩm
    NẾU "2"/"3"/"4": NHẬP mã → strip().upper(); found_index ← vị trí trong list (−1 nếu không có)
        "2": mã trùng → "Mã sản phẩm bị trùng"
             NHẬP tên, giá, số lượng; giá/SL không phải số nguyên dương → "Giá/Số lượng không hợp lệ"
             append(dict mới); "Thêm sản phẩm thành công"
        "3": không có → "Không tìm thấy mã sản phẩm cần cập nhật!"
             NHẬP tên, giá, SL mới (kiểm tra như trên) → gán lại vào dict
        "4": không có → "Không tìm thấy mã sản phẩm cần xoá!"; có → pop(found_index)
    NẾU "5": "Thoát chương trình."; THOÁT
    NGƯỢC LẠI: "Lựa chọn không hợp lệ, vui lòng nhập lại!"
```

## (2) Triển khai code

File: [`quan_ly_san_pham.py`](quan_ly_san_pham.py)

```python
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
```

## Kết quả

Kiểm thử đủ chức năng và 5 bẫy *(ẩn menu lặp lại cho gọn)*:

```
Nhập lựa chọn (1-5): 1
Danh sách sản phẩm hiện tại:
1. Mã SP: SP001 | Tên: Áo polo nam | Giá: 299000 | Số lượng: 20
2. Mã SP: SP002 | Tên: Quần kaki nam | Giá: 399000 | Số lượng: 15
3. Mã SP: SP003 | Tên: Váy công sở nữ | Giá: 459000 | Số lượng: 10

Nhập lựa chọn (1-5): 2
Nhập mã sản phẩm:    sp004
Nhập tên sản phẩm: Áo sơ mi nữ
Nhập giá sản phẩm: 359000
Nhập số lượng sản phẩm: 12
Thêm sản phẩm thành công

Nhập lựa chọn (1-5): 2
Nhập mã sản phẩm: SP001
Mã sản phẩm bị trùng

Nhập lựa chọn (1-5): 2
Nhập mã sản phẩm: SP005
Nhập tên sản phẩm: Mũ
Nhập giá sản phẩm: 0
Nhập số lượng sản phẩm: 5
Giá/Số lượng không hợp lệ

Nhập lựa chọn (1-5): 2
Nhập mã sản phẩm: SP005
Nhập tên sản phẩm: Mũ
Nhập giá sản phẩm: abc
Nhập số lượng sản phẩm: 5
Giá/Số lượng không hợp lệ

Nhập lựa chọn (1-5): 3
Nhập mã sản phẩm cần cập nhật:  sp002 
Thông tin hiện tại: Quần kaki nam | Giá: 399000 | Số lượng: 15
Nhập tên sản phẩm mới: Quần kaki nam slim
Nhập giá sản phẩm mới: 419000
Nhập số lượng tồn kho mới: 14
Cập nhật sản phẩm SP002 thành công

Nhập lựa chọn (1-5): 3
Nhập mã sản phẩm cần cập nhật: SP999
Không tìm thấy mã sản phẩm cần cập nhật!

Nhập lựa chọn (1-5): 4
Nhập mã sản phẩm cần xóa: sp003
Đã xóa sản phẩm SP003 - Váy công sở nữ

Nhập lựa chọn (1-5): 4
Nhập mã sản phẩm cần xóa: SP999
Không tìm thấy mã sản phẩm cần xoá!

Nhập lựa chọn (1-5): 1
Danh sách sản phẩm hiện tại:
1. Mã SP: SP001 | Tên: Áo polo nam | Giá: 299000 | Số lượng: 20
2. Mã SP: SP002 | Tên: Quần kaki nam slim | Giá: 419000 | Số lượng: 14
3. Mã SP: SP004 | Tên: Áo sơ mi nữ | Giá: 359000 | Số lượng: 12

Nhập lựa chọn (1-5): 9
Lựa chọn không hợp lệ, vui lòng nhập lại!

Nhập lựa chọn (1-5): abc
Lựa chọn không hợp lệ, vui lòng nhập lại!

Nhập lựa chọn (1-5): 5
Thoát chương trình.
```
