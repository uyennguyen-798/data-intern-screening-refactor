from functions import (duong_ke_lon, them_ung_vien, xem_danh_sach, thong_ke, tim_ung_vien)
duong_ke_lon()
print("HỆ THỐNG SÀNG LỌC DATA INTERN".center(50))
duong_ke_lon()
while True:
    print()
    print("1. Thêm ứng viên")
    print("2. Xem danh sách")
    print("3. Thống kê")
    print("4. Tìm ứng viên")
    print("5. Thoát")
    print()
    lua_chon = int(input("Nhập lựa chọn: "))
    if lua_chon == 1:
        them_ung_vien()
    elif lua_chon == 2:
        xem_danh_sach()
    elif lua_chon == 3:
        thong_ke()
    elif lua_chon == 4:
        tim_ung_vien()
    elif lua_chon == 5:
        break
    else:
        print()
        print("Lựa chọn không hợp lệ, vui lòng nhập lại.")
