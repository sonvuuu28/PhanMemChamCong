import tkinter as tk
from tkinter import ttk  # Import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import os
import sys

class LichSuChamCongGUI:
    def __init__(self):
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
    
    def backTrangChu(self, window):
        window.destroy()
        from n1_TrangChuGUI import TrangChuGUI
        TrangChuGUI()
        
    def UI(self):
        ## đường dẫn động đến Icon
        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_dir = os.path.join(current_dir, '../Icon')
        
        root = tk.Tk()
        root.title("Check In/Check Out System")
        root.geometry("1000x650+250+40")

        main_frame = tk.Frame(root)
        main_frame.pack(fill="both", expand=True)

        left_panel = tk.Frame(main_frame, bg="white")
        left_panel.grid(row=0, column=0, sticky="nsew")

        right_panel = tk.Frame(main_frame, bg="white")
        right_panel.grid(row=0, column=1, sticky="nsew")

        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
    
        
        # ----------------- Phần Bên Trái -----------------
        # Date selection
        # Thêm label nội dung trở về vào góc trái cùng
        homeImage = Image.open(os.path.join(icon_dir, "home.png"))
        tk_homeImage = ImageTk.PhotoImage(homeImage)
        homeImageHover = Image.open(os.path.join(icon_dir, "homeHover.png"))
        tk_homeImageHover = ImageTk.PhotoImage(homeImageHover)

        label_home = tk.Label(left_panel, image=tk_homeImage, bg='white')
        label_home.image = tk_homeImage
        label_home.place(x=30, y=30)
        label_home.bind("<Button-1>", lambda event: self.backTrangChu(root))
        self.hover(label_home, tk_homeImage, tk_homeImageHover, None)
        label_home.pack(side="top", anchor="sw", padx=10, pady=10)
        
        nv_label = tk.Label(left_panel, text="Nhân Viên:")
        nv_label.pack(pady=10)
        nv = tk.Entry(left_panel, width=20, bg='#E5E5E5')
        nv.pack(pady=5)
        
        date_label = tk.Label(left_panel, text="Ngày:")
        date_label.pack(pady=10)

        cal = DateEntry(left_panel, width=16, background="darkblue", foreground="white", borderwidth=2)
        cal.pack(pady=5)

        # Check-in time
        checkin_label = tk.Label(left_panel, text="Check in time:")
        checkin_label.pack(pady=10)

        checkin_time = tk.Label(left_panel, text="--:--", font=("Helvetica", 14))
        checkin_time.pack(pady=5)

        # Check-out time
        checkout_label = tk.Label(left_panel, text="Check out time:")
        checkout_label.pack(pady=10)

        checkout_time = tk.Label(left_panel, text="--:--", font=("Helvetica", 14))
        checkout_time.pack(pady=5)
        
        ## 

        # ----------------- Phần Bên Phải -----------------
        details_label = tk.Label(right_panel, text="Chi tiết lịch sử chấm công", font=("Helvetica", 16), bg="white")
        details_label.pack(pady=(20, 10))

        # Tạo bảng Treeview cho phần chi tiết chấm công
        columns = ('#1', '#2', '#3', '#4', '#5')

        tree = ttk.Treeview(right_panel, columns=columns, show='headings', height=5)
        tree.heading('#1', text='Mã')
        tree.heading('#2', text='Ngày')
        tree.heading('#3', text='Thời gian vào')
        tree.heading('#4', text='Thời gian ra')
        tree.heading('#5', text='Tình trạng')

        tree.column('#1', width=100, anchor='center')
        tree.column('#2', width=100, anchor='center')
        tree.column('#3', width=100, anchor='center')
        tree.column('#4', width=100, anchor='center')
        tree.column('#5', width=100, anchor='center')

        # Kẻ đường viền cho bảng
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))  # Định dạng tiêu đề
        style.configure("Treeview", rowheight=25)  # Chiều cao mỗi hàng

        # Dữ liệu mẫu
        data = [
            ('bcc','12/10/2023', '08:00', '17:00', 'đi trễ'),
            ('bcc', '13/10/2023', '08:10', '17:05', 'đúng giờ'),
            ('bcc','14/10/2023', '08:05', '16:55', 'về sớm')
        ]

        # Chèn dữ liệu vào bảng
        for row in data:
            tree.insert('', tk.END, values=row)

        tree.pack(pady=(0, 20), padx=30, fill='both', expand=True)  # Thêm khoảng cách

        # Time input fields
        time_in_label = tk.Label(right_panel, text="Thời gian vào:", bg="white")
        time_in_label.pack(pady=5)
        time_in_entry = tk.Entry(right_panel, width=20, bg='#E5E5E5')
        time_in_entry.pack(pady=5)

        time_out_label = tk.Label(right_panel, text="Thời gian ra:", bg="white")
        time_out_label.pack(pady=5)
        time_out_entry = tk.Entry(right_panel, width=20, bg='#E5E5E5')
        time_out_entry.pack(pady=5)

        # Edit button
        edit_button = tk.Button(right_panel, text="Sửa", width=10)
        edit_button.pack(pady=20)


        # Chạy ứng dụng
        root.mainloop()
        
if __name__ == '__main__':
    LichSuChamCongGUI()
