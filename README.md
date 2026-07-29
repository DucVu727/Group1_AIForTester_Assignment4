# BÀI TẬP THỰC HÀNH: AI HỖ TRỢ AUTOMATION TESTING
**Nhóm thực hiện:** Nhóm 1 - Lớp Thực Tập Chuyên Ngành
**Dự án:** Kiểm thử tự động trang Đăng nhập (The Internet Herokuapp)
**Môi trường thử nghiệm:** [https://the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login)

---

## 1. Công nghệ & Thư viện sử dụng
*   **Ngôn ngữ lập trình:** Python (version 3.x)
*   **Thư viện Automation:** Selenium (version 4.x)
*   **Công cụ quản lý WebDriver:** `webdriver-manager` (Tự động tải Chrome WebDriver tương thích)
*   **Mô hình thiết kế:** Page Object Model (POM)

---

## 2. Hướng dẫn cài đặt & Chạy kiểm thử

### Cài đặt môi trường
Đảm bảo máy tính của bạn đã cài đặt Python 3. Chạy lệnh sau để cài đặt các thư viện cần thiết:
```bash
pip install selenium webdriver-manager
```

### Chạy kịch bản kiểm thử
*   **Chạy script thuần (Hoạt động 1):**
    ```bash
    python activity-1/test_login.py
    ```
*   **Chạy script theo mô hình Page Object Model (Hoạt động 2):**
    ```bash
    python activity-2/tests/test_login.py
    ```

---

## 3. Cấu trúc thư mục dự án
Cấu trúc thư mục bài nộp tuân thủ đúng yêu cầu đặc tả của Assignment 4:
```text
/Group1_AIForTester_Assignment4/
│
├── README.md                      # File hướng dẫn tổng quan dự án (File này)
│
├── activity-1/                    # Hoạt động 1: Sinh Automation Script bằng AI
│   ├── test_login.py              # Script test Selenium thuần do AI viết
│   ├── execution_evidence.png     # Ảnh chụp màn hình chạy test PASS thành công
│   ├── prompt_log.md              # Log toàn bộ các câu lệnh prompt đã dùng với AI
│   └── setup.md                   # Hướng dẫn setup nhanh HĐ1
│
├── activity-2/                    # Hoạt động 2: Thiết kế / Refactor Page Object Model
│   ├── pages/
│   │   └── login_page.py          # Lớp Page Object chứa locators và hành vi UI
│   ├── tests/
│   │   └── test_login.py          # Script test gọi Page Object
│   ├── before_after_comparison.md # So sánh cấu trúc code trước và sau khi refactor sang POM
│   ├── img-1.png                  # Ảnh chụp cấu trúc POM và kết quả chạy PASS
│   └── prompt_log.md              # Log prompt đã dùng để refactor POM
│
├── activity-3/                    # Hoạt động 3: Review Automation Code bằng AI
│   ├── review_report.md           # Bảng đánh giá 4 tiêu chí, flaky test và phản biện của Tester
│   └── prompt_log.md              # Log prompt dùng để yêu cầu AI review
│
├── activity-4/                    # Hoạt động 4: Debug Automation Failure bằng AI
│   ├── login_test.py              # Script test chứa lỗi do Tester chủ động tạo ra
│   ├── login_test_fixed.py        # Script test sau khi được fix lỗi theo gợi ý của AI
│   ├── error_log.txt              # Stack trace báo lỗi NoSuchElementException
│   ├── bug_description.md         # Mô tả chi tiết lỗi và cách tái hiện kịch bản
│   ├── ai_hypothesis.md           # Bảng xếp hạng các giả thuyết lỗi do AI phân tích
│   ├── veryfication_log.md        # Nhật ký xác minh và kiểm chứng lỗi thực tế (veryfication)
│   ├── fix_commit.diff            # File diff so sánh code trước/sau khi fix lỗi
│   └── prompt_log.md              # Log các câu lệnh prompt dùng để debug với AI
│
└── activity-5/                    # Hoạt động 5: Review kết quả bởi Tester (Human-in-the-loop)
    └── ai_vs_tester_log.md        # Nhật ký đối chiếu nhận xét AI đúng/sai và tổng kết của Tester
```

---

## 4. Tóm tắt nội dung các hoạt động kiểm thử

### Hoạt động 1: Sinh Automation Script bằng AI
*   AI được cung cấp tài liệu yêu cầu đăng nhập, ảnh chụp màn hình và mã nguồn HTML.
*   AI sinh ra file [test_login.py](file:///d:/Thực%20Tập%20Chuyên%20Ngành/AI%20For%20Tester/Group1_AIForTester_Assignment4/activity-1/test_login.py) bao phủ 2 kịch bản (Login thành công với tài khoản `tomsmith` / `SuperSecretPassword!` và Login thất bại).

### Hoạt động 2: Thiết kế / Refactor Page Object Model bằng AI
*   AI hỗ trợ tách code test thô thành mô hình POM tiêu chuẩn.
*   Tầng Page Object ([login_page.py](file:///d:/Thực%20Tập%20Chuyên%20Ngành/AI%20For%20Tester/Group1_AIForTester_Assignment4/activity-2/pages/login_page.py)) chứa định nghĩa locator và hàm tương tác UI. Tầng Test ([test_login.py](file:///d:/Thực%20Tập%20Chuyên%20Ngành/AI%20For%20Tester/Group1_AIForTester_Assignment4/activity-2/tests/test_login.py)) thực hiện verify kết quả thông qua các assert logic.

### Hoạt động 3: Review Automation Code bằng AI
*   AI đánh giá chất lượng mã nguồn POM theo 4 khía cạnh: Maintainability, Stability, Reusability, và Readability.
*   AI nhận diện đúng nguy cơ Flaky Test liên quan đến việc render chậm của các phần tử và đề xuất sử dụng Explicit Wait để tối ưu tính ổn định.

### Hoạt động 4: Debug Automation Failure bằng AI
*   Giả lập lỗi **NoSuchElementException** (Selector ô nhập Username bị sửa đổi cố ý từ `username` thành `username123` trong script [login_test.py](file:///d:/Thực%20Tập%20Chuyên%20Ngành/AI%20For%20Tester/Group1_AIForTester_Assignment4/activity-4/login_test.py), dẫn đến script Selenium bị crash).
*   AI phân tích Stack trace lỗi và đưa ra bảng xếp hạng giả thuyết chính xác đến 90% cho nguyên nhân sai locator (`Incorrect Locator`), đề xuất giải pháp cập nhật lại selector đúng chuẩn trong file [login_test_fixed.py](file:///d:/Thực%20Tập%20Chuyên%20Ngành/AI%20For%20Tester/Group1_AIForTester_Assignment4/activity-4/login_test_fixed.py) và tạo code diff vá lỗi.

### Hoạt động 5: Đánh giá Human-in-the-loop
*   Tester tiến hành đối chiếu và kiểm tra chéo 100% output của AI từ HĐ1 đến HĐ4, tổng hợp tại file [ai_vs_tester_log.md](file:///d:/Thực%20Tập%20Chuyên%20Ngành/AI%20For%20Tester/Group1_AIForTester_Assignment4/activity-5/ai_vs_tester_log.md).
*   Ở HĐ4, Tester phát hiện AI xếp hạng xác suất lỗi chưa tối ưu (đánh giá lỗi locator cao hơn lỗi Timeout do element chưa render), thực hiện Re-rank mức độ ưu tiên lên hàng đầu và kiểm chứng thực tế giúp bộ test suite chạy thành công **PASSED** cả 2 kịch bản.
