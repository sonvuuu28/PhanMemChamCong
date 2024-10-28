class CaLamDTO:
    def __init__(self, MaCa, TenCa, ThoiGianVao, ThoiGianRa, status):
        self._MaCa = MaCa  # Mã ca làm việc (để private)
        self._TenCa = TenCa  # Tên ca làm việc
        self._ThoiGianVao = ThoiGianVao  # Thời gian vào ca
        self._ThoiGianRa = ThoiGianRa  # Thời gian ra ca
        self._status = status  # Trạng thái ca làm

    # Getter và Setter cho MaCa
    def get_MaCa(self):
        return self._MaCa

    def set_MaCa(self, MaCa):
        self._MaCa = MaCa

    # Getter và Setter cho TenCa
    def get_TenCa(self):
        return self._TenCa

    def set_TenCa(self, TenCa):
        self._TenCa = TenCa

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

    # Getter và Setter cho status
    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    # Hàm display_info để hiển thị thông tin ca làm
    def display_info(self):
        print(f"Mã Ca Làm: {self.get_MaCa()}")
        print(f"Tên Ca Làm: {self.get_TenCa()}")
        print(f"Thời Gian Vào: {self.get_ThoiGianVao()}")
        print(f"Thời Gian Ra: {self.get_ThoiGianRa()}")
        print(f"Trạng Thái: {self.get_status()}")

# Ví dụ sử dụng
ca_lam = CaLamDTO("CL001", "Ca Sáng", "08:00", "12:00", "Hoạt động")
ca_lam.display_info()
