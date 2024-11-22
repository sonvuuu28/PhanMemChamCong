from Connection import Connection
import pyodbc
import os
import sys

# Lấy đường dẫn của thư mục hiện tại và thêm đường dẫn tới thư mục DTO
current_dir = os.path.dirname(os.path.abspath(__file__))
dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)
from LsccDTO import LsccDTO

class LsccDAO:
    def __init__(self):
        self.connection = Connection()
    
    @staticmethod
    def getInstance():
        return LsccDAO()

    def update(self, dataUpdate):
        con = self.connection.getConnection()
        cursor = con.cursor()

        # print(shift_id)
        # cursor.execute("SELECT * FROM BangChamCong WHERE MaBCC = ?", (shift_id,))
        # row = cursor.fetchone()
        # print("Row to update:", row)



        update_query = '''
            UPDATE BangChamCong
            SET Ngay = ?, ThoiGianVao = ?, ThoiGianRa = ?, Status = ?
            WHERE MaBCC = ?
        '''
        
        shift_data = (
            dataUpdate.get_Ngay(),
            dataUpdate.get_ThoiGianVao(),
            dataUpdate.get_ThoiGianRa(),
            dataUpdate.get_TinhTrang(),
            dataUpdate.get_MaBCC(),
            
        )

        # print(updated_shift.get_TinhTrang)

        try:
            cursor.execute(update_query, shift_data)
            con.commit()
            return 1  # Success
        except Exception as e:
            con.rollback()
            print(f"Error updating shift: {e}")
            return 0  # Failure
        finally:
            cursor.close()
            con.close()
    def get_by_date(self, date):
        """ Lấy tất cả các bản ghi lịch sử chấm công từ cơ sở dữ liệu """
        con = self.connection.getConnection()
        cursor = con.cursor()
        query = '''
            SELECT *
            FROM BangChamCong 
            WHERE Ngay = ?
        '''
        data=(date)
        cursor.execute(query, data)
        
        danh_sach_lich_su = []
        for row in cursor:
            # Create LsccDTO object for each row
            dto = LsccDTO(
                MaBCC=row[0],             # Mapping MaBCC to MaCa
                ThoiGianVao=row[1],      # ThoiGianVao
                ThoiGianRa=row[2],       # ThoiGianRa
                Ngay=row[3],             # Ngay
                TinhTrang=row[4],      # TinhTrang
                MaNhanVien=row[5],
                Status=row[6]  
            )
            # Add DTO object to the list
            danh_sach_lich_su.append(dto)
        
        # Trả về danh sách kết quả
        return danh_sach_lich_su
    def get_all(self):
        """ Lấy tất cả các bản ghi lịch sử chấm công từ cơ sở dữ liệu """
        con = self.connection.getConnection()
        cursor = con.cursor()

        cursor.execute('''
            SELECT MaBCC, ThoiGianVao, ThoiGianRa, Ngay, TinhTrang, BangChamCong.MaNhanVien, BangChamCong.Status, Ten
            FROM BangChamCong 
            JOIN NhanVien ON BangChamCong.MaNhanVien = NhanVien.MaNhanVien 
            WHERE BangChamCong.Status = 0 and NhanVien.Status = 1
        ''')
        
        danh_sach_lich_su = []
        for row in cursor:
            # Create LsccDTO object for each row
            dto = LsccDTO(
                MaCa=row[0],             # Mapping MaBCC to MaCa
                Ngay=row[3],             # Ngay
                ThoiGianVao=row[1],      # ThoiGianVao
                ThoiGianRa=row[2],       # ThoiGianRa
                TinhTrang=row[4],      # TinhTrang
                # Ten=row[7]  #ten nhan vien
            )
            # Add DTO object to the list
            danh_sach_lich_su.append(dto)
        
        # Trả về danh sách kết quả
        return danh_sach_lich_su
