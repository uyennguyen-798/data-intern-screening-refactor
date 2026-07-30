def duong_ke_lon():
    print("=" * 50)
def duong_ke_nho():
    print("-" * 50)
def nhap_ho_ten():
    return input("Họ tên: ").upper()
def nhap_truong():
    return input("Trường: ").upper()
def nhap_nganh():
    return input("Ngành: ").strip().lower()
def nhap_ielts():
    while True:
        try:
            ielts = float(input("IELTS: "))
            if 0 <= ielts <= 9.0:
                print("Đã lưu điểm.")
                return ielts                
            else:
                print("Điểm không hợp lệ.")
        except ValueError:
            print("Vui lòng nhập số.")
def nhap_github():
    return input("GitHub: ")
def nhap_kaggle():
    return input("Kaggle: ")
def nhap_gpa():
    while True:
        try:
            gpa = float(input("GPA: "))
            if 0 <= gpa <= 4.0:
                print("Đã lưu điểm.")
                return gpa
            else:
                print("Điểm không hợp lệ.")
        except ValueError:
            print("Vui lòng nhập số.")
def nhap_python_skill():
    return input("Kỹ năng Python: ")
def hien_thi_ung_vien(ung_vien, stt):
    print()
    print(f"Ứng viên {stt}")
    print("Họ tên:", ung_vien["ho_ten"])
    print("Trường:", ung_vien["truong"])
    print("Ngành:", ung_vien["nganh"])
    print("IELTS:", ung_vien["ielts"])
    print("GitHub:", ung_vien["github"])
    print("Kaggle:", ung_vien["kaggle"])
    print("GPA:", ung_vien["gpa"])
    print("Kỹ năng Python:", ung_vien["python_skill"])
    if dat_vong_ho_so(ung_vien["ielts"], ung_vien["nganh"]):
        print("Kết quả: Đạt")
    else:
        print("Kết quả: Không đạt")
    duong_ke_nho()
danh_sach = []
nganh_tuyen = ["khoa học dữ liệu", "ai"]
def dat_vong_ho_so(ielts, nganh):
    return ielts >= 7.0 and nganh in nganh_tuyen
def them_ung_vien():
    print()
    ho_ten = nhap_ho_ten()
    truong = nhap_truong()
    nganh = nhap_nganh()
    ielts = nhap_ielts()
    github = nhap_github()
    kaggle = nhap_kaggle()
    gpa = nhap_gpa()
    python_skill = nhap_python_skill()
    ung_vien = {"ho_ten": ho_ten,
            "truong": truong,
            "nganh": nganh,
            "ielts": ielts,
            "github": github,
            "kaggle": kaggle,
            "gpa": gpa,
            "python_skill": python_skill}
    danh_sach.append(ung_vien)
    print("Đã lưu hồ sơ của", ung_vien["ho_ten"])
def xem_danh_sach():
    if not danh_sach:
        print()
        print("Chưa có ứng viên.")
    else:
        for stt, ung_vien in enumerate(danh_sach, start=1):
            hien_thi_ung_vien(ung_vien, stt)
def thong_ke():
    print()
    print(f"Tổng ứng viên: {len(danh_sach)}")
    tong_dat = 0
    for ung_vien in danh_sach:
        if dat_vong_ho_so(ung_vien["ielts"], ung_vien["nganh"]):
            tong_dat += 1
    print(f"Tổng ứng viên đạt: {tong_dat}")
    print(f"Tổng ứng viên không đạt: {len(danh_sach) - (tong_dat)}")
def tim_ung_vien():
    print()
    if not danh_sach:
        print("Chưa có ứng viên.")
    else:
        tim = input("Họ tên ứng viên cần tìm: ").upper()
        tim_thay = False
        for stt, ung_vien in enumerate(danh_sach, start=1):
            if tim == ung_vien["ho_ten"]:
                hien_thi_ung_vien(ung_vien, stt)
                tim_thay = True
                break
        if not tim_thay:
            print()
            print("Không tìm thấy ứng viên.")
