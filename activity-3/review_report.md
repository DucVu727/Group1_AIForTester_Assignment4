# Báo cáo Code Review - Hoạt động 3

Báo cáo này đánh giá chất lượng mã nguồn Automation Test sau khi đã được refactor sang mô hình Page Object Model (POM) ở Hoạt động 2. Việc đánh giá được thực hiện tự động bởi AI và phản biện bởi học viên.

## 1. Kết quả đánh giá theo 5 tiêu chí

### Tiêu chí 1: Maintainability (Khả năng bảo trì)
* **Trạng thái:** WARNING
* **Đánh giá & Nhận xét của AI:**
  * Các thành phần giao diện (Locators) và hành động (Actions) đã được tách biệt thành công ra khỏi kịch bản test và đưa vào [login_page.py](../activity-2/pages/login_page.py).
  * Tuy nhiên, driver và các cấu hình chạy trình duyệt vẫn đang được khởi tạo thủ công trong từng hàm test qua `create_driver()` thay vì quản lý tập trung qua Test Fixture (như của Pytest), dẫn đến việc khó bảo trì khi số lượng test case tăng lên.

### Tiêu chí 2: Stability (Độ ổn định)
* **Trạng thái:** WARNING
* **Đánh giá & Nhận xét của AI:**
  * Code đã áp dụng Explicit Wait (`WebDriverWait`) tại các tương tác cốt lõi trong `LoginPage` như nhập text hay click nút.
  * Có nguy cơ cao xảy ra **Flaky Test (chạy lúc pass lúc fail)** do lỗi `StaleElementReferenceException` khi truy cập Flash Message ngay sau khi submit form mà không đồng bộ tải trang (Xem chi tiết mục 2).

### Tiêu chí 3: Reusability (Khả năng tái sử dụng)
* **Trạng thái:** PASS
* **Đánh giá & Nhận xét của AI:**
  * Hàm `login(username, password)` trong `LoginPage` được tái sử dụng thành công cho cả hai trường hợp đăng nhập đúng và sai.
  * Loại bỏ hoàn toàn sự trùng lặp locator giữa các kịch bản kiểm thử.

### Tiêu chí 4: Readability (Khả năng đọc)
* **Trạng thái:** PASS
* **Đánh giá & Nhận xét của AI:**
  * Tên các biến, hàm và lớp tuân theo chuẩn đặt tên rõ ràng (`LoginPage`, `open`, `login`, `get_flash_message`).
  * Độ dài mỗi hàm/phương thức đều rất ngắn gọn (dưới 20 dòng), dễ theo dõi luồng thực thi.

### Tiêu chí 5: Coding Convention & Framework Standard (Quy chuẩn & Tiêu chuẩn Framework)
* **Trạng thái:** WARNING
* **Đánh giá & Nhận xét của AI:**
  * Mã nguồn viết đúng định dạng PEP 8.
  * Tuy nhiên, việc sử dụng `sys.path.append(...)` để import module giữa các thư mục là một giải pháp tình thế (anti-pattern). Nên sử dụng cấu trúc package Python tiêu chuẩn và chạy qua test runner chuyên nghiệp.
  * Việc dùng hàm `main()` tự viết để chạy tuần tự các test case thay vì dùng một Test Runner (như `pytest` hoặc `unittest`) làm giảm tính chuyên nghiệp của framework kiểm thử.

---

## 2. Điểm Flaky phát hiện & Đề xuất khắc phục

### Điểm Flaky phát hiện:
* **Vị trí xảy ra:** Phương thức [get_flash_message](../activity-2/pages/login_page.py#L47-L52) trong lớp `LoginPage` được gọi ngay sau hành động click đăng nhập ở [test_login.py](../activity-2/tests/test_login.py#L50) và [test_login.py](../activity-2/tests/test_login.py#L72).
* **Nguyên nhân:** Khi click vào nút Login, trang web thực hiện gửi yêu cầu POST lên máy chủ và reload lại trang (hoặc chuyển sang trang `/secure`). Quá trình reload trang khiến các phần tử trên DOM cũ bị hủy và thay thế bằng phần tử mới trên DOM mới. 
  Nếu hàm `get_flash_message()` chạy quá nhanh, `self.wait.until(EC.visibility_of_element_located(self.FLASH_MESSAGE))` có thể tìm thấy phần tử `#flash` của trang cũ khi nó chưa kịp biến mất, nhưng đến khi thực hiện lệnh `.text.strip()` thì phần tử đó đã bị hủy trên DOM mới, gây ra lỗi **`StaleElementReferenceException`**.

### Đề xuất khắc phục (Fix):
Thay đổi hàm `get_flash_message` để kiểm tra độ tươi mới của phần tử, hoặc bắt ngoại lệ và lấy lại phần tử nếu gặp lỗi stale element.

```python
from selenium.common.exceptions import StaleElementReferenceException
import time

def get_flash_message(self):
    """Lấy nội dung thông báo sau khi đăng nhập (đã chống flaky)."""
    # Đợi cho đến khi phần tử xuất hiện và hiển thị
    for _ in range(3):  # Thử lại tối đa 3 lần nếu gặp Stale Element
        try:
            flash = self.wait.until(
                EC.visibility_of_element_located(self.FLASH_MESSAGE)
            )
            return flash.text.strip()
        except StaleElementReferenceException:
            time.sleep(0.5)
    raise Exception("Không thể lấy thông báo flash do phần tử bị stale liên tục.")
```

---

## 3. Ý kiến phản biện & Đồng thuận của Học viên

Học viên đã xem xét báo cáo đánh giá của AI và đưa ra ý kiến phản hồi như sau:

* **Đồng ý hoàn toàn:**
  * Đồng ý với đánh giá **WARNING** ở tiêu chí **Stability** và **Framework Standard**. Việc chạy thử nghiệm bằng hàm `main()` thủ công và chắp vá đường dẫn bằng `sys.path.append` khiến project rất khó mở rộng và thiếu đi tính năng báo cáo trực quan (Test Report) của các runner chuyên nghiệp như pytest.
  * Phân tích về lỗi flaky `StaleElementReferenceException` là hoàn toàn chính xác và rất thực tế đối với các trang web sử dụng cơ chế tải lại toàn trang truyền thống như Herokuapp.
* **Kế hoạch hành động:**
  * Sẽ tích hợp thư viện **`pytest`** vào dự án để thay thế hàm `main()`, chuyển việc quản lý driver sang **pytest fixture** nằm trong tệp `conftest.py` nhằm tối ưu hóa khả năng bảo trì và tái sử dụng ở các hoạt động tiếp theo.
  * Áp dụng đề xuất fix lỗi flaky cho hàm `get_flash_message`.
