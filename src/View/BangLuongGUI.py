import tkinter as tk
import utilView
import customtkinter as ctk
from tkinter import ttk
from time import strftime
from PIL import Image, ImageTk


class BangLuongGUI:
    def __init__(self):
        self.myPath = "C:\\Users\\X\\HocPython\\PJ\\Test\\src\\"
        self.initUI()
    
    
    
    
    def initUI(self):
        salaryWindow = tk.Tk()
        wWindow = 1000
        hWindow = 650
        salaryWindow.geometry(f"{wWindow}x{hWindow}")
        frameSalary = utilView.frameUtil(salaryWindow, wWindow, hWindow, 0, 0, bg = '#ffffff')
        
        # Tạo frame cho header
        headerSalary = tk.Frame(frameSalary, width=1000, height=40, bg="#908181")
        headerSalary.pack(pady=(10, 0), fill='x')
        headerSalary.pack_propagate(False)  # Không thay đổi kích thước theo nội dung
       
        titleSalary = tk.Label(headerSalary, text="BẢNG LƯƠNG NHÂN VIÊN", font=("Arial", 16, "bold"), bg="#908181", fg="black")
        titleSalary.pack(side="left", expand=True)  # Căn giữa bên trái

        self.close_icon = ImageTk.PhotoImage(file=self.myPath + "Icon\\close.png")
        close_button = tk.Button(headerSalary, image=self.close_icon, height=40, width=40,bg="#908181", bd=0, command=salaryWindow.destroy)
        close_button.pack(side="right")  # Đặt nút bên phải của header



    
        body_height = hWindow - 60 - 180 - 10  # -60:header -180:footer - 10:paddingBody = 400

        body = tk.Frame(frameSalary, width=980, height=body_height, bg="white")
        body.pack(pady=(10, 0), padx=10, fill='both') 
        body.pack_propagate(False)


        # Phần trên của body: Chọn tháng và năm
        select_frame = tk.Frame(body, width=350, height=40, bg="lightgray")
        select_frame.pack(pady=(0,10), anchor="e")
        select_frame.pack_propagate(False)

        # Chọn tháng
        tk.Label(select_frame, text="Chọn tháng:",font=("Arial", 11), bg="lightgray").pack(side="left", padx=10)
        month_cb = ttk.Combobox(select_frame, values=[str(i) for i in range(1, 13)], width=5, font=("Arial", 11))
        month_cb.pack(side="left")
        month_cb.set("1")  # Giá trị mặc định là tháng 1


        # Chọn năm
        tk.Label(select_frame, text="/", bg="lightgray").pack(side="left", padx=10)
        year_cb = ttk.Combobox(select_frame, values=[str(i) for i in range(1999, 2031)], width=5, font=("Arial", 11))
        year_cb.pack(side="left")
        year_cb.set("2024")  # Giá trị mặc định là năm 2024
       
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
            hover_color="#383838"
        )
        view_button.pack(side="left", padx=10)




           # Phần dưới của body: Hiển thị bảng lương
        table_frame = tk.Frame(body, bg="white")
        table_frame.pack(fill='both',expand=True)

        # Tạo bảng lương với Treeview
        columns = ("stt",'ma_nv','ten_nv','luong_cb','phu_cap','khau_tru','tong_luong',)
        salary_table = ttk.Treeview(table_frame, columns=columns, show='headings')
        salary_table.pack(fill='both',expand=True)

        # Đặt tên cột
        salary_table.heading('stt', text='STT')
        salary_table.heading('ma_nv', text='#ID')
        salary_table.heading('ten_nv', text='Họ tên')
        salary_table.heading('luong_cb', text='Lương cơ bản')
        salary_table.heading('phu_cap', text='Phụ cấp')
        salary_table.heading('khau_tru', text='Khấu trừ')
        salary_table.heading('tong_luong', text='Tổng lương')

        # Đặt chiều rộng các cột
        total_width = 980  # Tổng chiều rộng của bảng
        # Tính toán kích thước cho các cột
        width_span_1 = total_width // 23  # Cột có span 1
        width_span_2 = width_span_1 * 2  # Cột có span 5
        width_span_5 = width_span_1 * 5  # Cột có span 5
        width_span_4 = width_span_1 * 4  # Cột có span 4

        salary_table.column('stt', width=width_span_1)
        salary_table.column('ma_nv', width=width_span_2)
        salary_table.column('ten_nv', width=width_span_4)
        salary_table.column('luong_cb', width=width_span_4)
        salary_table.column('phu_cap', width=width_span_4)
        salary_table.column('khau_tru', width=width_span_4)
        salary_table.column('tong_luong', width=width_span_4)

        

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
        left_footer_frame.pack(side="left", fill='both', expand=True)  # Chiếm hết phần còn lại của footer
        left_footer_frame.pack_propagate(False)

        input1 = utilView.create_input_with_label(left_footer_frame, "ID", 0, 0)
        input2 = utilView.create_input_with_label(left_footer_frame, "Họ tên", 0, 1)
        input3 = utilView.create_input_with_label(left_footer_frame, "Lương cơ bản", 1, 0)
        input4 = utilView.create_input_with_label(left_footer_frame, "Phụ cấp", 1, 1)
        input5 = utilView.create_input_with_label(left_footer_frame, "Khấu trừ", 2, 0)
        input6 = utilView.create_input_with_label(left_footer_frame, "Tổng lương", 2, 1)
        
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



        salaryWindow.mainloop()



if __name__ == "__main__":
    bang_luong = BangLuongGUI()