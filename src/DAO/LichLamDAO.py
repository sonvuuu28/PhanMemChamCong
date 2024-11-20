from Connection import Connection
import pyodbc
import os
import sys

from datetime import date


# Lấy đường dẫn của thư mục hiện tại và thêm đường dẫn tới thư mục DTO
current_dir = os.path.dirname(os.path.abspath(__file__))
dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)
from LichLamDTO import LichLamDTO

class LichLamDAO:
    def __init__(self):
        self.connection = Connection()

    @staticmethod
    def getInstance():
        return LichLamDAO()
    
     
    def insert(self, lichlam):
        con = self.connection.getConnection()
        cursor = con.cursor()
        insert_query = '''
            INSERT INTO LichLam(MaLich,MaNhanVien,MaCa,Ngay,Status)
            VALUES(?,?,?,?,?)
        '''
        lichlam_data = (lichlam.get_MaLich(),lichlam.get_MaNhanVien(), lichlam.get_MaCa(), lichlam.get_Ngay(), lichlam.get_deleteStatus())

        try:
            cursor.execute(insert_query, lichlam_data)
            if cursor.rowcount > 0:  # Kiểm tra số dòng bị ảnh hưởng bởi câu lệnh SQL
                    con.commit()
                    print("Thêm lịch làm thành công")
                    return 1
            else:
                    print("Thêm lịch làm thất bại")
                    con.rollback()
                    return 0
        except Exception as e:
            print("Thêm lịch làm thất bại except ", e)
            con.rollback()
            return 0
    

    def update(self, lichlam):
        con = self.connection.getConnection()
        cursor = con.cursor()
        update_query = '''UPDATE LichLam
                          set MaNhanVien = ?, 
                          MaCa = ?, 
                          Ngay = ?,
                          Status = ?
                          where MaLich = ?'''
        lichlam_data = (lichlam.get_MaNhanVien(), lichlam.get_MaCa(), lichlam.get_Ngay(), lichlam.get_deleteStatus(), lichlam.get_MaLich())
        try:
            cursor.execute(update_query, lichlam_data)
            if cursor.rowcount > 0:  # Kiểm tra số dòng bị ảnh hưởng bởi câu lệnh SQL
                    con.commit()
                    print("Sửa lịch làm thành công")
                    return 1
            else:
                    print("Sửa lịch làm thất bại")
                    con.rollback()
                    return 0
        except Exception as e:
            print("Sửa lịch làm thất bại except ", e)
            con.rollback()
            return 0
    
    def TimKiem_Theo_Ma(self, Ma):
        con = self.connection.getConnection()
        cursor = con.cursor()
        
        # Truy vấn tìm kiếm theo MaNhanVien
        query = "SELECT * FROM LichLam WHERE MaLich=?"
        
        try:
            cursor.execute(query, Ma)
            result = cursor.fetchone()  # Lấy kết quả đầu tiên
            
            if result:
                # Gán kết quả truy vấn vào đối tượng CaLamDTO
                lich_lam = LichLamDTO(
                    MaLich=result[0],  # Mã ca làm
                    MaNhanVien=result[1],          # Tên ca làm
                    MaCa=result[2],      # H vào ca
                    Ngay=result[3],      # H ra ca
                    deleteStatus=result[4]         # Trạng thái xóa
                )
                return lich_lam  # Trả về đối tượng CaLamDTO
            else:
                print(f"Không tìm thấy lịch làm với mã: {Ma}")
                return None  # Trả về None nếu không tìm thấy

        except pyodbc.Error as e:
            print("Lỗi khi tìm kiếm lịch làm:")
            return None
        

    def listbydate(self, start, end):
        con = self.connection.getConnection()
        cursor = con.cursor()
        list_query = 'SELECT * FROM LichLam WHERE Ngay BETWEEN ? AND ? AND Status=?'
        data=(start, end, 1)
        try:
            cursor.execute(list_query, data)
            danh_sach_lich_lam = []

            for row in cursor:
                # print(row)
                lich_lam = LichLamDTO(
                    MaLich=row[0],  # Mã ca làm
                    MaNhanVien=row[1],          # Tên ca làm
                    MaCa=row[2],      # H vào ca
                    Ngay=row[3],      # H ra ca
                    deleteStatus=row[4]         # Trạng thái xóa
                )
                danh_sach_lich_lam.append(lich_lam)

        except pyodbc.Error as e:
            print("Lỗi rồi ", e)
    
        return danh_sach_lich_lam
        

    def list(self):
        con = self.connection.getConnection()
        cursor = con.cursor()
        cursor.execute('SELECT * FROM LichLam where Status=1')

        danh_sach_ca_lam = []

        for row in cursor:
            # print(row)
            ca_lam = CaLamDTO(
                MaCa=row[0],  # Mã ca làm
                TenCa=row[1],          # Tên ca làm
                ThoiGianVao=row[2],      # H vào ca
                ThoiGianRa=row[3],      # H ra ca
                Status=row[4]         # Trạng thái xóa
            )
            danh_sach_ca_lam.append(ca_lam)

        return danh_sach_ca_lam

    def tao_MaLichLam(self):
        con = self.connection.getConnection()
        cursor = con.cursor()
        cursor.execute('select count(*) FROM LichLam')
        ma = None
        result = cursor.fetchone()
        if result:
            ma = result[0] + 1 
        
        if ma < 10:
            ma = 'LL00'+ str(ma) 
        elif ma < 100 and ma > 9:
            ma = 'LL0'+ str(ma)
        else:
            ma = 'LL'+ str(ma) 
            
        return ma
    
    
if __name__ == '__main__':

    ngay_bat_dau = date(2024, 11, 4)
    ngay_ket_thuc = date(2024, 11, 7)

    list = LichLamDAO.getInstance().listbydate(ngay_bat_dau, ngay_ket_thuc)

    for item in list:
        item.display_info()