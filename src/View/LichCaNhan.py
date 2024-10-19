import tkinter as tk
import utilView
import customtkinter as ctk
import datetime
import random
from tkcalendar import Calendar
from tkcalendar import DateEntry
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk

class LichLamCaNhanGUI:
    def __init__(self):
        self.myPath = "C:\\Users\\X\\HocPython\\PJ\\Test\\src\\"
        self.initUI()

    def initUI(self):
        scheduleWindow = tk.Tk()
        wWindow = 1000
        hWindow = 650
        scheduleWindow.geometry(f"{wWindow}x{hWindow}")
        frameSchedule = utilView.frameUtil(scheduleWindow, wWindow, hWindow, 0, 0, bg = '#ffffff')
        
        # Tạo frame cho header
        headerSchedule = tk.Frame(frameSchedule, width=1000, height=40, bg="#908181")
        headerSchedule.pack(pady=(10, 0), fill='x')
        headerSchedule.pack_propagate(False)  # Không thay đổi kích thước theo nội dung
       
        titleSchedule = tk.Label(headerSchedule, text="LỊCH LÀM CÁ NHÂN", font=("Arial", 16, "bold"), bg="#908181", fg="black")
        titleSchedule.pack(side="left", expand=True)  # Căn giữa bên trái

        self.close_icon = ImageTk.PhotoImage(file=self.myPath + "Icon\\close.png")
        close_button = tk.Button(headerSchedule, image=self.close_icon, height=40, width=40,bg="#908181", bd=0, command=scheduleWindow.destroy)
        close_button.pack(side="right")  # Đặt nút bên phải của header



        

    
        body_height = hWindow - 60 - 180 - 10  # -60:header -180:footer - 10:paddingBody = 400

        body = tk.Frame(frameSchedule, width=980, height=body_height, bg="#fff")
        body.pack(pady=(10, 0), padx=10, fill='both') 
        body.pack_propagate(False)

        # Phần trên của body: Chọn tháng và năm
        select_frame = tk.Frame(body, width=480, height=40, bg="#fff")
        select_frame.pack(pady=(0,10), anchor="e")
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


        # Nút Xem lương với các yêu cầu đặc biệt
        view_button = ctk.CTkButton(
            select_frame, 
            text="Xem", 
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
            frameSchedule, 
            width=980, height=170, 
            bg="#fff", highlightbackground="gray",  # Màu viền là #000 (đen)
            highlightthickness=1,        # Độ dày viền là 1px
            bd=0 
        )
        footer.pack(pady=(10, 0), padx=10, fill='x')  # Padding giữa footer và body là 10px
        footer.pack_propagate(False)


        # Frame bên trái của footer (phần còn lại của footer)
        left_footer_frame = tk.Frame(footer,width=780, bg="#fff")
        left_footer_frame.pack(side="left", fill='both', anchor="w")  # Chiếm hết phần còn lại của footer
        left_footer_frame.pack_propagate(False)

        
        # Cấu hình cột để chúng giãn đều
        left_footer_frame.grid_columnconfigure(0, weight=1)
        left_footer_frame.grid_columnconfigure(1, weight=1)

       # Hàng đầu tiên (Nhân viên) và thứu 2
        inpEmployee=utilView.create_input_with_label_v2(left_footer_frame, "Nhân viên:", 0, 0) 
        inpMon=utilView.create_input_with_label_v2(left_footer_frame, "Thứ 2:", 0,2) 

        # Hàng thứ 2 (Thứ 3 và Thứ4)
        inpTues=utilView.create_input_with_label_v2(left_footer_frame, "Thứ 3:", 1, 0) 
        inpWed=utilView.create_input_with_label_v2(left_footer_frame, "Thứ 4:", 1, 2) 

        # Hàng thứ 3 (Thứ 5 và Thứ 6)
        inpThur=utilView.create_input_with_label_v2(left_footer_frame, "Thứ 5:", 2, 0) 
        inpFri=utilView.create_input_with_label_v2(left_footer_frame, "Thứ 6:", 2, 2)  

        # Hàng thứ 4 (Thứ 7 và CN)
        inpSat=utilView.create_input_with_label_v2(left_footer_frame, "Thứ 7:", 3, 0) 
        inpSun=utilView.create_input_with_label_v2(left_footer_frame, "Chủ nhật:", 3, 2) 




        # Frame bên phải của footer, width=200 và chiều cao bằng footer
        right_footer_frame = tk.Frame(footer, width=200, height=170)
        right_footer_frame.pack(side="right", fill='y')  # Căn phải và giữ nguyên chiều cao của footer
        right_footer_frame.pack_propagate(False)


        # Tạo các nút Thêm, Sửa, Xóa với chiều rộng 160px, chiều cao 30px
        add_button =  ctk.CTkButton(
            right_footer_frame, 
            text="Thêm", width=160, height=30,
            fg_color="#000",  # Màu nền
            text_color="#fff",  # Màu chữ
            font=("Arial", 12, "bold"),  # Font chữ
            corner_radius=4,  # Bo góc 4px
            border_width=0,  # Không có viền
            hover_color="#383838"
        )
        edit_button = ctk.CTkButton(
            right_footer_frame, 
            text="Sửa", width=160, height=30,
            fg_color="#000",  # Màu nền
            text_color="#fff",  # Màu chữ
            font=("Arial", 12, "bold"),  # Font chữ
            corner_radius=4,  # Bo góc 4px
            border_width=0,  # Không có viền
            hover_color="#383838"
        )
        delete_button = ctk.CTkButton(
            right_footer_frame, 
            text="Xoá", width=160, height=30,
            fg_color="#000",  # Màu nền
            text_color="#fff",  # Màu chữ
            font=("Arial", 12, "bold"),  # Font chữ
            corner_radius=4,  # Bo góc 4px
            border_width=0,  # Không có viền
            hover_color="#383838"
        )

        # Đặt các nút theo chiều dọc
        add_button.pack(pady=(10, 5))  # Khoảng cách phía trên là 10, phía dưới là 5
        edit_button.pack(pady=5)       # Khoảng cách đều nhau giữa các nút
        delete_button.pack(pady=5)


        self.add_row_to_table(self.start_date.get_date())

        scheduleWindow.mainloop()


    def show_selected_dates(self):
        """Xác thực ngày bắt đầu và ngày kết thúc."""
        start_date = self.start_date.get_date()
        end_date = self.end_date.get_date()

        # Kiểm tra xem ngày bắt đầu có phải là thứ Hai không
        if start_date.weekday() != 0:  # 0 là thứ Hai
            messagebox.showerror("Lỗi", "Ngày bắt đầu phải là thứ Hai.")
            return

        # Tính ngày Chủ Nhật của tuần kế tiếp
        next_sunday = start_date + datetime.timedelta(days=6)  # Chủ Nhật tuần hiện tại

        # Nếu ngày kết thúc không phải là Chủ Nhật của tuần kế tiếp
        if end_date != next_sunday:
            messagebox.showerror("Lỗi", "Ngày kết thúc phải là Chủ Nhật đứng sau gần nhất.")
            return

        # Nếu hợp lệ

         # Thêm hàng vào bảng
        self.add_row_to_table(start_date)
        # todooo call data
        messagebox.showinfo("Thông báo", f"Khoảng thời gian từ {start_date} đến {end_date} hợp lệ.")

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

        # Tạo dữ liệu hàng đầu tiên
        row_data = ["", "", *day_strings]  # Dữ liệu cho hàng đầu tiên
        self.table.insert("", "end", values=row_data)  # Thêm vào bảng
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
        # Xóa tất cả dữ liệu trong bảng trước khi thêm dữ liệu mới
        # for item in self.table.get_children():
        #     self.table.delete(item)

        # Các khung giờ bắt đầu cho ca làm
        start_times = list(range(9, 24))  # Khung giờ từ 9h đến 24h
        shift_durations = [4, 6, 8]  # Thời gian mỗi ca: 4, 6 hoặc 8 tiếng

        # Thêm 10 hàng dữ liệu ngẫu nhiên
        for i in range(1, 10):
            # Random mã nhân viên và họ tên
            employee_id = f"NV{random.randint(100, 999)}"
            employee_name = random.choice(["Nguyễn Văn A", "Trần Thị B", "Lê Văn C", "Phạm Minh D", "Hoàng Thị E"])

            # Tạo danh sách ca làm ngẫu nhiên từ thứ 2 đến Chủ Nhật
            shifts = []
            for _ in range(7):
                # Random thời gian bắt đầu ca
                start_time = random.choice(start_times)
                duration = random.choice(shift_durations)
                end_time = start_time + duration

                # Nếu thời gian vượt quá 24h, giới hạn lại
                if end_time > 24:
                    end_time = 24

                # Format thời gian ca làm thành chuỗi "HH:00-HH:00"
                shift_time = f"{start_time:02d}:00-{end_time:02d}:00"
                shifts.append(shift_time)

            # Tạo dữ liệu hàng với mã số nhân viên, họ tên, và ca làm
            row_data = (i, f"{employee_id} - {employee_name}") + tuple(shifts)
            self.table.insert("", "end", values=row_data)

if __name__ == "__main__":
    lich_lam = LichLamCaNhanGUI() 