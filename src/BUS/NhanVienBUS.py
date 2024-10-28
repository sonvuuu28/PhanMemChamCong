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
def test():
    nv_bus = NhanVienBUS.getInstance()
    # nv_bus.list()
    # nv_bus.delete('nv002')
    nv = NhanVienDTO("'hell0aaaáao1ss11'", "Trần Thị B", "2000-01-28", "Nữ","12 An Dương Vương", "0285314097","Nhân Viên","anh1.png", True)
    nv_bus.insert(nv)

if __name__ == "__main__":
    # test()
    pass