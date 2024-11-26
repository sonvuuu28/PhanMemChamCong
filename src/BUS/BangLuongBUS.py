import os
import sys


current_dir = os.path.dirname(os.path.abspath(__file__))

bl_bus_dir = os.path.join(current_dir, '../BUS')
sys.path.append(bl_bus_dir)
from NhanVienBUS import NhanVienBUS

dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)
from BangLuongDTO import BangLuongDTO

dao_dir = os.path.join(current_dir, '../DAO')
sys.path.append(dao_dir)
from BangLuongDAO import BangLuongDAO

class BangLuongBUS:
    def __init__(self):
        pass
    
    @staticmethod
    def getInstance():
        return BangLuongBUS()
        
    def insert(self, luong):
        luong_dao = BangLuongDAO.getInstance()
        check = luong_dao.insert(luong)
        noti = "Thêm lương thành công" if check == 1 else "Thêm lương thất bại, đã có lỗi xảy ra"
        return [check, noti]
    
    def update(self, luong):
        luong_dao = BangLuongDAO.getInstance()
        check = luong_dao.update(luong)
        noti = "Cập nhật lương thành công" if check == 1 else "Cập nhật lương thất bại"
        return [check, noti]
    
    def getAll(self):
        luong_dao=BangLuongDAO.getInstance()
        data=luong_dao.selectAll()
        return None if not data else data

    def getByDate(self, month, year):
        luong_dao=BangLuongDAO.getInstance()
        data=luong_dao.selectByDate(month, year)

        return None if not data else data
        
    def taoma(self):
        return BangLuongDAO.getInstance().tao_MaBangLuong()

def test():
    tk_bus = BangLuongBUS.getInstance()


    ls = tk_bus.getAll()

    for item in ls:
        print(item.display_info())

if __name__ == "__main__":
    # test()
    pass