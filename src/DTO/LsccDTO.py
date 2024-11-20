class LsccDTO:
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
