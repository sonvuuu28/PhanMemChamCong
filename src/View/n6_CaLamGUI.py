# import tkinter as tk
# import utilView
# import customtkinter as ctk
# from tkinter import ttk
# from time import strftime
# from PIL import ImageTk, Image
# from tkinter import simpledialog
# from datetime import datetime
# import os, sys

# class ShiftGUI():
#     def __init__(self):
#         self.shiftWindow = None
#         self.initUI()

#     def initUI(self):
#         current_dir = os.path.dirname(os.path.abspath(__file__))
#         myPath = os.path.join(current_dir, '../Icon')
        
#         current_dir = os.path.dirname(os.path.abspath(__file__))
#         icon_dir = os.path.join(current_dir, '../Icon')
        
#         self.shiftWindow = tk.Tk()
#         wWindow = 1000
#         hWindow = 650
#         self.shiftWindow.geometry(f"{wWindow}x{hWindow}+300+40")
#         frameShift = utilView.frameUtil(self.shiftWindow, wWindow, hWindow, 0, 0, bg = '#ffffff')
        
#         # Tạo frame cho header
#         header = tk.Frame(frameShift, width=1000, height=40, bg="#908181")
#         header.pack(pady=(10, 0), fill='x')
#         header.pack_propagate(False)  # Không thay đổi kích thước theo nội dung
       
#         title = tk.Label(header, text="QUẢN LÍ CA LÀM", font=("Arial", 16, "bold"), bg="#908181", fg="black")
#         title.pack(side="right", expand=True)  # Căn giữa bên phải
        
#         arrow = Image.open(os.path.join(icon_dir, "arrow.png"))
#         self.close_icon = ImageTk.PhotoImage(arrow)
#         close_button = tk.Button(header, image=self.close_icon, height=40, width=40,bg="#908181", bd=0, command= lambda : self.back_LichLamViec())
#         close_button.pack(side="left")  # Đặt nút bên trái của header



#         body_height = hWindow - 50  # -50:header

#         # # Body
#         body = tk.Frame(frameShift, width=980, height=body_height, bg="#fff")
#         body.pack(pady=0, padx=0, fill='both') 
#         body.pack_propagate(False)

#         # # Left frame in body
#         left_frame = tk.Frame(body, width=400, height=body_height, bg="#fff")
#         left_frame.pack(side="left", fill="y")

#          # Chia left_frame thành form và buttons
#         form_shift = ctk.CTkFrame(left_frame, width=400, height=400, fg_color="#fff", corner_radius=0)
#         form_shift.pack(side="top", fill="both", expand=True, pady=(50, 0))

#         # Tạo các hàng trong form shift
#         self.create_form_row(form_shift, "Mã ca:", 0)
#         shifts_from_db = ["Ca A", "Ca B", "Ca C"]
#         self.create_combobox_row(form_shift, "Tên ca:", 1, shifts_from_db)  # Sử dụng hàm tạo combobox
#         self.create_form_row(form_shift, "Thời gian vào:", 2)
#         self.create_form_row(form_shift, "Thời gian ra:", 3)
#         states_shift = ["Active", "Inactive"]
#         self.create_combobox_row(form_shift, "Trạng thái:", 4, states_shift)  # Sử dụng hàm tạo combobox


#         # Đường kẻ đen giữa form và buttons
#         separator = tk.Frame(left_frame, height=2, bg="#dfdfdf")
#         separator.pack(fill="x", pady=(10, 10))  # Đường kẻ dày 2px, cách trên dưới 10px


#         # Thêm các nút vào frame buttons, chia 2 hàng 3 cột
#         buttons = tk.Frame(left_frame, width=400, height=200, bg="#fff")
#         buttons.pack(side="bottom", fill="both")  # Chiếm không gian dưới cùng
#         buttons.grid_propagate(False)
       
#         # Tạo các nút với font chỉ định
#         btn_add=ctk.CTkButton(
#             buttons, 
#             text="Thêm", 
#             width=100, 
#             height=30, 
#             fg_color="#000",  # Màu nền
#             text_color="#fff",  # Màu chữ
#             font=("Arial", 14,"bold"),  # Font chữ
#             corner_radius=4,  # Bo góc 4px
#             border_width=0,  # Không có viền
#             hover_color="#383838", 
#             command=self.add_shift
#         )
#         btn_add.grid(row=0, column=0, padx=(35,5), pady=(20,5))

#         btn_edit=ctk.CTkButton(
#             buttons, 
#             text="Sửa", 
#             width=100, 
#             height=30, 
#             fg_color="#000",  # Màu nền
#             text_color="#fff",  # Màu chữ
#             font=("Arial", 14,"bold"),  # Font chữ
#             corner_radius=4,  # Bo góc 4px
#             border_width=0,  # Không có viền
#             hover_color="#383838", 
#             command=self.edit_shift
#         )
#         btn_edit.grid(row=0, column=1, padx=5, pady=(20,5))

#         btn_delete=ctk.CTkButton(
#             buttons, 
#             text="Xoá", 
#             width=100, 
#             height=30, 
#             fg_color="#000",  # Màu nền
#             text_color="#fff",  # Màu chữ
#             font=("Arial", 14,"bold"),  # Font chữ
#             corner_radius=4,  # Bo góc 4px
#             border_width=0,  # Không có viền
#             hover_color="#383838", 
#             command=self.delete_shift
#         )
#         btn_delete.grid(row=0, column=2, padx=5, pady=(20,5))

#         btn_refresh=ctk.CTkButton(
#             buttons, 
#             text="Refresh", 
#             width=100, 
#             height=30, 
#             fg_color="#000",  # Màu nền
#             text_color="#fff",  # Màu chữ
#             font=("Arial", 14,"bold"),  # Font chữ
#             corner_radius=4,  # Bo góc 4px
#             border_width=0,  # Không có viền
#             hover_color="#383838", 
#             command=self.refresh_shift
#         )
#         btn_refresh.grid(row=1, column=0, padx=(35,5), pady=(10,5))

#         btn_reset =ctk.CTkButton(
#             buttons, 
#             text="Reset", 
#             width=100, 
#             height=30, 
#             fg_color="#000",  # Màu nền
#             text_color="#fff",  # Màu chữ
#             font=("Arial", 14,"bold"),  # Font chữ
#             corner_radius=4,  # Bo góc 4px
#             border_width=0,  # Không có viền
#             hover_color="#383838", 
#             command=self.reset_shift
#         )
#         btn_reset.grid(row=1, column=1, padx=(5,10), pady=(10,5))


#         ## Right frame in body với padding
#         right_frame = tk.Frame(body, width=600, height=body_height, bg="pink")
#         right_frame.pack(side="right", fill="y", padx=10, pady=10)


#         # Tạo Treeview (bảng) cho danh sách ca làm
#         columns = ("STT", "Mã ca", "Tên ca", "Thời gian vào", "Thời gian ra", "Trạng thái")
#         self.table = ttk.Treeview(right_frame, columns=columns, show="headings", height=20)

#         column_width = 580 // len(columns)  # Tính width cho từng cột để đạt tổng là 580
#         for col in columns:
#             self.table.heading(col, text=col)
#             self.table.column(col, anchor="center", width=column_width)

#         # Thêm Scrollbar cho bảng
#         scrollbar = ttk.Scrollbar(right_frame, orient="vertical", command=self.table.yview)
#         self.table.configure(yscrollcommand=scrollbar.set)

#         # Đặt vị trí cho bảng và scrollbar
#         self.table.pack(side="left", fill="both", expand=True)
#         scrollbar.pack(side="right", fill="y")

#         # Thêm dữ liệu mẫu vào bảng (tùy chọn)
#         sample_data = [
#             (1, "CA001", "Ca A", "08:00", "17:00", "Active"),
#             (2, "CA002", "Ca B", "09:00", "18:00", "Inactive"),
#             (3, "CA003", "Ca C", "10:00", "19:00", "Active"),
#         ]

#         # Lặp qua dữ liệu mẫu và thêm vào bảng
#         for row in sample_data:
#             self.table.insert("", "end", values=row)

#         self.shiftWindow.mainloop()

#     def back_LichLamViec(self):
#         self.shiftWindow.destroy()
#         from Backup.src.View.n6_LichLamViecGUI import LichLamViecGUI
#         LichLamViecGUI()
    
#     def create_form_row(self, parent, label_text, row_index):
#          # Tạo label với font đã chỉ định
#         label = ctk.CTkLabel(parent, text=label_text, font=("Arial", 14, "bold"), text_color="#000")
#         label.grid(row=row_index, column=0, padx=(30, 10), pady=10, sticky="w")
        
#         # Tạo input entry với font đã chỉ định
#         entry = ctk.CTkEntry(parent, font=("Arial", 14), height=34, bg_color="white")
#         entry.grid(row=row_index, column=1, padx=(10,30), pady=10, sticky="ew")  # Căn đều theo chiều ngang
        
#         # Cấu hình chiều rộng cho các cột
#         parent.grid_columnconfigure(0, minsize=100)  # Cột label có min width là 100px
#         parent.grid_columnconfigure(1, weight=1)  # Cột input chiếm phần còn lại

#          # Trả về đối tượng entry
#         return entry

#     def create_combobox_row(self, parent, label_text, row_index, values):
#         # Tạo label với font đã chỉ định
#         label = ctk.CTkLabel(parent, text=label_text, font=("Arial", 14, "bold"), text_color="#000")
#         label.grid(row=row_index, column=0, padx=(30, 10), pady=10, sticky="w")
        
#         # Tạo combobox với font đã chỉ định và giá trị
#         combobox = ctk.CTkComboBox(parent, values=values, font=("Arial", 14), height=34, state="readonly")
#         combobox.grid(row=row_index, column=1, padx=(10, 30), pady=10, sticky="ew")  # Căn đều theo chiều ngang

#         # Cấu hình chiều rộng cho các cột
#         parent.grid_columnconfigure(0, minsize=100)  # Cột label có min width là 100px
#         parent.grid_columnconfigure(1, weight=1)  # Cột combobox chiếm phần còn lại

#         # Trả về đối tượng combobox
#         return combobox
    
#     def add_shift(self):
#         # Xử lý thêm ca làm mới
#         print("Thêm ca làm mới")
#         # Thực hiện các thao tác cần thiết khi thêm ca, ví dụ lưu vào cơ sở dữ liệu.

#     def edit_shift(self):
#         # Xử lý chỉnh sửa ca làm đã chọn
#         print("Chỉnh sửa ca làm")
#         # Lấy thông tin từ các input và cập nhật ca làm đã chọn.

#     def delete_shift(self):
#         # Xử lý xóa ca làm đã chọn
#         print("Xóa ca làm")
#         # Thực hiện thao tác xóa trên cơ sở dữ liệu hoặc danh sách hiện tại.

#     def refresh_shift(self):
#         # Làm mới danh sách ca làm từ cơ sở dữ liệu
#         print("Làm mới danh sách ca làm")
#         # Ví dụ, có thể tải lại danh sách từ cơ sở dữ liệu và hiển thị lại trong bảng.

#     def reset_shift(self):
#         # Xóa các trường input trong form
#         print("Reset form ca làm")
#         # Xóa sạch các ô input trong form về trạng thái ban đầu.
#



import tkinter as tk
import utilView
import customtkinter as ctk
from tkinter import ttk, messagebox
from time import strftime
from PIL import ImageTk, Image
from tkinter import simpledialog
from datetime import datetime
import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
bus_dir = os.path.join(current_dir, '../BUS')
sys.path.append(bus_dir)
from CaLamBUS import CaLamBUS

dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)
from CaLamDTO import CaLamDTO


class ShiftGUI:
    def __init__(self):
        self.shiftWindow = None
        self.is_view_detail = False

        # Khởi tạo giao diện người dùng
        self.initUI()

        # Khởi tạo BUS và danh sách ca làm
        self.ca_lam_bus = CaLamBUS.getInstance()
        self.ds_calam = self.ca_lam_bus.getall()

        # Hiển thị bảng dữ liệu
        self.render_table(self.ds_calam)

        # Bắt đầu vòng lặp chính của cửa sổ
        self.shiftWindow.mainloop()

    def initUI(self):
        icon_dir = os.path.join(current_dir, '../Icon')

        self.shiftWindow = tk.Tk()
        wWindow = 1000
        hWindow = 650
        self.shiftWindow.geometry(f"{wWindow}x{hWindow}+300+40")
        frameShift = utilView.frameUtil(self.shiftWindow, wWindow, hWindow, 0, 0, bg='#ffffff')

        # Header
        header = tk.Frame(frameShift, width=1000, height=40, bg="#908181")
        header.pack(pady=(10, 0), fill='x')
        header.pack_propagate(False)
        title = tk.Label(header, text="QUẢN LÍ CA LÀM", font=("Arial", 16, "bold"), bg="#908181", fg="black")
        title.pack(side="right", expand=True)

        # Close button
        arrow = Image.open(os.path.join(icon_dir, "arrow.png"))
        self.close_icon = ImageTk.PhotoImage(arrow)
        close_button = tk.Button(header, image=self.close_icon, height=40, width=40, bg="#908181", bd=0,
                                 command=self.back_LichLamViec)
        close_button.pack(side="left")

        body_height = hWindow - 50
        body = tk.Frame(frameShift, width=980, height=body_height, bg="#fff")
        body.pack(pady=0, padx=0, fill='both')
        body.pack_propagate(False)

        # Left frame for form
        left_frame = tk.Frame(body, width=400, height=body_height, bg="#fff")
        left_frame.pack(side="left", fill="y")

        form_shift = ctk.CTkFrame(left_frame, width=400, height=400, fg_color="#fff", corner_radius=0)
        form_shift.pack(side="top", fill="both", expand=True, pady=(50, 0))

        # Create form fields
        self.maca = self.create_form_row(form_shift, "Mã ca:", 0)
        self.maca.configure(state="readonly")
        self.tenca = self.create_form_row(form_shift, "Tên ca:", 1)
        self.tgvao = self.create_form_row(form_shift, "Thời gian vào:", 2)
        self.tgra = self.create_form_row(form_shift, "Thời gian ra:", 3)
        states_shift = ["Active", "Inactive"]
        self.tt = self.create_combobox_row(form_shift, "Trạng thái:", 4, states_shift)
        self.tt.configure(state="readonly")


        # Separator
        separator = tk.Frame(left_frame, height=2, bg="#dfdfdf")
        separator.pack(fill="x", pady=(10, 10))

        # Buttons
        buttons = tk.Frame(left_frame, width=400, height=200, bg="#fff")
        buttons.pack(side="bottom", fill="both")
        buttons.grid_propagate(False)

        btn_add = ctk.CTkButton(
            buttons,
            text="Thêm",
            width=100,
            height=30,
            fg_color="#000",
            text_color="#fff",
            font=("Arial", 14, "bold"),
            corner_radius=4,
            border_width=0,
            hover_color="#383838",
            command=self.add_shift
        )
        btn_add.grid(row=0, column=0, padx=(35, 5), pady=(20, 5))

        btn_edit = ctk.CTkButton(
            buttons,
            text="Sửa",
            width=100,
            height=30,
            fg_color="#000",
            text_color="#fff",
            font=("Arial", 14, "bold"),
            corner_radius=4,
            border_width=0,
            hover_color="#383838",
            command=self.edit_shift
        )
        btn_edit.grid(row=0, column=1, padx=5, pady=(20, 5))

        btn_delete = ctk.CTkButton(
            buttons,
            text="Xoá",
            width=100,
            height=30,
            fg_color="#000",
            text_color="#fff",
            font=("Arial", 14, "bold"),
            corner_radius=4,
            border_width=0,
            hover_color="#383838",
            command=self.delete_shift
        )
        btn_delete.grid(row=0, column=2, padx=5, pady=(20, 5))

        btn_refresh = ctk.CTkButton(
            buttons,
            text="Refresh",
            width=100,
            height=30,
            fg_color="#000",
            text_color="#fff",
            font=("Arial", 14, "bold"),
            corner_radius=4,
            border_width=0,
            hover_color="#383838",
            command=self.refresh_shift
        )
        btn_refresh.grid(row=1, column=0, padx=(35, 5), pady=(10, 5))

        btn_reset = ctk.CTkButton(
            buttons,
            text="Reset",
            width=100,
            height=30,
            fg_color="#000",
            text_color="#fff",
            font=("Arial", 14, "bold"),
            corner_radius=4,
            border_width=0,
            hover_color="#383838",
            command=self.reset_shift
        )
        btn_reset.grid(row=1, column=1, padx=(5, 10), pady=(10, 5))

        # Right frame for table
        right_frame = tk.Frame(body, width=600, height=body_height, bg="pink")
        right_frame.pack(side="right", fill="y", padx=10, pady=10)

        # Create table (Treeview) for shifts
        columns = ("STT", "Mã ca", "Tên ca", "Thời gian vào", "Thời gian ra", "Trạng thái")
        self.table = ttk.Treeview(right_frame, columns=columns, show="headings", height=20)
        self.table.bind("<Double-1>", self.on_double_click)

        column_width = 580 // len(columns)
        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, anchor="center", width=column_width)

        scrollbar = ttk.Scrollbar(right_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)

        self.table.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def create_form_row(self, parent, label_text, row_index):
        label = ctk.CTkLabel(parent, text=label_text, font=("Arial", 14, "bold"), text_color="#000")
        label.grid(row=row_index, column=0, padx=(30, 10), pady=10, sticky="w")

        entry = ctk.CTkEntry(parent, font=("Arial", 14), height=34, bg_color="white")
        entry.grid(row=row_index, column=1, padx=(10, 30), pady=10, sticky="ew")

        parent.grid_columnconfigure(0, minsize=100)
        parent.grid_columnconfigure(1, weight=1)

        return entry

    def create_combobox_row(self, parent, label_text, row_index, values):
        label = ctk.CTkLabel(parent, text=label_text, font=("Arial", 14, "bold"), text_color="#000")
        label.grid(row=row_index, column=0, padx=(30, 10), pady=10, sticky="w")

        combobox = ctk.CTkComboBox(parent, values=values, font=("Arial", 14), height=34)
        combobox.grid(row=row_index, column=1, padx=(10, 30), pady=10, sticky="ew")

        parent.grid_columnconfigure(0, minsize=100)
        parent.grid_columnconfigure(1, weight=1)

        return combobox

    def render_table(self, ds_calam):
        for i in self.table.get_children():
            self.table.delete(i)
        for index, calam in enumerate(ds_calam, start=1):
            tt = "Active" if calam.get_Status() else "Inactive"
            self.table.insert("", "end", values=(index, calam.get_MaCa(), calam.get_TenCa(), calam.get_ThoiGianVao(), calam.get_ThoiGianRa(), tt))

    def add_shift(self):
        if self.is_view_detail: return

        tenca = self.tenca.get()
        tgvao = self.tgvao.get()
        tgra = self.tgra.get()
        tt = 1 if self.tt.get() == "Active" else 0

        if not tenca or not tgvao or not tgra:
            utilView.show_message("Vui lòng nhập đầy đủ thông tin!", "warning")
            return

        maca = self.ca_lam_bus.tao_ma()

        shift = CaLamDTO(maca, tenca, tgvao, tgra, tt)
        res = self.ca_lam_bus.add(shift)

        if res[0] == 1:
            messagebox.showinfo("Thông báo", res[1])
            self.refresh_shift()
        else:
            messagebox.showerror("Lỗi", res[1])
            

    def edit_shift(self):
        if not self.is_view_detail: return

        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn ca làm cần sửa")
            return
        shift_info = self.table.item(selected_item)["values"]
        maca = self.maca.get()
        tenca = self.tenca.get()
        tgvao = self.tgvao.get()
        tgra = self.tgra.get()
        tt = 1 if self.tt.get() == "Active" else 0


        if not tenca or not tgvao or not tgra:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin!")
            return

        shift = CaLamDTO(maca, tenca, tgvao, tgra, tt)
        res = self.ca_lam_bus.update(shift)
        if res[0] == 1:
            messagebox.showinfo("Thông báo", res[1])
            self.refresh_shift()
        else:
            messagebox.showerror("Lỗi", res[1])


    def delete_shift(self):
        if not self.is_view_detail: return

        selected_item = self.table.selection()
        if not selected_item:           
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn ca làm cần xoá")
            return
        

        shift_info = self.table.item(selected_item)["values"]
        maca = shift_info[1]

        if maca == 'CA999':
            messagebox.showwarning("Cảnh báo", "Ca làm này không nên xoá(Ca OFF)")
            return
        
        res = self.ca_lam_bus.delete(maca)

        if res[0] == 1:
            messagebox.showinfo("Thông báo", res[1])
            self.refresh_shift()
        else:
            messagebox.showerror("Lỗi", res[1])


    def refresh_shift(self):
        self.reset_shift()
        self.ds_calam = self.ca_lam_bus.getall()
        self.render_table(self.ds_calam)
        self.is_view_detail = False


    def reset_shift(self):
        self.maca.configure(state="normal")
        self.maca.delete(0, 'end')
        self.maca.configure(state="readonly")
        self.tenca.delete(0, 'end')
        self.tgvao.delete(0, 'end')
        self.tgra.delete(0, 'end')
        self.tt.set("Active")
        self.shiftWindow.focus_set() 
        self.is_view_detail = False


    def on_double_click(self, event):
        selected_item = self.table.selection()
        if selected_item:
            self.is_view_detail = True
            shift_info = self.table.item(selected_item)["values"]

            # Xóa nội dung cũ trước khi chèn mới
            self.maca.configure(state="normal")
            self.maca.delete(0, tk.END)
            self.tenca.delete(0, tk.END)
            self.tgvao.delete(0, tk.END)
            self.tgra.delete(0, tk.END)
            self.tt.set("")  # Clear StringVar

            self.maca.insert(0, shift_info[1])
            self.maca.configure(state="readonly")
            self.tenca.insert(0, shift_info[2])
            self.tgvao.insert(0, shift_info[3])
            self.tgra.insert(0, shift_info[4])
            self.tt.set(shift_info[5])

    def back_LichLamViec(self):
        self.shiftWindow.destroy()
        from n6_LichLamViecGUI import LichLamViecGUI
        LichLamViecGUI()


if __name__ == "__main__":
    xep_ca = ShiftGUI()

