raw_registers = [
    {"name": "  Nguyen Van An  ", "email": "an.nguyen@gmail.com", "phone": "0987654321"},
    {"name": "Tran Thi Bich", "email": "bich_gmail.com", "phone": "0912345678"},
    {"name": "Le Hoang Cuong", "email": "cuong@rikkei.edu.vn", "phone": "0123456789"},
    {"name": "  Pham Minh Dung ", "email": "dung@gmail.com  ", "phone": "0355667788"}
]

orders = [
    {"id": "DH01", "total": "12500000", "discount_code": "VIP10", "is_vip": True},
    {"id": "DH02", "total": "450000", "discount_code": "INVALID", "is_vip": False},
    {"id": "DH03", "total": "ABC_ERROR", "discount_code": "", "is_vip": False},
    {"id": "DH04", "total": "8500000", "discount_code": "VIP20", "is_vip": True}
]

# Bài1:
def validate_registration_input(name, email, phone):
    name = name.strip()
    email = email.strip().lower()
    phone = phone.strip()
    errors = []
    if "@" not in email:
        errors.append("Thiếu '@'")
    if not phone.isdigit():
        errors.append("SĐT phải là số")
    elif len(phone) != 10:
        errors.append("SĐT phải có 10 số")
    elif not phone.startswith(("03", "05", "07", "08", "09")):
        errors.append("Sai đầu số VN")
    return name, email, phone, errors
print("===== Bài1 =====")
print("BÁO CÁO CHUẨN HÓA & VALIDATE THÔNG TIN ĐĂNG KÝ")
for i, student in enumerate(raw_registers, start=1):
    name, email, phone, errors = validate_registration_input(
        student["name"],
        student["email"],
        student["phone"]
    )
    if len(errors) == 0:
        print(f"[{i}] {name} | Email: {email} | SĐT: {phone} -> Trạng thái: HỢP LỆ")
    else:
        print(f"[{i}] {name} | Email: {email} | SĐT: {phone} -> Trạng thái: KHÔNG HỢP LỆ ({', '.join(errors)})")


# Bài2:
def safe_process_invoice(order_id, raw_total, discount_code, is_vip):
    try:
        total = float(raw_total)
        # Chiết khấu
        discount = 0
        if is_vip:
            if discount_code == "VIP10":
                discount = total * 0.10
            elif discount_code == "VIP20":
                discount = total * 0.20
        amount_after_discount = total - discount

        # VAT 10%
        vat = amount_after_discount * 0.10
        final_total = amount_after_discount + vat

        # Phân loại hóa đơn
        if final_total >= 10000000:
            invoice_type = "HÓA ĐƠN LỚN (VIP)"
        else:
            invoice_type = "HÓA ĐƠN THƯỜNG"

        if discount > 0:
            print(
                f"[{order_id}] Tiền hàng: {total:,.0f} | "
                f"CK ({discount_code}): {discount:,.0f} | "
                f"VAT 10%: {vat:,.0f} -> "
                f"Tổng: {final_total:,.0f} VNĐ [{invoice_type}]"
            )
        else:
            print(
                f"[{order_id}] Tiền hàng: {total:,.0f} | "
                f"CK: 0 | "
                f"VAT 10%: {vat:,.0f} -> "
                f"Tổng: {final_total:,.0f} VNĐ [{invoice_type}]"
            )
    except ValueError:
        print(
            f"Xử lý lỗi [{order_id}]: "
            f"Số tiền '{raw_total}' không hợp lệ! Bỏ qua đơn hàng."
        )
print("\n===== Bài2 =====")
print("BÁO CÁO XỬ LÝ HÓA ĐƠN AN TOÀN (TRY-EXCEPT & VAT)")
for order in orders:
    safe_process_invoice(
        order["id"],
        order["total"],
        order["discount_code"],
        order["is_vip"]
    )
