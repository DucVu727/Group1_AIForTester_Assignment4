# Hoạt động 5: Review kết quả bởi Tester (HUMAN-IN-THE-LOOP)

## 1. Tổng quan công việc
Tester thực hiện kiểm tra chéo (Cross-check) toàn bộ output do AI sinh ra ở Hoạt động 1, Hoạt động 2, Hoạt động 3 và Hoạt động 4. Mục tiêu nhằm đảm bảo AI không tự suy diễn thêm bước, không làm sai logic kiểm thử, đánh giá đúng nguyên nhân gây ra lỗi automation và tuân thủ chuẩn kiến trúc Automation Testing trước khi nghiệm thu.

---

## 2. Bảng đối chiếu và kiểm tra chéo Output của AI (Validation Log)

| Hoạt động | AI Output | Tester nhận xét | AI Đúng? | Nếu sai, Tester sửa thành | Lý do / Bằng chứng |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **HĐ1** | Sinh script `test_login.py` bằng Playwright gồm 2 kịch bản: Login thành công (`tomsmith`/`SuperSecretPassword!`) và Login thất bại. | Script bám sát 100% Test Case gốc. Có đầy đủ assertion kiểm tra thông báo flash message chính xác theo yêu cầu. Không tự suy diễn thêm các bước không có trong requirement. | **ĐÚNG (✓)** | Giữ nguyên script gốc (`test_login.py`). | **Bằng chứng:** Ảnh `execution_evidence.png` xác nhận cả 2 test case (`TC_01` & `TC_02`) đều đạt kết quả **PASSED** khi chạy thực tế. |
| **HĐ2** | Refactor code sang mô hình Page Object Model (POM), tạo class `LoginPage` (`pages/login_page.py`) và file test riêng (`tests/test_login.py`). | Cấu trúc phân lớp rõ ràng. AI tuân thủ chuẩn POM: Tầng Page Object chỉ chứa locator/hành động UI, câu lệnh `assert` nằm hoàn toàn ở tầng Test. | **ĐÚNG (✓)** | Giữ nguyên cấu trúc refactor của AI (`pages/` và `tests/`). | **Bằng chứng:** Ảnh `activity-2/img-1.png` cho thấy cấu trúc thư mục chuẩn và thực thi lệnh `python activity-2\tests\test_login.py` chạy thành công **PASSED** cả 2 kịch bản. |
| **HĐ3** | Báo cáo review `review_report.md` đánh giá theo 4 tiêu chí (Maintainability, Stability, Reusability, Readability) và nhận diện nguy cơ Flaky Test. | Phân tích chính xác các điểm mạnh/yếu của code. Chỉ ra đúng rủi ro flaky test liên quan đến thời gian chờ element render và đề xuất dùng Explicit Wait. | **ĐÚNG (✓)** | Tiếp thu đánh giá của AI và áp dụng giải pháp bổ sung `wait_for_selector` trước khi tương tác. | Đánh giá của AI sát với thực tế, giúp tăng độ ổn định cho bộ test automation. |
| **HĐ4** | Phân tích log lỗi/stack trace, đưa ra bảng xếp hạng giả thuyết nguyên nhân (Rank, Probability, Evidence, Verification) và đề xuất phương án fix. | AI phân tích logic và đưa ra các giả thuyết phù hợp. Tuy nhiên, thứ tự ưu tiên (Ranking) có thời điểm chưa chính xác giữa lỗi Locator bị thay đổi và lỗi Race condition/Timeout khi element chưa kịp render. | **SAI MỘT PHẦN (X)** | Điều chỉnh lại Bảng xếp hạng xác suất (Re-rank): Đưa nguyên nhân do element chưa kịp render/Timeout lên ưu tiên cao hơn và cập nhật selector đúng chuẩn. | **Lý do:** Qua kiểm tra thực tế (Verification), DOM của trang vẫn giữ element nhưng do độ trễ mạng khiến script tương tác quá nhanh dẫn đến Timeout trước khi locator thực sự xuất hiện. |

---

## 3. Tổng kết đánh giá của Tester (Human Summary)

1. **Về độ chính xác của AI:** 
   * AI thực hiện rất tốt từ HĐ1 đến HĐ3: Sinh code chính xác (100% test case coverage), refactor chuẩn mô hình POM và đưa ra nhận xét code review sát thực tế.
   * Ở HĐ4 (Debug lỗi), AI đưa ra đủ các khả năng gây ra lỗi nhưng đôi khi đánh giá sai lệch tỷ lệ xác suất (Probability) giữa lỗi thay đổi DOM và lỗi bất đồng bộ/Race condition.

2. **Vai trò của Tester (Human-In-The-Loop):**
   * Tester đóng vai trò quyết định trong việc **nghiệm thu thực tế**: Chạy thử script, kiểm tra DOM hiện tại để xác minh giả thuyết của AI ở HĐ4, điều chỉnh lại thứ tự ưu tiên (Ranking) và chụp ảnh chứng minh kết quả thực thi (`PASSED`) trên môi trường thật.