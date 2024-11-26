import tkinter as tk 
import customtkinter as ctk
from time import strftime
from datetime import datetime
from tkinter import messagebox
from datetime import datetime

def msg_boxUtil(title, description):
    messagebox.showinfo(title, description)

def get_img_label(window):
    label = tk.Label(window)
    label.grid(row=0, column=0)
    return label

def labelUtil(frame, text, x, y, **kwargs):
    label = tk.Label(master=frame, text=text, **kwargs)
    label.place(x=x, y=y)
    return label

def entryUtil(frame, text, x, y, width, **kwargs):
    def click(event):
        if entry.get() == text:
            entry.delete(0, tk.END)
    def out_click(event):
        if entry.get() == "":
            entry.insert(0,text)
    
    entry = tk.Entry(master=frame, text=text, width=width, relief=tk.FLAT, **kwargs)
    entry.insert(0, text) 
    entry.place(x=x, y=y)
    entry.bind("<FocusIn>", click)
    # entry.bind("<FocusOut>", out_click)
    
    return entry
    
def buttonUtil(frame, text, x, y, width, height, **kwargs):
    button = tk.Button(master=frame, text=text, width=width, height=height, **kwargs)
    button.place(x=x, y=y)

def cusButtonUtil_Image(frame, text, x, y, width, height, image=None, hover_image=None, text_color="black", hover_text_color="#636363", fg_color=None, hover_fg_color=None, **kwargs):
    # Tạo nút với màu nền mặc định
    button = ctk.CTkButton(
        master=frame,
        text=text,
        width=width,
        height=height,
        image=image,
        text_color=text_color,
        fg_color=fg_color,  # Màu nền nút mặc định
        **kwargs
    )
    button.place(x=x, y=y)

    # Nếu có hover_image, hover_text_color và hover_fg_color, bind sự kiện để thay đổi ảnh, màu chữ và màu nền khi hover
    if hover_image or hover_text_color or hover_fg_color:
        button.bind("<Enter>", lambda e: button.configure(
            image=hover_image if hover_image else image,
            text_color=hover_text_color if hover_text_color else text_color,
            fg_color=hover_fg_color if hover_fg_color else fg_color  # Thay đổi màu nền khi hover
        ))

        # Khi chuột rời khỏi nút, trả lại các giá trị mặc định
        button.bind("<Leave>", lambda e: button.configure(
            image=image,
            text_color=text_color,
            fg_color=fg_color  # Trả lại màu nền ban đầu
        ))

    return button



def cusButtonUtil(frame, text, x, y, width, height, **kwargs):
    button = ctk.CTkButton(master=frame, text=text, width=width, height=height, **kwargs)
    button.place(x=x, y=y)

def frameUtil(frame, width, height, x, y, **kwargs):
    frame = tk.Frame(master=frame, width=width,height=height, **kwargs) 
    frame.place(x=x, y=y)  
    return frame

def lineUtil(parrent, head, tail, y, **kwargs):
    canvas = tk.Canvas(master=parrent, width=500, height=2)
    canvas.configure(bg="white", highlightbackground = 'white')
    canvas.place(x = head, y = y)
    canvas.create_line(head, 2, tail, 2, fill="black", width=2)
    
def clockUtil(parent, x ,y ):
    Label_DongHo = labelUtil(parent, \
                    "07:00", x, y, font = ('Helvetica', 18, "bold"), bg = 'white', fg = 'black', height = 1, justify = 'left')
    def time():
        string = strftime('%H:%M:%S')
        Label_DongHo.config(text=string)
        Label_DongHo.after(1000, time)
    time()
    
def dateUtil(parent, x ,y ):
    ngay_hien_tai = datetime.now()
    thu = ngay_hien_tai.weekday()
    ngay = ngay_hien_tai.day
    thang = ngay_hien_tai.month
    nam = ngay_hien_tai.year
    if thu != 6:
        thu = thu + 2
        thu = f"Thứ {thu}"
    else:
        thu = "Chủ Nhật"
        
    Label_DongHo = labelUtil(parent, \
                    f"{thu}, {ngay} tháng {thang} năm {nam}", x, y, font = ('Helvetica', 13, "italic"), bg = 'white', fg = '#373737', height = 2, justify = 'left')
    
    

        
def create_input_with_label(parent, label_text, row, column):
      # Tạo label
    label = tk.Label(parent, text=label_text, font=("Arial", 11), bg="#fff")
    label.grid(row=row, column=column * 2, padx=(10, 5), pady=(10, 0), sticky='w')  # Đặt label ở bên trái

    # Tạo entry
    entry = ctk.CTkEntry(parent, width=180, height=30, fg_color="white", text_color="black", font=("Arial", 11))
    entry.grid(row=row, column=column * 2 + 1, padx=(10, 10), pady=(10, 0))  # Đặt entry bên phải label và cách 10px

    return entry  # Trả về đối tượng entry nếu cần sử dụng sau này

    
def create_input_with_label_v2(parent, label_text, row, column, label_width=0):
 # Tạo label
    label = tk.Label(parent, text=label_text, font=("Arial", 11), bg="#fff")
    label.grid(row=row, column=column, padx=(10, 5), pady=(10, 0), sticky='w')  # Đặt label ở bên trái

    # Tạo entry
    entry = ctk.CTkEntry(parent, width=180, height=30, fg_color="white", text_color="black", font=("Arial", 11))
    entry.grid(row=row, column=column + 1, padx=(10, 10), pady=(10, 0))  # Đặt entry bên phải label

    return entry  # Trả về đối tượng entry nếu cần sử dụng sau này

def convert_date_format(date_str):
    try:
        # Chuyển đổi chuỗi ngày tháng sang định dạng datetime
        date_obj = datetime.strptime(date_str, '%d/%m/%Y')

        # Kiểm tra năm từ 1900 đến 2100
        if 1900 <= date_obj.year <= 2100:
            # Chuyển định dạng sang 'yyyy-mm-dd'
            new_date_str = date_obj.strftime('%Y-%m-%d')
            return new_date_str
        else:
            return 0
    except ValueError:
        return 0
    
def kiem_tra_so_dien_thoai(so_dien_thoai):
    # Chỉ chấp nhận số điện thoại có đúng 10 số và bắt đầu bằng số 0
    if len(so_dien_thoai) == 10 and so_dien_thoai.startswith('0') and so_dien_thoai.isdigit():
        return so_dien_thoai
    else:
        return False
