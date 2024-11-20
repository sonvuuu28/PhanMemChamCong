import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)
from NhanVienDTO import NhanVienDTO

dao_dir = os.path.join(current_dir, '../DAO')
sys.path.append(dao_dir)
from NhanVienDAO import NhanVienDAO

class NhanVienBUS:
    def __init__(self):
        pass
    
    @staticmethod
    def getInstance():
        return NhanVienBUS()
    
    def getById(self, id):
        employee_dao = NhanVienDAO.getInstance()
        return employee_dao.TimKiem_Theo_Ma(id)
    
    def list(self):
        employee_dao = NhanVienDAO.getInstance()
        danh_sach_nv = employee_dao.list()
        return danh_sach_nv
        
    def insert(self, nv):
        employee_dao = NhanVienDAO.getInstance()
        check = employee_dao.insert(nv)
        noti = "Thêm Thành Công" if check == 1 else "Thêm Thất Bại, mã bị trùng lặp"
        return noti
         
    def delete(self, id):
        employee_dao = NhanVienDAO.getInstance()
        check = employee_dao.delete(id)
        noti = "Xóa Thành Công" if check == 1 else "Xóa Thất Bại, mã không tồn tại"
        return noti
    
    def update(self, nv):
        nv_dao = NhanVienDAO.getInstance()
        check = nv_dao.update(nv)
        noti = "Sửa Thành Công" if check == 1 else "Sửa Thất Bại, mã không tồn tại"
        return noti
  
    def TimKiem_Theo_MaNhanVien(self, Ma):
        dto = NhanVienDAO.getInstance().TimKiem_Theo_Ma(Ma)
        return dto
    
    def TimKiem_Theo_Anh(self, Anh):
        dto = NhanVienDAO.getInstance().TimKiem_Theo_Anh(Anh)
        return dto

def test():
    ten = NhanVienBUS.getInstance().TimKiem_Theo_Anh("NV001.png")

if __name__ == "__main__":
    test()
    # pass