from Connection import Connection
import pyodbc
import os
import sys
# Lấy đường dẫn của thư mục hiện tại và thêm đường dẫn tới thư mục DTO
current_dir = os.path.dirname(os.path.abspath(__file__))
dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)
from TaiKhoanDTO import TaiKhoanDTO

class TaiKhoanDAO:
    def __init__(self):
        self.connection = Connection()

    @staticmethod
    def getInstance():
        return TaiKhoanDAO()
    
    def insert(self, tk):
        con = self.connection.getConnection()
        cursor = con.cursor()
        insert_query = '''INSERT INTO TaiKhoan(MaTK, TenDangNhap, MatKhau, MaQuyen, MaNhanVien, Status) VALUES (?, ?, ?, ?, ?, ?)'''
        data = (tk.get_MaTK(), tk.get_TenDangNhap(), tk.get_MatKhau(), 
                        tk.get_MaQuyen(), tk.get_MaNhanVien(), tk.get_Status())
        try:
            cursor.execute(insert_query, data)
            con.commit()
            if cursor.rowcount > 0:  
                    print("Thêm tài khoản thành công")
                    return 1
            else:
                    print("Thêm tài khoản thất bại")
                    con.rollback()
                    return 0
        except Exception as e:
            print("Thêm tài khoản thất bại except")
            con.rollback()
            return 0
        
    def update(self, tk):
        con = self.connection.getConnection()
        cursor = con.cursor()
        insert_query = '''update TaiKhoan
                        set 
                        TenDangNhap = ?,   
                        MatKhau = ?,  
                        MaQuyen = ? 
                        where  MaTK = ?'''
        data = (tk.get_TenDangNhap(), tk.get_MatKhau(), tk.get_MaQuyen(), tk.get_MaTK())
        try:
            cursor.execute(insert_query, data)
            con.commit()
            if cursor.rowcount > 0:  
                    print("Sửa tài khoản thành công")
                    return 1
            else:
                    print("Sửa tài khoản thất bại")
                    con.rollback()
                    return 0
        except Exception as e:
            print("Sửa tài khoản thất bại except")
            con.rollback()
            return 0
        
    def tao_MaTaiKhoan(self):
        con = self.connection.getConnection()
        cursor = con.cursor()
        cursor.execute('select count(*) FROM TaiKhoan')
        ma = None
        result = cursor.fetchone()
        if result:
            ma = result[0] + 1
        
        if ma < 10:
            ma = 'TK00'+ str(ma) 
        elif ma < 100 and ma > 9:
            ma = 'TK0'+ str(ma)
        else:
            ma = 'TK'+ str(ma) 
            
        return ma
    def DangNhap(self, tenDangNhap, password):
        con = self.connection.getConnection()
        cursor = con.cursor()
        query = "select * from TaiKhoan where TenDangNhap = ? and MatKhau = ?"
        data = (tenDangNhap, password)
        try:
            cursor.execute(query, data)
            result = cursor.fetchone()
            
            if result:
                # Gán kết quả truy vấn vào đối tượng NhanVienDTO
                tk = TaiKhoanDTO(
                    MaTK=result[0], 
                    TenDangNhap=result[1],    
                    MatKhau=result[2], 
                    MaQuyen=result[3],  
                    MaNhanVien=result[4],      
                    Status=result[5]
                )
                return tk  # Trả về đối tượng NhanVienDTO
            else:
                print(f"Không tìm thấy tài khoản")
                return None  # Trả về None nếu không tìm thấy

        except pyodbc.Error as e:
            print("Lỗi khi tìm kiếm tài khoản:", e)
            return None
        
        
    def TimKiem_Theo_Ma(self, Ma):
        con = self.connection.getConnection()
        cursor = con.cursor()
        
        query = "SELECT * FROM TaiKhoan WHERE MaTK = ?"
        
        try:
            cursor.execute(query, Ma)
            result = cursor.fetchone()  # Lấy kết quả đầu tiên
            
            if result:
                # Gán kết quả truy vấn vào đối tượng NhanVienDTO
                tk = TaiKhoanDTO(
                    MaTK=result[0], 
                    TenDangNhap=result[1],    
                    MatKhau=result[2], 
                    MaQuyen=result[3],  
                    MaNhanVien=result[4],      
                    Status=result[5]
                )
                return tk  # Trả về đối tượng NhanVienDTO
            else:
                print(f"Không tìm thấy tài khoản với mã: {Ma}")
                return None  # Trả về None nếu không tìm thấy

        except pyodbc.Error as e:
            print("Lỗi khi tìm kiếm tài khoản:", e)
            return None
    
    def TimKiem_Theo_MaNhanVien(self, Ma):
        con = self.connection.getConnection()
        cursor = con.cursor()
        
        # Truy vấn tìm kiếm theo MaNhanVien
        query = "SELECT * FROM TaiKhoan WHERE MaNhanVien = ?"
        
        try:
            cursor.execute(query, Ma)
            result = cursor.fetchone()  # Lấy kết quả đầu tiên
            
            if result:
                # Gán kết quả truy vấn vào đối tượng NhanVienDTO
                tk = TaiKhoanDTO(
                    MaTK=result[0], 
                    TenDangNhap=result[1],    
                    MatKhau=result[2], 
                    MaQuyen=result[3],  
                    MaNhanVien=result[4],      
                    Status=result[5]
                )
                return tk  # Trả về đối tượng NhanVienDTO
            else:
                print(f"Không tìm thấy tài khoản với mã: {Ma}")
                return None  # Trả về None nếu không tìm thấy

        except pyodbc.Error as e:
            print("Lỗi khi tìm kiếm tài khoản:", e)
            return None

def test():
    tk_dao = TaiKhoanDAO.getInstance()
    # tk = TaiKhoanDTO("TK001", "TenTaiKhoan", "password", "Q001", "1", True)
    # tk_dao.insert(tk)
    
    # tk_dao.TimKiem_Theo_Ma("TK001")
    
    # tk = TaiKhoanDTO("TK001", "TenTaiKhoanUpdated", "passwordUpdated", "Q002", "1", True)
    # tk_dao.update(tk)
    
    # print(tk_dao.tao_MaTaiKhoan())
    print(tk_dao.DangNhap("NV001", "123").display_info())

if __name__ == "__main__":
    test()