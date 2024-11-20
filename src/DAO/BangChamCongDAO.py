from Connection import Connection
import pyodbc
import os
import sys

from datetime import datetime, timedelta
# Lấy đường dẫn của thư mục hiện tại và thêm đường dẫn tới thư mục DTO
current_dir = os.path.dirname(os.path.abspath(__file__))
dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)

from BangChamCongDTO import BangChamCongDTO

class BangChamCongDAO:
    def __init__(self):
        self.connection = Connection()

    @staticmethod
    def getInstance():
        return BangChamCongDAO()
    
    def selectAll(self):
        con = self.connection.getConnection()
        cursor = con.cursor()
        
        query = "SELECT * FROM BangChamCong WHERE Status=1"
        
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            
            if not results:
                print("Không có bản ghi nào trong bảng BangChamCong.")
                return None
        
            rs_list = []
            for item in results:
                cong = BangChamCongDTO(
                    MaBCC=item[0],
                    ThoiGianVao=item[1],
                    ThoiGianRa=item[2],
                    Ngay=item[3],
                    TinhTrang=item[4],
                    MaNhanVien=item[5],
                    deleteStatus=item[6]
                )
                rs_list.append(cong)

            return rs_list  # Trả về danh sách BangChamCongDTO
        
        except pyodbc.Error as e:
            print("Lỗi khi lấy danh sách lương:", e)
            return None

    def selectByNVAndDate(self, MaNhanVien, Thang, Nam):
        con = self.connection.getConnection()
        cursor = con.cursor()
        
        query = '''
            SELECT * FROM BangChamCong
            WHERE MaNhanVien = ?
            AND MONTH(Ngay) = ?
            AND YEAR(Ngay) = ?;
        '''
        data=(MaNhanVien, Thang, Nam)
        try:
            cursor.execute(query, data)
            results = cursor.fetchall()
            
            if not results:
                print("Không có bản ghi nào trong bảng BangChamCong.")
                return None
        
            rs_list = []
            for item in results:
                cong = BangChamCongDTO(
                    MaBCC=item[0],
                    ThoiGianVao=item[1],
                    ThoiGianRa=item[2],
                    Ngay=item[3],
                    TinhTrang=item[4],
                    MaNhanVien=item[5],
                    deleteStatus=item[6]
                )
                rs_list.append(cong)

            return rs_list  # Trả về danh sách BangChamCongDTO
        
        except pyodbc.Error as e:
            print("Lỗi khi lấy danh sách lương:", e)
            return None
        
    def selectByNgay(self, Thang, Nam):
        con = self.connection.getConnection()
        cursor = con.cursor()
        
        query = '''
            SELECT * FROM BangChamCong
            WHERE MONTH(Ngay) = ?
            AND YEAR(Ngay) = ?;
        '''
        data=(Thang, Nam)
        try:
            cursor.execute(query, data)
            results = cursor.fetchall()
            
            if not results:
                print("Không có bản ghi nào trong bảng BangChamCong.")
                return None
        
            rs_list = []
            for item in results:
                cong = BangChamCongDTO(
                    MaBCC=item[0],
                    ThoiGianVao=item[1],
                    ThoiGianRa=item[2],
                    Ngay=item[3],
                    TinhTrang=item[4],
                    MaNhanVien=item[5],
                    deleteStatus=item[6]
                )
                rs_list.append(cong)

            return rs_list  # Trả về danh sách BangChamCongDTO
        
        except pyodbc.Error as e:
            print("Lỗi khi lấy danh sách lương:", e)
            return None


    




if __name__ == "__main__":

   pass




