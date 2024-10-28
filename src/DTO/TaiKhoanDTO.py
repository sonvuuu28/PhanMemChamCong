class TaiKhoanDTO:
    def __init__(self, MaTK, TenDangNhap, MatKhau, MaQuyen, MaNhanVien, Status):
        self._MaTK = MaTK  # Mã tài khoản (Primary Key)
        self._TenDangNhap = TenDangNhap  # Tên đăng nhập
        self._MatKhau = MatKhau  # Mật khẩu
        self._MaQuyen = MaQuyen  # Mã quyền (Foreign Key tới PhanQuyen)
        self._MaNhanVien = MaNhanVien  # Mã nhân viên (Foreign Key tới NhanVien)
        self._Status = Status  # Trạng thái xóa (bit)

    # Getter và Setter cho MaTK
    def get_MaTK(self):
        return self._MaTK

    def set_MaTK(self, MaTK):
        self._MaTK = MaTK

    # Getter và Setter cho TenDangNhap
    def get_TenDangNhap(self):
        return self._TenDangNhap

    def set_TenDangNhap(self, TenDangNhap):
        self._TenDangNhap = TenDangNhap

    # Getter và Setter cho MatKhau
    def get_MatKhau(self):
        return self._MatKhau

    def set_MatKhau(self, MatKhau):
        self._MatKhau = MatKhau

    # Getter và Setter cho MaQuyen
    def get_MaQuyen(self):
        return self._MaQuyen

    def set_MaQuyen(self, MaQuyen):
        self._MaQuyen = MaQuyen

    # Getter và Setter cho MaNhanVien
    def get_MaNhanVien(self):
        return self._MaNhanVien

    def set_MaNhanVien(self, MaNhanVien):
        self._MaNhanVien = MaNhanVien

    # Getter và Setter cho Status
    def get_Status(self):
        return self._Status

    def set_Status(self, Status):
        self._Status = Status

    # Hàm display_info để hiển thị thông tin tài khoản
    def display_info(self):
        print(f"Mã Tài Khoản: {self.get_MaTK()}")
        print(f"Tên Đăng Nhập: {self.get_TenDangNhap()}")
        print(f"Mật Khẩu: {self.get_MatKhau()}")
        print(f"Mã Quyền: {self.get_MaQuyen()}")
        print(f"Mã Nhân Viên: {self.get_MaNhanVien()}")
        print(f"Trạng Thái Xóa: {'Họat Động' if self.get_Status() else 'Đã Xóa'}")
