import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Import DateEntry
from PIL import ImageTk, Image
from tkinter import simpledialog
from datetime import datetime
import os, sys

# Định nghĩa đường dẫn cho các thư mục cần thiết
current_dir = os.path.dirname(os.path.abspath(__file__))
bus_dir = os.path.join(current_dir, '../BUS')
sys.path.append(bus_dir)
from LsccBUS import LsccBUS

dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)
from LsccDTO import LsccDTO

class ShiftGUI:
    def __init__(self):
        self.shiftWindow = None
        self.is_view_detail = False

        # Khởi tạo giao diện người dùng
        self.initUI()

        # Khởi tạo BUS và danh sách ca làm
        self.lich_su_bus = LsccBUS.getInstance()  # Lấy instance của LsccBUS
        self.ds_lichsu = self.lich_su_bus.getall()  # Lấy tất cả dữ liệu lịch sử chấm công

        # Hiển thị bảng dữ liệu
        self.render_table(self.ds_lichsu)

        # Bắt đầu vòng lặp chính của cửa sổ
        self.shiftWindow.mainloop()

    def initUI(self):
        icon_dir = os.path.join(current_dir, '../Icon')

        # Khởi tạo cửa sổ chính
        self.shiftWindow = tk.Tk()
        wWindow = 1000
        hWindow = 650
        self.shiftWindow.geometry(f"{wWindow}x{hWindow}+300+40")
        self.shiftWindow.title("Quản Lý Ca Làm")

        # Frame chứa tất cả các widget
        frameShift = tk.Frame(self.shiftWindow, bg='#ffffff')
        frameShift.pack(fill=tk.BOTH, expand=True)

        # Tạo giao diện bên trái (nơi nhập liệu)
        left_panel = tk.Frame(frameShift, bg="white", width=400)
        left_panel.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Tạo giao diện bên phải (nơi hiển thị bảng)
        right_panel = tk.Frame(frameShift, bg="white", width=600)
        right_panel.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        frameShift.grid_columnconfigure(0, weight=1)
        frameShift.grid_columnconfigure(1, weight=2)

        # ---------------------- Phần Bên Trái ----------------------
        self.maca_label = tk.Label(left_panel, text="Mã Ca:", bg="white")
        self.maca_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.maca_entry = tk.Entry(left_panel, width=20, bg='#E5E5E5')
        self.maca_entry.grid(row=0, column=1, padx=10, pady=10)

        self.ngay_label = tk.Label(left_panel, text="Ngày:", bg="white")
        self.ngay_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.ngay_entry = DateEntry(left_panel, width=16, background="darkblue", foreground="white", borderwidth=2)
        self.ngay_entry.grid(row=1, column=1, padx=10, pady=10)

        self.tgvao_label = tk.Label(left_panel, text="Thời gian vào:", bg="white")
        self.tgvao_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.tgvao_entry = tk.Entry(left_panel, width=20, bg='#E5E5E5')
        self.tgvao_entry.grid(row=2, column=1, padx=10, pady=10)

        self.tgra_label = tk.Label(left_panel, text="Thời gian ra:", bg="white")
        self.tgra_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.tgra_entry = tk.Entry(left_panel, width=20, bg='#E5E5E5')
        self.tgra_entry.grid(row=3, column=1, padx=10, pady=10)

        self.tt_label = tk.Label(left_panel, text="Tình trạng:", bg="white")
        self.tt_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.tt_entry = tk.Entry(left_panel, width=20, bg='#E5E5E5')
        self.tt_entry.grid(row=4, column=1, padx=10, pady=10)

        self.edit_button = tk.Button(left_panel, text="Sửa", command=self.on_edit_button_click)
        self.edit_button.grid(row=5, column=0, padx=10, pady=20, sticky="w")

        # ---------------------- Phần Bên Phải ----------------------
        details_label = tk.Label(right_panel, text="Chi tiết ca làm", font=("Helvetica", 16), bg="white")
        details_label.pack(pady=20)

        # Tạo bảng Treeview cho ca làm
        columns = ('Mã Ca', 'Ngày', 'Thời gian vào', 'Thời gian ra', 'Tình trạng')

        self.tree = ttk.Treeview(right_panel, columns=columns, show='headings', height=10)
        self.tree.heading('Mã Ca', text='Mã Ca')
        self.tree.heading('Ngày', text='Ngày')
        self.tree.heading('Thời gian vào', text='Thời gian vào')
        self.tree.heading('Thời gian ra', text='Thời gian ra')
        self.tree.heading('Tình trạng', text='Tình trạng')

        self.tree.column('Mã Ca', width=100, anchor='center')
        self.tree.column('Ngày', width=100, anchor='center')
        self.tree.column('Thời gian vào', width=120, anchor='center')
        self.tree.column('Thời gian ra', width=120, anchor='center')
        self.tree.column('Tình trạng', width=120, anchor='center')

        self.tree.pack(pady=10)

        self.tree.bind("<Double-1>", self.on_double_click)

        

    def render_table(self, ds_lichsu):
        """ Hiển thị dữ liệu vào bảng Treeview """
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        # check if ds_lichsu is empty
        if not ds_lichsu:
            return

        for item in ds_lichsu:
            # Convert LsccDTO to a tuple of its attributes
            if isinstance(item, LsccDTO):
                print(item)
                row = (
                    item.get_MaCa(),
                    item.get_Ngay(),
                    item.get_ThoiGianVao(),
                    item.get_ThoiGianRa(),
                    item.get_TinhTrang()
                )
            else:
                # If it's not an LsccDTO instance, skip or handle other types
                # console output
                print(item)
                continue

            # Insert the tuple as a row into the Treeview
            self.tree.insert('', 'end', values=row)

    def on_edit_button_click(self):
        """ Sự kiện khi nhấn nút Sửa """
        selected_item = self.tree.selection()
        if selected_item:
            print(selected_item)
            maca = self.maca_entry.get()
            ngay = self.ngay_entry.get_date()  # Lấy ngày từ DateEntry
            tgvao = self.tgvao_entry.get()
            tgra = self.tgra_entry.get()
            tt = self.tt_entry.get()

            if maca and ngay and tgvao and tgra and tt:
                # Tạo đối tượng LsccDTO với dữ liệu mới
                updated_shift = LsccDTO(maca, ngay, tgvao, tgra, tt)
                
                # Cập nhật ca làm thông qua BUS
                self.lich_su_bus.update_shift(selected_item[0], updated_shift)
                
                # Cập nhật lại danh sách lịch sử chấm công và làm mới bảng
                self.ds_lichsu = self.lich_su_bus.getall()
                self.render_table(self.ds_lichsu)
                
                messagebox.showinfo("Thông báo", "Cập nhật ca làm thành công!")
            else:
                messagebox.showwarning("Cảnh báo", "Vui lòng điền đầy đủ thông tin!")
        else:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một ca làm để sửa!")

    def on_double_click(self, event):
        selected_item = self.tree.selection()
        if selected_item:

            self.is_view_detail = True
            shift_info = self.tree.item(selected_item)["values"]
            # print(shift_info)

            # Xóa nội dung cũ trước khi chèn mới
            # self.mabcc.configure(state="normal")
            self.maca_entry.delete(0, tk.END)
            self.ngay_entry.delete(0, tk.END)
            self.tgvao_entry.delete(0, tk.END)
            self.tgra_entry.delete(0, tk.END)
            self.tt_entry.delete(0,tk.END)  # Clear StringVar

            self.maca_entry.insert(0, shift_info[0])
            # self.mabcc.configure(state="readonly")
            self.ngay_entry.insert(0, shift_info[1])
            self.tgvao_entry.insert(0, shift_info[2])
            self.tgra_entry.insert(0, shift_info[3])
            self.tt_entry.insert(0,shift_info[4])
if __name__ == "__main__":
    ShiftGUI()
