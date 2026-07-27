# Prompt Log - Activity 2

## Prompt 1: Chuyển đổi Script Selenium sang mô hình Page Object Model (POM)

**Vai trò (Role):**

Bạn là một Senior Automation Test Engineer có nhiều năm kinh nghiệm với Selenium WebDriver, Python và mô hình thiết kế Page Object Model (POM).

**Nhiệm vụ (Task):**

Tôi đã có một script Automation Test viết bằng Python sử dụng Selenium WebDriver. Script hiện đang chạy ổn định và gồm 2 test case:

- TC01: Đăng nhập thành công.
- TC02: Đăng nhập thất bại.

Hãy refactor (chuyển đổi) script hiện tại sang mô hình **Page Object Model (POM)**.

**Yêu cầu:**

- Giữ nguyên ngôn ngữ Python.
- Sử dụng Selenium WebDriver 4.x.
- Không thay đổi logic của các test case.
- Không thêm hoặc bớt bất kỳ bước kiểm thử nào.
- Chuyển toàn bộ Locator vào class `LoginPage`.
- Chuyển toàn bộ các thao tác trên trang Login (mở trang, nhập Username, nhập Password, click Login, lấy thông báo) vào class `LoginPage`.
- Giữ toàn bộ Assertion trong file Test.
- Tiếp tục sử dụng Explicit Wait (`WebDriverWait`) để đảm bảo tính ổn định.
- Code cần rõ ràng, dễ đọc và dễ bảo trì.

**Đầu ra mong muốn (Output):**

Sinh mã nguồn theo cấu trúc sau:

activity-2/

- pages/
  - login_page.py
- tests/
  - test_login.py

Trong đó:

- `login_page.py` chỉ chứa Locator và các thao tác với trang Login.
- `test_login.py` chỉ chứa WebDriver, các Test Case và Assertion.
- Đảm bảo sau khi refactor, code vẫn chạy PASS cả 2 test case.