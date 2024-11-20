import tkinter as tk
import utilView
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import ttk
import os
import sys
from tkinter import messagebox
current_dir = os.path.dirname(os.path.abspath(__file__))
dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)
from NhanVienDTO import NhanVienDTO
from TaiKhoanDTO import TaiKhoanDTO

dao_dir = os.path.join(current_dir, '../DAO')
sys.path.append(dao_dir)
from TaiKhoanDAO import TaiKhoanDAO

bus_dir = os.path.join(current_dir, '../BUS')
sys.path.append(bus_dir)
from TaiKhoanBUS import TaiKhoanBUS

dao_dir = os.path.join(current_dir, '../DAO')
sys.path.append(dao_dir)
from NhanVienDAO import NhanVienDAO

class TaiKhoanGUI:
    
    def __init__(self, parent_window, MaNhanVien):
        print("TaiKhoanGUI")
        self.TenNhanVien = MaNhanVien.get_Ten()
        self.MaNhanVien = MaNhanVien.get_MaNhanVien()
        print(self.MaNhanVien)
        self.ChucVu = MaNhanVien.get_ChucVu()
        print(self.ChucVu)
        
        self.Ma = self.tao_MaTaiKhoan()
        print(self.Ma)
        self.TenTaiKhoan = None
        self.MatKhau = None
        self.BtnCapTk = None
        self.BtnSua = None
        
        # Đường dẫn đến folder Icon
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.icon_dir = os.path.join(current_dir, '../Icon')
        
        self.initUI(parent_window)

    def tao_MaTaiKhoan(self):
        employee_dao = NhanVienDAO.getInstance()
        tk = employee_dao.CoTaiKhoanChua(self.MaNhanVien)
        print(tk)
        if tk == 0:
            print("no")
            ma = TaiKhoanDAO.getInstance().tao_MaTaiKhoan()
        else:
            print(f"nhân viên {self.MaNhanVien} có tài khoản là tk")
            ma = tk
        return ma
    
    def CapTk(self):
        if self.TenTaiKhoan.get() == "":
            messagebox.showinfo("Thông báo", "Vui lòng nhập tên đăng nhập !")
            self.TenTaiKhoan.focus_set()
            return
        
        if self.MatKhau.get() == "":
            messagebox.showinfo("Thông báo", "Vui lòng nhập mật khẩu !")
            self.MatKhau.focus_set()
            return
        
        tk_bus = TaiKhoanBUS.getInstance()
        print(self.Ma)
        tk_dto = TaiKhoanDTO(self.Ma, self.TenTaiKhoan.get(), self.MatKhau.get(), "Q002", self.MaNhanVien, 1)
        tk_dto.display_info()
        noti = tk_bus.insert(tk_dto)
        messagebox.showinfo("Thông báo", noti)
    
    def Sua(self):
        if self.TenTaiKhoan.get() == "":
            messagebox.showinfo("Thông báo", "Vui lòng nhập tên đăng nhập !")
            self.TenTaiKhoan.focus_set()
            return
        
        if self.MatKhau.get() == "":
            messagebox.showinfo("Thông báo", "Vui lòng nhập mật khẩu !")
            self.MatKhau.focus_set()
            return
        
        tk_bus = TaiKhoanBUS.getInstance()
        print(self.Ma)
        tk_dto = TaiKhoanDTO(self.Ma, self.TenTaiKhoan.get(), self.MatKhau.get(), "Q002", self.MaNhanVien, 1)
        tk_dto.display_info()
        noti = tk_bus.update(tk_dto)
        messagebox.showinfo("Thông báo", noti)
       
    def initUI(self, parent_window):
        window = tk.Toplevel(parent_window)
        
        wWindow = 300
        hWindow = 380
        window.geometry(f"{wWindow}x{hWindow}+660+200")
        
        # window.overrideredirect(True)
        frameNote = utilView.frameUtil(window, wWindow, hWindow, 0, 0, bg='#F2F2F2')
        
        # headerWindow
        headerWindow = utilView.frameUtil(frameNote, wWindow, 35, 0, 0, bg='#C1C1C1')
        labelNote = tk.Label(headerWindow, text=self.TenNhanVien, bg="#C1C1C1", fg="#000000", font=("Arial", 12))
        label_width = labelNote.winfo_reqwidth()  # Lấy chiều rộng của Label
        label_height = labelNote.winfo_reqheight() 
        x_center = (wWindow - label_width) // 2
        y_center = (35 - label_height) // 2

        # Đặt Label vào vị trí giữa
        labelNote.place(x=x_center, y=y_center)
        
        ## Cột trường thông tin
        utilView.labelUtil(window,'Tài Khoản',100, 70, bg='#F2F2F2', font=("Arial", 14))
        
        xLabel = 40 
        xTextField = 163
         
        utilView.labelUtil(window,'Tên Đăng Nhập',xLabel, 140, bg='#F2F2F2', font=("Arial", 10))
        utilView.labelUtil(window,'Mật Khẩu',xLabel, 220, bg='#F2F2F2', font=("Arial", 10))
        
        ## TextField trường thông tin
        self.TenTaiKhoan = utilView.entryUtil(window, '',xTextField, 142, 18, bg='#ffffff')
        self.TenTaiKhoan.delete(0, tk.END)
        self.TenTaiKhoan.insert(tk.END, self.MaNhanVien)
        
        self.MatKhau = utilView.entryUtil(window,'',xTextField, 222, 18, bg='#ffffff', show = "*")
        
        ## Nút Tạo, Sửa
        dto = TaiKhoanBUS.getInstance().TimKiem_Theo_MaNhanVien(self.MaNhanVien)
        if dto is None:
            self.BtnCapTk = utilView.cusButtonUtil(window, 'Cấp Tài Khoản', xLabel + 65, 320, 100,30, fg_color="#000000", hover_color="#383838",  command=lambda: self.CapTk())
            # self.BtnSua = utilView.cusButtonUtil(window, 'Sửa TK', xLabel + 140, 320, 80, 30, fg_color="#000000", hover_color="#383838",  command=lambda: self.Sua())
        else:
            # self.BtnCapTk = utilView.cusButtonUtil(window, 'Cấp TK', xLabel,320,80,30, fg_color="#000000", hover_color="#383838",  command=lambda: self.CapTk())
            self.BtnSua = utilView.cusButtonUtil(window, 'Sửa Tài Khoản', xLabel + 65, 320, 100, 30, fg_color="#000000", hover_color="#383838",  command=lambda: self.Sua())
        
        window.mainloop()

