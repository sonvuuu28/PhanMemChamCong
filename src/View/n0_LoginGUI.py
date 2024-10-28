import tkinter as tk
import utilView
import customtkinter as ctk
from time import strftime
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
dao_dir = os.path.join(current_dir, '../DAO')
sys.path.append(dao_dir)
from TaiKhoanDAO import TaiKhoanDAO

current_dir = os.path.dirname(os.path.abspath(__file__))
dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)
from TaiKhoanDTO import TaiKhoanDTO

class LoginGUI:
    def __init__(self):
        self.TenTaiKhoan = None
        self.MatKhau = None
        self.window = None
        self.UI()
    
    def notify(self):
        utilView.labelUtil(self.window, "Tên đăng nhập hoặc mật khẩu không đúng !!!", 100, 510, font = ("Helvetica", 11, "bold"), bg = 'white', height = 2, justify = 'left')
    
    def DangNhap(self):
        if self.TenTaiKhoan.get() == "":
            messagebox.showinfo("Thông báo", "Vui lòng nhập tên đăng nhập !")
            self.TenTaiKhoan.focus_set()
            return
        
        if self.MatKhau.get() == "":
            messagebox.showinfo("Thông báo", "Vui lòng nhập mật khẩu !")
            self.MatKhau.focus_set()
            return
        tk_dao = TaiKhoanDAO.getInstance()
        tk = tk_dao.DangNhap(self.TenTaiKhoan.get(), self.MatKhau.get())
        if tk is not None:
            Quyen = tk.get_MaQuyen()  # Di chuyển dòng này vào trong điều kiện
            if self.window:
                self.window.destroy()
                if Quyen == 'Q001':  
                    from n1_TrangChuGUI import TrangChuGUI
                    TrangChuGUI()
                elif Quyen == 'Q002':
                    from n1_TrangChuGUI import TrangChuGUI
                    TrangChuGUI()
                elif Quyen == 'Q003':
                    from n1_MayChamCongGUI import MayChamCongGUI
                    MayChamCongGUI()
        else:
            self.notify()
            
            
    def UI(self):
        self.window = tk.Tk()
        xWindow = 514
        yWindow = 714
        
        frameBiggest = utilView.frameUtil(self.window, xWindow, yWindow, 0, 0, bg = '#ffffff')
        ### Label Quản Lý Chấm Công
        Label_QuanLyChamCong = utilView.labelUtil(frameBiggest, \
                    "QUẢN LÝ \nCHẤM CÔNG", 80, 55, font = ('Helvetica', 28, "bold"), bg = '#FFFFFF', height = 2, justify = 'left')
        
        ### Tài khoản
        frameTaiKhoan = utilView.frameUtil(frameBiggest, 356, 157, 79, 254, bg = 'white')
        Label_TaiKhoan = utilView.labelUtil(frameTaiKhoan, \
                    "TÀI KHOẢN", 0, 0, font = ("Helvetica", 11, "bold"), bg = 'white', height = 2, justify = 'left')
        self.TenTaiKhoan = Entry_TaiKhoan = utilView.entryUtil(frameTaiKhoan, \
                    "ABC", 0, 42, 350, font = ("Helvetica Light", 10), bg = 'white', fg = '#666464')
        utilView.lineUtil(frameTaiKhoan, 0, 400, 70)

        ### Mật khẩu
        frameMatKhau = utilView.frameUtil(frameBiggest, 356, 157, 79, 377, bg = 'white')
        Label_MatKhau = utilView.labelUtil(frameMatKhau, \
                    "MẬT KHẨU", 0, 0, font = ("Helvetica", 11, "bold"), bg = 'white', height = 2, justify = 'left')
        self.MatKhau = Entry_MatKhau = utilView.entryUtil(frameMatKhau, \
                    "abcabc", 0, 42, 350, font = ("Helvetica Light", 10), bg = 'white', fg = '#666464', show = "*")
        utilView.lineUtil(frameMatKhau, 0, 400, 70)

        ## Nút đăng nhập
        utilView.cusButtonUtil(frameBiggest, 'Đăng Nhập', 80, 586, 357, 50, text_color = 'white',\
        fg_color = 'black', font = ("", 13,"bold"), corner_radius = 0, hover_color = '#383838', command=lambda: self.DangNhap())
            
        
        self.window.geometry(f"{xWindow}x{yWindow}+500+20")
        self.window.mainloop()
        
if __name__ == '__main__':
    LoginGUI()
