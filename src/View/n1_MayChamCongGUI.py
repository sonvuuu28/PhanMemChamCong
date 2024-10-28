import tkinter as tk
import utilView
import customtkinter as ctk
from PIL import Image, ImageTk
import cv2
import os
import subprocess
from time import strftime
from datetime import datetime

class MayChamCongGUI:
    def __init__(self):
        self.db_dir = "./ImageEmployee"
        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)
        # Đường dẫn đến folder Icon
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.icon_dir = os.path.join(current_dir, '../Icon')
        self.UI()

    def enter_label(self, label, anhGoc, title):
        label.config(image=anhGoc)
        if title is not None:
            title.config(fg='#5A5A5A')
            
    def leave_label(self, label, anhHover, title):
        label.config(image=anhHover)
        if title is not None:
            title.config(fg='#000000')
            
    def hover(self, label, anhGoc, anhHover, title):
        label.bind("<Enter>", lambda event: self.enter_label(label, anhHover, title))
        label.bind("<Leave>", lambda event: self.leave_label(label, anhGoc, title))
        
    def welcome(self, name):
        utilView.msg_boxUtil('welcome', 'Xin chào ' + name) 
        
    def switchToLoginGUI(self, window):
        window.destroy()
        from View.n0_LoginGUI import LoginGUI
        login_gui = LoginGUI()
        login_gui.UI()
        
    def getTime(self):
        time = strftime('%H:%M:%S')
        date = self.getDate()
        return f'{date} {time}'
    
    def getDate(self):
        ngayHienTai = datetime.now()
        ngay = ngayHienTai.day
        thang = ngayHienTai.month
        nam = ngayHienTai.year
        if len(str(ngay)) < 2:
            ngay = f"0{ngay}"
        if len(str(thang)) < 2:
            thang = f"0{thang}"
        return f'{nam}-{thang}-{ngay}'
    
    def dangXuat(self, name, window = None):
        print(f"Đây là nút {name}")
        if name == "DangXuat" and window:
            window.destroy() 
            from n0_LoginGUI import LoginGUI
            nvGui = LoginGUI()
    
    def process_webcam(self):
        ret, frame = self.cap.read()
        self.most_recent_capture_arr = frame

        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
        self.most_recent_capture_pil = Image.fromarray(img_)

        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)

        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)

        self._label.after(20, self.process_webcam)

    def add_webcam(self, label):
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 200)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 200)
        self._label = label
        self.process_webcam()

    def checkIn(self):
        # Thêm logic cho việc chấm công ở đây
        print("checkIn thành công!")

    def checkOut(self):
        # Thêm logic cho việc chấm công ở đây
        print("checkOut thành công!")
    
    def UI(self):
        window = tk.Tk()
        xWindow = 514
        yWindow = 714
        
        # Đường dẫn đến folder Icon
        # icon_dir = os.path.join(self.current_dir, '../Icon')
        
        # Frame Tổng
        frameBiggest = utilView.frameUtil(window, xWindow, yWindow, 0, 0, bg='#ffffff')
        
        ### Label exit
        exitImage = Image.open(os.path.join(self.icon_dir, "exit.png"))
        exitImageHover = Image.open(os.path.join(self.icon_dir, "exitHover.png"))
        tk_exitImage = ImageTk.PhotoImage(exitImage)
        tk_exitImageHover = ImageTk.PhotoImage(exitImageHover)

        # Tạo Label để hiển thị hình ảnh trong Frame
        label_exit = tk.Label(frameBiggest, image=tk_exitImage, bg='white')
        label_exit.image = tk_exitImage
        label_exit.place(x=445, y=25)
        label_exit.bind("<Button-1>", lambda event: self.dangXuat("DangXuat", window))
        self.hover(label_exit, tk_exitImage, tk_exitImageHover, None)

        ### LABEL ngày tháng năm
        utilView.dateUtil(frameBiggest, 61, 37)

        ### LABEL Đồng Hồ
        utilView.clockUtil(frameBiggest, 61, 70)

        ### BUTTON CheckIn
        utilView.cusButtonUtil(frameBiggest, 'CHECKIN', 123, 575, 280, 40, text_color='white',
                              fg_color='black', font=("", 13, "bold"), corner_radius=5, hover_color='#383838', command=lambda: self.checkIn())

        ### BUTTON CheckOut
        utilView.cusButtonUtil(frameBiggest, 'CHECKOUT', 123, 630, 280, 40, text_color='black',
                              fg_color='#D9D9D9', font=("", 13, "bold"), corner_radius=5, hover_color='#CACACA', command=lambda: self.checkOut())
        
        ### Label để add image
        webcam_label = utilView.labelUtil(window, None, 61, 142, width=393, height=379, bg='black')
        self.add_webcam(webcam_label)

        window.geometry(f"{xWindow}x{yWindow}+500+20")
        window.mainloop()

if __name__ == '__main__':
    may = MayChamCongGUI()
    # may.UI()