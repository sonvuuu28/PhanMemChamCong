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
            
    def welcome(self, name):
        utilView.msg_boxUtil('welcome', 'Xin chào ' + name) 
        
    def switchToLoginGUI(self, window):
        window.destroy()
        from LoginGUI import LoginGUI
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
    
        os.remove(unknown_img_path)
    
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
            # self.cap.set(cv2.CAP_PROP_EXPOSURE, -3.0)
        self._label = label
        self.process_webcam()

    def UI(self):
        window = tk.Tk()
        xWindow = 514
        yWindow = 714
        ## Frame Tổng
        frameBiggest = utilView.frameUtil(window, xWindow, yWindow, 0, 0, bg='#ffffff')
        ### SETTINGS
        img = Image.open("Icon/image.png")
        tk_img = ImageTk.PhotoImage(img)

        # Tạo Label để hiển thị hình ảnh trong Frame
        label = tk.Label(frameBiggest, image=tk_img, bg='white')
        label.image = tk_img  # Giữ một tham chiếu để hình ảnh không bị hủy
        # label.bind("<Button-1>", lambda event: self.switchToLoginGUI(window))
        label.place(x=445, y=25)

        ### LABEL ngày tháng năm
        utilView.dateUtil(frameBiggest, 61, 37)

        ### LABEL Đồng Hồ
        utilView.clockUtil(frameBiggest, 61, 70)

        ### BUTTON ĐĂNG NHẬP
        utilView.cusButtonUtil(frameBiggest, 'Chấm Công', 80, 586, 357, 50, text_color='white',
                              fg_color='black', font=("", 13, "bold"), corner_radius=0, hover_color='#383838', command = lambda: self.chamCong())

        ### Label để add image
        webcam_label = utilView.labelUtil(window, None, 61, 142,width=393, height=379, bg='black')
        self.add_webcam(webcam_label)

        window.geometry(f"{xWindow}x{yWindow}+500+20")
        window.mainloop()

if __name__ == '__main__':
    may = MayChamCongGUI()
    may.UI()