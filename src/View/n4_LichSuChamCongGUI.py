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
from NhanVienBUS import NhanVienBUS

dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)
from LsccDTO import LsccDTO
from NhanVienDTO import NhanVienDTO

class LichSuChamCongGUI:
    def __init__(self):
        self.shiftWindow = None
        self.is_view_detail = False

        # Khởi tạo giao diện người dùng
        self.initUI()

        # Khởi tạo BUS và danh sách ca làm
        self.lich_su_bus = LsccBUS.getInstance()  # Lấy instance của LsccBUS
        self.nhanvien_bus = NhanVienBUS.getInstance()  # Lấy instance của NhaNVviENbuS
        self.ds_lichsu = self.lich_su_bus.getbydate(self.ngay_entry.get_date())
   
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
        self.shiftWindow.title("LỊCH SỬ CHẤM CÔNG")

        # Frame chứa tất cả các widget
        frameShift = tk.Frame(self.shiftWindow, bg='#ffffff')
        frameShift.pack(fill=tk.BOTH, expand=True)

        homeImage = Image.open(os.path.join(icon_dir, "home.png"))
        tk_homeImage = ImageTk.PhotoImage(homeImage)
        homeImageHover = Image.open(os.path.join(icon_dir, "homeHover.png"))
        tk_homeImageHover = ImageTk.PhotoImage(homeImageHover)

        label_home = tk.Label(frameShift, image=tk_homeImage, bg='white')
        label_home.image = tk_homeImage
        label_home.place(x=30, y=30)
        label_home.bind("<Button-1>", lambda event: self.print_nut("Home", self.shiftWindow))
        self.hover(label_home, tk_homeImage, tk_homeImageHover, None)
        
        # Tạo giao diện bên trái (nơi nhập liệu)
        left_panel = tk.Frame(frameShift, bg="white", width=400)
        left_panel.grid(row=0, column=0, padx=10, pady=80, sticky="nsew")

        # Tạo giao diện bên phải (nơi hiển thị bảng)
        right_panel = tk.Frame(frameShift, bg="white", width=600)
        right_panel.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        frameShift.grid_columnconfigure(0, weight=1)
        frameShift.grid_columnconfigure(1, weight=2)

        # ---------------------- Phần Bên Trái ----------------------
        self.nv_label = tk.Label(left_panel, text="Nhân viên:", bg="white")
        self.nv_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.nv_entry = tk.Entry(left_panel, width=20, bg='#E5E5E5')
        self.nv_entry.grid(row=0, column=1, padx=10, pady=10)

        self.ngay_label = tk.Label(left_panel, text="Ngày:", bg="white")
        self.ngay_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.ngay_entry = DateEntry(left_panel, width=16, background="darkblue", foreground="white", borderwidth=2,date_pattern="dd/MM/yyyy")
        self.ngay_entry.grid(row=1, column=1, padx=10, pady=10)
        # Bắt sự kiện khi giá trị trong DateEntry thay đổi
        self.ngay_entry.bind("<<DateEntrySelected>>", self.on_date_change)

        self.tgvao_label = tk.Label(left_panel, text="Thời gian vào:", bg="white")
        self.tgvao_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.tgvao_entry = tk.Entry(left_panel, width=20, bg='#E5E5E5')
        self.tgvao_entry.grid(row=2, column=1, padx=10, pady=10)

        self.tgra_label = tk.Label(left_panel, text="Thời gian ra:", bg="white")
        self.tgra_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.tgra_entry = tk.Entry(left_panel, width=20, bg='#E5E5E5')
        self.tgra_entry.grid(row=3, column=1, padx=10, pady=10)

        # self.tt_label = tk.Label(left_panel, text="Tình trạng:", bg="white")
        # self.tt_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        # self.tt_entry = tk.Entry(left_panel, width=20, bg='#E5E5E5')
        # self.tt_entry.grid(row=4, column=1, padx=10, pady=10)
        # Tạo label cho tình trạng
        self.tt_label = tk.Label(left_panel, text="Tình trạng:", bg="white")
        self.tt_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        # Tạo combobox với các giá trị "Đúng" và "Trễ"
        self.tt_entry = tk.Entry(left_panel, width=20, bg='#E5E5E5')
        self.tt_entry.grid(row=4, column=1, padx=10, pady=10)



        # self.edit_button = tk.Button(left_panel, text="Sửa", command=self.on_edit_button_click)
        # self.edit_button.grid(row=5, column=0, padx=10, pady=20, sticky="w")

        # ---------------------- Phần Bên Phải ----------------------
        details_label = tk.Label(right_panel, text="CHI TIẾT CHẤM CÔNG", font=("Helvetica", 16), bg="white")
        details_label.pack(pady=20)

       # Tạo bảng Treeview với các cột mới
        columns = ('STT', 'Mã', 'Nhân viên', 'Ngày', 'Thời gian vào', 'Thời gian ra', 'Tình trạng')

        self.tree = ttk.Treeview(right_panel, columns=columns, show='headings', height=25)
        self.tree.heading('STT', text='STT')
        self.tree.heading('Mã', text='Mã')
        self.tree.heading('Nhân viên', text='Nhân viên')
        self.tree.heading('Ngày', text='Ngày')
        self.tree.heading('Thời gian vào', text='Thời gian vào')
        self.tree.heading('Thời gian ra', text='Thời gian ra')
        self.tree.heading('Tình trạng', text='Tình trạng')

        self.tree.column('STT', width=50, anchor='center')
        self.tree.column('Mã', width=100, anchor='center')
        self.tree.column('Nhân viên', width=100, anchor='center')
        self.tree.column('Ngày', width=100, anchor='center')
        self.tree.column('Thời gian vào', width=120, anchor='center')
        self.tree.column('Thời gian ra', width=120, anchor='center')
        self.tree.column('Tình trạng', width=120, anchor='center')
        self.tree.pack(pady=10)

        self.tree.bind("<Double-1>", self.on_double_click)

    def on_date_change(self, event):
        """ Xử lý khi ngày được thay đổi trong DateEntry """
        # Lấy ngày mới từ DateEntry
        selected_date = self.ngay_entry.get_date()
        
        # Lấy danh sách ca làm theo ngày từ BUS
        self.ds_lichsu = self.lich_su_bus.getbydate(selected_date)
        
        # Làm mới lại bảng với dữ liệu mới
        self.render_table(self.ds_lichsu)
    def render_table(self, ds_lichsu):
        """ Hiển thị dữ liệu vào bảng Treeview """
        # Xóa toàn bộ dữ liệu cũ trong bảng
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        # Nếu không có dữ liệu, thoát sớm
        if not ds_lichsu:
            messagebox.showinfo("Thông báo", "Không có dữ liệu để hiển thị!")
            return

        # Thêm dữ liệu vào bảng với số thứ tự
        for idx, item in enumerate(ds_lichsu, start=1):
            nv = self.nhanvien_bus.getById(item.get_MaNhanVien())
            row = (
                idx,  # Số thứ tự
                item.get_MaBCC(),  # Mã
                f"{nv.get_MaNhanVien()} - {nv.get_Ten()}",  # Ngày
                item.get_Ngay(),  # Ngày
                item.get_ThoiGianVao(),  # Thời gian vào
                item.get_ThoiGianRa(),  # Thời gian ra
                item.get_TinhTrang()  # Tình trạng
            )
            # Chèn dòng vào Treeview
            self.tree.insert('', 'end', values=row)

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

    def print_nut(self, nut, window=None):
        if nut == "Home" and window:
            window.destroy()
            from n1_TrangChuGUI import TrangChuGUI
            TrangChuGUI()

    def on_edit_button_click(self):
        """ Sự kiện khi nhấn nút Sửa """
        selected_item = self.tree.selection()
        if selected_item:
            print(selected_item)
            nv = self.nv_entry.get()
            ngay = self.ngay_entry.get_date()  # Lấy ngày từ DateEntry
            tgvao = self.tgvao_entry.get()
            tgra = self.tgra_entry.get()
            tt = self.tt_entry.get()

            if nv and ngay and tgvao and tgra and tt:
                # Tạo đối tượng LsccDTO với dữ liệu mới
                updated_shift = LsccDTO(nv, ngay, tgvao, tgra, tt)
                
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
            self.nv_entry.configure(state="normal")
            self.ngay_entry.configure(state="normal")
            self.tgvao_entry.configure(state="normal")
            self.tgra_entry.configure(state="normal")
            self.tt_entry.configure(state="normal")
            
            self.nv_entry.delete(0, tk.END)
            self.ngay_entry.delete(0, tk.END)
            self.tgvao_entry.delete(0, tk.END)
            self.tgra_entry.delete(0, tk.END)
            self.tt_entry.delete(0,tk.END)  # Clear StringVar

            self.nv_entry.insert(0, shift_info[2])
            # self.mabcc.configure(state="readonly")
            self.ngay_entry.insert(0, shift_info[3])
            self.tgvao_entry.insert(0, shift_info[4])
            self.tgra_entry.insert(0, shift_info[5])
            if shift_info[6] == 'Dung gio':
                self.tt_entry.insert(0, 'Đúng giờ')
            else: 
                self.tt_entry.insert(0, 'Trễ giờ')

            self.nv_entry.configure(state="readonly")
            self.ngay_entry.configure(state="readonly")
            self.tgvao_entry.configure(state="readonly")
            self.tgra_entry.configure(state="readonly")
            self.tt_entry.configure(state="readonly")

                
if __name__ == "__main__":
    LichSuChamCongGUI()