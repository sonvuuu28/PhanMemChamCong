import tkinter as tk
from tkinter import ttk
import utilView
import customtkinter as ctk
from PIL import Image, ImageTk
import os
import sys
from tkinter import messagebox
import shutil
from tkinter import filedialog, messagebox

current_dir = os.path.dirname(os.path.abspath(__file__))
dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)
from NhanVienDTO import NhanVienDTO

bus_dir = os.path.join(current_dir, '../BUS')
sys.path.append(bus_dir)
from NhanVienBUS import NhanVienBUS

dao_dir = os.path.join(current_dir, '../DAO')
sys.path.append(dao_dir)
from NhanVienDAO import NhanVienDAO

class NhanVienGUI:
    def __init__(self, id):
        self.id = id
        self.BtnThem = None
        self.BtnSua = None
        self.BtnXoa = None
        self.BtnTimKiem = None
        self.BtnTaiLai = None
        self.BtnThongTinTK = None
        self.tree = None
        self.Ma = None
        self.Ten = None
        self.NgaySinh = None
        self.GioiTinh = None
        self.DiaChi = None
        self.SDT = None
        self.ChucVu = None
        self.HinhAnh = None
        self.UI()
    def on_item_selected(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item(selected_item[0])['values']

            self.Ma.delete(0, tk.END)
            self.Ma.insert(0, item_values[0])

            self.Ten.delete(0, tk.END)
            self.Ten.insert(0, item_values[1])

            self.NgaySinh.delete(0, tk.END)
            self.NgaySinh.insert(0, item_values[2])

            self.GioiTinh.set(item_values[3])

            self.DiaChi.delete(0, tk.END)
            self.DiaChi.insert(0, item_values[4])

            self.SDT.delete(0, tk.END)
            self.SDT.insert(0,'0' +  str(item_values[5]))

            self.ChucVu.set(item_values[6])

            self.update_hinh_anh_entry(item_values[7])
            
    def chon_anh(self):
        # Lấy đường dẫn thư mục gốc của dự án (dựa trên vị trí file hiện tại)
        project_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Đường dẫn thư mục ảnh
        source_folder = os.path.join(project_dir, "../../ImageEmployee")  # Điều chỉnh theo cấu trúc dự án

        # Mở hộp thoại chọn file
        file_path = filedialog.askopenfilename(
            title="Chọn ảnh",
            initialdir=source_folder,  # Thư mục mở mặc định
            filetypes=[("Ảnh", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
        )

        if file_path:  # Nếu người dùng chọn ảnh
            # Lấy tên file gốc
            file_name = os.path.basename(file_path)
            self.HinhAnh.delete(0, 'end')  # Xóa nội dung cũ trong Entry
            self.HinhAnh.insert(0, file_name)
            self.update_hinh_anh_entry(file_name)
            messagebox.showinfo("Thành công", f"Bạn đã chọn ảnh: {file_name}")
        else:
            # Hiển thị thông báo hủy bỏ
            messagebox.showwarning("Hủy bỏ", "Bạn chưa chọn ảnh nào!")
         
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
            TrangChuGUI(self.id)
            
        if nut == "ChonTK" and window:
            from n2_TaiKhoanGUI import TaiKhoanGUI
            ma = self.Ma.get()
            nv_dao = NhanVienDAO.getInstance()
            try:
                nv = nv_dao.TimKiem_Theo_Ma(ma)
                # nv.display_info()
                tk = TaiKhoanGUI(window, nv)
            except Exception as e:
                messagebox.showinfo("Thông báo", "Mã nhân viên không tồn tại !")
                print(e)
                
    def update_hinh_anh_entry(self, value):
        self.HinhAnh.configure(state="normal")  # Chuyển sang chế độ có thể chỉnh sửa
        self.HinhAnh.delete(0, tk.END)         # Xóa nội dung cũ
        self.HinhAnh.insert(0, value)         # Gán nội dung mới
        self.HinhAnh.configure(state="readonly")  # Đặt lại chế độ readonly

      
    def listBang(self):
        self.tree.delete(*self.tree.get_children())
        nv_bus = NhanVienBUS.getInstance()
        danh_sach_nv = nv_bus.list()
        num = 1
        for i in danh_sach_nv:
            self.tree.insert("", "end", text=str(num), values=(i.get_MaNhanVien(), i.get_Ten(), i.get_NgaySinh().strftime('%d/%m/%Y'), i.get_GioiTinh(), i.get_DiaChi(), i.get_SDT(), i.get_ChucVu(), i.get_HinhAnh()))
            num += 1
            
    def delete(self):
        nv_bus = NhanVienBUS.getInstance()
        ma = self.Ma.get()
        ten = self.Ten.get()
        noti = nv_bus.delete(ma)
        messagebox.showinfo("Thông báo", noti)
        if noti == 'Xóa Thành Công':
            self.refresh()
        self.listBang()
    
    def insert(self):
        if self.checkInput():
            return
        ## check ngày sinh
        NgaySinh = self.NgaySinh.get()
        if utilView.convert_date_format(NgaySinh) == 0:
            self.NgaySinh.focus_set()
            messagebox.showinfo("Thông báo", "Ngày sinh không hợp lệ !")
            return
        else:
            NgaySinh = utilView.convert_date_format(NgaySinh)
        ## check sdt
        SDT = self.SDT.get()
        if utilView.kiem_tra_so_dien_thoai(SDT) == False:
            self.SDT.focus_set()
            messagebox.showinfo("Thông báo", "Số điện thoại không hợp lệ !")
            return
        else:
            SDT = utilView.kiem_tra_so_dien_thoai(SDT)
        
        nv_bus = NhanVienBUS.getInstance()
        ma = self.Ma.get()
        ten = self.Ten.get()
        GioiTinh = self.GioiTinh.get()
        DiaChi = self.DiaChi.get()
        ChucVu = self.ChucVu.get() 
        HinhAnh = self.HinhAnh.get()
        
        nv =  NhanVienDTO(ma, ten, NgaySinh, GioiTinh, DiaChi, SDT, ChucVu, HinhAnh, True)
        nv.display_info()
        nv_gui = NhanVienBUS.getInstance()
        noti = nv_gui.insert(nv)
        messagebox.showinfo("Thông báo", noti)
        if noti == 'Thêm Thành Công':
            self.refresh()
        self.listBang()
    
    def update(self):
        if self.checkInput():
            return
            
        ## check ngày sinh
        NgaySinh = self.NgaySinh.get()
        if utilView.convert_date_format(NgaySinh) == 0:
            self.NgaySinh.focus_set()
            messagebox.showinfo("Thông báo", "Ngày sinh không hợp lệ !")
            return
        else:
            NgaySinh = utilView.convert_date_format(NgaySinh)
        ## check sdt
        SDT = self.SDT.get()
        if utilView.kiem_tra_so_dien_thoai(SDT) == False:
            self.SDT.focus_set()
            messagebox.showinfo("Thông báo", "Số điện thoại không hợp lệ !")
            return
        else:
            SDT = utilView.kiem_tra_so_dien_thoai(SDT)
        
        ma = self.Ma.get()
        ten = self.Ten.get()
        GioiTinh = self.GioiTinh.get()
        DiaChi = self.DiaChi.get()
        ChucVu = self.ChucVu.get() 
        HinhAnh = self.HinhAnh.get()
        
        nv =  NhanVienDTO(ma, ten, NgaySinh, GioiTinh, DiaChi, SDT, ChucVu, HinhAnh, True)
        nv.display_info()
        nv_gui = NhanVienBUS.getInstance()
        noti = nv_gui.update(nv)
        messagebox.showinfo("Thông báo", noti)
        self.listBang()
    
    def refresh(self):
        self.Ma.delete(0, 'end')
        self.Ma.insert(0, self.tao_MaNhanVien())
        self.Ten.delete(0, 'end')
        self.NgaySinh.delete(0, 'end')
        self.DiaChi.delete(0, 'end')
        self.SDT.delete(0, 'end')
        self.HinhAnh.configure(state="normal")
        self.HinhAnh.delete(0, 'end')
        self.HinhAnh.configure(state="readonly") 
        self.listBang()
        
    def tao_MaNhanVien(self):
        ma = NhanVienDAO.getInstance().tao_MaNhanVien()
        return ma
        
    def checkInput(self):
        error_flag = False
        if self.Ma.get() == "" and error_flag == False:
            messagebox.showinfo("Thông báo", "Vui lòng nhập mã nhân viên!")
            self.Ma.focus_set()
            error_flag = True

        if self.Ten.get() == "" and error_flag == False:
            messagebox.showinfo("Thông báo", "Vui lòng nhập tên nhân viên!")
            self.Ten.focus_set()
            error_flag = True

        if self.NgaySinh.get() == "" and error_flag == False:
            messagebox.showinfo("Thông báo", "Vui lòng nhập ngày sinh!")
            self.NgaySinh.focus_set()
            error_flag = True

        if self.DiaChi.get() == "" and error_flag == False:
            messagebox.showinfo("Thông báo", "Vui lòng nhập địa chỉ!")
            self.DiaChi.focus_set()
            error_flag = True

        if self.SDT.get() == "" and error_flag == False:
            messagebox.showinfo("Thông báo", "Vui lòng nhập số điện thoại!")
            self.SDT.focus_set()
            error_flag = True

        if self.HinhAnh.get() == "" and error_flag == False:
            messagebox.showinfo("Thông báo", "Vui lòng nhập đường dẫn hình ảnh!")
            self.HinhAnh.focus_set()
            error_flag = True
            
        return error_flag
    
    def TimKiem(self):
        self.tree.delete(*self.tree.get_children())
        nv_bus = NhanVienDAO.getInstance()
        NgaySinh = self.NgaySinh.get()
        SDT = self.SDT.get()
        ma = self.Ma.get()
        ten = self.Ten.get()
        GioiTinh = self.GioiTinh.get()
        DiaChi = self.DiaChi.get()
        ChucVu = self.ChucVu.get() 
        HinhAnh = self.HinhAnh.get()
        
        nv =  NhanVienDTO(ma, ten, NgaySinh, GioiTinh, DiaChi, SDT, ChucVu, HinhAnh, True)
        danh_sach_nv = nv_bus.timKiem(nv)
        nv.display_info()
        num = 1
        for i in danh_sach_nv:
            self.tree.insert("", "end", text=str(num), values=(i.get_MaNhanVien(), i.get_Ten(), i.get_NgaySinh(), i.get_GioiTinh(), i.get_DiaChi(), i.get_SDT(), i.get_ChucVu(), i.get_HinhAnh()))
            num += 1
    
    def UI(self):
        window = tk.Tk()
        xWindow = 1200
        yWindow = 700
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_dir = os.path.join(current_dir, '../Icon')
        
        frameBiggest = utilView.frameUtil(window, xWindow, yWindow, 0, 0, bg='#ffffff')
        
        homeImage = Image.open(os.path.join(icon_dir, "home.png"))
        tk_homeImage = ImageTk.PhotoImage(homeImage)
        homeImageHover = Image.open(os.path.join(icon_dir, "homeHover.png"))
        tk_homeImageHover = ImageTk.PhotoImage(homeImageHover)

        label_home = tk.Label(frameBiggest, image=tk_homeImage, bg='white')
        label_home.image = tk_homeImage
        label_home.place(x=30, y=30)
        label_home.bind("<Button-1>", lambda event: self.print_nut("Home", window))
        self.hover(label_home, tk_homeImage, tk_homeImageHover, None)
        
        utilView.labelUtil(frameBiggest,'Quản Lý Nhân Viên', 420, 50, bg='#ffffff', font=("Arial", 28, "bold"))
        
        frameVo = utilView.frameUtil(frameBiggest, 270, 400, 50, 150, bg='#000000')
        frameInput = utilView.frameUtil(frameVo, 258, 388, 6, 6, bg='#ffffff')
        
        utilView.labelUtil(frameInput,'Thông Tin Nhân Viên',58, 10, bg='#ffffff', font=("Arial", 12, "bold"))
        
        utilView.labelUtil(frameInput,'Mã',20, 60, bg='#ffffff', font=("Arial", 12))
        utilView.labelUtil(frameInput,'Tên',20, 100, bg='#ffffff', font=("Arial", 12))
        utilView.labelUtil(frameInput,'Ngày Sinh',20, 140, bg='#ffffff', font=("Arial", 12))
        utilView.labelUtil(frameInput,'Giới Tính',20, 180, bg='#ffffff', font=("Arial", 12))
        utilView.labelUtil(frameInput,'Địa Chỉ',20, 220, bg='#ffffff', font=("Arial", 12))
        utilView.labelUtil(frameInput,'SĐT',20, 260, bg='#ffffff', font=("Arial", 12))
        utilView.labelUtil(frameInput,'Chức Vụ',20, 300, bg='#ffffff', font=("Arial", 12))
        utilView.labelUtil(frameInput,'Hình Ảnh',20, 340, bg='#ffffff', font=("Arial", 12))
        
        self.Ma = utilView.entryUtil(frameInput, self.tao_MaNhanVien(), 120, 60, 100)
        utilView.lineUtil(frameInput, 60, 180, 80)
        
        self.Ten = utilView.entryUtil(frameInput, '', 120, 100, 100)
        utilView.lineUtil(frameInput, 60, 180, 120)
        
        self.NgaySinh = utilView.entryUtil(frameInput, '', 120, 140, 100)
        utilView.lineUtil(frameInput, 60, 180, 160)
        
        self.GioiTinh = ttk.Combobox(frameInput, values=["Nam", "Nữ"], width=10)
        self.GioiTinh.place(x = 120, y = 180)
        self.GioiTinh.set("Nam")
        
        self.DiaChi = utilView.entryUtil(frameInput, '', 120, 220, 100)
        utilView.lineUtil(frameInput, 60, 180, 240)
        
        self.SDT = utilView.entryUtil(frameInput, '', 120, 260, 100)
        utilView.lineUtil(frameInput, 60, 180, 280)
        
        self.ChucVu = ttk.Combobox(frameInput, values=["Nhân Viên", "Quản Lý"], width=10)
        self.ChucVu.place(x = 120, y = 300)
        self.ChucVu.set("Nhân Viên")
        
        nutChonHinhAnh = utilView.cusButtonUtil(frameBiggest, '...', 270, 497, 25, 25, fg_color="#CDCDCD", hover_color="#7F7D7D", text_color="#000000", command=lambda: self.chon_anh())
        self.HinhAnh = utilView.entryUtil(frameInput, '', 120, 340, 13, background="#e0e0e0",)
        self.HinhAnh.configure(state="readonly")
        utilView.lineUtil(frameInput, 60, 141, 360)
        
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 8, "bold"))
        
        self.tree = ttk.Treeview(frameBiggest, columns=("column1", "column2", "column3", "column4",\
                                                   "column5", "column6", "column7", "column8"), height=18)
        self.tree.heading("#0", text="STT")
        self.tree.heading("column1", text="Mã")
        self.tree.heading("column2", text="Tên")
        self.tree.heading("column3", text="Ngày Sinh")
        self.tree.heading("column4", text="Giới Tính")
        self.tree.heading("column5", text="Địa Chỉ")
        self.tree.heading("column6", text="Số Điện Thoại")
        self.tree.heading("column7", text="Chức Vụ")
        self.tree.heading("column8", text="Hình Ảnh") 
        
        self.tree.column("#0", width=50, anchor=tk.CENTER) 
        self.tree.column("column1", width=50, anchor=tk.W)  
        self.tree.column("column2", width=150, anchor=tk.W)  
        self.tree.column("column3", width=75, anchor=tk.W) 
        self.tree.column("column4", width=60, anchor=tk.W)
        self.tree.column("column5", width=150, anchor=tk.W)
        self.tree.column("column6", width=100, anchor=tk.W)
        self.tree.column("column7", width=75, anchor=tk.W)
        self.tree.column("column8", width=75, anchor=tk.W)
        self.tree.bind("<<TreeviewSelect>>", self.on_item_selected)
        self.listBang()
        self.tree.place(x=380, y=150)
        
        self.BtnThem = utilView.cusButtonUtil(frameBiggest, 'Thêm', 25, 600, 80, 30, fg_color="#000000", hover_color="#383838", command=lambda: self.insert())
        self.BtnSua = utilView.cusButtonUtil(frameBiggest, 'Sửa', 145, 600, 80, 30, fg_color="#000000", hover_color="#383838", command=lambda: self.update())
        self.BtnXoa = utilView.cusButtonUtil(frameBiggest, 'Xóa', 265, 600, 80, 30, fg_color="#000000", hover_color="#383838", command=lambda: self.delete())
        self.BtnTimKiem = utilView.cusButtonUtil(frameBiggest, 'Tìm Kiếm', 25, 650, 80, 30, fg_color="#000000", hover_color="#383838", command=lambda: self.TimKiem())
        self.BtnTaiLai = utilView.cusButtonUtil(frameBiggest, 'Tải Lại', 145, 650, 80, 30, fg_color="#000000", hover_color="#383838", command=lambda: self.refresh())
        self.BtnThongTinTK = utilView.cusButtonUtil(frameBiggest, 'Thông tin TK', 265, 650, 80, 30, fg_color="#000000", hover_color="#383838", command=lambda: self.print_nut("ChonTK", window))
              
        window.geometry(f"{xWindow}x{yWindow}+150+40")
        window.mainloop()

if __name__ == '__main__':
    NhanVienGUI()
