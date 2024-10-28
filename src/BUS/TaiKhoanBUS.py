import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)
from TaiKhoanDTO import TaiKhoanDTO

dao_dir = os.path.join(current_dir, '../DAO')
sys.path.append(dao_dir)
from TaiKhoanDAO import TaiKhoanDAO

class TaiKhoanBUS:
    def __init__(self):
        pass
    
    @staticmethod
    def getInstance():
        return TaiKhoanBUS()
        
    def insert(self, tk):
        tk_dao = TaiKhoanDAO.getInstance()
        check = tk_dao.insert(tk)
        noti = "Cấp tài khoản thành công" if check == 1 else "Cấp tài khoản thất bại, tài khoản đã được cấp"
        return noti
    
    def update(self, nv):
        tk_dao = TaiKhoanDAO.getInstance()
        check = tk_dao.update(nv)
        noti = "Sửa Thành Công" if check == 1 else "Sửa Thất Bại"
        return noti
    
def test():
    tk_bus = TaiKhoanBUS.getInstance()

if __name__ == "__main__":
    # test()
    pass