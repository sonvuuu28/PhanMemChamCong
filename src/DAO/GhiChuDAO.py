from Connection import Connection
import pyodbc
import os
import sys
# Lấy đường dẫn của thư mục hiện tại và thêm đường dẫn tới thư mục DTO
current_dir = os.path.dirname(os.path.abspath(__file__))
dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)

from GhiChuDTO import GhiChuDTO

class GhiChuDAO:
    def __init__(self):
        self.connection = Connection()

    @staticmethod
    def getInstance():
        return GhiChuDAO()
    
    def insert(self, gc):
        con = self.connection.getConnection()
        cursor = con.cursor()
        insert_query = '''INSERT INTO GhiChu(MaGC, Ngay, NoiDung) VALUES (?, ?, ?)'''
        data = (gc.get_MaGC(), gc.get_Ngay(), gc.get_NoiDung())
        try:                                                        
            cursor.execute(insert_query, data)
            if cursor.rowcount > 0:  
                    print("Thêm ghi chú thành công")
                    con.commit()
                    return 1
            else:
                    print("Thêm ghi chú thất bại")
                    con.rollback()
                    return 0
        except Exception as e:
            print("Thêm ghi chú thất bại except ", e)
            con.rollback()
            return 0
        
    def update(self, gc):
        con = self.connection.getConnection()
        cursor = con.cursor()
        insert_query = '''UPDATE GhiChu
                        SET Ngay = ?, NoiDung = ? WHERE  MaGC = ?'''
        data = (gc.get_Ngay(), gc.get_NoiDung(), gc.get_MaGC())
        try:
            cursor.execute(insert_query, data)
            if cursor.rowcount > 0:  
                    print("Sửa ghi chú thành công")
                    con.commit()
                    return 1
            else:
                    print("Sửa ghi chú thất bại")
                    con.rollback()
                    return 0
        except Exception as e:
            print("Sửa ghi chú thất bại except")
            con.rollback()
            return 0
        
    def tao_MaGhiChu(self):
        con = self.connection.getConnection()
        cursor = con.cursor()
        cursor.execute('select count(*) FROM GhiChu')
        ma = None
        result = cursor.fetchone()
        if result:
            ma = result[0] + 1
        
        if ma < 10:
            ma = 'GC00'+ str(ma) 
        elif ma < 100 and ma > 9:
            ma = 'GC0'+ str(ma)
        else:
            ma = 'GC'+ str(ma) 
            
        return ma

    def TimKiem_Theo_Ngay(self, Ngay):
        con = self.connection.getConnection()
        cursor = con.cursor()
        
        # Truy vấn tìm kiếm theo MaNhanVien
        query = "SELECT * FROM GhiChu WHERE Ngay = ?"
        
        try:
            cursor.execute(query, Ngay)
            result = cursor.fetchone()  # Lấy kết quả đầu tiên
            
            if result:
                # Gán kết quả truy vấn vào đối tượng NhanVienDTO
                gc = GhiChuDTO(
                    MaGC=result[0], 
                    Ngay=result[1], 
                    NoiDung=result[2]
                )
                return gc  # Trả về đối tượng NhanVienDTO
            else:
                print(f"Không tìm thấy ghi chú với ngày: {Ngay}")
                return None  # Trả về None nếu không tìm thấy

        except pyodbc.Error as e:
            print("Lỗi khi tìm kiếm ghi chú:", e)
            return None

    def TimKiem_Theo_Ma(self, Ma):
        con = self.connection.getConnection()
        cursor = con.cursor()
        
        # Truy vấn tìm kiếm theo MaNhanVien
        query = "SELECT * FROM GhiChu WHERE MaGC = ?"
        
        try:
            cursor.execute(query, Ma)
            result = cursor.fetchone()  # Lấy kết quả đầu tiên
            
            if result:
                # Gán kết quả truy vấn vào đối tượng NhanVienDTO
                gc = GhiChuDTO(
                    MaGC=result[0], 
                    Ngay=result[1], 
                    NoiDung=result[2]
                )
                return gc  # Trả về đối tượng NhanVienDTO
            else:
                print(f"Không tìm thấy ghi chú với mã: {Ma}")
                return None  # Trả về None nếu không tìm thấy

        except pyodbc.Error as e:
            print("Lỗi khi tìm kiếm ghi chú:", e)
            return None

def test():
    pass
    # tk_dao = GhiChuDAO.getInstance()
    # tk = GhiChuDTO("TK001", "TenTaiKhoan", "password", "Q001", "1", True)
    # tk_dao.insert(tk)
    
    # tk_dao.TimKiem_Theo_Ma("TK001")
    
    # tk = GhiChuDTO("TK001", "TenTaiKhoanUpdated", "passwordUpdated", "Q002", "1", True)
    # tk_dao.update(tk)
    
    # print(tk_dao.tao_MaTaiKhoan())
    # print(tk_dao.DangNhap("NV001", "123").display_info())

if __name__ == "__main__":
    test()