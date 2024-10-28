class GhiChuDTO:
    def __init__(self, MaGC, Ngay, NoiDung):
        self._MaGC = MaGC  # Sử dụng biến private với dấu gạch dưới
        self._Ngay = Ngay
        self._NoiDung = NoiDung

    # Getter và Setter cho MaGC
    def get_MaGC(self):
        return self._MaGC

    def set_MaGC(self, MaGC):
        self._MaGC = MaGC

    # Getter và Setter cho Ngay
    def get_Ngay(self):
        return self._Ngay

    def set_Ngay(self, Ngay):
        self._Ngay = Ngay

    # Getter và Setter cho NoiDung
    def get_NoiDung(self):
        return self._NoiDung

    def set_NoiDung(self, NoiDung):
        self._NoiDung = NoiDung

    # Hàm display_info để hiển thị các thuộc tính
    def display_info(self):
        print(f"Mã Ghi Chú: {self.get_MaGC()}")
        print(f"Ngày: {self.get_Ngay()}")
        print(f"Nội Dung: {self.get_NoiDung()}")

# Ví dụ sử dụng
ghi_chu = GhiChuDTO("GC001", "2024-10-21", "Nội dung ghi chú ban đầu")
ghi_chu.display_info()
