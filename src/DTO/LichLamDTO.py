class LichLamDTO:
    def __init__(self, MaLich, MaNhanVien, MaCa, Ngay, deleteStatus):
        self._MaLich = MaLich  # Mã lịch làm (Primary Key)
        self._MaNhanVien = MaNhanVien  # Mã nhân viên (Foreign Key tới bảng NhanVien)
        self._MaCa = MaCa  # Mã ca làm (Foreign Key tới bảng CaLam)
        self._Ngay = Ngay  # Ngày làm việc (kiểu DATE)
        self._deleteStatus = deleteStatus  # Trạng thái xóa (bit)

    # Getter và Setter cho MaLich
    def get_MaLich(self):
        return self._MaLich

    def set_MaLich(self, MaLich):
        self._MaLich = MaLich

    # Getter và Setter cho MaNhanVien
    def get_MaNhanVien(self):
        return self._MaNhanVien

    def set_MaNhanVien(self, MaNhanVien):
        self._MaNhanVien = MaNhanVien

    # Getter và Setter cho MaCa
    def get_MaCa(self):
        return self._MaCa

    def set_MaCa(self, MaCa):
        self._MaCa = MaCa

    # Getter và Setter cho Ngay
    def get_Ngay(self):
        return self._Ngay

    def set_Ngay(self, Ngay):
        self._Ngay = Ngay

    # Getter và Setter cho deleteStatus
    def get_deleteStatus(self):
        return self._deleteStatus

    def set_deleteStatus(self, deleteStatus):
        self._deleteStatus = deleteStatus

    # Hàm display_info để hiển thị thông tin lịch làm
    def display_info(self):
        print(f"Mã Lịch Làm: {self.get_MaLich()}")
        print(f"Mã Nhân Viên: {self.get_MaNhanVien()}")
        print(f"Mã Ca: {self.get_MaCa()}")
        print(f"Ngày: {self.get_Ngay()}")
        print(f"Trạng Thái Xóa: {'Đã Xóa' if self.get_deleteStatus() else 'Hoạt Động'}")

# Ví dụ sử dụng
lich_lam = LichLamDTO("LICH001", "NV001", "CA001", "2024-10-21", False)
lich_lam.display_info()
