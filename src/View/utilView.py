import tkinter as tk 
import customtkinter as ctk
from time import strftime
from datetime import datetime
from tkinter import messagebox
import face_recognition

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
    entry.bind("<FocusOut>", out_click)
    
    return entry
    
def buttonUtil(frame, text, x, y, width, height, **kwargs):
    button = tk.Button(master=frame, text=text, width=width, height=height, **kwargs)
    button.place(x=x, y=y)
    
def cusButtonUtil(frame, text, x, y, width, height, **kwargs):
    button = ctk.CTkButton(master=frame, text=text, width=width, height=height, **kwargs)
    button.place(x=x, y=y)

def frameUtil(frame, width, height, x, y, **kwargs):
    frame = tk.Frame(master=frame, width=width,height=height, **kwargs) 
    frame.place(x=x, y=y)  
    return frame

def lineUtil(parrent, head, tail, y):
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
