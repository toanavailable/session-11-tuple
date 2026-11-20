# Bài 4 - [Phân tích] Hệ thống vận hành bán hàng Yody

## Đề bài

Tại cửa hàng thời trang Yody, nhân viên cần chương trình hỗ trợ vận hành hằng ngày: quản lý danh sách sản phẩm, mỗi sản phẩm là **dictionary** gồm mã, tên, giá bán, số lượng tồn kho, số lượng đã bán:

```python
product_list = [
    {"product_id": "SP001", "product_name": "Áo polo nam", "price": 299000, "quantity": 20, "sold": 5},
    {"product_id": "SP002", "product_name": "Quần kaki nam", "price": 399000, "quantity": 8, "sold": 3},
    {"product_id": "SP003", "product_name": "Váy công sở nữ", "price": 459000, "quantity": 3, "sold": 7},
]
```

```
===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====
1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho
2. Bán sản phẩm cho khách hàng
3. Nhập thêm hàng vào kho
4. Xem báo cáo doanh thu
5. Thoát chương trình
```

- **Chức năng 1:** in `Mã SP | Tên | Giá | Tồn kho | Đã bán | Trạng thái`. Trạng thái: tồn kho bằng 0 → `Hết hàng`; nhỏ hơn hoặc bằng 5 → `Sắp hết hàng`; lớn hơn 5 → `Còn hàng`. Rỗng thì `Danh sách sản phẩm hiện đang trống.`
- **Chức năng 2 - Bán:** chuẩn hóa mã; kiểm tra tồn tại; số lượng mua là số nguyên dương và không vượt tồn kho; hợp lệ thì trừ tồn kho, tăng số đã bán, tính tiền khách thanh toán.
- **Chức năng 3 - Nhập kho:** chuẩn hóa mã; kiểm tra tồn tại; số lượng nhập là số nguyên dương; cộng vào tồn kho.
- **Chức năng 4 - Báo cáo doanh thu:** doanh thu từng sản phẩm = giá bán × số lượng đã bán; tổng doanh thu; sản phẩm bán chạy nhất. Chưa có sản phẩm nào bán được thì `Chưa có doanh thu phát sinh.`
- **Chức năng 5:** `Thoát chương trình.`

Báo cáo mẫu cần hiển thị:

```
===== BÁO CÁO DOANH THU CỬA HÀNG YODY =====
1. Áo polo nam | Đã bán: 5 | Doanh thu: 1495000
2. Quần kaki nam | Đã bán: 3 | Doanh thu: 1197000
3. Váy công sở nữ | Đã bán: 7 | Doanh thu: 3213000

Tổng doanh thu: 5905000
Sản phẩm bán chạy nhất: Váy công sở nữ
```

**Edge cases:** Bẫy 1 mã thừa khoảng trắng / viết thường; Bẫy 2 mã không tồn tại → `Không tìm thấy sản phẩm cần bán/Nhập kho`; Bẫy 3 số lượng là chữ, âm hoặc 0 → `Số lượng mua/Nhập kho không hợp lệ`; Bẫy 4 mua vượt tồn kho → `Số lượng trong kho không đủ để bán`; Bẫy 5 sai menu → `Lựa chọn không hợp lệ, vui lòng nhập lại!`

## (1) Phân tích và thiết kế giải pháp

### Phân tích Input / Output

| Dữ liệu | Biến | Kiểu | Xử lý |
|---|---|---|---|
| Danh sách sản phẩm | `product_list` | `list[dict]` | 5 key: product_id, product_name, price, quantity, sold |
| Mã sản phẩm | `product_id` | `str` | strip().upper() |
| Số lượng mua / nhập | `quantity_text → quantity` | `str → int` | isdigit() và khác 0 |
| Sản phẩm tìm thấy | `found_product` | `dict hoặc None` | Tham chiếu tới dict trong list, sửa trực tiếp |
| Tổng doanh thu | `total_revenue` | `int` | Cộng dồn price × sold |
| Sản phẩm bán chạy nhất | `best_seller` | `dict` | Thuật toán tìm Max theo key sold |

### Đề xuất giải pháp

- Tìm sản phẩm theo mã, lưu **chính dict đó** vào `found_product` (không copy). Sửa `found_product['quantity']` là sửa luôn phần tử trong list.
- Thứ tự kiểm tra khi bán: mã tồn tại (Bẫy 2) → số lượng hợp lệ (Bẫy 3) → không vượt tồn kho (Bẫy 4) → thực hiện.
- Trạng thái tồn kho dùng chuỗi `if / elif / else` xét `== 0` trước, rồi `<= 5`.
- Báo cáo: duyệt list một lần vừa cộng tổng doanh thu vừa tìm sản phẩm có `sold` lớn nhất. Nếu tổng doanh thu bằng 0 thì in `Chưa có doanh thu phát sinh.`
- Hai chức năng bán / nhập kho dùng chung phần tìm sản phẩm và kiểm tra số lượng, chỉ khác bước cập nhật cuối.

### Thiết kế thuật toán (Pseudocode)

```
LẶP MÃI:
    IN menu; NHẬP choice
    NẾU "1": với mỗi sản phẩm: trạng thái ← Hết hàng (=0) / Sắp hết hàng (≤5) / Còn hàng; IN 1 dòng
    NẾU "2" hoặc "3":
        NHẬP mã (strip().upper()), NHẬP số lượng
        không tìm thấy → "Không tìm thấy sản phẩm cần bán/Nhập kho"
        số lượng không phải số nguyên dương → "Số lượng mua/Nhập kho không hợp lệ"
        "2": số lượng > tồn kho → "Số lượng trong kho không đủ để bán"
             tồn kho −= SL; đã bán += SL; IN tiền thanh toán = giá × SL
        "3": tồn kho += SL
    NẾU "4": tổng ← Σ giá × đã bán; best ← sản phẩm có đã bán lớn nhất
        tổng == 0 → "Chưa có doanh thu phát sinh."; ngược lại IN báo cáo
    NẾU "5": "Thoát chương trình."; THOÁT
    NGƯỢC LẠI: "Lựa chọn không hợp lệ, vui lòng nhập lại!"
```

## (2) Triển khai code

File: [`van_hanh_ban_hang.py`](van_hanh_ban_hang.py)

```python
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
```

## Kết quả

Báo cáo doanh thu ban đầu khớp đề (tổng **5905000**), sau đó thử bán / nhập kho và các bẫy *(ẩn menu lặp lại cho gọn)*:

```
Nhập lựa chọn (1-5): 1
Danh sách sản phẩm hiện tại:
1. Mã SP: SP001 | Tên: Áo polo nam | Giá: 299000 | Tồn kho: 20 | Đã bán: 5 | Trạng thái: Còn hàng
2. Mã SP: SP002 | Tên: Quần kaki nam | Giá: 399000 | Tồn kho: 8 | Đã bán: 3 | Trạng thái: Còn hàng
3. Mã SP: SP003 | Tên: Váy công sở nữ | Giá: 459000 | Tồn kho: 3 | Đã bán: 7 | Trạng thái: Sắp hết hàng

Nhập lựa chọn (1-5): 4
===== BÁO CÁO DOANH THU CỬA HÀNG YODY =====
1. Áo polo nam | Đã bán: 5 | Doanh thu: 1495000
2. Quần kaki nam | Đã bán: 3 | Doanh thu: 1197000
3. Váy công sở nữ | Đã bán: 7 | Doanh thu: 3213000

Tổng doanh thu: 5905000
Sản phẩm bán chạy nhất: Váy công sở nữ

Nhập lựa chọn (1-5): 2
Nhập mã sản phẩm khách muốn mua:  sp003 
Nhập số lượng khách mua: 3
Bán thành công 3 x Váy công sở nữ. Khách cần thanh toán: 1377000 VND

Nhập lựa chọn (1-5): 1
Danh sách sản phẩm hiện tại:
1. Mã SP: SP001 | Tên: Áo polo nam | Giá: 299000 | Tồn kho: 20 | Đã bán: 5 | Trạng thái: Còn hàng
2. Mã SP: SP002 | Tên: Quần kaki nam | Giá: 399000 | Tồn kho: 8 | Đã bán: 3 | Trạng thái: Còn hàng
3. Mã SP: SP003 | Tên: Váy công sở nữ | Giá: 459000 | Tồn kho: 0 | Đã bán: 10 | Trạng thái: Hết hàng

Nhập lựa chọn (1-5): 2
Nhập mã sản phẩm khách muốn mua: SP002
Nhập số lượng khách mua: 10
Số lượng trong kho không đủ để bán

Nhập lựa chọn (1-5): 2
Nhập mã sản phẩm khách muốn mua: SP999
Nhập số lượng khách mua: 1
Không tìm thấy sản phẩm cần bán/Nhập kho

Nhập lựa chọn (1-5): 2
Nhập mã sản phẩm khách muốn mua: SP001
Nhập số lượng khách mua: abc
Số lượng mua/Nhập kho không hợp lệ

Nhập lựa chọn (1-5): 2
Nhập mã sản phẩm khách muốn mua: SP001
Nhập số lượng khách mua: -2
Số lượng mua/Nhập kho không hợp lệ

Nhập lựa chọn (1-5): 3
Nhập mã sản phẩm cần nhập thêm: sp003
Nhập số lượng nhập thêm: 5
Nhập kho thành công. Tồn kho mới của Váy công sở nữ: 5

Nhập lựa chọn (1-5): 3
Nhập mã sản phẩm cần nhập thêm: SP777
Nhập số lượng nhập thêm: 5
Không tìm thấy sản phẩm cần bán/Nhập kho

Nhập lựa chọn (1-5): 1
Danh sách sản phẩm hiện tại:
1. Mã SP: SP001 | Tên: Áo polo nam | Giá: 299000 | Tồn kho: 20 | Đã bán: 5 | Trạng thái: Còn hàng
2. Mã SP: SP002 | Tên: Quần kaki nam | Giá: 399000 | Tồn kho: 8 | Đã bán: 3 | Trạng thái: Còn hàng
3. Mã SP: SP003 | Tên: Váy công sở nữ | Giá: 459000 | Tồn kho: 5 | Đã bán: 10 | Trạng thái: Sắp hết hàng

Nhập lựa chọn (1-5): 4
===== BÁO CÁO DOANH THU CỬA HÀNG YODY =====
1. Áo polo nam | Đã bán: 5 | Doanh thu: 1495000
2. Quần kaki nam | Đã bán: 3 | Doanh thu: 1197000
3. Váy công sở nữ | Đã bán: 10 | Doanh thu: 4590000

Tổng doanh thu: 7282000
Sản phẩm bán chạy nhất: Váy công sở nữ

Nhập lựa chọn (1-5): x
Lựa chọn không hợp lệ, vui lòng nhập lại!

Nhập lựa chọn (1-5): 5
Thoát chương trình.
```

> Trường hợp `Chưa có doanh thu phát sinh.` chỉ xảy ra khi mọi sản phẩm đều có `sold = 0`. Dữ liệu mẫu đã có hàng bán ra nên không gặp, nhưng code đã xử lý.
