import tkinter as tk
from tkinter import Toplevel, Label, Frame, ttk
import customtkinter as ctk

class AddShiftModal:
    def __init__(self, parent_frame):
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
        self.employee_combobox = ttk.Combobox(self.topModal, values=self.get_fake_employee_list(), state="readonly")
        self.employee_combobox.pack(side="left", padx=5)


        # Phần bodyModal trong body
        self.bodyModal = Frame(self.body, width=600, height=210, bg="#fff")
        self.bodyModal.pack_propagate(False)
        self.bodyModal.pack()

         # Frame chứa lưới (để margin-left 20px)
        self.gridContainer = Frame(self.bodyModal, bg="#fff")
        self.gridContainer.pack(pady=(20,10), padx=20, anchor="w")  # margin-left 20px

        # Cấu trúc 4 hàng 2 cột trong gridContainer
        self.create_schedule_grid(self.gridContainer)


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
            command=self.close_modal
        )
        add_button.pack(side="right", padx=20, pady=5)

    def center_modal(self, parent):
        parent.update_idletasks()
        x = parent.winfo_x() + (parent.winfo_width() // 2) - (600 // 2)
        y = parent.winfo_y() + (parent.winfo_height() // 2) - (400 // 2)
        self.modal.geometry(f"+{x}+{y}")

    def close_modal(self):
        self.modal.destroy()

    def get_fake_employee_list(self):
        # Hàm trả về danh sách nhân viên mẫu
        return ["Nguyễn Văn A", "Trần Thị B", "Lê Văn C", "Phạm Thị D", "Hoàng Văn E"]
    
    def get_fake_shift_list(self):
        # Hàm trả về danh sách ca làm mẫu
        return ["OFF","Ca A", "Ca B", "Ca C"]
    
    def create_schedule_grid(self, parent):
        days = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ Nhật"]

        # Tạo 4 hàng, mỗi hàng 2 cột cho các ngày trong tuần
        for row in range(4):
            for col in range(2):
                day_index = row * 2 + col
                if day_index >= len(days):  # Ngừng nếu vượt quá số ngày
                    break

                # Tạo label và combobox cho từng ngày
                label = Label(parent, text=days[day_index], bg="#fff", fg="black", font=("Arial", 11))
                label.grid(row=row, column=col * 2, padx=(0, 13), pady=10, sticky="w")

                combobox = ttk.Combobox(parent, values=self.get_fake_shift_list(), state="readonly")
                combobox.grid(row=row, column=col * 2 + 1, padx=(5, 40), pady=10, sticky="w")