# Bài 5 - [Sáng tạo] Hệ thống quản lý giao dịch bán hàng Yody

## Đề bài

Tại cửa hàng thời trang Yody, nhân viên thu ngân cần quản lý sản phẩm trong ca làm việc và xử lý các nghiệp vụ tại quầy. Mỗi sản phẩm là **dictionary** gồm: mã, tên, giá bán, số lượng tồn kho, số lượng đã bán, số lượng đã đổi trả, phần trăm giảm giá hiện tại:

```python
product_list = [
    {"product_id": "SP001", "product_name": "Áo polo nam", "price": 299000,
     "quantity": 20, "sold": 5, "returned": 1, "discount": 0},
    {"product_id": "SP002", "product_name": "Quần kaki nam", "price": 399000,
     "quantity": 8, "sold": 3, "returned": 0, "discount": 10},
    {"product_id": "SP003", "product_name": "Váy công sở nữ", "price": 459000,
     "quantity": 3, "sold": 7, "returned": 1, "discount": 15},
]
```

```
===== HỆ THỐNG QUẢN LÝ GIAO DỊCH CỬA HÀNG YODY =====
1. Hiển thị danh sách sản phẩm
2. Bán sản phẩm cho khách hàng
3. Xử lý đổi trả sản phẩm
4. Áp dụng giảm giá cho sản phẩm
5. Nhập thêm hàng vào kho cửa hàng
6. Thoát chương trình
```

| Chức năng | Yêu cầu |
|---|---|
| 1 - Hiển thị | `Mã SP \| Tên \| Giá \| Tồn kho \| Đã bán \| Đổi trả \| Giảm giá: x% \| Trạng thái`; trạng thái: 0 → Hết hàng, ≤ 5 → Sắp hết hàng, > 5 → Còn hàng |
| 2 - Bán | Chuẩn hóa mã; kiểm tra tồn tại; số lượng nguyên dương, không vượt tồn kho; tính giá sau giảm; trừ tồn kho, tăng đã bán, hiển thị tổng tiền |
| 3 - Đổi trả | Chuẩn hóa mã; kiểm tra tồn tại; số lượng nguyên dương, không vượt số đã bán; giảm đã bán, tăng tồn kho, tăng đổi trả; tính tiền hoàn lại theo giá hiện tại sau giảm |
| 4 - Giảm giá | Chuẩn hóa mã; kiểm tra tồn tại; phần trăm là số nguyên **0 đến 70** (cửa hàng không cho nhân viên tự giảm quá cao khi chưa có phê duyệt); cập nhật phần trăm giảm giá |
| 5 - Nhập kho | Chuẩn hóa mã; kiểm tra tồn tại; số lượng nguyên dương; cộng vào tồn kho |
| 6 - Thoát | `Thoát chương trình.` |

**Công thức:**

```
Giá sau giảm = Giá bán * (100 - Phần trăm giảm giá) / 100
Tổng tiền   = Giá sau giảm * Số lượng mua
```

**Edge cases:** Bẫy 1 mã thừa khoảng trắng / viết thường; Bẫy 2 bán mã không tồn tại → `Không tìm thấy sản phẩm cần bán`; Bẫy 3 bán vượt tồn kho → `Số lượng trong kho không đủ để bán`; Bẫy 4 đổi trả mã không tồn tại → `Không tìm thấy sản phẩm cần đổi trả`; Bẫy 5 đổi trả vượt số đã bán → `Số lượng đổi/trả không được vượt quá số lượng đã bán`; Bẫy 6 phần trăm giảm giá là chữ, số âm... → `Phần trăm giảm giá không hợp lệ`; Bẫy 7 sai menu → `Lựa chọn không hợp lệ, vui lòng nhập lại!`

## (1) Phân tích và thiết kế giải pháp

### Phân tích Input / Output

| Dữ liệu | Biến | Kiểu | Xử lý |
|---|---|---|---|
| Danh sách sản phẩm | `product_list` | `list[dict]` | 7 key: product_id, product_name, price, quantity, sold, returned, discount |
| Mã sản phẩm | `product_id` | `str` | strip().upper() |
| Số lượng / phần trăm | `number_text` | `str → int` | isdigit(); số lượng khác 0; phần trăm ≤ 70 |
| Giá sau giảm | `discounted_price` | `int` | price * (100 - discount) // 100 |
| Tổng tiền / tiền hoàn | `total_payment, refund_amount` | `int` | discounted_price × số lượng |

### Đề xuất giải pháp

- Chức năng 2 - 5 có cùng khung: nhập mã + một con số → tìm sản phẩm → kiểm tra → cập nhật. Phần nhập và tìm được viết **một lần**; mỗi chức năng chỉ khác câu hỏi, thông báo "không tìm thấy" và bước xử lý cuối.
- Giá sau giảm dùng `//` (chia lấy phần nguyên) vì tiền VND không có phần lẻ; với dữ liệu mẫu kết quả chia hết nên không sai số (VD 399000 × 90 // 100 = 359100).
- Đổi trả hoàn tiền theo **giá hiện tại sau giảm** đúng như đề yêu cầu.
- Phần trăm giảm giá: `isdigit()` đã loại số âm, số thập phân và chữ; thêm điều kiện ≤ 70. Giá trị 0 hợp lệ (bỏ giảm giá).
- Thông báo lỗi menu không ghi cụ thể khoảng số (đề ghi 1-5 nhưng menu có 6 chức năng) để không gây hiểu nhầm.

### Thiết kế thuật toán (Pseudocode)

```
LẶP MÃI:
    IN menu; NHẬP choice
    NẾU "1": IN từng sản phẩm kèm trạng thái tồn kho
    NẾU choice ∈ {"2","3","4","5"}:
        NHẬP mã (strip().upper()) và con số (strip())
        không tìm thấy → thông báo "Không tìm thấy..." tương ứng
        "4": không phải số nguyên 0..70 → "Phần trăm giảm giá không hợp lệ"; ngược lại cập nhật discount
        "2","3","5": không phải số nguyên dương → báo lỗi
            giá_sau_giảm ← giá * (100 - discount) // 100
            "2": SL > tồn kho → "Số lượng trong kho không đủ để bán"
                 tồn kho −= SL; đã bán += SL; IN tổng tiền = giá_sau_giảm × SL
            "3": SL > đã bán → "Số lượng đổi/trả không được vượt quá số lượng đã bán"
                 đã bán −= SL; tồn kho += SL; đổi trả += SL; IN tiền hoàn = giá_sau_giảm × SL
            "5": tồn kho += SL
    NẾU "6": "Thoát chương trình."; THOÁT
    NGƯỢC LẠI: "Lựa chọn không hợp lệ, vui lòng nhập lại!"
```

## (2) Triển khai code

File: [`quan_ly_giao_dich.py`](quan_ly_giao_dich.py)

```python
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
```

## Kết quả

Kiểm thử đủ 6 chức năng và 7 bẫy *(ẩn menu lặp lại cho gọn)*:

```
Nhập lựa chọn (1-6): 1
Danh sách sản phẩm hiện tại:
1. Mã SP: SP001 | Tên: Áo polo nam | Giá: 299000 | Tồn kho: 20 | Đã bán: 5 | Đổi trả: 1 | Giảm giá: 0% | Trạng thái: Còn hàng
2. Mã SP: SP002 | Tên: Quần kaki nam | Giá: 399000 | Tồn kho: 8 | Đã bán: 3 | Đổi trả: 0 | Giảm giá: 10% | Trạng thái: Còn hàng
3. Mã SP: SP003 | Tên: Váy công sở nữ | Giá: 459000 | Tồn kho: 3 | Đã bán: 7 | Đổi trả: 1 | Giảm giá: 15% | Trạng thái: Sắp hết hàng

Nhập lựa chọn (1-6): 2
Nhập mã sản phẩm khách muốn mua:  sp002 
Nhập số lượng khách mua: 2
Giá sau giảm: 359,100 VND (giảm 10%)
Tổng tiền khách cần thanh toán: 718,200 VND

Nhập lựa chọn (1-6): 2
Nhập mã sản phẩm khách muốn mua: SP003
Nhập số lượng khách mua: 5
Số lượng trong kho không đủ để bán

Nhập lựa chọn (1-6): 2
Nhập mã sản phẩm khách muốn mua: SP999
Nhập số lượng khách mua: 1
Không tìm thấy sản phẩm cần bán

Nhập lựa chọn (1-6): 2
Nhập mã sản phẩm khách muốn mua: SP001
Nhập số lượng khách mua: 0
Số lượng không hợp lệ (phải là số nguyên dương)

Nhập lựa chọn (1-6): 3
Nhập mã sản phẩm khách muốn đổi/trả: sp001
Nhập số lượng đổi/trả: 2
Đổi trả thành công 2 x Áo polo nam.
Số tiền hoàn lại: 598,000 VND

Nhập lựa chọn (1-6): 3
Nhập mã sản phẩm khách muốn đổi/trả: SP002
Nhập số lượng đổi/trả: 9
Số lượng đổi/trả không được vượt quá số lượng đã bán

Nhập lựa chọn (1-6): 3
Nhập mã sản phẩm khách muốn đổi/trả: SP999
Nhập số lượng đổi/trả: 1
Không tìm thấy sản phẩm cần đổi trả

Nhập lựa chọn (1-6): 4
Nhập mã sản phẩm cần áp dụng giảm giá: sp001
Nhập phần trăm giảm giá: 20
Đã áp dụng giảm giá 20% cho Áo polo nam

Nhập lựa chọn (1-6): 4
Nhập mã sản phẩm cần áp dụng giảm giá: SP001
Nhập phần trăm giảm giá: 80
Phần trăm giảm giá không hợp lệ

Nhập lựa chọn (1-6): 4
Nhập mã sản phẩm cần áp dụng giảm giá: SP001
Nhập phần trăm giảm giá: abc
Phần trăm giảm giá không hợp lệ

Nhập lựa chọn (1-6): 5
Nhập mã sản phẩm cần nhập thêm: sp003
Nhập số lượng nhập thêm: 10
Nhập kho thành công. Tồn kho mới của Váy công sở nữ: 13

Nhập lựa chọn (1-6): 1
Danh sách sản phẩm hiện tại:
1. Mã SP: SP001 | Tên: Áo polo nam | Giá: 299000 | Tồn kho: 22 | Đã bán: 3 | Đổi trả: 3 | Giảm giá: 20% | Trạng thái: Còn hàng
2. Mã SP: SP002 | Tên: Quần kaki nam | Giá: 399000 | Tồn kho: 6 | Đã bán: 5 | Đổi trả: 0 | Giảm giá: 10% | Trạng thái: Còn hàng
3. Mã SP: SP003 | Tên: Váy công sở nữ | Giá: 459000 | Tồn kho: 13 | Đã bán: 7 | Đổi trả: 1 | Giảm giá: 15% | Trạng thái: Còn hàng

Nhập lựa chọn (1-6): 7
Lựa chọn không hợp lệ, vui lòng nhập lại!

Nhập lựa chọn (1-6): x
Lựa chọn không hợp lệ, vui lòng nhập lại!

Nhập lựa chọn (1-6): 6
Thoát chương trình.
```

Kiểm tra công thức: SP002 giá 399000, giảm 10% → giá sau giảm **359,100**; mua 2 → **718,200 VND**. SP001 (giảm 0%) đổi trả 2 → hoàn **598,000 VND**.
