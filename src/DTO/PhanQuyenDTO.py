class PhanQuyenDTO:
    def __init__(self, MaQuyen, TenQuyen, QuyenChamCong, QuyenAdmin, QuyenNhanVien):
        self._MaQuyen = MaQuyen  # Mã quyền (Primary Key)
        self._TenQuyen = TenQuyen  # Tên quyền
        self._QuyenChamCong = QuyenChamCong  # Quyền chấm công (bit)
        self._QuyenAdmin = QuyenAdmin  # Quyền admin (bit)
        self._QuyenNhanVien = QuyenNhanVien  # Quyền nhân viên (bit)

    # Getter và Setter cho MaQuyen
    def get_MaQuyen(self):
        return self._MaQuyen

    def set_MaQuyen(self, MaQuyen):
        self._MaQuyen = MaQuyen

    # Getter và Setter cho TenQuyen
    def get_TenQuyen(self):
        return self._TenQuyen

    def set_TenQuyen(self, TenQuyen):
        self._TenQuyen = TenQuyen

    # Getter và Setter cho QuyenChamCong
    def get_QuyenChamCong(self):
        return self._QuyenChamCong

    def set_QuyenChamCong(self, QuyenChamCong):
        self._QuyenChamCong = QuyenChamCong

    # Getter và Setter cho QuyenAdmin
    def get_QuyenAdmin(self):
        return self._QuyenAdmin

    def set_QuyenAdmin(self, QuyenAdmin):
        self._QuyenAdmin = QuyenAdmin

    # Getter và Setter cho QuyenNhanVien
    def get_QuyenNhanVien(self):
        return self._QuyenNhanVien

    def set_QuyenNhanVien(self, QuyenNhanVien):
        self._QuyenNhanVien = QuyenNhanVien

    # Hàm display_info để hiển thị thông tin quyền
    def display_info(self):
        print(f"Mã Quyền: {self.get_MaQuyen()}")
        print(f"Tên Quyền: {self.get_TenQuyen()}")
        print(f"Quyền Chấm Công: {'Có' if self.get_QuyenChamCong() else 'Không'}")
        print(f"Quyền Admin: {'Có' if self.get_QuyenAdmin() else 'Không'}")
        print(f"Quyền Nhân Viên: {'Có' if self.get_QuyenNhanVien() else 'Không'}")

# Ví dụ sử dụng
nhan_vien = PhanQuyenDTO("Q001", "Quyền Quản Lý", True, False, False)
nhan_vien.display_info()
