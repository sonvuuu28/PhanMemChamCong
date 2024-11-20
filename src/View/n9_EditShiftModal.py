import tkinter as tk
from tkinter import Toplevel, Label, Frame, ttk
import customtkinter as ctk
import os, sys
from tkinter import messagebox

current_dir = os.path.dirname(os.path.abspath(__file__))
dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)
from CaLamDTO import CaLamDTO
from LichLamDTO import LichLamDTO


bus_dir = os.path.join(current_dir, '../BUS')
sys.path.append(bus_dir)
from CaLamBUS import CaLamBUS
from LichLamBUS import LichLamBUS



class EditShiftModal:
    def __init__(self, parent_frame, schedule_of_employee, schedule_list):
        
        self.cl_bus = CaLamBUS.getInstance()
        self.ll_bus = LichLamBUS.getInstance()

        self.schedule_of_employee = schedule_of_employee
        self.schedule_list = schedule_list

        # print(f"lich ca nhan: {self.schedule_of_employee}")
        # print(f"lich: {self.schedule_list}")

        self.initUI(parent_frame)
       
        self.show_data_edit()

    def initUI(self , parent_frame):
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
        title = Label(self.header, text="SỬA CA", font=("Arial", 14, "bold"), bg="#908181", fg="black")
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
        self.employee_combobox = ttk.Combobox(self.topModal, width=160, state="readonly")
        self.employee_combobox.pack(side="left", padx=(5, 285))


        # Phần bodyModal trong body
        self.bodyModal = Frame(self.body, width=600, height=210, bg="#fff")
        self.bodyModal.pack_propagate(False)
        self.bodyModal.pack()

         # Frame chứa lưới (để margin-left 20px)
        self.gridContainer = Frame(self.bodyModal, bg="#fff")
        self.gridContainer.pack(pady=(20,10), padx=20, anchor="w")  # margin-left 20px

        # Cấu trúc 4 hàng 2 cột trong gridContainer
        self.list_cbbox =self.create_schedule_grid(self.gridContainer)


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
            command=self.confirm_edit
        )
        add_button.pack(side="right", padx=20, pady=5)

    def confirm_edit(self):
        confirm = messagebox.askyesno(
                "Xác nhận",
                "Bạn đã kiểm tra kĩ thông tin?"
            )
        if confirm:
            
            
            dataEdited = list()
            for cbb in self.list_cbbox:
                dataEdited.append(cbb.get())
            

            rs = self.editSchedule(dataEdited)
            if rs[0] == 1:
                self.close_modal()
            messagebox.showinfo("Thông báo", rs[1])
            return
        else:
            return  # Người dùng chọn "No", không làm gì cả

    def editSchedule(self, data):
        manv = self.nhanvien.split(' - ')[0]
        lich = self.schedule_list.get(manv)
        
        # Thay thế dữ liệu
        for i, value in enumerate(data):
            key = list(lich[i].keys())[0]  # Lấy khóa từ phần tử hiện tại
            lich[i][key] = value           # Cập nhật giá trị
        rs = None
        for item in lich:
            malich = (list(item.keys())[0])
            lichlam = self.ll_bus.getbyid(malich)
            calam = list(item.values())[0]
            if calam == 'OFF':
                calam = "CA999"
            lichlam.set_MaCa(calam)
            res = self.ll_bus.update(lichlam)
            if res[0] == 0:
                return res
            rs = res
        return rs
                

            
            

    def show_data_edit(self):
        self.nhanvien = list(self.schedule_of_employee.keys())[0]
        self.lichlam =  list(self.schedule_of_employee.values())[0]
        self.employee_combobox.set(value=self.nhanvien)
        for i, cbb in enumerate(self.list_cbbox):
            cbb.set(value=self.lichlam[i])

    def center_modal(self, parent):
        parent.update_idletasks()
        x = parent.winfo_x() + (parent.winfo_width() // 2) - (600 // 2)
        y = parent.winfo_y() + (parent.winfo_height() // 2) - (400 // 2)
        self.modal.geometry(f"+{x}+{y}")

    def close_modal(self):
        self.modal.destroy()

    
    def get_shift_list(self):
        # init data
        data_shifts = self.cl_bus.getall()
        rs = list()
        for i,ca in enumerate(data_shifts, start=1):
            if ca.get_MaCa() != 'CA999':
                rs.insert(i, ca.get_MaCa())
        rs.insert(0, "OFF")
        return rs
    
    def create_schedule_grid(self, parent):
        days = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ Nhật"]
        comboboxes = []  # Danh sách để lưu các Combobox
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
                # Thêm Combobox vào danh sách
                comboboxes.append(combobox)

        return comboboxes  # Trả về danh sách các Combobox