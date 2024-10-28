import tkinter as tk
import utilView
import customtkinter as ctk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import datetime
import os

class ThongTinTaiKhoanGUI:
    
    def __init__(self):
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

        utilView.labelUtil(frameBiggest,'NV001',120, 60, bg='#ffffff', font=("Arial", 12, "italic"))
        utilView.labelUtil(frameBiggest,'Nguyễn Văn A',120, 100, bg='#ffffff', font=("Arial", 12, "italic"))
        utilView.labelUtil(frameBiggest,'28/01/2004',120, 140, bg='#ffffff', font=("Arial", 12, "italic"))
        utilView.labelUtil(frameBiggest,'Nam',120, 180, bg='#ffffff', font=("Arial", 12, "italic"))
        utilView.labelUtil(frameBiggest,'123 An Dương Vương',120, 220, bg='#ffffff', font=("Arial", 12, "italic"))
        utilView.labelUtil(frameBiggest,'0825143790',120, 260, bg='#ffffff', font=("Arial", 12, "italic"))
        utilView.labelUtil(frameBiggest,'Nhân Viên',120, 300, bg='#ffffff', font=("Arial", 12, "italic"))


        window.mainloop()

if __name__ == '__main__':
    ThongTinTaiKhoanGUI()