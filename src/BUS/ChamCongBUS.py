import os
import sys
from datetime import datetime

current_dir = os.path.dirname(os.path.abspath(__file__))
dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)
from NhanVienDTO import NhanVienDTO
from BangChamCongDTO import BangChamCongDTO

dao_dir = os.path.join(current_dir, '../DAO')
sys.path.append(dao_dir)
from NhanVienDAO import NhanVienDAO

class ChamCongBUS:
    def __init__(self):
        pass
    
    @staticmethod
    def getInstance():
        return ChamCongBUS()
    
    def check_in_insert_BCC(self, MaNhanVien):
        current_date = datetime.now().strftime('%Y-%m-%d') 
        current_time = datetime.now().strftime('%H:%M:%S')
        
        MaBCC_auto = NhanVienDAO.getInstance().tao_BangChamCong()
        bang_cham_cong = BangChamCongDTO(MaBCC_auto, current_time, current_time, current_date, 1, MaNhanVien, True)
        NhanVienDAO.getInstance().insert_BangChamCong(bang_cham_cong)
        
    def check_out_insert_BCC(self, MaNhanVien):
        current_date = datetime.now().strftime('%Y-%m-%d') 
        current_time = datetime.now().strftime('%H:%M:%S')
        
        if NhanVienDAO.getInstance().update_BangChamCong_checkOut(current_time, MaNhanVien) == 0:
            MaBCC_auto = NhanVienDAO.getInstance().tao_BangChamCong()
            bang_cham_cong = BangChamCongDTO(MaBCC_auto, current_time, current_time, current_date, 1, MaNhanVien, True)
            NhanVienDAO.getInstance().insert_BangChamCong(bang_cham_cong)
            
        
def test():
    ChamCongBUS.getInstance().check_in_insert_BCC("NV001")
    

if __name__ == "__main__":
    test()
    # pass