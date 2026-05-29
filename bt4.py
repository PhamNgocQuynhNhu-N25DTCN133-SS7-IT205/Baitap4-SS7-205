# 1. PHÂN TÍCH INPUT / OUTPUT
# * Input: Số lượng phiếu đăng ký nhập từ bàn phím (Kiểu dữ liệu: String/Int). Chuỗi thông tin đăng ký thô của từng phiếu có dạng Họ tên | Khóa học | Mã học viên | Email phân cách bằng dấu '|' (Kiểu dữ liệu: String).
# * Output: Thông báo lỗi và dừng chương trình nếu số lượng phiếu không hợp lệ. Thông báo lỗi và bỏ qua phiếu nếu dữ liệu bị thiếu, mã quá ngắn hoặc email sai định dạng. In ra màn hình tiêu đề và các thông tin đã chuẩn hóa bao gồm Học viên, Khóa học, Mã học viên, Email và Mã xác nhận tự động tạo đối với các phiếu hợp lệ.

# 2. ĐỀ XUẤT GIẢI PHÁP (HÀM & PHƯƠNG THỨC SỬ DỤNG)
# * Kiểm tra số lượng phiếu: Dùng phương thức `.isdigit()` để xác định chuỗi nhập vào có phải số nguyên hay không và biểu thức so sánh để kiểm tra giá trị lớn hơn 0.
# * Tách và xử lý khoảng trắng thừa: Dùng phương thức `.split('|')` để phân rã chuỗi dữ liệu thành 4 phần độc lập. Sử dụng kỹ thuật `" ".join(chuỗi.split())` cho phần họ tên và tên khóa học để xóa bỏ triệt để mọi khoảng trắng thừa ở hai đầu và khoảng trắng bị lặp ở giữa các từ.
# * Chuẩn hóa chữ hoa chữ thường: Dùng `.title()` để viết hoa chữ cái đầu mỗi từ cho Họ tên và Khóa học. Dùng `.upper()` để viết hoa toàn bộ Mã học viên. Dùng `.lower()` để viết thường toàn bộ Địa chỉ email.
# * Kiểm tra tính hợp lệ của phiếu: Dùng hàm `len()` để kiểm tra số lượng phần tử sau khi split phải đủ 4 phần và kiểm tra độ dài Mã học viên sau chuẩn hóa phải lớn hơn hoặc bằng 5 ký tự. Dùng toán tử `in` kiểm tra sự tồn tại của ký tự `@` trong chuỗi email.
# * Tạo mã xác nhận tự động: Sử dụng phương thức `.replace(' ', '-')` trên tên khóa học đã viết hoa toàn bộ để thay thế khoảng trắng thành dấu gạch ngang, sau đó dùng F-string kết hợp với Mã học viên theo cấu trúc `{Mã_HV}_{Tên_Khóa_Học_Format}`.

# 3. THIẾT KẾ THUẬT TOÁN (LUỒNG CHƯƠNG TRÌNH)
# Bước 1: Khởi tạo vòng lặp chính để yêu cầu người dùng nhập vào số lượng phiếu đăng ký cần xử lý.
# Bước 2: Kiểm tra dữ liệu số lượng phiếu nhập vào. Nếu không phải là ký tự số hoặc giá trị nhỏ hơn hoặc bằng 0 thì in thông báo lỗi "Số lượng phiếu đăng ký không hợp lệ" và dùng lệnh `break` để kết thúc toàn bộ chương trình ngay lập tức.
# Bước 3: Sử dụng vòng lặp `for` chạy từ 0 đến số lượng phiếu hợp lệ vừa nhập để tiến hành xử lý tuần tự từng phiếu một.
# Bước 4: Nhận chuỗi thông tin đăng ký thô của phiếu hiện tại thông qua hàm `input()`.
# Bước 5: Tách chuỗi thô bằng dấu phân cách '|'. Kiểm tra nếu danh sách kết quả có độ dài nhỏ hơn 4 thì in ra thông báo "Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này" và dùng lệnh `continue` để nhảy sang lượt nhập của phiếu tiếp theo.
# Bước 6: Tiến hành làm sạch khoảng trắng và chuẩn hóa định dạng chữ cho từng thuộc tính: Họ tên dùng `.title()`, Khóa học dùng `.title()`, Mã học viên dùng `.upper()`, Email dùng `.lower()`.
# Bước 7: Kiểm tra độ dài Mã học viên sau chuẩn hóa. Nếu nhỏ hơn 5 ký tự thì in thông báo "Mã học viên không hợp lệ. Bỏ qua phiếu này" và gọi lệnh `continue`.
# Bước 8: Kiểm tra cấu trúc Email sau chuẩn hóa. Nếu không chứa ký tự `@` thì in thông báo "Email không hợp lệ. Bỏ qua phiếu này" và gọi lệnh `continue`.
# Bước 9: Thực hiện tạo Mã xác nhận bằng cách lấy Mã học viên kết hợp dấu gạch dưới và tên Khóa học đã được viết hoa toàn bộ kèm thay thế khoảng trắng bằng dấu gạch ngang.
# Bước 10: In ra màn hình khối văn bản kết quả hiển thị thông tin tiêu đề và 5 trường dữ liệu đã được xử lý chuẩn hóa thành công của phiếu đó.
# Bước 11: Sau khi vòng lặp `for` kết thúc việc duyệt qua toàn bộ số lượng phiếu, thực hiện gán cờ điều kiện để dừng vòng lặp `while` chính và đóng chương trình.

check_loop = True

while check_loop:
    user_input = input('Nhập số lượng phiếu đăng ký: ').strip()
    
    if not user_input.isdigit():
        print('Số lượng phiếu đăng ký không hợp lệ')
        break
        
    ticket = int(user_input)
    
    if ticket <= 0:
        print('Số lượng phiếu đăng ký không hợp lệ')
        break
        
    for i in range(ticket):
        registration_data = input('')
        
        parts = registration_data.split('|')
        
        if len(parts) < 4:
            print('Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này')
            continue
            
        raw_name = parts[0].strip()
        raw_course = parts[1].strip()
        raw_code = parts[2].strip()
        raw_email = parts[3].strip()
        
        student_name = " ".join(raw_name.split()).title()
        course = " ".join(raw_course.split()).title()
        student_code = raw_code.upper()
        
        if len(student_code) < 5:
            print('Mã học viên không hợp lệ. Bỏ qua phiếu này')
            continue
            
        email = raw_email.lower()
        
        if '@' not in email:
            print('Email không hợp lệ. Bỏ qua phiếu này')
            continue
            
        course_format_code = course.upper().replace(' ', '-')
        check_code = f"{student_code}_{course_format_code}"
        
        print("===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====")
        print(f"Học viên: {student_name}")
        print(f"Khóa học: {course}")
        print(f"Mã học viên: {student_code}")
        print(f"Email: {email}")
        print(f"Mã xác nhận: {check_code}")
        
    check_loop = False
