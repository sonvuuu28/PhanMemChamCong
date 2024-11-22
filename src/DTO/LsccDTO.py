class LsccDTO:
    # def __init__(self, MaCa, Ngay, ThoiGianVao, ThoiGianRa, TinhTrang, Ten):
    #     self.MaCa = MaCa
    #     self.Ngay = Ngay
    #     self.ThoiGianVao = ThoiGianVao
    #     self.ThoiGianRa = ThoiGianRa
    #     self.TinhTrang = TinhTrang
    #     self.Ten = Ten

    def __init__(self, MaBCC, Ngay, ThoiGianVao, ThoiGianRa, TinhTrang, MaNhanVien, Status):
        self.MaBCC = MaBCC
        self.ThoiGianVao = ThoiGianVao
        self.ThoiGianRa = ThoiGianRa
        self.Ngay = Ngay
        self.TinhTrang = TinhTrang
        self.MaNhanVien = MaNhanVien
        self.Status = Status
    
    def get_MaBCC(self):
        return self.MaBCC
    
    def get_Ngay(self):
        return self.Ngay
    
    def get_ThoiGianVao(self):
        return self.ThoiGianVao
    
    def get_ThoiGianRa(self):
        return self.ThoiGianRa
    
    def get_TinhTrang(self):
        return self.TinhTrang
    
    def get_MaNhanVien(self):
        return self.MaNhanVien
    
    def get_Status(self):
        return self.Status
    
    # thêm tên nhân viên vào đây
    # def get_Ten(self):
    #     return self.Ten
    
    def __str__(self):
        return f"MaBCC: {self.MaBCC}, Ngay: {self.Ngay}, ThoiGianVao: {self.ThoiGianVao}, ThoiGianRa: {self.ThoiGianRa}, TinhTrang: {self.TinhTrang}, NhanVien: {self.MaNhanVien}, Status: {self.Status}"