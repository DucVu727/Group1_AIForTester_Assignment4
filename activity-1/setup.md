1. Cài đặt Python
Tải về: Truy cập python.org và tải phiên bản mới nhất (khuyến nghị từ 3.10 trở lên).
Lưu ý quan trọng: Khi cài đặt trên Windows, phải tích vào ô "Add Python to PATH" ở màn hình đầu tiên.

2. Cài đặt Trình soạn thảo (IDE)
Nhóm chúng ta thống nhất sử dụng công cụ sau:
VS Code: Cài thêm Extension "Python" của Microsoft.

3. Clone Project & Tạo môi trường ảo (Virtual Environment)
Môi trường ảo giúp các thư viện của dự án không bị xung đột với máy tính.

Mở Terminal/Command Prompt tại thư mục dự án.

Tạo môi trường ảo:
python -m venv venv

Kích hoạt môi trường ảo:
Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate

Sau khi kích hoạt, bạn sẽ thấy chữ (venv) hiện đầu dòng lệnh.

4. Cài đặt các thư viện cần thiết
Chúng ta sử dụng 2 thư viện chính là selenium và webdriver-manager. Chạy lệnh sau để cài đặt:
pip install selenium webdriver-manager

5. Cấu trúc thư mục dự án
Mọi người chú ý đẩy file vào đúng thư mục để nhóm trưởng dễ tổng hợp:
activity-1: Script thô ban đầu + Log chat AI.
activity-2: Code sau khi đã chuyển sang POM.
activity-3: Báo cáo review code.
...

6. Cách chạy thử script
Đảm bảo đã kích hoạt venv.
Di chuyển vào thư mục chứa file test (ví dụ activity-1).
Chạy lệnh:
python test_login.py