import os
import sys


current_dir = os.path.dirname(os.path.abspath(__file__))

bl_bus_dir = os.path.join(current_dir, '../BUS')
sys.path.append(bl_bus_dir)

dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)
from GhiChuDTO import GhiChuDTO

dao_dir = os.path.join(current_dir, '../DAO')
sys.path.append(dao_dir)
from GhiChuDAO import GhiChuDAO

class GhiChuBUS:
    def __init__(self):
        pass
    
    @staticmethod
    def getInstance():
        return GhiChuBUS()
        
    def add(self, ghichu):
        gc_dao = GhiChuDAO.getInstance()
        maGC=gc_dao.tao_MaGhiChu()
        ghichu.set_MaGC(maGC)
        check = gc_dao.insert(ghichu)
        noti = "Thêm ghi chú thành công" if check == 1 else "Thêm ghi chú thất bại, đã có lỗi xảy ra"
        return noti
    
    def update(self, ghichu):
        gc_dao = GhiChuDAO.getInstance()
        check = gc_dao.update(ghichu)
        noti = "Cập nhật ghi chú thành công" if check == 1 else "Cập nhật ghi chú thất bại"
        return noti
    
    def timkiemtheoMa(self, maGC):
        gc_dao = GhiChuDAO.getInstance()
        data = gc_dao.TimKiem_Theo_Ma(maGC)
        return None if not data else data
    
    
    def timkiemtheoNgay(self, ngay):
        gc_dao = GhiChuDAO.getInstance()
        data = gc_dao.TimKiem_Theo_Ngay(ngay)
        return None if not data else data
    

            

# def test():
#     tk_bus = GhiChuBUS.getInstance()


#     ls = tk_bus.getAll()

#     for item in ls:
#         print(item.display_info())

# if __name__ == "__main__":
#     # test()
#     pass