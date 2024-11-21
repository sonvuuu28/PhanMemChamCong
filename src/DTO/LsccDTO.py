class LsccDTO:
    # def __init__(self, MaCa, Ngay, ThoiGianVao, ThoiGianRa, TinhTrang, Ten):
    #     self.MaCa = MaCa
    #     self.Ngay = Ngay
    #     self.ThoiGianVao = ThoiGianVao
    #     self.ThoiGianRa = ThoiGianRa
    #     self.TinhTrang = TinhTrang
    #     self.Ten = Ten

    def __init__(self, MaCa, Ngay, ThoiGianVao, ThoiGianRa, TinhTrang):
        self.MaCa = MaCa
        self.Ngay = Ngay
        self.ThoiGianVao = ThoiGianVao
        self.ThoiGianRa = ThoiGianRa
        self.TinhTrang = TinhTrang
    
    def get_MaCa(self):
        return self.MaCa
    
    def get_Ngay(self):
        return self.Ngay
    
    def get_ThoiGianVao(self):
        return self.ThoiGianVao
    
    def get_ThoiGianRa(self):
        return self.ThoiGianRa
    
    def get_TinhTrang(self):
        return self.TinhTrang
    
    # thêm tên nhân viên vào đây
    # def get_Ten(self):
    #     return self.Ten
    
    def __str__(self):
        return f"MaCa: {self.MaCa}, Ngay: {self.Ngay}, ThoiGianVao: {self.ThoiGianVao}, ThoiGianRa: {self.ThoiGianRa}, TinhTrang: {self.TinhTrang},"
