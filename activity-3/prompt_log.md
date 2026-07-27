# Prompt Log - Activity 3

## Prompt 1: Review mã nguồn Selenium Automation Test

**Vai trò (Role):**

Bạn là một Senior Automation Test Engineer kiêm QA Tech Lead giàu kinh nghiệm. Bạn có kiến thức sâu rộng về Python, Selenium WebDriver 4.x, các mẫu thiết kế (Design Patterns) như Page Object Model (POM), và các nguyên tắc thiết kế mã nguồn sạch (Clean Code), tối ưu độ ổn định kịch bản kiểm thử (Flaky Test prevention).

**Nhiệm vụ (Task):**

Hãy tiến hành review và đánh giá chất lượng mã nguồn Automation Test hiện tại của tôi (bao gồm lớp Page Object và file Test Script) dựa trên các tiêu chí cốt lõi dưới đây. Đưa ra đánh giá bằng các nhãn trạng thái: **PASS**, **WARNING** hoặc **FAIL** kèm theo nhận xét chi tiết, chỉ rõ lý do và đề xuất cách cải tiến cụ thể.

**Các tiêu chí đánh giá:**

1. **Maintainability (Khả năng bảo trì):**
   - Đánh giá cách đặt tên lớp, hàm, biến.
   - Việc tuân thủ cấu trúc thư mục, phân tách giữa Page Object và Test.
   - Khả năng mở rộng mã nguồn khi có thêm các trang hoặc các ca kiểm thử mới.

2. **Stability (Độ ổn định):**
   - Sự ổn định của các locator được sử dụng.
   - Tính hợp lý khi sử dụng các cơ chế chờ đợi (Explicit Waits, Implicit Waits, Hard sleep).
   - Xác định và chỉ ra **ít nhất 1 vị trí** có nguy cơ gây lỗi test chạy không ổn định (Flaky Test) và đề xuất mã nguồn sửa đổi.

3. **Reusability (Khả năng tái sử dụng):**
   - Khả năng dùng lại các phương thức hành động (actions) giữa các kịch bản test.
   - Mức độ trùng lặp mã nguồn (cả locator lẫn logic xử lý).

4. **Readability (Khả năng đọc hiểu):**
   - Cách sử dụng chú thích (comment) trong mã nguồn (có làm rõ lý do tại sao thay vì mô tả lệnh không).
   - Độ dài của các hàm/phương thức và tính nhất quán trong phong cách viết code.

5. **Framework Standards & Coding Conventions (Chuẩn Framework & Quy tắc viết code):**
   - Đánh giá tổng quan về việc áp dụng quy chuẩn PEP 8.
   - Cách quản lý Driver (WebDriver lifecycle) và phương thức chạy test (Test Runner).

**Mã nguồn đầu vào để Review:**
- Lớp Page Object: [login_page.py](../activity-2/pages/login_page.py)
- Lớp Test Script: [test_login.py](../activity-2/tests/test_login.py)
