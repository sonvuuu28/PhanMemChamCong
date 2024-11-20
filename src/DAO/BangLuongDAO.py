from Connection import Connection
import pyodbc
import os
import sys
# Lấy đường dẫn của thư mục hiện tại và thêm đường dẫn tới thư mục DTO
current_dir = os.path.dirname(os.path.abspath(__file__))
dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)

from BangLuongDTO import BangLuongDTO

class BangLuongDAO:
    def __init__(self):
        self.connection = Connection()

    @staticmethod
    def getInstance():
        return BangLuongDAO()
    
    def selectAll(self):
        con = self.connection.getConnection()
        cursor = con.cursor()
        
        # Truy vấn tìm kiếm theo MaBangLuong
        query = "SELECT * FROM BangLuong WHERE Status=1"
        
        try:
            cursor.execute(query)
            results = cursor.fetchall()  # Lấy kết quả đầu tiên
            
            if not results:
                print("Không có bản ghi nào trong bảng BangLuong.")
                return None
        
            rs_list = []
            for item in results:
                luong = BangLuongDTO(
                    MaBangLuong=item[0],
                    Thang=item[1],
                    Nam=item[2],
                    PhuCap=item[3],
                    KhauTru=item[4],
                    HeSoLuong=item[5],
                    TongTien=item[6],
                    MaNhanVien=item[7],
                    deleteStatus=item[8],
                    SoGioLam=item[9]
                )
                rs_list.append(luong)

            return rs_list  # Trả về danh sách BangLuongDTO
        
        except pyodbc.Error as e:
            print("Lỗi khi lấy danh sách lương:", e)
            return None
        
    def selectByDate(self, month, year):
        con = self.connection.getConnection()
        cursor = con.cursor()
        is_exist_stt=1
        # Truy vấn tìm kiếm theo MaBangLuong
        query = "SELECT * FROM BangLuong WHERE Thang=? AND Nam=? AND Status=?"
        data = (month, year, is_exist_stt)
        try:
            cursor.execute(query, data)
            results = cursor.fetchall()  # Lấy kết quả đầu tiên
            
            if not results:
                print("Không có bản ghi nào trong bảng BangLuong.")
                return None
        
            rs_list = []
            for item in results:
                luong = BangLuongDTO(
                    MaBangLuong=item[0],
                    Thang=item[1],
                    Nam=item[2],
                    PhuCap=item[3],
                    KhauTru=item[4],
                    HeSoLuong=item[5],
                    TongTien=item[6],
                    MaNhanVien=item[7],
                    deleteStatus=item[8],
                    SoGioLam=item[9]
                )
                rs_list.append(luong)

            return rs_list  # Trả về danh sách BangLuongDTO
        
        except pyodbc.Error as e:
            print("Lỗi khi lấy danh sách lương:", e)
            return None

    def insert(self, luong):
        con = self.connection.getConnection()
        cursor = con.cursor()
        insert_query = '''
            INSERT INTO BangLuong(MaBangLuong, Thang, Nam, PhuCap,
              KhauTru, HeSoLuong, TongTien, MaNhanVien, Status, SoGioLam) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        
        data = (
             luong.get_MaBangLuong(), luong.get_Thang(), luong.get_Nam(), luong.get_PhuCap(),
             luong.get_KhauTru(), luong.get_HeSoLuong(), luong.get_TongTien(), 
             luong.get_MaNhanVien(),luong.get_deleteStatus(), luong.get_SoGioLam()
        )
        try:
            cursor.execute(insert_query, data)
            if cursor.rowcount > 0:  
                con.commit()
                return 1
            else:
                con.rollback()
                return 0
        except Exception as e:
            con.rollback()
            print("Thêm lương thất bại ", e)
            return 0
        
    def update(self, luong):
        con = self.connection.getConnection()
        cursor = con.cursor()
        insert_query = '''
                UPDATE BangLuong SET Thang=?, Nam=?, PhuCap=?,
                    KhauTru=?, HeSoLuong=?, TongTien=?, MaNhanVien=?, Status=?, SoGioLam=? 
                WHERE MaBangLuong=?
        '''

        data = (luong.get_Thang(), luong.get_Nam(), luong.get_PhuCap(),
             luong.get_KhauTru(), luong.get_HeSoLuong(), luong.get_TongTien(), luong.get_MaNhanVien(),
             luong.get_deleteStatus(), luong.get_SoGioLam(), luong.get_MaBangLuong() 
        )
        try:
            cursor.execute(insert_query, data)
            if cursor.rowcount > 0:  
                con.commit()
                return 1
            else:
                con.rollback()
                return 0
        except Exception as e:
            con.rollback()
            print("Sửa lương thất bại ", e)
            return 0
        
    def tao_MaBangLuong(self):
        con = self.connection.getConnection()
        cursor = con.cursor()
        cursor.execute('select count(*) FROM BangLuong')
        ma = None
        result = cursor.fetchone()
        if result:
            ma = result[0] + 1
        
        if ma < 10:
            ma = 'BL00'+ str(ma) 
        elif ma < 100 and ma > 9:
            ma = 'BL0'+ str(ma)
        else:
            ma = 'BL'+ str(ma) 
        
        return ma
    
    def TimKiem_Theo_Ma(self, Ma):
        con = self.connection.getConnection()
        cursor = con.cursor()
        
        # Truy vấn tìm kiếm theo MaBangLuong
        query = "SELECT * FROM BangLuong WHERE MaBangLuong = ?"
        
        try:
            cursor.execute(query, Ma)
            item = cursor.fetchone()  # Lấy kết quả đầu tiên
            
            if item:
                # Gán kết quả truy vấn vào đối tượng NhanVienDTO
                luong = BangLuongDTO(
                    MaBangLuong=item[0],
                    Thang=item[1],
                    Nam=item[2],
                    PhuCap=item[3],
                    KhauTru=item[4],
                    HeSoLuong=item[5],
                    TongTien=item[6],
                    MaNhanVien=item[7],
                    deleteStatus=item[8],
                    SoGioLam=item[9]
                )

                return luong  # Trả về đối tượng NhanVienDTO
            else:
                return None  # Trả về None nếu không tìm thấy

        except pyodbc.Error as e:
            print("Lỗi khi tìm kiếm lương:", e)
            return None


def test():
    luong_dao = BangLuongDAO.getInstance()

    # danhsach_luong = luong_dao.selectAll()
    # for luong in danhsach_luong:
    #     print(luong.display_info())


    luong = BangLuongDTO("BL001", 11, 2024, 200, 0, 25, 2700, "NV001", 1, 10.2)
    rs = luong_dao.update(luong)
    print(f"Ket qua: {'Thanh cong' if rs == 1 else 'That bai'}")


    # luong = BangLuongDTO("luong001", "TenTaiKhoan", "password", "Q001", "1", True)
    # luong_dao.insert(luong)
    
    # kq = luong_dao.TimKiem_Theo_Ma("BL003")
    # if not kq:
    #     return
    # kq.display_info()
    
    # luong = BangLuongDTO("luong001", "TenTaiKhoanUpdated", "passwordUpdated", "Q002", "1", True)
    # luong_dao.update(luong)
    
    # print(luong_dao.tao_MaTaiKhoan())
    # print(luong_dao.DangNhap("NV001", "123").display_info())

if __name__ == "__main__":
    test()