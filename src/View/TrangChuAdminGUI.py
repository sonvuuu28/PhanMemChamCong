import tkinter as tk
import utilView
import customtkinter as ctk
from PIL import Image, ImageTk
from time import strftime

class TrangChuAdminGUI:
    def __init__(self):
        self.label_chuong = None
        self.UI()

    def enter_label(self, label, anhGoc, title):
        label.config(image=anhGoc)
        if title != None:
            title.config(fg='#5A5A5A')
            
    def leave_label(self, label, anhHover, title):
        label.config(image=anhHover)
        if title != None:
            title.config(fg='#000000')
            
    def click_label(self, label, frame):
        label.bind("<Button-1>", lambda event: self.toggle_frame(frame))
            
    def toggle_frame(self, frame):
        if frame.winfo_manager():
            frame.place_forget()
        else:
            frame.place( x= 860, y = 60) 



    def hover(self, label, anhGoc, anhHover, title):
        label.bind("<Enter>", lambda event: self.enter_label(label, anhHover, title))
        label.bind("<Leave>", lambda event: self.leave_label(label, anhGoc, title))
    
    def UI(self):
        window = tk.Tk()
        xWindow = 1000
        yWindow = 650
        
        ## Frame lớn nhẩt
        frameBiggest = utilView.frameUtil(window, xWindow, yWindow, 0, 0, bg = '#ffffff')
        
        ### LABEL ngày tháng năm
        utilView.dateUtil(frameBiggest, 60, 30)
        
        ### LABEL Đồng Hồ
        utilView.clockUtil(frameBiggest, 60, 70)
        
        ### Label chuông Thông báo
        ChuongImage = Image.open("Icon/chuong.png")
        ChuongImageHover = Image.open("Icon/chuong_hover.png")
        tk_chuongImage = ImageTk.PhotoImage(ChuongImage)
        tk_chuongImageHover = ImageTk.PhotoImage(ChuongImageHover)
        # Tạo Label để hiển thị hình ảnh trong Frame
        label_chuong = tk.Label(frameBiggest, image=tk_chuongImage, bg='white')
        label_chuong.image = tk_chuongImage
        label_chuong.place(x=800, y=15)
        self.hover(label_chuong, tk_chuongImage, tk_chuongImageHover, None)
        
        ### Label setting
        settingImage = Image.open("Icon/setting.png")
        tk_settingImage = ImageTk.PhotoImage(settingImage)
        settingImageHover = Image.open("Icon/settingHover.png")
        tk_settingImageHover = ImageTk.PhotoImage(settingImageHover)
        # Tạo Label để hiển thị hình ảnh trong Frame
        label_setting = tk.Label(frameBiggest, image=tk_settingImage, bg='white')
        label_setting.image = tk_settingImage
        label_setting.place(x=860, y=15)
        self.hover(label_setting, tk_settingImage, tk_settingImageHover, None)
        
        ## Nội dung chuông, đăng xuất, tài khoản cá nhân
        
        frameSetting = utilView.frameUtil(frameBiggest, 134, 81, 860, 60, bg='#FBF6F6')
        DangXuat = utilView.cusButtonUtil(frameSetting, 'Đăng Xuất', 0, 0, 136, 40, text_color='black',
                              fg_color='#D9D9D9', font=("", 13, "bold"), corner_radius=5, hover_color='#CACACA')
        ThongTinCaNhan = utilView.cusButtonUtil(frameSetting, 'Thông Tin Cá Nhân', 0, 41, 136, 40, text_color='black',
                              fg_color='#D9D9D9', font=("", 13, "bold"), corner_radius=5, hover_color='#CACACA')        
        frameSetting.place_forget()
        self.click_label(label_setting, frameSetting)
        #Frame chứa chức năng
        frameChucNang = utilView.frameUtil(frameBiggest, 600, 200, 200, 140, bg='#FBF6F6')
        
        ##Nội dung trong frame 3 nút
        
        ##Nút nhân viên
        nhanVienImage = Image.open("Icon/NhanVien.png")
        tk_nhanVienImage = ImageTk.PhotoImage(nhanVienImage)
        nhanVienImageHover = Image.open("Icon/NhanVienHover.png")
        tk_nhanVienImageHover = ImageTk.PhotoImage(nhanVienImageHover)
        # Tạo Label để hiển thị hình ảnh trong Frame
        label_nhanVien = tk.Label(frameChucNang, image=tk_nhanVienImage, bg='#FBF6F6')
        label_nhanVien.image = tk_nhanVienImage  # Giữ một tham chiếu để hình ảnh không bị hủy
        label_nhanVien.place(x=60, y=25)
        label_nhanVien_title = utilView.labelUtil(frameChucNang, \
                    "Nhân Viên", 68, 120, font = ("Helvetica", 10, ""), bg = '#FBF6F6')
        self.hover(label_nhanVien, tk_nhanVienImage, tk_nhanVienImageHover, label_nhanVien_title)
        
        ##Nút lương
        LuongImage = Image.open("Icon/Luong.png")
        tk_LuongImage = ImageTk.PhotoImage(LuongImage)
        LuongImageHover = Image.open("Icon/LuongHover.png")
        tk_LuongImageLuong = ImageTk.PhotoImage(LuongImageHover)
        # Tạo Label để hiển thị hình ảnh trong Frame
        label_Luong = tk.Label(frameChucNang, image=tk_LuongImage, bg='#FBF6F6')
        label_Luong.image = tk_LuongImage  # Giữ một tham chiếu để hình ảnh không bị hủy
        label_Luong.place(x=260, y=25)
        Label_Luong_title = utilView.labelUtil(frameChucNang, \
                    "Bảng Lương", 264, 120, font = ("Helvetica", 10, ""), bg = '#FBF6F6')
        self.hover(label_Luong, tk_LuongImage, tk_LuongImageLuong, Label_Luong_title)
        
        ##Nút chấm công
        lichSuChamCongImage = Image.open("Icon/LichSuChamCong.png")
        tk_lichSuChamCongImage = ImageTk.PhotoImage(lichSuChamCongImage)
        lichSuChamCongImageHover = Image.open("Icon/LichSuChamCongHover.png")
        tk_lichSuChamCongImageHover = ImageTk.PhotoImage(lichSuChamCongImageHover)
        # Tạo Label để hiển thị hình ảnh trong Frame
        label_LichSuChamCong = tk.Label(frameChucNang, image=tk_lichSuChamCongImage, bg='#FBF6F6')
        label_LichSuChamCong.image = tk_lichSuChamCongImage  # Giữ một tham chiếu để hình ảnh không bị hủy
        label_LichSuChamCong.place(x=460, y=25)
        label_LichSuChamCong_title = utilView.labelUtil(frameChucNang, \
                    "Lịch Sử\nChấm Công", 464, 120, font = ("Helvetica", 10, ""), bg = '#FBF6F6')
        self.hover(label_LichSuChamCong, tk_lichSuChamCongImage, tk_lichSuChamCongImageHover, label_LichSuChamCong_title)
        
        ### BUTTON Ghi Chú
        utilView.cusButtonUtil(frameBiggest, 'Ghi Chú', 350, 390, 300, 41, text_color='black',
                              fg_color='#D9D9D9', font=("", 13, "bold"), corner_radius=5, hover_color='#CACACA')
        ### BUTTON Lịch Làm Việc
        utilView.cusButtonUtil(frameBiggest, 'Lịch Làm Việc',350, 460, 300, 41,text_color='black',
                              fg_color='#D9D9D9', font=("", 13, "bold"), corner_radius=5, hover_color='#CACACA')
        ### BUTTON Xếp Lịch Làm
        utilView.cusButtonUtil(frameBiggest, 'Xếp Lịch Làm', 322, 545, 355, 50, text_color='white',
                              fg_color='black', font=("", 13, "bold"), corner_radius=0, hover_color='#383838')
        
        window.geometry(f"{xWindow}x{yWindow}+300+40")
        window.mainloop()
        
if __name__ == '__main__':
    trang_chu = TrangChuAdminGUI()
