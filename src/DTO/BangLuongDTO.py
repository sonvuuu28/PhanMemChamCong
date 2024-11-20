class BangLuongDTO:
    def __init__(self, MaBangLuong, Thang, Nam, PhuCap, KhauTru, HeSoLuong, TongTien, MaNhanVien, deleteStatus, SoGioLam):
        self._MaBangLuong = MaBangLuong  # Mã bảng lương (Primary Key)
        self._Thang = Thang  # Tháng tính lương
        self._Nam = Nam  # Năm tính lương
        self._SoGioLam = SoGioLam  #Số giừo làm (kiểu DECIMAL)
        self._PhuCap = PhuCap  # Phụ cấp (kiểu DECIMAL)
        self._KhauTru = KhauTru  # Khấu trừ (kiểu DECIMAL)
        self._HeSoLuong = HeSoLuong  # Hệ số lương (kiểu DECIMAL)
        self._TongTien = TongTien  # Tổng tiền lương (kiểu DECIMAL)
        self._MaNhanVien = MaNhanVien  # Mã nhân viên (Foreign Key tới bảng NhanVien)
        self._deleteStatus = deleteStatus  # Trạng thái xóa (bit)

    # Getter và Setter cho MaBangLuong
    def get_MaBangLuong(self):
        return self._MaBangLuong

    def set_MaBangLuong(self, MaBangLuong):
        self._MaBangLuong = MaBangLuong

    # Getter và Setter cho Thang
    def get_Thang(self):
        return self._Thang

    def set_Thang(self, Thang):
        self._Thang = Thang

    # Getter và Setter cho Nam
    def get_Nam(self):
        return self._Nam

    def set_Nam(self, Nam):
        self._Nam = Nam

    # Getter và Setter cho SoGioLam
    def get_SoGioLam(self):
        return self._SoGioLam

    def set_SoGioLam(self, SoGioLam):
        self._SoGioLam = SoGioLam

    # Getter và Setter cho PhuCap
    def get_PhuCap(self):
        return self._PhuCap

    def set_PhuCap(self, PhuCap):
        self._PhuCap = PhuCap

    # Getter và Setter cho KhauTru
    def get_KhauTru(self):
        return self._KhauTru

    def set_KhauTru(self, KhauTru):
        self._KhauTru = KhauTru

    # Getter và Setter cho HeSoLuong
    def get_HeSoLuong(self):
        return self._HeSoLuong

    def set_HeSoLuong(self, HeSoLuong):
        self._HeSoLuong = HeSoLuong

    # Getter và Setter cho TongTien
    def get_TongTien(self):
        return self._TongTien

    def set_TongTien(self, TongTien):
        self._TongTien = TongTien

    # Getter và Setter cho MaNhanVien
    def get_MaNhanVien(self):
        return self._MaNhanVien

    def set_MaNhanVien(self, MaNhanVien):
        self._MaNhanVien = MaNhanVien

    # Getter và Setter cho deleteStatus
    def get_deleteStatus(self):
        return self._deleteStatus

    def set_deleteStatus(self, deleteStatus):
        self._deleteStatus = deleteStatus

    # Hàm display_info để hiển thị thông tin bảng lương
    def display_info(self):
        print(f"Mã Bảng Lương: {self.get_MaBangLuong()}")
        print(f"Tháng: {self.get_Thang()}")
        print(f"Năm: {self.get_Nam()}")
        print(f"Phụ Cấp: {self.get_PhuCap()}")
        print(f"Khấu Trừ: {self.get_KhauTru()}")
        print(f"Hệ Số Lương: {self.get_HeSoLuong()}")
        print(f"Tổng Tiền: {self.get_TongTien()}")
        print(f"Mã Nhân Viên: {self.get_MaNhanVien()}")
        print(f"Trạng Thái Xóa: {'Đã Xóa' if self.get_deleteStatus()==0 else 'Hoạt Động'}")

# # Ví dụ sử dụng
# bang_luong = BangLuongDTO("BL001", 10, 2024, 500.50, 100.00, 23.5, 1500.50, "NV001", False)
# bang_luong.display_info()
