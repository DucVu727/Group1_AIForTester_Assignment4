# Before & After Comparison

## Mục tiêu

Refactor script Selenium ban đầu sang mô hình Page Object Model (POM) nhằm tăng khả năng bảo trì, tái sử dụng và mở rộng mã nguồn.

| Tiêu chí | Trước khi Refactor | Sau khi Refactor |
|----------|--------------------|------------------|
| Cấu trúc | Toàn bộ code nằm trong một file | Tách thành Page Object và Test |
| Locator | Locator nằm trong các hàm test | Locator được quản lý tập trung trong LoginPage |
| Page Action | Thao tác với UI nằm trong file test | Được chuyển vào LoginPage |
| Assertion | Nằm trong file test | Vẫn giữ trong file test (đúng chuẩn POM) |
| Khả năng bảo trì | Khi UI thay đổi phải sửa nhiều nơi | Chỉ cần sửa trong LoginPage |
| Khả năng tái sử dụng | Thấp | Cao |
| Khả năng mở rộng | Khó thêm test case mới | Dễ dàng mở rộng thêm nhiều test case |

## Lợi ích sau khi Refactor

- Code được tổ chức rõ ràng theo mô hình POM.
- Giảm trùng lặp Locator.
- Dễ bảo trì khi giao diện thay đổi.
- Các thao tác trên trang Login có thể tái sử dụng cho nhiều test case.
- Test case ngắn gọn, dễ đọc và dễ bảo trì.