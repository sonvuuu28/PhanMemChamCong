# from Connection import Connection
# import pyodbc
# import os
# import sys
# # Lấy đường dẫn của thư mục hiện tại và thêm đường dẫn tới thư mục DTO
# current_dir = os.path.dirname(os.path.abspath(__file__))
# dto_dir = os.path.join(current_dir, '../DTO')
# sys.path.append(dto_dir)
# from CaLamDTO import CaLamDTO

# class CaLamDAO:
#     def __init__(self):
#         self.connection = Connection()

#     @staticmethod
#     def getInstance():
#         return CaLamDAO()
    
#     def insert(self, calam):
#         con = self.connection.getConnection()
#         cursor = con.cursor()
#         insert_query = '''INSERT INTO CaLam(MaCa, TenCa, ThoiGianVao, ThoiGianRa, Status) VALUES (?, ?, ?, ?, ?)'''
#         calam_data = (calam.get_MaCa(), calam.get_TenCa(), calam.get_ThoiGianVao(), calam.get_ThoiGianRa(), calam.get_Status())
#         try:
#             cursor.execute(insert_query, calam_data)
#             if cursor.rowcount > 0:  # Kiểm tra số dòng bị ảnh hưởng bởi câu lệnh SQL
#                     print("Thêm ca làm thành công")
#                     con.commit()
#                     return 1
#             else:
#                     print("Thêm ca làm thất bại")
#                     con.rollback()
#                     return 0
#         except Exception as e:
#             print("Thêm ca làm thất bại except ", e)
#             con.rollback()
#             return 0

#     def update(self, calam):
#         con = self.connection.getConnection()
#         cursor = con.cursor()
#         update_query = '''UPDATE CaLam
#                           set TenCa = ?, 
#                           ThoiGianVao = ?, 
#                           ThoiGianRa = ?,
#                           Status = ?
#                           where MaCa = ?'''
#         calam_data = (calam.get_TenCa(), calam.get_ThoiGianVao(), calam.get_ThoiGianRa(), calam.get_Status(), calam.get_MaCa())
#         try:
#             cursor.execute(update_query, calam_data)
#             if cursor.rowcount > 0:  # Kiểm tra số dòng bị ảnh hưởng bởi câu lệnh SQL
#                     con.commit()
#                     print("Sửa ca làm thành công")
#                     return 1
#             else:
#                     print("Sửa ca làm thất bại")
#                     con.rollback()
#                     return 0
#         except Exception as e:
#             print("Sửa ca làm thất bại except ", e)
#             con.rollback()
#             return 0
            
#     def delete(self, id):
#         con = self.connection.getConnection()
#         cursor = con.cursor()
#         delete_query = '''UPDATE NhanVien
#                         SET Status = 0
#                         WHERE MaNhanVien = ? and Status = 1'''
#         calam_data = (id)
        
#         try:
#             cursor.execute(delete_query, calam_data)
#             rows_affected = cursor.rowcount  # Số hàng bị ảnh hưởng
            
#             if rows_affected > 0:
#                 con.commit()
#                 print("Xóa ca làm thành công")
#                 return 1
#             else:
#                 con.rollback()
#                 print("Ca làm không tồn tại hoặc không thể xóa")
#                 return 0
#         except pyodbc.Error as e:
#             print("Xóa ca làm thất bại")
#             con.rollback()
#             return 0
            
#     def TimKiem_Theo_Ma(self, Ma):
#         con = self.connection.getConnection()
#         cursor = con.cursor()
        
#         # Truy vấn tìm kiếm theo MaNhanVien
#         query = "SELECT * FROM CaLam WHERE MaCa=?"
        
#         try:
#             cursor.execute(query, Ma)
#             result = cursor.fetchone()  # Lấy kết quả đầu tiên
            
#             if result:
#                 # Gán kết quả truy vấn vào đối tượng CaLamDTO
#                 ca_lam = CaLamDTO(
#                     MaCa=result[0],  # Mã ca
#                     TenCa=result[1],          # Tên ca
#                     ThoiGianVao=result[2],      # H vào ca
#                     ThoiGianRa=result[3],      # H ra ca
#                     Status=result[4]         # Trạng thái xóa
#                 )
#                 return ca_lam  # Trả về đối tượng CaLamDTO
#             else:
#                 print(f"Không tìm thấy ca làm với mã: {Ma}")
#                 return None  # Trả về None nếu không tìm thấy

#         except pyodbc.Error as e:
#             print("Lỗi khi tìm kiếm ca làm:")
#             return None
        
#     def list(self):
#         con = self.connection.getConnection()
#         cursor = con.cursor()
#         cursor.execute('SELECT * FROM CaLam where Status=1')

#         danh_sach_ca_lam = []

#         for row in cursor:
#             # print(row)
#             ca_lam = CaLamDTO(
#                 MaCa=row[0],  # Mã ca làm
#                 TenCa=row[1],          # Tên ca làm
#                 ThoiGianVao=row[2],      # H vào ca
#                 ThoiGianRa=row[3],      # H ra ca
#                 Status=row[4]         # Trạng thái xóa
#             )
#             danh_sach_ca_lam.append(ca_lam)

#         return danh_sach_ca_lam

#     def tao_MaCaLam(self):
#         con = self.connection.getConnection()
#         cursor = con.cursor()
#         cursor.execute('select count(*) FROM CaLam')
#         ma = None
#         result = cursor.fetchone()
#         if result:
#             ma = result[0] + 1 
        
#         if ma < 10:
#             ma = 'CA00'+ str(ma) 
#         elif ma < 100 and ma > 9:
#             ma = 'CA0'+ str(ma)
#         else:
#             ma = 'CA'+ str(ma) 
            
#         return ma
    
   

from Connection import Connection
import pyodbc
import os
import sys
# Lấy đường dẫn của thư mục hiện tại và thêm đường dẫn tới thư mục DTO
current_dir = os.path.dirname(os.path.abspath(__file__))
dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)
from CaLamDTO import CaLamDTO

class CaLamDAO:
    def __init__(self):
        self.connection = Connection()

    @staticmethod
    def getInstance():
        return CaLamDAO()

    def insert(self, calam):
        con = self.connection.getConnection()
        cursor = con.cursor()
        insert_query = '''INSERT INTO CaLam(MaCa, TenCa, ThoiGianVao, ThoiGianRa, Status) VALUES (?, ?, ?, ?, ?)'''
        calam_data = (calam.get_MaCa(), calam.get_TenCa(), calam.get_ThoiGianVao(), 
                      calam.get_ThoiGianRa(), calam.get_Status())
        try:
            cursor.execute(insert_query, calam_data)
            if cursor.rowcount > 0:  # Kiểm tra số dòng bị ảnh hưởng bởi câu lệnh SQL
                con.commit()
                print("Thêm ca làm thành công")
                return 1
            else:
                print("Thêm ca làm thất bại")
                con.rollback()
                return 0
        except Exception as e:
            print("Thêm ca làm thất bại except", e)
            con.rollback()
            return 0

    def update(self, calam):
        con = self.connection.getConnection()
        cursor = con.cursor()
        update_query = '''UPDATE CaLam
                          set TenCa = ?, 
                          ThoiGianVao = ?,
                          ThoiGianRa = ?, 
                          Status = ? 
                          where MaCa = ?'''
        calam_data = (calam.get_TenCa(), calam.get_ThoiGianVao(), 
                      calam.get_ThoiGianRa(), calam.get_Status(), calam.get_MaCa())
        try:
            cursor.execute(update_query, calam_data)
            if cursor.rowcount > 0:
                con.commit()
                print("Sửa ca làm thành công")
                return 1
            else:
                print("Sửa ca làm thất bại")
                con.rollback()
                return 0
        except Exception as e:
            print("Sửa ca làm thất bại except", e)
            con.rollback()
            return 0

    def delete(self, id):
        con = self.connection.getConnection()
        cursor = con.cursor()
        delete_query = '''UPDATE CaLam
                          SET Status = 0
                          WHERE MaCa = ? and Status = 1'''
        calam_data = (id,)
        try:
            cursor.execute(delete_query, calam_data)
            rows_affected = cursor.rowcount  # Số hàng bị ảnh hưởng
            if rows_affected > 0:
                con.commit()
                print("Xóa ca làm thành công")
                return 1
            else:
                print("Ca làm không tồn tại hoặc không thể xóa")
                return 0
        except pyodbc.Error as e:
            print("Xóa ca làm thất bại", e)
            con.rollback()
            return 0

    def TimKiem_Theo_Ma(self, Ma):
        con = self.connection.getConnection()
        cursor = con.cursor()
        query = "SELECT * FROM CaLam WHERE MaCa=?"
        try:
            cursor.execute(query, Ma)
            result = cursor.fetchone()  # Lấy kết quả đầu tiên
            if result:
                ca_lam = CaLamDTO(
                    MaCa=result[0], 
                    TenCa=result[1],          
                    ThoiGianVao=result[2],     
                    ThoiGianRa=result[3],      
                    Status=result[4]       
                )
                return ca_lam
            else:
                print(f"Không tìm thấy ca làm với mã: {Ma}")
                return None
        except pyodbc.Error as e:
            print("Lỗi khi tìm kiếm ca làm:", e)
            return None

    def list(self):
        con = self.connection.getConnection()
        cursor = con.cursor()
        cursor.execute('SELECT * FROM CaLam where Status=1')
        danh_sach_ca_lam = []
        for row in cursor:
            ca_lam = CaLamDTO(
                MaCa=row[0], 
                TenCa=row[1],          
                ThoiGianVao=row[2],     
                ThoiGianRa=row[3],      
                Status=row[4]
            )  
            danh_sach_ca_lam.append(ca_lam)
        return danh_sach_ca_lam

    def tao_MaCa(self):
        con = self.connection.getConnection()
        cursor = con.cursor()
        cursor.execute('SELECT COUNT(*) FROM CaLam')
        result = cursor.fetchone()
        if result:
            ma = result[0] + 1
            # Generate MaCa based on the count
            if ma < 10:
                return f"CA00{ma}"
            elif ma < 100:
                return f"CA0{ma}"
            else:
                return f"CA{ma}"
        return "CA001"  # Default starting value

    def timKiem(self, ca):
        con = self.connection.getConnection()
        cursor = con.cursor()
        query = "SELECT * FROM CaLam WHERE MaCa LIKE ? AND TenCa LIKE ? AND ThoiGianVao LIKE ? AND ThoiGianRa LIKE ? AND Status = 1"
        ca_data = ('%' + ca.get_MaCa() + '%', '%' + ca.get_TenCa() + '%', '%' + ca.get_ThoiGianVao() + '%',
                   '%' + ca.get_ThoiGianRa() + '%')
        danh_sach_ca_lam = []
        cursor.execute(query, ca_data)
        results = cursor.fetchall()  # Lấy tất cả kết quả
        for result in results:
            ca_lam = CaLamDTO(
                MaCa=result[0], 
                TenCa=result[1],          
                ThoiGianVao=result[2],     
                ThoiGianRa=result[3],      
                Status=result[4]
            )
            danh_sach_ca_lam.append(ca_lam)
        return danh_sach_ca_lam
        
def test():
    employee_dao = CaLamDAO.getInstance()
    # Test some methods here
    # Test insertion
    # ca_lam_insert = CaLamDTO("CA001", "Ca Sáng", "08:00", "16:00", 1)
    # employee_dao.insert(ca_lam_insert)

    # Test search by ID
    ca_lam = employee_dao.TimKiem_Theo_Ma("CA001")
    if ca_lam:
        print(ca_lam.get_TenCa())

if __name__ == "__main__":
    test()
