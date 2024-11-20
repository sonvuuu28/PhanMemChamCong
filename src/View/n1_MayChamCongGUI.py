import tkinter as tk
import utilView
import customtkinter as ctk
from PIL import Image, ImageTk
import cv2
import os
import subprocess
from time import strftime
from datetime import datetime
import face_recognition
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)
from NhanVienDTO import NhanVienDTO

bus_dir = os.path.join(current_dir, '../BUS')
sys.path.append(bus_dir)
from NhanVienBUS import NhanVienBUS
from ChamCongBUS import ChamCongBUS

dao_dir = os.path.join(current_dir, '../DAO')
sys.path.append(dao_dir)
from NhanVienDAO import NhanVienDAO

class MayChamCongGUI:
    def __init__(self):
        # Đường dẫn đến folder Icon
        self.icon_dir = os.path.join(current_dir, '../Icon')
        
        self.ImageEmployee_dir = os.path.join(current_dir, '../../ImageEmployee')
        # self.ImageEmployee_dir = '../../ImageEmployee'
        if not os.path.exists(self.ImageEmployee_dir):
            os.mkdir(self.ImageEmployee_dir)
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

    def add_img_to_label(self, label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)

        self.anhCapture = self.most_recent_capture_arr.copy()

    def accept(self):
        name = self.tenAnh.get().strip()  # Loại bỏ khoảng trắng thừa
        if name == "":
            utilView.msg_boxUtil("Error!", f"Vui lòng nhập tên ảnh !")
            return
        print(name)

        # Xây dựng đường dẫn file
        image_path = os.path.join(self.ImageEmployee_dir, f"{name}.jpg")

        # Kiểm tra ảnh trùng tên
        if os.path.exists(image_path):
            utilView.msg_boxUtil("Error!", f"Tên ảnh '{name}' đã tồn tại. Vui lòng chọn tên khác.")
            return

        # Lưu ảnh nếu không trùng
        cv2.imwrite(image_path, self.anhCapture)
        utilView.msg_boxUtil("Success!", "Thêm ảnh vào kho!")
        
        # Đóng cửa sổ
        self.window_DangKy.destroy()
        
    def tryAgain(self):
        self.window_DangKy.destroy()

    def MoTrang_DangKyAnh(self):
        self.window_DangKy = tk.Toplevel(self.window)
        self.window_DangKy .transient(self.window)
        self.window_DangKy .grab_set()  # Đảm bảo focus luôn ở cửa sổ con
        xWindow = 514
        yWindow = 714
        self.window_DangKy.geometry(f"{xWindow}x{yWindow}+500+20")
        frameBiggest_TrangDangKy = utilView.frameUtil(self.window_DangKy, xWindow, yWindow, 0, 0, bg='white') 
        
        ### BUTTON CheckIn
        utilView.cusButtonUtil(frameBiggest_TrangDangKy, 'Đồng ý', 122, 560, 280, 40, text_color='white',
                              fg_color='#000000', font=("", 13, "bold"), corner_radius=5, hover_color='#383838', command=lambda: self.accept())

        ### BUTTON CheckOut
        utilView.cusButtonUtil(frameBiggest_TrangDangKy, 'Thử Lại', 122, 630, 280, 40, text_color='white',
                              fg_color='#CB2323', font=("", 13, "bold"), corner_radius=5, hover_color='#F23737', command=lambda: self.tryAgain())
        
        ### Label để add image
        self.capture_label = utilView.labelUtil(frameBiggest_TrangDangKy, None, 61, 132, width=393, height=379, bg='black')

        self.add_img_to_label(self.capture_label)

        utilView.labelUtil(frameBiggest_TrangDangKy,'NHẬP TÊN ẢNH:',61, 35, bg='#ffffff', font=("Arial", 14, 'bold'))
        self.tenAnh = utilView.entryUtil(frameBiggest_TrangDangKy, '', 81, 76, 30, font=("Arial", 11))
        utilView.lineUtil(frameBiggest_TrangDangKy, 41, 200, 100)
        self.tenAnh.focus_set()

    def compare_faces_in_folder(self, temp_image_path, folder_path):
        temp_image = face_recognition.load_image_file(temp_image_path)
        temp_face_encoding = face_recognition.face_encodings(temp_image)

        if len(temp_face_encoding) == 0:
            utilView.msg_boxUtil("Fail !", "Không phát hiện khuôn mặt !")
            return
        
        temp_face_encoding = temp_face_encoding[0]
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            
            if file_path.lower().endswith(('png', 'jpg', 'jpeg')):
                # Load ảnh trong folder
                image = face_recognition.load_image_file(file_path)
                face_encodings = face_recognition.face_encodings(image)

                # Kiểm tra nếu có khuôn mặt trong ảnh
                if len(face_encodings) > 0:
                    face_encoding = face_encodings[0]
                    
                    # So sánh khuôn mặt giữa ảnh tạm và ảnh trong folder
                    results = face_recognition.compare_faces([face_encoding], temp_face_encoding)

                    if results[0]:
                        try:
                            self.nv = NhanVienBUS.getInstance().TimKiem_Theo_Anh(filename)
                            utilView.msg_boxUtil("Success !", f"Xin chào {self.nv.get_Ten()}")
                            return True
                        except Exception as e:
                            utilView.msg_boxUtil("Success !", f"Ảnh bạn đã được đăng ký\nVui lòng thông báo quản lý để được xử lý !")

                        
    
    def checkIn(self):
        unknown_img_path = './.tmp.jpg'

        cv2.imwrite(unknown_img_path, self.most_recent_capture_arr)

        if self.compare_faces_in_folder(unknown_img_path, self.ImageEmployee_dir) == True:
            ChamCongBUS.getInstance().check_in_insert_BCC(self.nv.get_MaNhanVien())
        os.remove(unknown_img_path)
        
    def checkOut(self):
        unknown_img_path = './.tmp.jpg'

        cv2.imwrite(unknown_img_path, self.most_recent_capture_arr)

        if self.compare_faces_in_folder(unknown_img_path, self.ImageEmployee_dir) == True:
            ChamCongBUS.getInstance().check_out_insert_BCC(self.nv.get_MaNhanVien())
        os.remove(unknown_img_path)
    
    def dangKy(self):
        self.MoTrang_DangKyAnh()
        
    def UI(self):
        self.window = tk.Tk()
        xWindow = 514
        yWindow = 714
        
        # Đường dẫn đến folder Icon
        # icon_dir = os.path.join(self.current_dir, '../Icon')
        
        # Frame Tổng
        frameBiggest = utilView.frameUtil(self.window, xWindow, yWindow, 0, 0, bg='#ffffff')
        
        ### Label exit
        exitImage = Image.open(os.path.join(self.icon_dir, "exit.png"))
        exitImageHover = Image.open(os.path.join(self.icon_dir, "exitHover.png"))
        tk_exitImage = ImageTk.PhotoImage(exitImage)
        tk_exitImageHover = ImageTk.PhotoImage(exitImageHover)

        # Tạo Label để hiển thị hình ảnh trong Frame
        label_exit = tk.Label(frameBiggest, image=tk_exitImage, bg='white')
        label_exit.image = tk_exitImage
        label_exit.place(x=445, y=25)
        label_exit.bind("<Button-1>", lambda event: self.dangXuat("DangXuat", self.window))
        self.hover(label_exit, tk_exitImage, tk_exitImageHover, None)

        ### LABEL ngày tháng năm
        utilView.dateUtil(frameBiggest, 61, 37)

        ### LABEL Đồng Hồ
        utilView.clockUtil(frameBiggest, 61, 70)

        ### BUTTON CheckIn
        utilView.cusButtonUtil(frameBiggest, 'CHECKIN', 122, 560, 280, 40, text_color='white',
                              fg_color='black', font=("", 13, "bold"), corner_radius=5, hover_color='#383838', command=lambda: self.checkIn())

        ### BUTTON CheckOut
        utilView.cusButtonUtil(frameBiggest, 'CHECKOUT', 122, 630, 280, 40, text_color='white',
                              fg_color='#CB2323', font=("", 13, "bold"), corner_radius=5, hover_color='#F23737', command=lambda: self.checkOut())
        
        user_btn_image = Image.open(os.path.join(self.icon_dir, "user_Btn.png"))
        icon = ctk.CTkImage(user_btn_image, size=(20, 20))
        
        user_btn_image_hover = Image.open(os.path.join(self.icon_dir, "user_Btn_hover.png"))
        icon_hover = ctk.CTkImage(user_btn_image_hover, size=(20, 20))
        ### BUTTON register new user
        utilView.cusButtonUtil_Image(frameBiggest, '+', 420, 660, 10, 40, text_color='black', hover_text_color="#636363", fg_color='#D9D9D9', hover_fg_color='#CACACA',
                        font=("", 14, "bold"), corner_radius=100, image=icon, hover_image=icon_hover, command=lambda: self.dangKy() 
)
        ### Label để add image
        webcam_label = utilView.labelUtil(self.window, None, 61, 132, width=393, height=379, bg='black')
        self.add_webcam(webcam_label)

        self.window.geometry(f"{xWindow}x{yWindow}+500+20")
        self.window.mainloop()

if __name__ == '__main__':
    may = MayChamCongGUI()
    # may.UI()