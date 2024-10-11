import tkinter as tk
import utilView
import customtkinter as ctk
from time import strftime
from PIL import Image, ImageTk
class LoginGUI:
    def __init__(self) -> None:
        pass
    
    def notify(self, window):
        utilView.labelUtil(window, "Tên đăng nhập hoặc mật khẩu không đúng !!!", 100, 510, font = ("Helvetica", 11, "bold"), bg = 'white', height = 2, justify = 'left')
    
    def UI(self):
        window = tk.Tk()
        xWindow = 514
        yWindow = 714
        
        frameBiggest = utilView.frameUtil(window, xWindow, yWindow, 0, 0, bg = '#ffffff')
        ### Label Quản Lý Chấm Công
        Label_QuanLyChamCong = utilView.labelUtil(frameBiggest, \
                    "QUẢN LÝ \nCHẤM CÔNG", 80, 55, font = ('Helvetica', 28, "bold"), bg = '#FFFFFF', height = 2, justify = 'left')
        
        ### Tài khoản
        frameTaiKhoan = utilView.frameUtil(frameBiggest, 356, 157, 79, 254, bg = 'white')
        Label_TaiKhoan = utilView.labelUtil(frameTaiKhoan, \
                    "TÀI KHOẢN", 0, 0, font = ("Helvetica", 11, "bold"), bg = 'white', height = 2, justify = 'left')
        Entry_TaiKhoan = utilView.entryUtil(frameTaiKhoan, \
                    "ABC", 0, 42, 350, font = ("Helvetica Light", 10), bg = 'white', fg = '#666464')
        utilView.lineUtil(frameTaiKhoan, 0, 400, 70)

        ### Mật khẩu
        frameMatKhau = utilView.frameUtil(frameBiggest, 356, 157, 79, 377, bg = 'white')
        Label_MatKhau = utilView.labelUtil(frameMatKhau, \
                    "MẬT KHẨU", 0, 0, font = ("Helvetica", 11, "bold"), bg = 'white', height = 2, justify = 'left')
        Entry_MatKhau = utilView.entryUtil(frameMatKhau, \
                    "Ít nhất 8 ký tự", 0, 42, 350, font = ("Helvetica Light", 10), bg = 'white', fg = '#666464')
        utilView.lineUtil(frameMatKhau, 0, 400, 70)

        ## Nút đăng nhập
        utilView.cusButtonUtil(frameBiggest, 'Đăng Nhập', 80, 586, 357, 50, text_color = 'white',\
        fg_color = 'black', font = ("", 13,"bold"), corner_radius = 0, hover_color = '#383838', command = None)
            
        
        window.geometry(f"{xWindow}x{yWindow}+500+20")
        window.mainloop()
        
if __name__ == '__main__':
    login = LoginGUI()
    login.UI()
