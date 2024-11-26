import tkinter as tk
import utilView
import customtkinter as ctk 

from  customtkinter import CTkImage 
from tkinter import ttk, messagebox
from time import strftime
from PIL import Image, ImageTk
import os, sys
from datetime import datetime


current_dir = os.path.dirname(os.path.abspath(__file__))
dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)
from BangLuongDTO import BangLuongDTO


bus_dir = os.path.join(current_dir, '../BUS')
sys.path.append(bus_dir)
from BangLuongBUS import BangLuongBUS
from BangChamCongBUS import BangChamCongBUS
from NhanVienBUS import NhanVienBUS



class BangLuongGUI:
    def __init__(self):
        # Đường dẫn đến folder Icon
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.icon_dir = os.path.join(current_dir, '../Icon')

        self.bangluong_bus=BangLuongBUS.getInstance()
        self.nv_bus=NhanVienBUS.getInstance()
        self.is_view_detail=False


        self.initUI()
        self.getData()
        self.salaryWindow.mainloop()

    def format_currency(self, value):
        # Nếu là int, chỉ cần định dạng trực tiếp
        if isinstance(value, int):
            formatted = f"{value:,}".replace(",", ".")  # Định dạng số nguyên
        else:  # Nếu là float, định dạng với 2 chữ số thập phân
            formatted = f"{float(value):,.2f}".replace(",", " ").replace(".", ",").replace(" ", ".")
        
        return f"{formatted} VNĐ"
    
    
    def parse_currency(self, currency_str):
        try:
            # Loại bỏ đơn vị "VNĐ" và các khoảng trắng dư thừa
            cleaned_str = currency_str.replace("VNĐ", "").strip()

            # Chuyển dấu "." thành khoảng trắng tạm thời để xử lý đúng
            # Chuyển dấu "," (thập phân) thành dấu "."
            normalized_str = cleaned_str.replace(".", "").replace(",", ".")

            # Chuyển đổi chuỗi thành số thực (float) và sau đó lấy phần nguyên (int)
            return int(float(normalized_str))  # Trả về kiểu int
        except ValueError:
            raise ValueError("Chuỗi đầu vào không hợp lệ")

    def back_Trang_Chu(self, window):
        window.destroy()
        from n1_TrangChuGUI import TrangChuGUI
        TrangChuGUI()
    
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

    def render_salary_list(self, salary_list):
        # Xóa tất cả các hàng hiện có trong bảng
        for item in self.salary_table.get_children():
            self.salary_table.delete(item)

        for i, salary in enumerate(salary_list, start=1):
            # Giả sử salary là một dictionary chứa các trường như dưới đây
            mabl=salary.get_MaBangLuong()
            manv=salary.get_MaNhanVien()
            tennv=self.nv_bus.getById(salary.get_MaNhanVien()).get_Ten()
            # sogio=self.calculate_total_hours_minutes(salary.get_MaNhanVien(), self.month_cb.get(), self.year_cb.get())
            sogio=salary.get_SoGioLam()
            hsluong=salary.get_HeSoLuong()
            phucap = int(round(salary.get_PhuCap()))  # Làm tròn rồi chuyển sang int
            khautru = int(round(salary.get_KhauTru()))
            tongluong=self.calc_tongluong(sogio=sogio, hesoluong=hsluong, phucap=phucap, khautru=khautru)

            phucap = self.format_currency(phucap)
            khautru = self.format_currency(khautru)
            tongluong = self.format_currency(tongluong)
            
            self.salary_table.insert('', 'end', values=(
                f"{i}",  # STT với padding
                f"{mabl}",
                f"{manv}-{tennv}",
                f"{round(sogio, 2)}", 
                f"{hsluong}", 
                f"{phucap}",
                f"{khautru}",
                f"{tongluong}"
                # f"{salary.get_TongTien()}"
        ))

    def initUI(self):
        self.salaryWindow = tk.Tk()
        wWindow = 1000
        hWindow = 650
        self.salaryWindow.geometry(f"{wWindow}x{hWindow}+250+40")
        frameSalary = utilView.frameUtil(self.salaryWindow, wWindow, hWindow, 0, 0, bg = '#ffffff')
        
        # Tạo frame cho header
        headerSalary = tk.Frame(frameSalary, width=1000, height=40, bg="white")
        headerSalary.pack(pady=(10, 0), fill='x')
        headerSalary.pack_propagate(False)  # Không thay đổi kích thước theo nội dung
       
        titleSalary = tk.Label(headerSalary, text="BẢNG LƯƠNG NHÂN VIÊN", font=("Arial", 18, "bold"), bg="#ffffff", fg="black")
        titleSalary.pack(side="right", expand=True)  # Căn giữa bên phảit
        ## nút home
        homeImage = Image.open(os.path.join(self.icon_dir, "home.png"))
        tk_homeImage = ImageTk.PhotoImage(homeImage)
        homeImageHover = Image.open(os.path.join(self.icon_dir, "homeHover.png"))
        tk_homeImageHover = ImageTk.PhotoImage(homeImageHover)

        label_home = tk.Label(frameSalary, image=tk_homeImage, bg='white')
        label_home.image = tk_homeImage
        label_home.place(x=30, y=10)
        label_home.bind("<Button-1>", lambda event: self.back_Trang_Chu(self.salaryWindow))
        self.hover(label_home, tk_homeImage, tk_homeImageHover, None)

        body_height = hWindow - 60 - 180 - 10  # -60:header -180:footer - 10:paddingBody = 400

        body = tk.Frame(frameSalary, width=980, height=body_height, bg="white")
        body.pack(pady=(10, 0), padx=10, fill='both') 
        body.pack_propagate(False)


        # Phần trên của body: Chọn tháng và năm
        select_frame = tk.Frame(body, width=390, height=40, bg="#fff")
        select_frame.pack(pady=(0,10), anchor="e")
        select_frame.pack_propagate(False)

        # Chọn tháng
        tk.Label(select_frame, text="Chọn tháng:",font=("Arial", 11), bg="#fff").pack(side="left", padx=(0, 5))
        self.month_cb = ttk.Combobox(select_frame, values=[str(i) for i in range(1, 13)], width=5, font=("Arial", 11), state="readonly")
        self.month_cb.pack(side="left")
        # Lấy tháng hiện tại
        current_month = datetime.now().month - 1
        self.month_cb.set(str(current_month))  # Thiết lập giá trị mặc định là tháng trước

        # Chọn năm
        tk.Label(select_frame, text="/", bg="#fff").pack(side="left", padx=2)
        self.year_cb = ttk.Combobox(select_frame, values=[str(i) for i in range(1999, 2031)], width=5, font=("Arial", 11), state="readonly")
        self.year_cb.pack(side="left")
        # Lấy năm hiện tại 
        current_year = datetime.now().year
        self.year_cb.set(str(current_year))  # Thiết lập giá trị mặc định là năm hiện tại
       
        # Nút Xem lương với các yêu cầu đặc biệt
        view_button = ctk.CTkButton(
            select_frame, 
            text="Xem", 
            width=100, 
            height=24, 
            fg_color="#000",  # Màu nền
            text_color="#fff",  # Màu chữ
            font=("Arial", 12),  # Font chữ
            corner_radius=4,  # Bo góc 4px
            border_width=0,  # Không có viền
            hover_color="#383838",
            command=self.view_salary
        )
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




        # Phần dưới của body: Hiển thị bảng lương
        table_frame = tk.Frame(body, bg="white")
        table_frame.pack(fill='both',expand=True)

        # Tạo bảng lương với Treeview
        columns = ("stt",'ma_bl','ten_nv','so_gio','heso_luong','phu_cap','khau_tru','tong_luong',)
        self.salary_table = ttk.Treeview(table_frame, columns=columns, show='headings')
        self.salary_table.pack(fill='both',expand=True)

        # Đặt tên cột
        self.salary_table.heading('stt', text='STT')
        self.salary_table.heading('ma_bl', text='ID')
        self.salary_table.heading('ten_nv', text='Nhân viên')
        self.salary_table.heading('so_gio', text='Số giờ')
        self.salary_table.heading('heso_luong', text='Hệ số lương')
        self.salary_table.heading('phu_cap', text='Phụ cấp')
        self.salary_table.heading('khau_tru', text='Khấu trừ')
        self.salary_table.heading('tong_luong', text='Tổng lương')

        # Đặt chiều rộng các cột
        total_width = 980  # Tổng chiều rộng của bảng
        # Tính toán kích thước cho các cột
        width_span_1 = total_width // 27  # Cột có span 1
        width_span_2 = width_span_1 * 2  # Cột có span 5
        width_span_4 = width_span_1 * 4  # Cột có span 4

        self.salary_table.column('stt', width=width_span_1)
        self.salary_table.column('ma_bl', width=width_span_2)
        self.salary_table.column('ten_nv', width=width_span_4)
        self.salary_table.column('so_gio', width=width_span_4)
        self.salary_table.column('heso_luong', width=width_span_4)
        self.salary_table.column('phu_cap', width=width_span_4)
        self.salary_table.column('khau_tru', width=width_span_4)
        self.salary_table.column('tong_luong', width=width_span_4)

          # Thêm sự kiện nhấp đúp
        self.salary_table.bind("<Double-1>", self.on_double_click)

        

        # Tạo footer frame với kích thước 990x40 và paddingX=10
        footer = tk.Frame(
            frameSalary, 
            width=980, height=170, 
            bg="#fff", highlightbackground="gray",  # Màu viền là #000 (đen)
            highlightthickness=1,        # Độ dày viền là 1px
            bd=0 
        )
        footer.pack(pady=(10, 0), padx=10, fill='x')  # Padding giữa footer và body là 10px
        footer.pack_propagate(False)


        # Frame bên trái của footer (phần còn lại của footer)
        left_footer_frame = tk.Frame(footer, bg="#fff")
        left_footer_frame.pack(side="left", fill='both')  # Chiếm hết phần còn lại của footer
        left_footer_frame.pack_propagate(False)

        self.inp_id = utilView.create_input_with_label(left_footer_frame, "ID", 0, 0)
        # self.inp_ten = utilView.create_input_with_label(left_footer_frame, "Họ tên", 0, 1)
        # self.inp_sogio = utilView.create_input_with_label(left_footer_frame, "Số giờ", 1, 0)
        # self.inp_hsl = utilView.create_input_with_label(left_footer_frame, "Hệ số lương", 1, 1)
        self.inp_phucap = utilView.create_input_with_label(left_footer_frame, "Phụ cấp", 1, 0)
        self.inp_khautru = utilView.create_input_with_label(left_footer_frame, "Khấu trừ", 2, 0)
        # self.inp_tong = utilView.create_input_with_label(left_footer_frame, "Tổng lương", 3, 0)
        
        # Cấu hình cột để chúng giãn đều
        left_footer_frame.grid_columnconfigure(0, weight=1)
        left_footer_frame.grid_columnconfigure(1, weight=1)

      



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
            hover_color="#383838",
            command=self.edit_bangluong
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
        reset_button = ctk.CTkButton(
            right_footer_frame, 
            text="Reset", width=160, height=30,
            fg_color="#000",  # Màu nền
            text_color="#fff",  # Màu chữ
            font=("Arial", 12, "bold"),  # Font chữ
            corner_radius=4,  # Bo góc 4px
            border_width=0,  # Không có viền
            hover_color="#383838",
            command=self.reset
        )

        # Đặt các nút theo chiều dọc
        # add_button.pack(pady=(10, 5))  # Khoảng cách phía trên là 10, phía dưới là 5
        edit_button.pack(pady=5)       # Khoảng cách đều nhau giữa các nút
        # delete_button.pack(pady=5)
        reset_button.pack(pady=5)

    def getData(self):
        self.salary_list=self.bangluong_bus.getByDate(self.month_cb.get(), self.year_cb.get())

        # Thêm dữ liệu mới từ salary_list vào bảng
        if not self.salary_list:
            ds_nv = self.nv_bus.list()

            luong = None
            for nv in ds_nv:
                ma_bl = self.bangluong_bus.taoma()
                sogio=self.calculate_total_hours_minutes(nv.get_MaNhanVien(), self.month_cb.get(), self.year_cb.get())
                hsluong = 1.5
                
                if nv.get_ChucVu() == 'Quản Lý':
                    hsluong = 1.7

                luong = BangLuongDTO(ma_bl, self.month_cb.get(), self.year_cb.get(), 0, 0, hsluong, 0, nv.get_MaNhanVien(), 1, sogio)
                self.bangluong_bus.insert(luong)

            self.salary_list=self.bangluong_bus.getByDate(self.month_cb.get(), self.year_cb.get())
            

            # return
        
        self.render_salary_list(self.salary_list)

    
    def view_salary(self):
        self.is_view_detail=False
        
        ngay_hien_tai = datetime.now()
        thang_hien_tai = ngay_hien_tai.month
        nam_hien_tai = ngay_hien_tai.year
        
        # Tách lấy tháng và năm từ ngày được chọn
        thang_chon =int (self.month_cb.get())
        nam_chon = int (self.year_cb.get())
        
        # Kiểm tra điều kiện
        if nam_chon > nam_hien_tai or (nam_chon == nam_hien_tai and thang_chon >= thang_hien_tai):
            messagebox.showinfo("Thông báo", "Bảng lương không tồn tại")
            # Xóa tất cả các hàng hiện có trong bảng
            for item in self.salary_table.get_children():
                self.salary_table.delete(item)
            return
        
        self.getData()

    def on_double_click(self, event):
        # Lấy item được chọn khi nhấp đúp
        selected_item = self.salary_table.selection()
        if selected_item:
            # set state
            self.is_view_detail=True

            # Lấy dữ liệu của hàng đã chọn
            item_values = self.salary_table.item(selected_item, "values")

            self.show_value_input(item_values)


    def show_value_input(self, values):
        self.reset()
        
        self.inp_id.insert(0, values[1])  # Gán giá trị mới
        self.inp_id.configure(state='readonly') 

        # self.inp_ten.insert(0, values[2])  # Gán giá trị mới
        # self.inp_ten.configure(state='readonly') 

        # self.inp_sogio.insert(0, values[3])  # Gán giá trị mới
        # self.inp_sogio.configure(state='readonly') 
        
        # self.inp_hsl.insert(0, values[4])  # Gán giá trị mới
        # self.inp_hsl.configure(state='readonly') 
        
        self.inp_phucap.insert(0, self.parse_currency(values[5]))  # Gán giá trị mới
        
        self.inp_khautru.insert(0, self.parse_currency(values[6]))  # Gán giá trị mới
        
        # self.inp_tong.insert(0, values[7])  # Gán giá trị mới
        # self.inp_tong.configure(state='readonly') 
        self.is_view_detail=True


    def edit_bangluong(self):
        if not self.is_view_detail: return  
        confirm = messagebox.askyesno(
                "Xác nhận",
                "Bạn đã kiểm tra kĩ thông tin?"
            )
        if confirm:
            try:
                # Kiểm tra nếu input_1 và input_2 là số nguyên
                ktru = int(self.inp_khautru.get())  # Chuyển input_1 sang int
                pcap = int(self.inp_phucap.get())  # Chuyển input_2 sang int

                luong_edit = None
                for l in self.salary_list:
                    if l.get_MaBangLuong() == self.inp_id.get():
                        luong_edit = l 
                if luong_edit:
                    luong_edit.set_KhauTru(ktru)
                    luong_edit.set_PhuCap(pcap)

                    luong_edit.set_TongTien(
                        self.calc_tongluong(luong_edit.get_SoGioLam(), luong_edit.get_HeSoLuong(), luong_edit.get_PhuCap(), luong_edit.get_KhauTru())
                    )

                    res=self.bangluong_bus.update(luong_edit)
                    if res[0] == 1:
                        messagebox.showinfo("Thông báo", res[1])
                        self.reset()
                    else:
                        messagebox.showerror("Lỗi", res[1])

                else: messagebox.showerror("Lỗi", "Lương không tồn tại")


            except ValueError:
                # Nếu không phải số nguyên, hiển thị thông báo lỗi
                messagebox.showerror("Lỗi","Phụ cấp và khấu trừ không hợp lệ!")
                return  # Dừng xử lý nếu dữ liệu không hợp lệ
        else:
            return  # Người dùng chọn "No", không làm gì cả



    def reset(self):
        self.is_view_detail=False

        self.inp_id.configure(state='normal') 
        self.inp_id.delete(0, tk.END)  # Xóa giá trị cũ trong input nếu có

        # self.inp_ten.configure(state='normal') 
        # self.inp_ten.delete(0, tk.END)  # Xóa giá trị cũ trong input nếu có
       
        # self.inp_hsl.configure(state='normal')   
        # self.inp_hsl.delete(0, tk.END)  # Xóa giá trị cũ trong input nếu có

        # self.inp_sogio.configure(state='normal') 
        # self.inp_sogio.delete(0, tk.END)  # Xóa giá trị cũ trong input nếu có
        
        self.inp_phucap.delete(0, tk.END)  # Xóa giá trị cũ trong input nếu có
        
        self.inp_khautru.delete(0, tk.END)  # Xóa giá trị cũ trong input nếu có
        
        # self.inp_tong.configure(state='normal') 
        # self.inp_tong.delete(0, tk.END)  # Xóa giá trị cũ trong input nếu có

        self.salaryWindow.focus_set() 

    def refresh(self):
        self.reset()
        # Lấy tháng hiện tại
        current_month = datetime.now().month - 1
        self.month_cb.set(str(current_month))  # Thiết lập giá trị mặc định là tháng trươzxc
        # Lấy năm hiện tại
        current_year = datetime.now().year
        self.year_cb.set(str(current_year))  # Thiết lập giá trị mặc định là tháng hiện tại
        self.getData()

    def calc_tongluong(self, sogio, hesoluong, phucap, khautru ):
        luong_co_ban = 24000
        return round(float(sogio) * float(hesoluong) * float(luong_co_ban) + float(phucap) - float(khautru), 2)

    
    
    def calculate_total_hours_minutes(self, ma_nhan_vien, thang, nam):
        total_seconds = 0
        cong_bus = BangChamCongBUS.getInstance()

        bang_cham_cong_list = cong_bus.getSoGioNV(ma_nhan_vien, thang, nam)
        if not bang_cham_cong_list:
            return 0.0  # Trả về 0.0 nếu không có dữ liệu
        
        for cham_cong in bang_cham_cong_list:
            # Kiểm tra mã nhân viên và tháng, năm
            if cham_cong.get_MaNhanVien() == ma_nhan_vien:
                # Lấy tháng và năm từ Ngay
                ngay = cham_cong.get_Ngay()
                
                if ngay.month == int(thang) and ngay.year == int(nam):
                    # Kiểm tra thời gian vào và ra
                    if cham_cong.get_ThoiGianVao() and cham_cong.get_ThoiGianRa():
                        time_in = cham_cong.get_ThoiGianVao()
                        time_out = cham_cong.get_ThoiGianRa()
                        # Kết hợp thời gian vào và ra với ngày
                        datetime_in = datetime.combine(ngay, time_in)
                        datetime_out = datetime.combine(ngay, time_out)

                        # Tính khoảng cách giữa thời gian vào và ra
                        delta = datetime_out - datetime_in
                        total_seconds += delta.total_seconds()
        
        # Tính tổng số giờ dưới dạng số thực
        total_hours = total_seconds / 3600

        # Tính giờ và phút từ tổng giây
        # total_hours_1 = int(total_seconds // 3600)
        # total_minutes_1 = int((total_seconds % 3600) // 60)
        # print( total_hours_1, total_minutes_1)

        # print(total_hours)
        return total_hours



if __name__ == "__main__":
    bang_luong = BangLuongGUI()


