import tkinter as tk
from tkinter import Toplevel, Label, Frame, ttk, messagebox
import customtkinter as ctk
import os, sys
from datetime import datetime, timedelta

current_dir = os.path.dirname(os.path.abspath(__file__))
dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)
from NhanVienDTO import NhanVienDTO
from CaLamDTO import CaLamDTO
from LichLamDTO import LichLamDTO


bus_dir = os.path.join(current_dir, '../BUS')
sys.path.append(bus_dir)
from NhanVienBUS import NhanVienBUS
from CaLamBUS import CaLamBUS
from LichLamBUS import LichLamBUS

class AddShiftModal:
    def __init__(self, parent_frame, table_schedule ,dataDate):
        self.startDate = dataDate[0]
        self.endDate = dataDate[1]
        self.table_schedule = table_schedule
        self.cl_bus = CaLamBUS.getInstance()
        self.nv_bus = NhanVienBUS.getInstance()
        self.ll_bus = LichLamBUS.getInstance()
        # 
        self.arrDay = self.get_date_range(self.startDate.get_date(), self.endDate.get_date())
        self.get_employee_list()
        self.get_shift_list()


        self.initUI(parent_frame)
    
    
    def initUI(self,parent_frame):
        # Tạo modal làm con của `parent`
        self.modal = Toplevel(parent_frame)
        self.modal.geometry("600x340")
        self.modal.configure(bg="#fdfdfd")
        # Căn giữa modal so với frame hiện tại
        self.modal.transient(parent_frame)
        self.modal.grab_set()  # Chặn tương tác ngoài modal

        # Đặt modal căn giữa parent
        self.center_modal(parent_frame)


        # Header
        self.header = Frame(self.modal, width=600, height=40, bg="#908181")
        self.header.pack_propagate(False)
        self.header.pack()
        title = Label(self.header, text="XẾP CA", font=("Arial", 14, "bold"), bg="#908181", fg="black")
        title.pack(expand=True)

        # Body
        self.body = Frame(self.modal, width=600, height=250, bg="red")
        self.body.pack()


        # Phần topModal trong body
        self.topModal = Frame(self.body, width=600, height=40, bg="#fff")
        self.topModal.pack_propagate(False)
        self.topModal.pack()

        # Label và Combobox trong topModal
        label = Label(self.topModal, text="Nhân viên:", bg="#fff", fg="black", font=("Arial", 11))
        label.pack(side="left", padx=(20, 5), pady=5)

        # Tạo Combobox cho danh sách nhân viên
        self.employee_combobox = ttk.Combobox(self.topModal,values=self.get_employee_list(), state="readonly")
        self.employee_combobox.pack(side="left", padx=5)


        # Phần bodyModal trong body
        self.bodyModal = Frame(self.body, width=600, height=210, bg="#fff")
        self.bodyModal.pack_propagate(False)
        self.bodyModal.pack()

         # Frame chứa lưới (để margin-left 20px)
        self.gridContainer = Frame(self.bodyModal, bg="#fff")
        self.gridContainer.pack(pady=(20,10), padx=20, anchor="w")  # margin-left 20px

        # Cấu trúc 4 hàng 2 cột trong gridContainer
        self.combobox_shifts = self.create_schedule_grid(self.gridContainer)


        # Footer
        self.footer = Frame(self.modal, width=600, height=50, bg="#fdfdfd")
        self.footer.pack_propagate(False)
        self.footer.pack(padx=80)

        cancel_button = ctk.CTkButton(
            self.footer, 
            text="Huỷ bỏ", width=160, height=30,
            fg_color="#000",  # Màu nền
            text_color="#fff",  # Màu chữ
            font=("Arial", 12, "bold"),  # Font chữ
            corner_radius=4,  # Bo góc 4px
            border_width=0,  # Không có viền
            hover_color="#383838",
            command=self.close_modal
           
        )
        cancel_button.pack(side="left", padx=20, pady=5)
        
        add_button = ctk.CTkButton(
            self.footer, 
            text="Xác nhận", width=160, height=30,
            fg_color="#000",  # Màu nền
            text_color="#fff",  # Màu chữ
            font=("Arial", 12, "bold"),  # Font chữ
            corner_radius=4,  # Bo góc 4px
            border_width=0,  # Không có viền
            hover_color="#383838",
            command=self.add_shift
        )
        add_button.pack(side="right", padx=20, pady=5)

    def center_modal(self, parent):
        parent.update_idletasks()
        x = parent.winfo_x() + (parent.winfo_width() // 2) - (600 // 2)
        y = parent.winfo_y() + (parent.winfo_height() // 2) - (400 // 2)
        self.modal.geometry(f"+{x}+{y}")

    def close_modal(self):
        self.modal.destroy()
    
     # Tính mảng ngày
    
    def get_date_range(self, start_date, end_date):
        delta = (end_date - start_date).days + 1  # Tổng số ngày trong khoảng
        dates = [
            (start_date + timedelta(days=i)).strftime('%Y-%m-%d')
            for i in range(min(delta, 7))  # Lấy tối đa 7 ngày
        ]
        return dates

    def get_employee_list(self):
        self.nv_list = self.nv_bus.list()
        rs = []
        for i in self.nv_list:
            rs.append(i.get_MaNhanVien() + ' - ' + i.get_Ten())
        # Hàm trả về danh sách nhân viên mẫu
        return rs
    
    def get_shift_list(self):
        self.cl_list = self.cl_bus.getall()
        rs = list()
        for i,c in enumerate(self.cl_list, start=1):
            if c.get_MaCa() != 'CA999':
                rs.insert(i, c.get_MaCa())
        rs.insert(0, 'OFF')
        # Hàm trả về danh sách ca làm mẫu
        return rs
    
    def create_schedule_grid(self, parent):
        days = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ Nhật"]
        # Danh sách để lưu trữ các Combobox
        combobox_list = []
        # Tạo 4 hàng, mỗi hàng 2 cột cho các ngày trong tuần
        for row in range(4):
            for col in range(2):
                day_index = row * 2 + col
                if day_index >= len(days):  # Ngừng nếu vượt quá số ngày
                    break

                # Tạo label và combobox cho từng ngày
                label = Label(parent, text=days[day_index], bg="#fff", fg="black", font=("Arial", 11))
                label.grid(row=row, column=col * 2, padx=(0, 13), pady=10, sticky="w")

                combobox = ttk.Combobox(parent, values=self.get_shift_list(), state="readonly")
                combobox.grid(row=row, column=col * 2 + 1, padx=(5, 40), pady=10, sticky="w")
                # Thêm combobox vào danh sách
                combobox_list.append(combobox)

        # Trả về danh sách 7 Combobox
        return combobox_list


    def add_shift(self):
        confirm = messagebox.askyesno(
                "Xác nhận",
                "Bạn đã kiểm tra kĩ thông tin?"
            )
        if confirm:
            self.schedules_add =  self.build_data_add()
            if self.schedules_add == None:
               messagebox.showerror("Lỗi", "Thêm lịch thất bại")
               return
            self.render_table_schedule(self.schedules_add)
            messagebox.showinfo("Thông báo", "Thêm lịch thành công")
            self.reset()
        else:
            return  # Người dùng chọn "No", không làm gì cả
        
    def reset(self):
        self.employee_combobox.set("")
        for i in self.combobox_shifts:
            i.set("")

    def build_data_add(self):
        if self.employee_combobox.get() == "":
            messagebox.showerror("Lỗi", "Nhân viên không được để trống")
            return
        ma_nv = self.employee_combobox.get().split(" - ")[0]
        shifts = self.combobox_shifts
        data_add = []
        for i, day in enumerate(self.arrDay):
            if shifts[i].get() == "":
                messagebox.showerror("Lỗi", "Ca làm không được để trống")
                return
            
            ma_ca = "CA999" if shifts[i].get() == 'OFF' else shifts[i].get()
            ma_ll = self.ll_bus.tao_ma()
            lich_lam_dto = LichLamDTO(ma_ll, ma_nv, ma_ca, day, 1)
            res = self.ll_bus.them_lich(lich_lam_dto)
            if res[0] == 0: return None
            data_add.append(lich_lam_dto)
        return data_add
    

    def build_data_schedule(self, data):
        schedule = {}
        for lichlam in data:
            ma_ll = lichlam.get_MaLich()
            ma_nv = lichlam.get_MaNhanVien()
            ma_ca = lichlam.get_MaCa() if lichlam.get_MaCa() != 'CA999' else 'OFF' 
            ngay = datetime.strptime(lichlam.get_Ngay(), '%Y-%m-%d')
            weekday = ngay.weekday()  # Monday = 0, Sunday = 6

            if ma_nv not in schedule:
                schedule[ma_nv] = [{ma_ll: 'OFF'} for _ in range(7)]
        
            # Cập nhật mã lịch và mã ca cho ngày cụ thể trong tuần
            schedule[ma_nv][weekday] = {ma_ll: ma_ca}
        
        # In dữ liệu trong schedule
        # for key,item in schedule.items():
        #     print(f"{key} : {item}")

        return schedule


    def render_table_schedule(self, data):
       
        self.schedule_list_build = self.build_data_schedule(data)

        stt = len(self.table_schedule.get_children())
        for ma_nv, days in self.schedule_list_build.items():
            nv= ma_nv + " - " + NhanVienBUS.getInstance().getById(ma_nv).get_Ten()
            row = [stt, nv] +  [list(day.values())[0] for day in days]
            self.table_schedule.insert("", "end", values=row)
            stt += 1


   
