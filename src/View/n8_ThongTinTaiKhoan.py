import tkinter as tk
import utilView
import customtkinter as ctk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import datetime
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)
from NhanVienDTO import NhanVienDTO

bus_dir = os.path.join(current_dir, '../BUS')
sys.path.append(bus_dir)
from NhanVienBUS import NhanVienBUS

dao_dir = os.path.join(current_dir, '../DAO')
sys.path.append(dao_dir)
from NhanVienDAO import NhanVienDAO

class ThongTinTaiKhoanGUI:
    
    def __init__(self, id):
        nv_dao = NhanVienDAO.getInstance()
        self.nv = nv_dao.TimKiem_Theo_Ma(id)
        
        # Đường dẫn đến folder Icon
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.icon_dir = os.path.join(current_dir, '../Icon')
        
        # self.window = None
        
        self.initUI()

    def initUI(self):
        # Khởi tạo cửa sổ
        window = tk.Toplevel()
        xWindow = 300
        yWindow = 380

        window.geometry(f"{xWindow}x{yWindow}+610+200")
        
        frameBiggest = utilView.frameUtil(window, xWindow, yWindow, 0, 0, bg='#ffffff')
        # Header
        header = utilView.labelUtil(frameBiggest, "TÀI KHOẢN", 0, 0, foreground="black", bg='#908181', font=("Arial", 12, "bold"), width = 30, height = 2)
        
        
        utilView.labelUtil(frameBiggest,'Mã',20, 60, bg='#ffffff', font=("Arial", 12, "bold"))
        utilView.labelUtil(frameBiggest,'Tên',20, 100, bg='#ffffff', font=("Arial", 12, "bold"))
        utilView.labelUtil(frameBiggest,'Ngày Sinh',20, 140, bg='#ffffff', font=("Arial", 12, "bold"))
        utilView.labelUtil(frameBiggest,'Giới Tính',20, 180, bg='#ffffff', font=("Arial", 12, "bold"))
        utilView.labelUtil(frameBiggest,'Địa Chỉ',20, 220, bg='#ffffff', font=("Arial", 12, "bold"))
        utilView.labelUtil(frameBiggest,'SĐT',20, 260, bg='#ffffff', font=("Arial", 12, "bold"))
        utilView.labelUtil(frameBiggest,'Chức Vụ',20, 300, bg='#ffffff', font=("Arial", 12, "bold"))

        utilView.labelUtil(frameBiggest,self.nv.get_MaNhanVien(),120, 60, bg='#ffffff', font=("Arial", 12, "italic"))
        utilView.labelUtil(frameBiggest,self.nv.get_Ten(),120, 100, bg='#ffffff', font=("Arial", 12, "italic"))
        utilView.labelUtil(frameBiggest,self.nv.get_NgaySinh().strftime('%d/%m/%Y'),120, 140, bg='#ffffff', font=("Arial", 12, "italic"))
        utilView.labelUtil(frameBiggest,self.nv.get_GioiTinh(),120, 180, bg='#ffffff', font=("Arial", 12, "italic"))
        utilView.labelUtil(frameBiggest,self.nv.get_DiaChi(),120, 220, bg='#ffffff', font=("Arial", 12, "italic"))
        utilView.labelUtil(frameBiggest,self.nv.get_SDT(),120, 260, bg='#ffffff', font=("Arial", 12, "italic"))
        utilView.labelUtil(frameBiggest,self.nv.get_ChucVu(),120, 300, bg='#ffffff', font=("Arial", 12, "italic"))


        window.mainloop()

if __name__ == '__main__':
    ThongTinTaiKhoanGUI()