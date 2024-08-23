import math
def tinh_DHP(KT1, KT2, TP, DTCK):
# Tính ĐKTĐK
    DKTDK = 1 / 3 * (KT1 + KT2) + round(TP * 2) / 2  # Làm tròn TP đến 0.5

# Tính ĐQT
    DQT = DKTDK * 0.6 + 4
    print(f"Điểm quá trình (ĐQT) = {DQT}; theo quy tắc làm tròn thì ĐQT = {round(DQT*2)/2}")


# Tính ĐHP
    DHP = 0.5 * (round(DQT*2)/2 + round(DTCK * 2) / 2)  # Làm tròn DTCK đến 0.5

# Kiểm tra điều kiện trượt môn
    if DHP < 4:
        print("Bạn đã trượt môn do ĐHP < 4")
        print(f"ĐHP của bạn = {DHP}")
    else:
        print(f"Bạn đã qua môn với ĐHP = {DHP}")

def nhap_so(message, data_type=float):
    while True:
        try:
            giatri = data_type(input(message))
            return giatri
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")

# Nhập dữ liệu từ người dùng
KT1 = nhap_so("Nhập điểm KT1 (0 đến 15): ", int)
if not (0 <= KT1 <= 15):
    print("Điểm nhập vào không hợp lệ. Vui lòng kiểm tra lại.")
else:
    KT2 = nhap_so("Nhập điểm KT2 (0 đến 15): ", int)
    if not (0 <= KT2 <= 15):
        print("Điểm nhập vào không hợp lệ. Vui lòng kiểm tra lại.")
    else:
        TP = nhap_so("Nhập điểm TP (-1 <= TP <= 1): ")
        if not (-1 <= TP <= 1):
            print("Điểm nhập vào không hợp lệ. Vui lòng kiểm tra lại.")
        else:
            DTCK = nhap_so("Nhập ĐTCK: ")
            if not (0 <= DTCK <= 10):
                print("Điểm nhập vào không hợp lệ. Vui lòng kiểm tra lại.")
            elif DTCK < 3:
                print("Bạn đã trượt môn do ĐTCK < 3")
            else:
                tinh_DHP(KT1, KT2, TP, DTCK)

