import os
import sys


current_dir = os.path.dirname(os.path.abspath(__file__))

bl_bus_dir = os.path.join(current_dir, '../BUS')
sys.path.append(bl_bus_dir)
from NhanVienBUS import NhanVienBUS
from BangLuongBUS import BangLuongBUS

dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)
from BangChamCongDTO import BangChamCongDTO
from BangLuongDTO import BangLuongDTO

dao_dir = os.path.join(current_dir, '../DAO')
sys.path.append(dao_dir)
from BangChamCongDAO import BangChamCongDAO
from BangLuongDAO import  BangLuongDAO

class BangChamCongBUS:
    def __init__(self):
        pass
    
    @staticmethod
    def getInstance():
        return BangChamCongBUS()
        
    def getByNgay(self, Thang, Nam):
        cong_dao = BangChamCongDAO.getInstance()
        data = cong_dao.selectByNgay(Thang, Nam)
        return None if not data else data

    def getSoGioNV(self, MaNhanVien, Thang, Nam):
        cong_dao = BangChamCongDAO.getInstance()
        data=cong_dao.selectByNVAndDate(MaNhanVien, Thang, Nam)

        return None if not data else data
    
    def tinhluong(self, thang, nam):
        cong_dao = BangChamCongDAO.getInstance()



def test():
    tk_bus = BangChamCongBUS.getInstance()


    ls = tk_bus.getByNgay(10,2024)

    for item in ls:
        print(item.display_info())

if __name__ == "__main__":
    test()
    # pass