import tkinter as tk
import utilView
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkcalendar import DateEntry
import datetime
import os, sys



current_dir = os.path.dirname(os.path.abspath(__file__))
dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)
from GhiChuDTO import GhiChuDTO


bus_dir = os.path.join(current_dir, '../BUS')
sys.path.append(bus_dir)
from GhiChuBUS import GhiChuBUS

class GhiChuGUI:
    
    def __init__(self):
        # Đường dẫn đến folder Icon
        self.icon_dir = os.path.join(current_dir, '../Icon')
        
        self.ghichu_bus=GhiChuBUS.getInstance()
        self.isExist = False

         # đoạn này sẽ lấy 2 khoảng ngày theo tuần xếp lịch
        # fake điều kiện
        self.start_date_limit = datetime.date(2024, 11, 4)
        self.end_date_limit = datetime.date(2024, 11, 10)

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
        
       

        # Thêm DateEntry cho ngày bắt đầu với định dạng dd/mm/yyyy
        self.start_date = DateEntry(select_frame, width=12, background='darkblue', 
                                    foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
        self.start_date.pack(side="left", padx=10)
        # Đặt giá trị mặc định của DateEntry là rỗng
        self.start_date.delete(0, "end")
         # Bind sự kiện khi ngày được chọn
        self.start_date.bind("<<DateEntrySelected>>", lambda e : self.checkExist())
        # chỉ chọn ngày kh nhập ngày
        self.start_date.configure(state='readonly') 


        # Text Area với height=260
        self.contentNote = tk.Text(bodyNote, wrap=tk.WORD, font=("Arial", 11), highlightthickness=1)
        self.contentNote.place(x=10, y=40, width=280, height=220)  # Đặt Text area bên dưới DateEntry
        
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
            command=self.save_note_content
        )
        save_button.pack(side=tk.RIGHT, padx=(10,30))

        noteWindow.mainloop()

    def save_note_content(self):
         # Lấy ngày đã chọn từ DateEntry
        selected_date = self.start_date.get_date()

       
        # Kiểm tra xem ngày chọn có nằm trong khoảng từ 2024-11-04 đến 2024-11-10 không
        if self.start_date_limit > selected_date or selected_date > self. end_date_limit:
            messagebox.showerror("Lỗi", f"Ngày đã chọn không nằm trong khoảng từ {self.start_date_limit} đến {self.end_date_limit}!")
            return


        content = self.contentNote.get("1.0", tk.END).strip()
        if not content:
            messagebox.showerror("Lỗi", "Nội dung ghi chú không được để trống")
            
            return
        
        if self.isExist:
            gc_Dto_update = GhiChuDTO(self.dataCheckExist.get_MaGC(),self.dataCheckExist.get_Ngay(), content)
            kq = self.ghichu_bus.update(gc_Dto_update)
            messagebox.showinfo("Thông báo", kq)
        
        else:
            gc_Dto = GhiChuDTO("",selected_date, content)
            check = self.ghichu_bus.add(gc_Dto)
            messagebox.showinfo("Thông báo", check)
        self.reset()

    def reset(self):
        # Đặt lại DateEntry về start_date_limit
        # Đặt giá trị mặc định của DateEntry là rỗng
        self.start_date.configure(state='normal') 
        self.start_date.delete(0, "end")
        self.start_date.configure(state='readonly') 
            # Làm trống text area
        self.contentNote.delete("1.0", tk.END)
        self.isExist = False
    def checkExist(self):
         # Lấy ngày đã chọn từ DateEntry
        selected_date = self.start_date.get_date()

        # Kiểm tra xem ngày chọn có nằm trong khoảng từ 2024-11-04 đến 2024-11-10 không
        if self.start_date_limit > selected_date or selected_date > self. end_date_limit:
            messagebox.showerror("Lỗi", f"Ngày đã chọn không nằm trong khoảng từ {self.start_date_limit} đến {self.end_date_limit}!")
            return


        #  nếu tồn tại ghi chú
        self.dataCheckExist = self.ghichu_bus.timkiemtheoNgay(selected_date)
        if self.dataCheckExist:
            self.isExist = True
            confirm = messagebox.askyesno("Xác nhận", "Ghi chú đã được tạo. Bạn xem/ sửa không?")
            if confirm:
                # Nếu người dùng chọn "Yes", thực hiện các hành động
                # Xóa nội dung cũ trước khi thêm nội dung mới
                self.contentNote.delete("1.0", tk.END)
                # Chèn nội dung mới vào Text widget
                self.contentNote.insert("1.0", self.dataCheckExist.get_NoiDung())
            else:
                self.reset()
        else:
            self.isExist = False
            self.contentNote.delete("1.0", tk.END)


if __name__ == '__main__':
    aa = GhiChuGUI()
