import os
import sys

from datetime import date

current_dir = os.path.dirname(os.path.abspath(__file__))

bl_bus_dir = os.path.join(current_dir, '../BUS')
sys.path.append(bl_bus_dir)

dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)
from LichLamDTO import LichLamDTO

dao_dir = os.path.join(current_dir, '../DAO')
sys.path.append(dao_dir)
from LichLamDAO import LichLamDAO

class LichLamBUS:
    def __init__(self):
        pass
    
    @staticmethod
    def getInstance():
        return LichLamBUS()
    
    def getallbydate(self, start, end):
        ll_dao = LichLamDAO.getInstance()
        data = ll_dao.listbydate(start, end)
        return None if len(data) == 0 else data
    
    def getbyid(self, id):
        ll_dao = LichLamDAO.getInstance()
        data = ll_dao.TimKiem_Theo_Ma(id)
        return None if not data else data
    
    def update(self, lichlam):
        ll_dao = LichLamDAO.getInstance()
        check = ll_dao.update(lichlam)
        rs = (1,"Cập nhật lịch làm thành công") if check == 1 else (0, "Cập nhật lịch làm thất bại")
        return rs

    def tao_ma(self):
        ll_dao = LichLamDAO.getInstance()
        return ll_dao.tao_MaLichLam()     

    def them_lich(self, lich):
        ll_dao = LichLamDAO.getInstance()
        check = ll_dao.insert(lich)
        rs = (1,"Thêm lịch làm thành công") if check == 1 else (0, "Thêm lịch làm thất bại")
        return rs

def test():
    ngay_bat_dau = date(2024, 11, 4)
    ngay_ket_thuc = date(2024, 11, 7)

    list = LichLamBUS.getInstance().getallbydate(ngay_bat_dau, ngay_ket_thuc)

    for item in list:
        item.display_info()
if __name__ == "__main__":
    test()