# Bài tập Python Session 11 - Tuple & Dict

Tổng hợp 6 bài tập thực hành về **Tuple** và **Dictionary** trong Python: tính bất biến của tuple, truy cập dict bằng key, CRUD trên dict, list of dict và kết hợp List - Dict - Tuple. Bối cảnh chung là hệ thống bán hàng thời trang **Yody** và ứng dụng quản lý kho hàng.

## Danh sách bài tập

| STT | Bài tập | Loại bài | Kiến thức trọng tâm |
|---|---|---|---|
| 1 | [Lỗi xử lý thông tin sản phẩm](bai-1-loi-xu-ly-thong-tin-san-pham/) | Vận dụng cơ bản - sửa lỗi legacy | Index của tuple, `len()`, tuple bất biến → tạo tuple mới |
| 2 | [Lỗi xử lý thông tin nhân viên](bai-2-loi-xu-ly-thong-tin-nhan-vien/) | Vận dụng cơ bản - sửa lỗi legacy | Truy cập dict bằng key, `KeyError`, thêm / sửa / xóa key, dict không có `append()` |
| 3 | [Hệ thống quản lý sản phẩm Yody](bai-3-he-thong-quan-ly-san-pham-yody/) | Vận dụng chuyên sâu | CRUD trên list of dict, kiểm tra trùng mã, validate giá / số lượng |
| 4 | [Hệ thống vận hành bán hàng Yody](bai-4-he-thong-van-hanh-ban-hang-yody/) | Phân tích, thiết kế & code | Bán / nhập kho, trạng thái tồn kho, báo cáo doanh thu, sản phẩm bán chạy nhất |
| 5 | [Hệ thống quản lý giao dịch bán hàng Yody](bai-5-he-thong-quan-ly-giao-dich-yody/) | Sáng tạo - thiết kế toàn bộ | Bán có giảm giá, đổi trả, áp dụng giảm giá 0-70%, nhập kho, 7 bẫy dữ liệu |
| 6 | [Ứng dụng quản lý kho hàng](bai-6-ung-dung-quan-ly-kho-hang/) | Bài tập tổng hợp | List chứa dict, thông tin `(giá, số lượng)` lưu bằng tuple, cập nhật tuple bằng cách tạo tuple mới |

Mỗi thư mục bài có `README.md` riêng (đề bài, phân tích, lời giải, kết quả chạy thử) và mã nguồn Python. Hai bài sửa lỗi (bài 1, 2) có cả `script_legacy.py` (code gốc bị lỗi) và `script.py` (code đã sửa).

## Cách chạy

Yêu cầu Python 3.x. Vào thư mục bài cần chạy, ví dụ:

```bash
cd bai-3-he-thong-quan-ly-san-pham-yody
python quan_ly_san_pham.py
```
