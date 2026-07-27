# Hoạt động 5: Review kết quả bởi Tester (HUMAN-IN-THE-LOOP)



## 1. Tổng quan công việc

Tester thực hiện kiểm tra chéo (Cross-check) toàn bộ output do AI sinh ra ở Hoạt động 1, Hoạt động 2 và Hoạt động 3. Mục tiêu nhằm đảm bảo AI không tự suy diễn thêm bước, không làm sai logic kiểm thử và tuân thủ chuẩn kiến trúc Automation Testing trước khi nghiệm thu.



---

## 2. Bảng đối chiếu và kiểm tra chéo Output của AI (Validation Log)



| Hoạt động | AI Output | Tester nhận xét | AI Đúng? | Nếu sai, Tester sửa thành | Lý do / Bằng chứng |

| :--- | :--- | :--- | :---: | :--- | :--- |

| **HĐ1** | Sinh script `test_login.py` bằng Playwright gồm 2 kịch bản: Login thành công (`tomsmith`/`SuperSecretPassword!`) và Login thất bại[cite: 1, 2]. | Script bám sát 100% Test Case gốc[cite: 1, 2]. Có đầy đủ assertion kiểm tra thông báo flash message chính xác theo yêu cầu[cite: 1, 2]. Không tự suy diễn thêm các bước không có trong requirement[cite: 1, 2]. | **ĐÚNG (✓)** | Giữ nguyên script gốc (`test_login.py`)[cite: 1]. | **Bằng chứng:** Ảnh `execution_evidence.png` xác nhận cả 2 test case (`TC_01` & `TC_02`) đều đạt kết quả **PASSED** khi chạy thực tế. |

| **HĐ2** | Refactor code sang mô hình Page Object Model (POM), tạo class `LoginPage` (`pages/login_page.py`) và file test riêng (`tests/test_login.py`)[cite: 1, 2]. | Cấu trúc phân lớp rõ ràng[cite: 1]. AI tuân thủ chuẩn POM: Tầng Page Object chỉ chứa locator/hành động UI, câu lệnh `assert` nằm hoàn toàn ở tầng Test[cite: 1, 2]. | **ĐÚNG (✓)** | Giữ nguyên cấu trúc refactor của AI (`pages/` và `tests/`)[cite: 1]. | **Bằng chứng:** Ảnh `activity-2/img-1.png` cho thấy cấu trúc thư mục chuẩn và thực thi lệnh `python activity-2\\tests\\test_login.py` chạy thành công **PASSED** cả 2 kịch bản[cite: 1]. |

| **HĐ3** | Báo cáo review `review_report.md` đánh giá theo 4 tiêu chí (Maintainability, Stability, Reusability, Readability) và nhận diện nguy cơ Flaky Test[cite: 1, 2]. | Phân tích chính xác các điểm mạnh/yếu của code[cite: 1, 2]. Chỉ ra đúng rủi ro flaky test liên quan đến thời gian chờ element render và đề xuất dùng Explicit Wait[cite: 1, 2]. | **ĐÚNG (✓)** | Tiếp thu đánh giá của AI và áp dụng giải pháp bổ sung `wait_for_selector` trước khi tương tác. | Đánh giá của AI sát với thực tế, giúp tăng độ ổn định cho bộ test automation[cite: 1, 2]. |

| **HĐ4** | *(Đang cập nhật)* | *(Chưa triển khai - Nhóm chưa bổ sung thư mục/file cho Hoạt động 4)* | N/A | Sẽ cập nhật bảng xếp hạng giả thuyết lỗi sau khi hoàn thiện HĐ4[cite: 2]. | Bổ sung sau khi nhóm thực hiện xong bài tập Hoạt động 4[cite: 2]. |



---

## 3. Tổng kết đánh giá của Tester (Human Summary)



1. **Về độ chính xác của AI:** 

   * AI thực hiện xuất sắc ở HĐ1, HĐ2 và HĐ3[cite: 1]. AI không bị hiện tượng "ảo tưởng" (hallucination), bám sát yêu cầu kịch bản kiểm thử (100% test case coverage) và áp dụng đúng thiết kế kịch bản kiểm thử theo mô hình POM[cite: 1, 2].



2. **Vai trò của Tester (Human-In-The-Loop):**

   * Dù AI sinh code và refactor đúng logic trên lý thuyết, Tester vẫn đóng vai trò bắt buộc trong việc **chạy thử script trên môi trường thực tế**, đối chiếu log terminal và chụp bằng chứng (`execution_evidence.png`, `img-1.png`) để đảm bảo hệ thống không bị lỗi runtime hoặc lỗi lệch đường dẫn module (import path)[cite: 1, 2].

