class NhanVienDTO:
    def __init__(self, MaNhanVien, Ten, NgaySinh, GioiTinh, DiaChi, SDT, ChucVu, HinhAnh, Status):
        self._MaNhanVien = MaNhanVien  # Mã nhân viên (Primary Key)
        self._Ten = Ten  # Tên nhân viên
        self._NgaySinh = NgaySinh  # Ngày sinh
        self._GioiTinh = GioiTinh  # Giới tính
        self._DiaChi = DiaChi  # Địa chỉ
        self._SDT = SDT  # Số điện thoại
        self._ChucVu = ChucVu  # Chức vụ (có thể null)
        self._HinhAnh = HinhAnh
        self._Status = Status  # Trạng thái xóa (bit)
        
    # def __init__(self, MaNhanVien):
    #     self._MaNhanVien = MaNhanVien

    # Getter và Setter cho MaNhanVien
    def get_MaNhanVien(self):
        return self._MaNhanVien

    def set_MaNhanVien(self, MaNhanVien):
        self._MaNhanVien = MaNhanVien

    # Getter và Setter cho Ten
    def get_Ten(self):
        return self._Ten

    def set_Ten(self, Ten):
        self._Ten = Ten

    # Getter và Setter cho NgaySinh
    def get_NgaySinh(self):
        return self._NgaySinh

    def set_NgaySinh(self, NgaySinh):
        self._NgaySinh = NgaySinh

    # Getter và Setter cho GioiTinh
    def get_GioiTinh(self):
        return self._GioiTinh

    def set_GioiTinh(self, GioiTinh):
        self._GioiTinh = GioiTinh

    # Getter và Setter cho DiaChi
    def get_DiaChi(self):
        return self._DiaChi

    def set_DiaChi(self, DiaChi):
        self._DiaChi = DiaChi

    # Getter và Setter cho SDT
    def get_SDT(self):
        return self._SDT

    def set_SDT(self, SDT):
        self._SDT = SDT

    # Getter và Setter cho ChucVu
    def get_ChucVu(self):
        return self._ChucVu

    def set_ChucVu(self, ChucVu):
        self._ChucVu = ChucVu
        
    def get_HinhAnh(self):
        return self._HinhAnh

    def set_HinhAnh(self, HinhAnh):
        self._HinhAnh = HinhAnh

    # Getter và Setter cho Status
    def get_Status(self):
        return self._Status

    def set_Status(self, Status):
        self._Status = Status

    # Hàm display_info để hiển thị thông tin nhân viên
    def display_info(self):
        print(f"Mã Nhân Viên: {self.get_MaNhanVien()}")
        print(f"Tên: {self.get_Ten()}")
        print(f"Ngày Sinh: {self.get_NgaySinh()}")
        print(f"Giới Tính: {self.get_GioiTinh()}")
        print(f"Địa Chỉ: {self.get_DiaChi()}")
        print(f"Số Điện Thoại: {self.get_SDT()}")
        print(f"Chức Vụ: {self.get_ChucVu()}")
        print(f"Hình Ảnh: {self.get_HinhAnh()}")
        print(f"Trạng Thái: {'Hoạt Động' if self.get_Status() else 'Nghỉ Làm'}")

# # Ví dụ sử dụng
# nhan_vien = NhanVienDTO("NV001", "Nguyễn Văn A", "1990-01-01", "Nam", "123 Đường A", "0900123456", "Quản lý", "anh.png",False)
# nhan_vien.display_info()
