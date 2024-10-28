import tkinter as tk
import utilView
import customtkinter as ctk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import datetime
import os

class ThongBaoGUI:
    
    def __init__(self):
        # Đường dẫn đến folder Icon
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.icon_dir = os.path.join(current_dir, '../Icon')
        self.notiWindow = None
        self.initUI()

    def initUI(self):
        notiWindow = tk.Toplevel()
        
        wWindow = 300
        hWindow = 380
        
        notiWindow.geometry(f"{wWindow}x{hWindow}+610+200")
        # notiWindow.overrideredirect(True)
        
        frameNoti = utilView.frameUtil(notiWindow, wWindow, hWindow, 0, 0, bg='#ffffff')

        titleNoti = tk.Label(frameNoti, text="THÔNG BÁO", foreground="black", bg='white', font=("Arial", 12, "bold"))
        titleNoti.place(x=100, y=9)

        # Body
        bodyNoti = tk.Frame(notiWindow, width=300, height=340, bg="#fff")
        bodyNoti.pack_propagate(False)
        bodyNoti.place(x=0, y=40)

        # Tạo canvas bên trong frame để thêm scrollbar
        canvas = tk.Canvas(bodyNoti, width=290, height=340)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Tạo scrollbar cho canvas 
        scrollbar = tk.Scrollbar(bodyNoti, orient="vertical", command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Kết nối canvas với scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)

        # Tạo một frame bên trong canvas để chứa các mục
        list_frame = tk.Frame(canvas)

        # Đặt frame này vào canvas
        canvas.create_window((0, 0), window=list_frame, anchor="nw")

        # Thêm các mục vào list_frame
        for i in range(20):  # Ví dụ với 20 mục
            item_text = f"Nhân viên #00{i + 1} đi trễ ca #012 -- 10p trước"
            item = tk.Label(list_frame, font=("Arial", 10), text=item_text, bg="#d9d9d9", width=290, height=3,
                            anchor="w", wraplength=290, justify="left", padx=5)
            item.pack(fill=tk.X, pady=(5, 5))
            self.hover(item)

        # Điều chỉnh kích thước canvas theo nội dung
        list_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        # Bắt sự kiện cuộn chuột
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))
        canvas.bind_all("<Button-4>", lambda event: canvas.yview_scroll(-1, "units"))  # Linux
        canvas.bind_all("<Button-5>", lambda event: canvas.yview_scroll(1, "units"))   # Linux

        notiWindow.mainloop()

    def enter_label(self, label, bgc):
        label.config(bg=bgc)

    def leave_label(self, label, bgc):
        label.config(bg=bgc)

    def hover(self, label):
        label.bind("<Enter>", lambda event: self.enter_label(label, "#FBF6F6"))
        label.bind("<Leave>", lambda event: self.leave_label(label, "#d9d9d9"))

if __name__ == '__main__':
    ThongBaoGUI()