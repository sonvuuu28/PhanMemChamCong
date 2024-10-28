import tkinter as tk
import utilView
import customtkinter as ctk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import datetime
import os

class GhiChuGUI:
    
    def __init__(self):
        # Đường dẫn đến folder Icon
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.icon_dir = os.path.join(current_dir, '../Icon')
        
        # self.noteWindow = None
        
        self.initUI()

    def initUI(self):
        # Khởi tạo cửa sổ
        noteWindow = tk.Toplevel()
        wWindow = 300
        hWindow = 380

        noteWindow.geometry(f"{wWindow}x{hWindow}+610+200")
        # noteWindow.overrideredirect(True)

        # Header
        headerNote = tk.Frame(noteWindow, width=wWindow, height=40, bg='#908181')
        headerNote.pack_propagate(False)
        headerNote.pack(side=tk.TOP, fill=tk.X)

        # Tiêu đề căn giữa
        titleNote = tk.Label(headerNote, text="GHI CHÚ", foreground="black", bg='#908181', font=("Arial", 12, "bold"))
        titleNote.pack(anchor="center", expand=True, pady=5)

        # Body
        bodyNote = tk.Frame(noteWindow, width=wWindow, height=270, bg="#fff")
        bodyNote.pack_propagate(False)
        bodyNote.pack(side=tk.TOP, fill=tk.X)

         # Phần trên của body: Chọn tháng và năm
        select_frame = tk.Frame(bodyNote, width=300, height=40, bg="#fff")
        select_frame.pack(anchor="e")
        select_frame.pack_propagate(False)

        tk.Label(select_frame, text="Thời gian:", font=("Arial", 11), bg="#fff").pack(side="left", padx=10)
        
       
        # Tính toán ngày bắt đầu và kết thúc của tuần hiện tại
        today = datetime.date.today()
        start_of_week = today - datetime.timedelta(days=today.weekday())  # Thứ 2 của tuần

        # Thêm DateEntry cho ngày bắt đầu với định dạng dd/mm/yyyy
        self.start_date = DateEntry(select_frame, width=12, background='darkblue', 
                                    foreground='white', borderwidth=2, 
                                    year=start_of_week.year, month=start_of_week.month, 
                                    day=start_of_week.day, date_pattern='dd/mm/yyyy')
        self.start_date.pack(side="left", padx=10)




        # Text Area với height=260
        contentNote = tk.Text(bodyNote, wrap=tk.WORD, font=("Arial", 11), highlightthickness=1)
        contentNote.place(x=10, y=40, width=280, height=220)  # Đặt Text area bên dưới DateEntry

        # Footer
        footerNote = tk.Frame(noteWindow, width=wWindow, height=60, bg="#fff")
        footerNote.pack_propagate(False)
        footerNote.pack(side=tk.BOTTOM, fill=tk.X, pady=(0,10))

        # Nút Hủy căn trái dùng customtkinter
        cancel_button = ctk.CTkButton(footerNote, 
            text="Hủy",
            width=100, height=30, 
            fg_color="#000",  # Màu nền
            text_color="#fff",  # Màu chữ
            font=("Arial", 12),  # Font chữ
            corner_radius=4,  # Bo góc 4px
            border_width=0,  # Không có viền
            hover_color="#383838", 
            command=noteWindow.destroy
        )
        cancel_button.pack(side=tk.LEFT, padx=(30,10))

        # Nút Lưu căn phải dùng customtkinter
        save_button = ctk.CTkButton(footerNote, 
            text="Lưu", 
            width=100, height=30, 
            fg_color="#000",  # Màu nền
            text_color="#fff",  # Màu chữ
            font=("Arial", 12),  # Font chữ
            corner_radius=4,  # Bo góc 4px
            border_width=0,  # Không có viền
            hover_color="#383838", 
            command=lambda: self.save_note_content(contentNote)
        )
        save_button.pack(side=tk.RIGHT, padx=(10,30))

        noteWindow.mainloop()

    def save_note_content(self, text_widget):
        """Lưu nội dung ghi chú từ Text widget"""
        content = text_widget.get("1.0", tk.END).strip()
        print(f"Nội dung ghi chú: {content}")  # Tạm thời in ra để kiểm tra, có thể lưu vào file hay cơ sở dữ liệu

if __name__ == '__main__':
    GhiChuGUI()