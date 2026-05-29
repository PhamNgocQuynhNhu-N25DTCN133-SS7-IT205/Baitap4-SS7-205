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