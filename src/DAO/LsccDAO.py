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

    def update(self, shift_id, updated_shift: LsccDTO):
        con = self.connection.getConnection()
        cursor = con.cursor()

        update_query = '''
            UPDATE LichSuChamCong
            SET MaCa = ?, Ngay = ?, ThoiGianVao = ?, ThoiGianRa = ?, TinhTrang = ?
            WHERE MaBCC = ?
        '''
        
        shift_data = (
            updated_shift.get_MaCa(),
            updated_shift.get_Ngay(),
            updated_shift.get_ThoiGianVao(),
            updated_shift.get_ThoiGianRa(),
            updated_shift.get_TinhTrang(),
            shift_id
        )

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

    def get_all(self):
        """ Lấy tất cả các bản ghi lịch sử chấm công từ cơ sở dữ liệu """
        con = self.connection.getConnection()
        cursor = con.cursor()
        
        cursor.execute('''
            SELECT MaBCC, ThoiGianVao, ThoiGianRa, Ngay, TinhTrang, MaNhanVien, deleteStatus, Ten
            FROM BangChamCong 
            JOIN NhanVien ON BangChamCong.MaNhanVien = NhanVien.MaNhanVien 
            WHERE Status = 1
        ''')
        
        danh_sach_lich_su = []
        for row in cursor:
            # Tạo đối tượng dictionary cho mỗi dòng
            lich_su = {
                'MaBCC': row[0],
                'ThoiGianVao': row[1],
                'ThoiGianRa': row[2],
                'Ngay': row[3],
                'TinhTrang': row[4],
                'MaNhanVien': row[5],
                'deleteStatus': row[6],
                'Ten': row[7]
            }
            # Thêm dictionary vào danh sách
            danh_sach_lich_su.append(lich_su)
        
        # Trả về danh sách kết quả
        return danh_sach_lich_su
