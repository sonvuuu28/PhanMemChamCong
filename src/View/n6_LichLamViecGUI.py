import tkinter as tk
import utilView
import customtkinter as ctk
import datetime
from n9_EditShiftModal import EditShiftModal
from n6_AddShiftModal import AddShiftModal
from  customtkinter import CTkImage 
from tkcalendar import DateEntry
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import os, sys



current_dir = os.path.dirname(os.path.abspath(__file__))
dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)
from CaLamDTO import CaLamDTO
from NhanVienDTO import NhanVienDTO


bus_dir = os.path.join(current_dir, '../BUS')
sys.path.append(bus_dir)
from CaLamBUS import CaLamBUS
from LichLamBUS import LichLamBUS
from NhanVienBUS import NhanVienBUS



class LichLamViecGUI:
    def __init__(self):
        # Đường dẫn đến folder Icon
        self.icon_dir = os.path.join(current_dir, '../Icon')

        self.cl_bus = CaLamBUS.getInstance()
        self.ll_bus = LichLamBUS.getInstance()
        
        self.is_create_new_schedule = False
        self.is_edit_schedule= False
        self.schedule_list_build = None

        self.initUI()
        
        # init data
        self.data_shifts = self.cl_bus.getall()
        self.data_schedules = self.ll_bus.getallbydate(self.start_date.get_date(), self.end_date.get_date())

        self.dataEdit = None

        self.render_table_shift(self.data_shifts)    
        self.render_table_schedule(self.data_schedules)

        self.schedule_window.mainloop()


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
        select_frame = tk.Frame(top_frame, width=530, height=40, bg="#fff")
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

        self.start_date.configure(state="readonly")
        self.end_date.configure(state="readonly")



        # Nút Xem 
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
        # nút refreshh
        refreshIcon = Image.open(os.path.join(self.icon_dir, "reload.png"))
        tk_refreshIcon = CTkImage(refreshIcon)
        refresh_button = ctk.CTkButton(
            select_frame, 
            image=tk_refreshIcon, 
            text="", 
            width=50, 
            height=24, 
            fg_color="#fff",  # Màu nền
            corner_radius=4,  # Bo góc 4px
            border_width=1,  # Không có viền
            hover_color="#d4d0c7",
            command=self.refresh
        )
        
        view_button.pack(side="left", padx=(10,0))
        refresh_button.pack(side="left", padx=(10,0))

        # Table lịch làm
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
            text="Quản lí ca làm", width=160, height=30,
            fg_color="#000",  # Màu nền
            text_color="#fff",  # Màu chữ
            font=("Arial", 12, "bold"),  # Font chữ
            corner_radius=4,  # Bo góc 4px
            border_width=0,  # Không có viền
            hover_color="#383838",
            command= lambda : self.show_shift_window()
        )
        edit_shift_btn = ctk.CTkButton(
            right_footer_frame, 
            text="Sửa ca làm", width=160, height=30,
            fg_color="#000",  # Màu nền
            text_color="#fff",  # Màu chữ
            font=("Arial", 12, "bold"),  # Font chữ
            corner_radius=4,  # Bo góc 4px
            border_width=0,  # Không có viền
            hover_color="#383838",
            command= self.open_edit_shift_modal
        )
        

        # Đặt các nút theo chiều dọc
        edit_shift_btn.pack(pady=(10, 5))  # Khoảng cách phía trên là 10, phía dưới là 5
        arrange_shift_btn.pack(pady=(10, 5))  # Khoảng cách phía trên là 10, phía dưới là 5
        create_shift_btn.pack(pady=5)       # Khoảng cách đều nhau giữa các nút
        # delete_button.pack(pady=5)


        



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

    def on_double_click(self, event):
        # Lấy item được chọn khi nhấp đúp
        selected_item = self.table_schedule.selection()
        if selected_item:
            # set state

            item_values = self.table_schedule.item(selected_item, "values")
            if not item_values[0]: return

            self.is_edit_schedule=True
            self.dataEdit = item_values 

    def refresh(self):
        self.is_create_new_schedule = False
        # Tính toán ngày bắt đầu và kết thúc của tuần hiện tại
        today = datetime.date.today()
        start_of_week = today - datetime.timedelta(days=today.weekday())  # Thứ 2 của tuần
        end_of_week = start_of_week + datetime.timedelta(days=6)  # Chủ nhật của tuần

        self.start_date.set_date(start_of_week)
        self.end_date.set_date(end_of_week)

        # init data
        self.data_shifts = self.cl_bus.getall()
        self.data_schedules = self.ll_bus.getallbydate(self.start_date.get_date(), self.end_date.get_date())


        self.render_table_shift(self.data_shifts)    
        self.render_table_schedule(self.data_schedules)

    def open_add_shift_modal(self):
        if not self.is_create_new_schedule: 
            messagebox.showinfo("Thông báo", "Lịch làm đã tồn tại, không thể xếp thêm ca làm")
            return
        dataDate = (self.start_date, self.end_date)
        AddShiftModal(self.schedule_window, self.table_schedule ,dataDate)

    def open_edit_shift_modal(self):
        if not self.is_edit_schedule: 
            messagebox.showinfo("Thông báo", "Chưa có lịch làm được chọn, vui lòng double click để chọn lịch")
            return

        # Chuyển đổi thành dictionary
        schedule_of_employee = {self.dataEdit[1]: list(self.dataEdit[2:])}

        # EditShiftModal(self.schedule_window, self.dataEdit)
        EditShiftModal(self.schedule_window, schedule_of_employee, self.schedule_list_build)
        self.is_edit_schedule=False

    def render_table_shift(self, data):
        # Xóa tất cả các hàng hiện có trong bảng
        for item in self.table_shift.get_children():
            self.table_shift.delete(item)

        # Thêm dữ liệu mới vào bảng
        if not data or len(data) == 0: return


        for i, shift in enumerate(data, start=1):
            # Giả sử salary là một dictionary chứa các trường như dưới đây
            maca=shift.get_MaCa()
            tenca=shift.get_TenCa()
            tgvao=shift.get_ThoiGianVao()
            tgra=shift.get_ThoiGianRa()

            self.table_shift.insert('', 'end', values=(
                f"{maca}",
                f"{tenca}",
                f"{tgvao}", 
                f"{tgra}" )
            )

        
    
    def create_footer_table(self, parent_frame):
        """Tạo bảng dưới phần left footer với thanh cuộn nếu vượt quá chiều cao."""
        columns = ("maca","tenca", "tgvao", "tgra")

        # Tạo khung cho Treeview và Scrollbar
        table_frame = tk.Frame(parent_frame, width=780, height=170)
        table_frame.pack(fill='both', expand=True)

        # Tạo Scrollbar
        scrollbar = tk.Scrollbar(table_frame)
        scrollbar.pack(side='right', fill='y')

        # Tạo Treeview với các cột
        self.table_shift = ttk.Treeview(table_frame, columns=columns, show="headings", height=7, yscrollcommand=scrollbar.set)
        self.table_shift.pack(side='left', fill='both', expand=True)

        # Kết nối thanh cuộn với Treeview
        scrollbar.config(command=self.table_shift.yview)

        # Đặt tiêu đề cho các cột
        self.table_shift.heading("maca", text="Mã ca")
        self.table_shift.heading("tenca", text="Ca làm")
        self.table_shift.heading("tgvao", text="Thời gian vào")
        self.table_shift.heading("tgra", text="Thời gian ra")

        # Đặt kích thước cột
        self.table_shift.column("maca", width=60, anchor='center')
        self.table_shift.column("tenca", width=140, anchor='center')
        self.table_shift.column("tgvao", width=250, anchor='center')
        self.table_shift.column("tgra", width=250, anchor='center')

       

    def show_selected_dates(self):
        """Xác thực ngày bắt đầu và ngày kết thúc."""
        start_date = self.start_date.get_date()
        end_date = self.end_date.get_date()


        
        # Kiểm tra xem ngày bắt đầu có phải là thứ Hai không
        if start_date.weekday() != 0:  # 0 là thứ Hai
            messagebox.showerror("Lỗi", "Ngày bắt đầu trong tuần phải là thứ Hai.")
            return

        # Tính ngày Chủ Nhật trong tuần
        curr_sunday = start_date + datetime.timedelta(days=6)  

        # Nếu ngày kết thúc không phải là Chủ Nhật của tuần hiện tại
        if end_date != curr_sunday:
            messagebox.showerror("Lỗi", "Ngày kết thúc trong tuần phải là Chủ Nhật gần nhất.")
            return
        
        # Nếu hợp lệ
        
        today = datetime.date.today()
        days_until_sunday = 6 - today.weekday() # => còn bao nhiêu ngày nữa đến chủ nhật
        now_sunday = today + datetime.timedelta(days=days_until_sunday)
        if start_date > now_sunday:
            self.data_schedules = self.ll_bus.getallbydate(self.start_date.get_date(), self.end_date.get_date())
            if self.data_schedules:
                self.render_table_schedule(self.data_schedules)
                messagebox.showinfo("Thông báo", "Lịch hiện tại là của tuần " + self.start_date.get_date().strftime("%d-%m-%Y") + " đến " + self.end_date.get_date().strftime("%d-%m-%Y"))

                self.is_create_new_schedule = True
                return

            # Nếu ngày bắt đầu là thuộc tuần sau => tạo lịch cho tuần sau
            confirm = messagebox.askyesno(
                "Xác nhận",
                "Bạn có muốn tạo lịch làm việc mới cho tuần này không?"
            )
            if confirm:
                self.is_create_new_schedule = True
                # //todooo
                messagebox.showinfo("Thông báo", f"Tạo lịch mới cho tuần sau")
                 # Xóa tất cả dữ liệu trong bảng trước khi thêm hàng mới
                for item in self.table_schedule.get_children():
                    self.table_schedule.delete(item)
                # Thêm hàng ngày tương ứng (t2-cn)
                self.init_row_table_schedule(start_date)
                return
            else:
                self.refresh()
                return  # Người dùng chọn "No", không làm gì cả
            
        
        # todooo call data
        self.data_schedules = self.ll_bus.getallbydate(self.start_date.get_date(), self.end_date.get_date())
        self.render_table_schedule(self.data_schedules)

    def readonly_comboboxes(self):
        """Set các Combobox thành trạng thái 'readonly'."""
        self.month_cb.config(state="readonly")  # Tắt chức năng chọn tháng
        self.year_cb.config(state="readonly")   # Tắt chức năng chọn năm
        self.date_range_cb.config(state="readonly")  # Tắt chức năng chọn khoảng thời gian

    def init_row_table_schedule(self, start_date):
        # Xóa tất cả dữ liệu trong bảng trước khi thêm hàng mới
        for item in self.table_schedule.get_children():
            self.table_schedule.delete(item)

        """Thêm hàng đầu tiên vào bảng với các ngày từ thứ Hai đến Chủ Nhật."""
        days = [start_date + datetime.timedelta(days=i) for i in range(7)]  # Các ngày từ thứ Hai đến Chủ Nhật
        day_strings = [day.strftime("%d/%m") for day in days]  # Định dạng ngày dd/mm

        # Tạo dữ liệu hàng đầu tiên(ngày tương ứng thứ)
        row_data = ["", "", *day_strings]  # Dữ liệu cho hàng đầu tiên
        self.table_schedule.insert("", "end", values=row_data)  # Thêm vào bảng
        

    def create_table(self, parent_frame):
        """Tạo bảng dưới phần select_frame với thanh cuộn nếu vượt quá chiều cao."""
        columns = ("stt", "nv", "t2", "t3", "t4", "t5", "t6", "t7", "cn")

        # Tạo khung cho Treeview và Scrollbar
        table_frame = tk.Frame(parent_frame)
        table_frame.pack(fill='both', expand=True)

        # Tạo Scrollbar
        scrollbar = tk.Scrollbar(table_frame)
        scrollbar.pack(side='right', fill='y')

        # Tạo Treeview với các cột
        self.table_schedule = ttk.Treeview(table_frame, columns=columns, show="headings", height=10, yscrollcommand=scrollbar.set)
        self.table_schedule.pack(side='left', fill='both', expand=True)

        # Kết nối thanh cuộn với Treeview
        scrollbar.config(command=self.table_schedule.yview)
          # Thêm sự kiện nhấp đúp
        self.table_schedule.bind("<Double-1>", self.on_double_click)

        w = 980
        col_1 = 980 // 28
        col_5 = col_1 * 5
        col_3 = col_1 * 3

        # Đặt tiêu đề cho các cột
        self.table_schedule.heading("stt", text="STT")
        self.table_schedule.column("stt", width=col_1, anchor='center')  # STT chiếm 1 cột

        self.table_schedule.heading("nv", text="Nhân viên")
        self.table_schedule.column("nv", width=col_5, anchor='w')  # Nhân viên chiếm 5 cột
        # Các cột thứ 2 đến chủ nhật
        text_cols = ("Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ Nhật")
        for i, col in enumerate(columns[2:]):
            self.table_schedule.heading(col, text=text_cols[i])
            self.table_schedule.column(col, width=col_3, anchor='center')  # Mỗi ngày trong tuần chiếm 3 cột

        # self.init_row_table_schedule(self.start_date.get_date())

    # hàm này dùng render data fake 
    def render_table_schedule(self, data):
        # Xóa tất cả các hàng hiện có trong bảng
        for item in self.table_schedule.get_children():
            self.table_schedule.delete(item)

        self.init_row_table_schedule(self.start_date.get_date())

        if not data or len(data) == 0:
            messagebox.showinfo("Thông báo", "Lịch làm không tồn tại")
            return
        
        self.schedule_list_build = self.build_data_schedule(data)
        
        stt = 1
        for ma_nv, days in self.schedule_list_build.items():
            nv= ma_nv + " - " + NhanVienBUS.getInstance().getById(ma_nv).get_Ten()
            row = [stt, nv] +  [list(day.values())[0] for day in days]
            self.table_schedule.insert("", "end", values=row)
            stt += 1


    def build_data_schedule(self, data):
        schedule = {}
        for entry in data:
            ma_ll = entry.get_MaLich()
            ma_nv = entry.get_MaNhanVien()
            ma_ca = entry.get_MaCa() if entry.get_MaCa() != 'CA999' else 'OFF' 
            ngay = datetime.datetime.strptime(entry.get_Ngay().strftime('%Y-%m-%d'), '%Y-%m-%d')
            weekday = ngay.weekday()  # Monday = 0, Sunday = 6

            if ma_nv not in schedule:
            #     schedule[ma_nv] = ['OFF'] * 7  # Khởi tạo giá trị 'off' cho cả tuần

            # schedule[ma_nv][weekday] = ma_ca  # Gán mã ca vào đúng thứ trong tuần
            #  # Khởi tạo danh sách 7 ngày với từ điển {'LL': 'OFF'} cho mỗi ngày
                schedule[ma_nv] = [{ma_ll: 'OFF'} for _ in range(7)]
        
            # Cập nhật mã lịch và mã ca cho ngày cụ thể trong tuần
            schedule[ma_nv][weekday] = {ma_ll: ma_ca}
        
        # In dữ liệu trong schedule
        # for key,item in schedule.items():
        #     print(f"{key} : {item}")

        return schedule

if __name__ == "__main__":
    lich_lam = LichLamViecGUI() 



    # !note: phần chọn khoảng thời gian (mặc định sẽ hiện thời gian tuần tới), chọn tuần tiếp theo( xếp nhiều tuần) để xếp lịch
    # sau khi chọn tuần hợp lí rồi thì ấn tạo mới