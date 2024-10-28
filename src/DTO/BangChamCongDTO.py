class BangChamCongDTO:
    def __init__(self, MaBCC, ThoiGianVao, ThoiGianRa, Ngay, TinhTrang, MaNhanVien, deleteStatus):
        self._MaBCC = MaBCC  # Mã bảng chấm công (Primary Key)
        self._ThoiGianVao = ThoiGianVao  # Thời gian vào (kiểu time)
        self._ThoiGianRa = ThoiGianRa  # Thời gian ra (kiểu time)
        self._Ngay = Ngay  # Ngày chấm công (kiểu DATE)
        self._TinhTrang = TinhTrang  # Tình trạng (nvarchar 50)
        self._MaNhanVien = MaNhanVien  # Mã nhân viên (Foreign Key tới bảng NhanVien)
        self._deleteStatus = deleteStatus  # Trạng thái xóa (bit)

    # Getter và Setter cho MaBCC
    def get_MaBCC(self):
        return self._MaBCC

    def set_MaBCC(self, MaBCC):
        self._MaBCC = MaBCC

    # Getter và Setter cho ThoiGianVao
    def get_ThoiGianVao(self):
        return self._ThoiGianVao

    def set_ThoiGianVao(self, ThoiGianVao):
        self._ThoiGianVao = ThoiGianVao

    # Getter và Setter cho ThoiGianRa
    def get_ThoiGianRa(self):
        return self._ThoiGianRa

    def set_ThoiGianRa(self, ThoiGianRa):
        self._ThoiGianRa = ThoiGianRa

    # Getter và Setter cho Ngay
    def get_Ngay(self):
        return self._Ngay

    def set_Ngay(self, Ngay):
        self._Ngay = Ngay

    # Getter và Setter cho TinhTrang
    def get_TinhTrang(self):
        return self._TinhTrang

    def set_TinhTrang(self, TinhTrang):
        self._TinhTrang = TinhTrang

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

    # Hàm display_info để hiển thị thông tin bảng chấm công
    def display_info(self):
        print(f"Mã Bảng Chấm Công: {self.get_MaBCC()}")
        print(f"Thời Gian Vào: {self.get_ThoiGianVao()}")
        print(f"Thời Gian Ra: {self.get_ThoiGianRa()}")
        print(f"Ngày: {self.get_Ngay()}")
        print(f"Tình Trạng: {self.get_TinhTrang()}")
        print(f"Mã Nhân Viên: {self.get_MaNhanVien()}")
        print(f"Trạng Thái Xóa: {'Đã Xóa' if self.get_deleteStatus() else 'Hoạt Động'}")

# Ví dụ sử dụng
bang_cham_cong = BangChamCongDTO("BCC001", "08:00:00", "17:00:00", "2024-10-21", "Đi làm", "NV001", False)
bang_cham_cong.display_info()
