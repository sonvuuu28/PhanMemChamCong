import tkinter as tk
import utilView
import customtkinter as ctk
import datetime
import random
from n6_AddShiftModal import AddShiftModal
from tkcalendar import DateEntry
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import os

class LichLamViecGUI:
    def __init__(self):
        # Đường dẫn đến folder Icon
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.icon_dir = os.path.join(current_dir, '../Icon')
        self.initUI()

    def initUI(self):
        self.schedule_window = tk.Tk()
        wWindow = 1000
        hWindow = 650
        self.schedule_window.geometry(f"{wWindow}x{hWindow}+250+40")
        schedule_frame = utilView.frameUtil(self.schedule_window, wWindow, hWindow, 0, 0, bg = '#ffffff')
        
        # Tạo frame cho header
        header = tk.Frame(schedule_frame, width=1000, height=40, bg="white")
        header.pack(pady=(10, 0), fill='x')
        header.pack_propagate(False)  # Không thay đổi kích thước theo nội dung
       
        title = tk.Label(header, text="LỊCH LÀM VIỆC", font=("Arial", 18, "bold"), bg="white", fg="black")
        title.pack(side="right", expand=True)  # Căn giữa bên trái

        ## nút home
        homeImage = Image.open(os.path.join(self.icon_dir, "home.png"))
        tk_homeImage = ImageTk.PhotoImage(homeImage)
        homeImageHover = Image.open(os.path.join(self.icon_dir, "homeHover.png"))
        tk_homeImageHover = ImageTk.PhotoImage(homeImageHover)

        label_home = tk.Label(schedule_frame, image=tk_homeImage, bg='white')
        label_home.image = tk_homeImage
        label_home.place(x=30, y=10)
        label_home.bind("<Button-1>", lambda event: self.back_TrangChu(self.schedule_window))
        self.hover(label_home, tk_homeImage, tk_homeImageHover, None)

        hBody = hWindow - 80 - 180 - 10  # -80:header -180:footer - 10:paddingBody = 400

        body = tk.Frame(schedule_frame, width=980, height=hBody, bg="#fff")
        body.pack(pady=(10, 0), padx=10, fill='both') 
        body.pack_propagate(False)

        # Frame chứa cả select_frame và features_frame
        top_frame = tk.Frame(body, width=980, height=60, bg="#fff")
        top_frame.pack(fill="x")
        top_frame.pack_propagate(False)

        # Phần trên của body: Chọn tháng và năm
        select_frame = tk.Frame(top_frame, width=480, height=40, bg="#fff")
        select_frame.pack(pady=(0,10), side="right")
        select_frame.pack_propagate(False)
        # Thay phần chọn ngày
        tk.Label(select_frame, text="Thời gian:", font=("Arial", 11), bg="#fff").pack(side="left", padx=10)
        
       
        # Tính toán ngày bắt đầu và kết thúc của tuần hiện tại
        today = datetime.date.today()
        start_of_week = today - datetime.timedelta(days=today.weekday())  # Thứ 2 của tuần
        end_of_week = start_of_week + datetime.timedelta(days=6)  # Chủ nhật của tuần

        # Thêm DateEntry cho ngày bắt đầu với định dạng dd/mm/yyyy
        self.start_date = DateEntry(select_frame, width=12, background='darkblue', 
                                    foreground='white', borderwidth=2, 
                                    year=start_of_week.year, month=start_of_week.month, 
                                    day=start_of_week.day, date_pattern='dd/mm/yyyy')
        self.start_date.pack(side="left", padx=10)

        tk.Label(select_frame, text="đến", font=("Arial", 11), bg="#fff").pack(side="left", padx=10)

        # Thêm DateEntry cho ngày kết thúc với định dạng dd/mm/yyyy
        self.end_date = DateEntry(select_frame, width=12, background='darkblue', 
                                  foreground='white', borderwidth=2, 
                                  year=end_of_week.year, month=end_of_week.month, 
                                  day=end_of_week.day, date_pattern='dd/mm/yyyy')
        self.end_date.pack(side="left", padx=10)


        # Nút Xem lịch
        view_button = ctk.CTkButton(
            select_frame, 
            text="Xem lịch", 
            width=100, 
            height=30, 
            fg_color="#000",  # Màu nền
            text_color="#fff",  # Màu chữ
            font=("Arial", 12),  # Font chữ
            corner_radius=4,  # Bo góc 4px
            border_width=0,  # Không có viền
            hover_color="#383838",
            command=self.show_selected_dates
           
        )
        view_button.pack(side="left", padx=(10,0))


        # Table bên dưới phần chọn tháng và năm
        self.create_table(body)


        

        # Tạo footer frame với kích thước 990x40 và paddingX=10
        footer = tk.Frame(
            schedule_frame, 
            width=980, height=170, 
            bg="#fff", highlightbackground="gray",  # Màu viền là #000 (đen)
            highlightthickness=1,        # Độ dày viền là 1px
            bd=0 
        )
        footer.pack(pady=(10, 0), padx=10, fill='x')  # Padding giữa footer và body là 10px
        footer.pack_propagate(False)


        # Frame bên trái của footer (phần còn lại của footer)
        left_footer_frame = tk.Frame(footer,width=780, bg="blue")
        left_footer_frame.pack(side="left", fill='both', anchor="w")  # Chiếm hết phần còn lại của footer
        left_footer_frame.pack_propagate(False)

        # Thêm bảng vào left_footer_frame
        self.create_footer_table(left_footer_frame) 
       


        # Frame bên phải của footer, width=200 và chiều cao bằng footer
        right_footer_frame = tk.Frame(footer, width=200, height=170)
        right_footer_frame.pack(side="right", fill='y')  # Căn phải và giữ nguyên chiều cao của footer
        right_footer_frame.pack_propagate(False)


        # Tạo các nút Thêm, Sửa, Xóa với chiều rộng 160px, chiều cao 30px
        arrange_shift_btn =  ctk.CTkButton(
            right_footer_frame, 
            text="Xếp ca làm", width=160, height=30,
            fg_color="#000",  # Màu nền
            text_color="#fff",  # Màu chữ
            font=("Arial", 12, "bold"),  # Font chữ
            corner_radius=4,  # Bo góc 4px
            border_width=0,  # Không có viền
            hover_color="#383838",
            command=self.open_add_shift_modal
        )
        create_shift_btn = ctk.CTkButton(
            right_footer_frame, 
            text="Tạo ca làm", width=160, height=30,
            fg_color="#000",  # Màu nền
            text_color="#fff",  # Màu chữ
            font=("Arial", 12, "bold"),  # Font chữ
            corner_radius=4,  # Bo góc 4px
            border_width=0,  # Không có viền
            hover_color="#383838",
            command= lambda : self.show_shift_window()
        )
        # delete_button = ctk.CTkButton(
        #     right_footer_frame, 
        #     text="Xoá", width=160, height=30,
        #     fg_color="#000",  # Màu nền
        #     text_color="#fff",  # Màu chữ
        #     font=("Arial", 12, "bold"),  # Font chữ
        #     corner_radius=4,  # Bo góc 4px
        #     border_width=0,  # Không có viền
        #     hover_color="#383838"
           
        # )

        # Đặt các nút theo chiều dọc
        arrange_shift_btn.pack(pady=(10, 5))  # Khoảng cách phía trên là 10, phía dưới là 5
        create_shift_btn.pack(pady=5)       # Khoảng cách đều nhau giữa các nút
        # delete_button.pack(pady=5)


        self.add_row_to_table(self.start_date.get_date())

        self.schedule_window.mainloop()
        
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
        
    def back_TrangChu(self, window):
            window.destroy()
            from n1_TrangChuGUI import TrangChuGUI
            TrangChuGUI()
    
    def show_shift_window(self):
        print("Tạo Ca Làm")
        self.schedule_window.destroy()
        from n6_CaLamGUI import ShiftGUI
        ShiftGUI()

    def open_add_shift_modal(self):
        AddShiftModal(self.schedule_window)

    def add_sample_footer_rows(self):
        """Thêm dữ liệu mẫu vào bảng của footer."""
        shift_data = [
            ("Ca 1", "09:00", "13:00"),
            ("Ca 2", "13:00", "17:00"),
            ("Ca 3", "17:00", "21:00")
        ]

        for shift in shift_data:
            self.footer_table.insert("", "end", values=shift)
    
    def create_footer_table(self, parent_frame):
        """Tạo bảng dưới phần left footer với thanh cuộn nếu vượt quá chiều cao."""
        columns = ("Ca làm", "Thời gian vào", "Thời gian ra")

        # Tạo khung cho Treeview và Scrollbar
        table_frame = tk.Frame(parent_frame, width=780, height=170)
        table_frame.pack(fill='both', expand=True)

        # Tạo Scrollbar
        scrollbar = tk.Scrollbar(table_frame)
        scrollbar.pack(side='right', fill='y')

        # Tạo Treeview với các cột
        self.footer_table = ttk.Treeview(table_frame, columns=columns, show="headings", height=7, yscrollcommand=scrollbar.set)
        self.footer_table.pack(side='left', fill='both', expand=True)

        # Kết nối thanh cuộn với Treeview
        scrollbar.config(command=self.footer_table.yview)

        # Đặt tiêu đề cho các cột
        self.footer_table.heading("Ca làm", text="Ca làm")
        self.footer_table.heading("Thời gian vào", text="Thời gian vào")
        self.footer_table.heading("Thời gian ra", text="Thời gian ra")

        # Đặt kích thước cột
        self.footer_table.column("Ca làm", width=200, anchor='center')
        self.footer_table.column("Thời gian vào", width=250, anchor='center')
        self.footer_table.column("Thời gian ra", width=250, anchor='center')

        # Thêm dữ liệu mẫu
        self.add_sample_footer_rows()    

    def show_selected_dates(self):
        """Xác thực ngày bắt đầu và ngày kết thúc."""
        start_date = self.start_date.get_date()
        end_date = self.end_date.get_date()

        # Kiểm tra xem ngày bắt đầu có phải là thứ Hai không
        if start_date.weekday() != 0:  # 0 là thứ Hai
            messagebox.showerror("Lỗi", "Ngày bắt đầu phải là thứ Hai.")
            return

        # Tính ngày Chủ Nhật của tuần kế tiếp
        curr_sunday = start_date + datetime.timedelta(days=6)  # Chủ Nhật tuần hiện tại

        # Nếu ngày kết thúc không phải là Chủ Nhật của tuần hiện tại
        if end_date != curr_sunday:
            messagebox.showerror("Lỗi", "Ngày kết thúc phải là Chủ Nhật đứng sau gần nhất.")
            return

        # Nếu hợp lệ
        today = datetime.date.today()
        days_until_sunday = 6 - today.weekday()
        now_sunday = today + datetime.timedelta(days=days_until_sunday)
        
        if start_date > now_sunday:
             # Nếu bắt đầu từ tuần tiếp theo và kết thúc là Chủ Nhật của tuần kế tiếp
            confirm = messagebox.askyesno(
                "Xác nhận",
                "Bạn có muốn tạo lịch cho tuần tiếp theo không?"
            )
            if confirm:
                # //todooo
                messagebox.showinfo("Thông báo", f"Tạo lịch mới cho tuần sau")
                 # Xóa tất cả dữ liệu trong bảng trước khi thêm hàng mới
                for item in self.table.get_children():
                    self.table.delete(item)
                return
            else:
                return  # Người dùng chọn "No", không làm gì cả
            
        # Thêm hàng vào bảng
        self.add_row_to_table(start_date)
        # todooo call data
        messagebox.showinfo("Thông báo", f"Xem lịch thời gian từ {start_date} đến {end_date} hợp lệ.")

    def readonly_comboboxes(self):
        """Set các Combobox thành trạng thái 'readonly'."""
        self.month_cb.config(state="readonly")  # Tắt chức năng chọn tháng
        self.year_cb.config(state="readonly")   # Tắt chức năng chọn năm
        self.date_range_cb.config(state="readonly")  # Tắt chức năng chọn khoảng thời gian

    def add_row_to_table(self, start_date):
        # Xóa tất cả dữ liệu trong bảng trước khi thêm hàng mới
        for item in self.table.get_children():
            self.table.delete(item)

        """Thêm hàng đầu tiên vào bảng với các ngày từ thứ Hai đến Chủ Nhật."""
        days = [start_date + datetime.timedelta(days=i) for i in range(7)]  # Các ngày từ thứ Hai đến Chủ Nhật
        day_strings = [day.strftime("%d/%m") for day in days]  # Định dạng ngày dd/mm

        # Tạo dữ liệu hàng đầu tiên(ngày tương ứng thứ)
        row_data = ["", "", *day_strings]  # Dữ liệu cho hàng đầu tiên
        self.table.insert("", "end", values=row_data)  # Thêm vào bảng
        
        # fake data
        self.add_random_rows_to_table()

    def create_table(self, parent_frame):
        """Tạo bảng dưới phần select_frame với thanh cuộn nếu vượt quá chiều cao."""
        columns = ("STT", "Nhân viên", "Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ nhật")

        # Tạo khung cho Treeview và Scrollbar
        table_frame = tk.Frame(parent_frame)
        table_frame.pack(fill='both', expand=True)

        # Tạo Scrollbar
        scrollbar = tk.Scrollbar(table_frame)
        scrollbar.pack(side='right', fill='y')

        # Tạo Treeview với các cột
        self.table = ttk.Treeview(table_frame, columns=columns, show="headings", height=10, yscrollcommand=scrollbar.set)
        self.table.pack(side='left', fill='both', expand=True)

        # Kết nối thanh cuộn với Treeview
        scrollbar.config(command=self.table.yview)

        w = 980
        col_1 = 980 // 28
        col_5 = col_1 * 5
        col_3 = col_1 * 3

        # Đặt tiêu đề cho các cột
        self.table.heading("STT", text="STT")
        self.table.column("STT", width=col_1, anchor='center')  # STT chiếm 1 cột

        self.table.heading("Nhân viên", text="Nhân viên")
        self.table.column("Nhân viên", width=col_5, anchor='w')  # Nhân viên chiếm 5 cột
        # Các cột thứ 2 đến chủ nhật
        for col in columns[2:]:
            self.table.heading(col, text=col)
            self.table.column(col, width=col_3, anchor='center')  # Mỗi ngày trong tuần chiếm 3 cột


    # hàm này dùng render data fake 
    def add_random_rows_to_table(self):
        """Thêm 10 hàng với dữ liệu ngẫu nhiên vào bảng."""
        # Các giá trị ca làm có thể random
        shift_options = ["OFF", "Ca 1", "Ca 2", "Ca 3"]
        
        # Tạo dữ liệu ngẫu nhiên cho 10 hàng
        row_count = 4  # Số lượng hàng ngẫu nhiên cần thêm

        for i in range(1, row_count + 1):
            employee_id = f"NV{random.randint(100, 999)}"
            employee_name = random.choice(["Nguyễn Văn A", "Trần Thị B", "Lê Văn C", "Phạm Minh D", "Hoàng Thị E"])
            shifts = [random.choice(shift_options) for _ in range(7)]
            row_data = (i, f"{employee_id} - {employee_name}") + tuple(shifts)
            self.table.insert("", "end", values=row_data)

       # Nếu không có hàng nào trong bảng, thay đổi cấu trúc bảng để hiển thị thông báo
        if len(self.table.get_children()) == 1:
            # Thêm tag cho hàng thông báo
            self.table.insert("", "end", values=("Lịch làm không tồn tại", "", "", "", "", "", "", "", ""))
    
    


if __name__ == "__main__":
    lich_lam = LichLamViecGUI() 



    # !note: phần chọn khoảng thời gian (mặc định sẽ hiện thời gian tuần tới), chọn tuần tiếp theo( xếp nhiều tuần) để xếp lịch
    # sau khi chọn tuần hợp lí rồi thì ấn tạo mới