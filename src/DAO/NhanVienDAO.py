from Connection import Connection
import pyodbc
import os
import sys
from datetime import datetime
# Lấy đường dẫn của thư mục hiện tại và thêm đường dẫn tới thư mục DTO
current_dir = os.path.dirname(os.path.abspath(__file__))
dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)
from NhanVienDTO import NhanVienDTO
from BangChamCongDTO import BangChamCongDTO

class NhanVienDAO:
    def __init__(self):
        self.connection = Connection()

    @staticmethod
    def getInstance():
        return NhanVienDAO()
    
    def insert(self, employee):
        con = self.connection.getConnection()
        cursor = con.cursor()
        insert_query = '''INSERT INTO NhanVien(MaNhanVien, Ten, NgaySinh, GioiTinh, DiaChi, SDT, ChucVu, HinhAnh, Status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        employee_data = (employee.get_MaNhanVien(), employee.get_Ten(), employee.get_NgaySinh(), 
                        employee.get_GioiTinh(), employee.get_DiaChi(), employee.get_SDT(), employee.get_ChucVu(), employee.get_HinhAnh(), employee.get_Status())
        try:
            cursor.execute(insert_query, employee_data)
            con.commit()
            if cursor.rowcount > 0:  # Kiểm tra số dòng bị ảnh hưởng bởi câu lệnh SQL
                    print("Thêm nhân viên thành công")
                    return 1
            else:
                    print("Thêm nhân viên thất bại")
                    con.rollback()
                    return 0
        except Exception as e:
            print("Thêm nhân viên thất bại except")
            con.rollback()
            return 0

    def update(self, employee):
        con = self.connection.getConnection()
        cursor = con.cursor()
        update_query = '''UPDATE NhanVien
                          set Ten = ?, 
                          NgaySinh = ?, 
                          GioiTinh = ?,
                          DiaChi = ?, 
                          SDT = ?,
                          ChucVu = ?,
                          HinhAnh = ?
                          
                          where MaNhanVien = ?'''
        employee_data = (employee.get_Ten(), employee.get_NgaySinh(), 
                         employee.get_GioiTinh(), employee.get_DiaChi(), employee.get_SDT(), employee.get_ChucVu(), employee.get_HinhAnh(), employee.get_MaNhanVien())
        try:
            cursor.execute(update_query, employee_data)
            con.commit()
            if cursor.rowcount > 0:  # Kiểm tra số dòng bị ảnh hưởng bởi câu lệnh SQL
                    print("Sửa nhân viên thành công")
                    return 1
            else:
                    print("Sửa nhân viên thất bại")
                    con.rollback()
                    return 0
        except Exception as e:
            print("Sửa nhân viên thất bại except")
            con.rollback()
            return 0
            
    def delete(self, id):
        con = self.connection.getConnection()
        cursor = con.cursor()
        delete_query = '''UPDATE NhanVien
                        SET Status = 0
                        WHERE MaNhanVien = ? and Status = 1'''
        employee_data = (id)
        
        try:
            cursor.execute(delete_query, employee_data)
            rows_affected = cursor.rowcount  # Số hàng bị ảnh hưởng
            con.commit()
            
            if rows_affected > 0:
                # print("Xóa nhân viên thành công")
                return 1
            else:
                # print("Nhân viên không tồn tại hoặc không thể xóa")
                return 0
        except pyodbc.Error as e:
            # print("Xóa nhân viên thất bại")
            con.rollback()
            return 0
            
    def TimKiem_Theo_Ma(self, Ma):
        con = self.connection.getConnection()
        cursor = con.cursor()
        
        # Truy vấn tìm kiếm theo MaNhanVien
        query = "SELECT MaNhanVien, Ten, NgaySinh, GioiTinh, DiaChi, SDT, ChucVu, HinhAnh, Status FROM NhanVien WHERE MaNhanVien=?"
        
        try:
            cursor.execute(query, Ma)
            result = cursor.fetchone()  # Lấy kết quả đầu tiên
            
            if result:
                # Gán kết quả truy vấn vào đối tượng NhanVienDTO
                nhan_vien = NhanVienDTO(
                    MaNhanVien=result[0],  # Mã nhân viên
                    Ten=result[1],          # Tên nhân viên
                    NgaySinh=result[2],      # Ngày sinh
                    GioiTinh=result[3],      # Giới tính
                    DiaChi=result[4],        # Địa chỉ
                    SDT=result[5],           # Số điện thoại
                    ChucVu=result[6],        # Chức vụ
                    HinhAnh=result[7],       # Hình ảnh
                    Status=result[8]         # Trạng thái xóa
                )
                return nhan_vien  # Trả về đối tượng NhanVienDTO
            else:
                print(f"Không tìm thấy nhân viên với mã: {Ma}")
                return None  # Trả về None nếu không tìm thấy

        except pyodbc.Error as e:
            print("Lỗi khi tìm kiếm nhân viên:")
            return None
    
    def TimKiem_Theo_Anh(self, Anh):
        con = self.connection.getConnection()
        cursor = con.cursor()
        
        # Truy vấn tìm kiếm theo MaNhanVien
        query = "SELECT MaNhanVien, Ten, NgaySinh, GioiTinh, DiaChi, SDT, ChucVu, HinhAnh, Status FROM NhanVien WHERE HinhAnh=?"
        
        try:
            cursor.execute(query, Anh)
            result = cursor.fetchone()  # Lấy kết quả đầu tiên
            
            if result:
                # Gán kết quả truy vấn vào đối tượng NhanVienDTO
                nhan_vien = NhanVienDTO(
                    MaNhanVien=result[0],  # Mã nhân viên
                    Ten=result[1],          # Tên nhân viên
                    NgaySinh=result[2],      # Ngày sinh
                    GioiTinh=result[3],      # Giới tính
                    DiaChi=result[4],        # Địa chỉ
                    SDT=result[5],           # Số điện thoại
                    ChucVu=result[6],        # Chức vụ
                    HinhAnh=result[7],       # Hình ảnh
                    Status=result[8]         # Trạng thái xóa
                )
                return nhan_vien  # Trả về đối tượng NhanVienDTO
            else:
                print(f"Không tìm thấy nhân viên với Ảnh: {Anh}")
                return None  # Trả về None nếu không tìm thấy

        except pyodbc.Error as e:
            print("Lỗi khi tìm kiếm nhân viên:")
            return None
        
    def list(self):
        con = self.connection.getConnection()
        cursor = con.cursor()
        cursor.execute('SELECT * FROM NhanVien where Status=1')

        danh_sach_nhan_vien = []

        for row in cursor:
            # print(row)
            nhan_vien = NhanVienDTO(
                MaNhanVien=row[0],  # Mã nhân viên
                Ten=row[1],          # Tên nhân viên
                NgaySinh=row[2],      # Ngày sinh
                GioiTinh=row[3],      # Giới tính
                DiaChi=row[4],        # Địa chỉ
                SDT=row[5],           # Số điện thoại
                ChucVu=row[6],        # Chức vụ
                HinhAnh=row[7],       # Hình ảnh
                Status=row[8]         # Trạng thái xóa
            )
            danh_sach_nhan_vien.append(nhan_vien)

        return danh_sach_nhan_vien

    def tao_MaNhanVien(self):
        con = self.connection.getConnection()
        cursor = con.cursor()
        cursor.execute('select count(*) FROM NhanVien')
        ma = None
        result = cursor.fetchone()
        if result:
            ma = result[0] + 1 
        
        if ma < 10:
            ma = 'NV00'+ str(ma) 
        elif ma < 100 and ma > 9:
            ma = 'NV0'+ str(ma)
        else:
            ma = 'NV'+ str(ma) 
            
        return ma
    
    def timKiem(self, nv):
        con = self.connection.getConnection()
        cursor = con.cursor()
        
        # Truy vấn tìm kiếm theo MaNhanVien
        query = "select * from NhanVien where MaNhanVien like ? and Ten like ? "\
                "and NgaySinh like ? and GioiTinh like ? and DiaChi like ? "\
                "and SDT like ? and ChucVu like ? and HinhAnh like ? and Status = 1"
        
        nv_data = ('%' + nv.get_MaNhanVien() + '%', '%' + nv.get_Ten() + '%', '%' + nv.get_NgaySinh() + '%',
                '%' + nv.get_GioiTinh() + '%', '%' + nv.get_DiaChi() + '%', '%' + nv.get_SDT() + '%',
                '%' + nv.get_ChucVu() + '%', '%' + nv.get_HinhAnh() + '%')

        danh_sach_nhan_vien = []
        
        cursor.execute(query, nv_data)
        results = cursor.fetchall()  # Lấy tất cả kết quả
            
        for result in results:
            nhan_vien = NhanVienDTO(
                MaNhanVien=result[0],  # Mã nhân viên
                Ten=result[1],          # Tên nhân viên
                NgaySinh=result[2],      # Ngày sinh
                GioiTinh=result[3],      # Giới tính
                DiaChi=result[4],        # Địa chỉ
                SDT=result[5],           # Số điện thoại
                ChucVu=result[6],        # Chức vụ
                HinhAnh=result[7],       # Hình ảnh
                Status=result[8]         # Trạng thái xóa
            )
            danh_sach_nhan_vien.append(nhan_vien)
        
        return danh_sach_nhan_vien
        
    def CoTaiKhoanChua(self, ma):
        con = self.connection.getConnection()
        cursor = con.cursor()
        cursor.execute('SELECT MaTK FROM TaiKhoan WHERE MaNhanVien = ? GROUP BY MaTK', (ma,))
        result = cursor.fetchone()

        if result is not None:
            return result[0]
        else:
            return 0
     
    ##########################################################
    ################### BẢNG CHẤM CÔNG #######################
    def tao_BangChamCong(self):
        con = self.connection.getConnection()
        cursor = con.cursor()
        cursor.execute('select count(*) FROM BangChamCong')
        ma = None
        result = cursor.fetchone()
        if result:
            ma = result[0] + 1 
        
        if ma < 10:
            ma = 'BCC00'+ str(ma) 
        elif ma < 100 and ma > 9:
            ma = 'BCC0'+ str(ma)
        else:
            ma = 'BCC'+ str(ma) 
            
        return ma  
    
    def insert_BangChamCong(self, cc):
        con = self.connection.getConnection()
        cursor = con.cursor()
        insert_query = '''
        IF EXISTS (
            SELECT 1 
            FROM LichLam
            WHERE MaNhanVien = ? AND Ngay = ?
        )
        AND NOT EXISTS (
            SELECT 1 
            FROM BangChamCong
            WHERE MaNhanVien = ? AND Ngay = ?

        )
        BEGIN
            INSERT INTO BangChamCong(MaBCC, ThoiGianVao, ThoiGianRa, Ngay, TinhTrang, MaNhanVien, Status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        END
        '''
        employee_data = (
            cc.get_MaNhanVien(), cc.get_Ngay(),
            cc.get_MaNhanVien(), cc.get_Ngay(),
            cc.get_MaBCC(), cc.get_ThoiGianVao(), cc.get_ThoiGianRa(), 
            cc.get_Ngay(), "Chưa đủ giờ", cc.get_MaNhanVien(), cc.get_deleteStatus())
            # cc.get_Ngay(), cc.get_TinhTrang(), cc.get_MaNhanVien(), cc.get_deleteStatus())
        
        try:
            cursor.execute(insert_query, employee_data)
            con.commit()
            if cursor.rowcount > 0:  # Kiểm tra số dòng bị ảnh hưởng bởi câu lệnh SQL
                    print("Thêm bảng chấm công thành công")
                    return 1
            else:
                    print("Thêm bảng chấm công thất bại")
                    con.rollback()
                    return 0
        except Exception as e:
            print("Thêm bảng chấm công thất bại except")
            con.rollback()
            return 0
    
    def update_BangChamCong_checkOut(self, ThoiGianRa, MaNhanVien):
        con = self.connection.getConnection()
        cursor = con.cursor()

        # Cập nhật ThoiGianRa
        update_checkout_query = '''
            UPDATE BangChamCong
            SET ThoiGianRa = ?
            WHERE MaNhanVien = ? AND ThoiGianRa = ThoiGianVao
        '''
        employee_data = (ThoiGianRa, MaNhanVien)

        # Cập nhật TinhTrang
        update_tinhtrang_query = '''
            UPDATE BangChamCong
            SET TinhTrang = CASE
                WHEN DATEDIFF(MINUTE, bcc.ThoiGianVao, bcc.ThoiGianRa) >= (
                    SELECT DATEDIFF(MINUTE, cl.ThoiGianVao, cl.ThoiGianRa)
                    FROM CaLam AS cl
                    JOIN LichLam AS ll ON ll.MaCa = cl.MaCa
                    WHERE ll.MaNhanVien = bcc.MaNhanVien AND ll.Ngay = bcc.Ngay
                ) THEN N'Đủ giờ'
                ELSE N'Thiếu giờ'
            END
            FROM BangChamCong AS bcc
            WHERE bcc.MaNhanVien = ? AND bcc.Ngay = ?;
        '''
        try:
            # Thực hiện cập nhật ThoiGianRa
            cursor.execute(update_checkout_query, employee_data)
            con.commit()

            if cursor.rowcount > 0:
                print("Update checkout bảng chấm công thành công")

                # Thực hiện cập nhật TinhTrang
                Ngay = datetime.now().strftime('%Y-%m-%d')
                tinhtrang_data = (MaNhanVien, Ngay)
                cursor.execute(update_tinhtrang_query, tinhtrang_data)
                con.commit()

                if cursor.rowcount > 0:  # Kiểm tra số dòng bị ảnh hưởng bởi câu lệnh SQL
                        print("Update checkout bảng chấm công thành công")
                        return 1
                else:
                        print("Update checkout bảng chấm công thất bại")
                        con.rollback()
                        return 0
        except Exception as e:
            print("Update checkout bảng chấm công thất bại except")
            con.rollback()
            return 0

    
    # def update_BangChamCong_checkOut(self, ThoiGianRa, MaNhanVien):
    #     con = self.connection.getConnection()
    #     cursor = con.cursor()
    #     insert_query = '''
    #         update BangChamCong
    #         set ThoiGianRa = ?
    #         where MaNhanVien = ? and ThoiGianRa = ThoiGianVao
    #     '''
    #     employee_data = (ThoiGianRa, MaNhanVien)
    #     try:
    #         cursor.execute(insert_query, employee_data)
    #         con.commit()
    #         if cursor.rowcount > 0:  # Kiểm tra số dòng bị ảnh hưởng bởi câu lệnh SQL
    #                 print("Update checkout bảng chấm công thành công")
    #                 return 1
    #         else:
    #                 print("Update checkout bảng chấm công thất bại")
    #                 con.rollback()
    #                 return 0
    #     except Exception as e:
    #         print("Update checkout bảng chấm công thất bại except")
    #         con.rollback()
    #         return 0
    
def test():
    bang_cham_cong = BangChamCongDTO("BCC001", "08:00:00", "17:00:00", "2024-10-21", "Đi làm", "NV001", True)
    # dao = NhanVienDAO.getInstance().insert_BangChamCong(bang_cham_cong)
    dao = NhanVienDAO.getInstance().update_BangChamCong_checkOut("10:00:00", "NV001")
    print(dao)
    

if __name__ == "__main__":
    test()