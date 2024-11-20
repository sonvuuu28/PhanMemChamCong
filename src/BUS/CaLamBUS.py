import os
import sys


current_dir = os.path.dirname(os.path.abspath(__file__))

bl_bus_dir = os.path.join(current_dir, '../BUS')
sys.path.append(bl_bus_dir)

dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)
from CaLamDTO import CaLamDTO

dao_dir = os.path.join(current_dir, '../DAO')
sys.path.append(dao_dir)
from CaLamDAO import CaLamDAO

class CaLamBUS:
    def __init__(self):
        pass
    
    @staticmethod
    def getInstance():
        return CaLamBUS()
    
    def getall(self):
        cl_dao = CaLamDAO.getInstance()
        data = cl_dao.list()
        return None if len(data) == 0 else data
    
    def getbyid(self, id):
        cl_dao = CaLamDAO.getInstance()
        data = cl_dao.TimKiem_Theo_Ma(id)
        return None if not data else data
    
    def add(self, calam):
        cl_dao = CaLamDAO.getInstance()
        check = cl_dao.insert(calam)
        noti = "Thêm ca làm thành công" if check == 1 else "Thêm ca làm thất bại"
        return [check,noti]
    

    def update(self, calam):
        cl_dao = CaLamDAO.getInstance()
        check = cl_dao.update(calam)
        noti = "Cập nhật ca làm thành công" if check == 1 else "Cập nhật ca làm thất bại"
        return [check,noti]
    
    def delete(self, calam):
        cl_dao = CaLamDAO.getInstance()
        check = cl_dao.delete(calam)
        noti = "Xoá ca làm thành công" if check == 1 else "Xoá ca làm thất bại"
        return [check,noti]
    
    def tao_ma(self):
        cl_dao = CaLamDAO.getInstance()
        return cl_dao.tao_MaCa()
# def test():
#     tk_bus = CaLamBUS.getInstance()


#     ls = tk_bus.getall()
#     for item in ls:
#         print(item.display_info())

# if __name__ == "__main__":
#     # test()
#     pass