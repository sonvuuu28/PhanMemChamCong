import tkinter as tk
import utilView
import customtkinter as ctk
from time import strftime
from PIL import Image, ImageTk

class GhiChuGUI:
	
	def __init__(self):
		self.staff = "Nguyễn Văn A - #01"
		self.shift = "#015"
		self.myPath = "C:\\Users\\X\\HocPython\\PJ\\Test\\src\\"
		self.initUI()

	def initUI(self):
		noteWindow = tk.Tk()
		wWindow = 300
		hWindow = 380
		noteWindow.geometry(f"{wWindow}x{hWindow}")
		noteWindow.overrideredirect(True)
		frameNote = utilView.frameUtil(noteWindow, wWindow, hWindow, 0, 0, bg = '#ffffff')

		headerNote = utilView.frameUtil(frameNote, wWindow, 80, 0, 0, bg='white')

		titleNote = tk.Label(headerNote, text="GHI CHÚ", foreground="black", bg='white', font=("Arial", 12, "bold"))                            
		staffNote = tk.Label(
			headerNote, 
			text=f"Nhân viên: {self.staff}", 
			foreground="black", 
			bg='white', font=("Arial",    10, "bold")
		)
		shiftNote = tk.Label(
			headerNote, 
			text=f"Ca làm     : {self.shift}", 
			foreground="black", 
			bg='white', font=("Arial",    10, "bold")
		)

		titleNote.place(x=100, y=9)
		staffNote.place(x=10, y=35)
		shiftNote.place(x=10, y=55)
		
		# Tạo button với icon
		close_icon = ImageTk.PhotoImage(file=self.myPath + "Icon\\close.png")  # Thay bằng đường dẫn đến ảnh của bạn
		close_button = tk.Button(headerNote, image=close_icon, width=40, height=40, bg="#fff", borderwidth=0, highlightthickness=0,cursor="hand2", command=lambda: noteWindow.destroy())
		close_button.place(x=260, y=0)

		# 
		bodyNote = tk.Frame(noteWindow, width=300, height=300, bg="#fff")
		bodyNote.pack_propagate(False)  # Không thay đổi kích thước của frame theo các widget con
		bodyNote.place(x=0, y=80)
        
		
        # Tạo Text widget
		contentNote = tk.Text(bodyNote, wrap=tk.WORD, font=("Arial", 11), highlightthickness=1)
		contentNote.pack(padx=10, pady=5)
		contentNote.place(x=10, y=5,  width=280, height=200)  # Đặt ở giữa giữa frame
		  
          # Tạo frame cho nút
		button_frame = tk.Frame(bodyNote, width=280, height=40, bg="white")
		button_frame.pack(padx=10)
		button_frame.place(x=10, y=225)  # Đặt frame nút ở cuối cửa sổ
	
        # Tạo hai nút
		cancel_button = tk.Button(button_frame, text="Hủy", fg="black", command=noteWindow.destroy)
		cancel_button.pack(side="left", padx=10)
		cancel_button.place(x=0, y=4,width=100, height=32)

		done_button = tk.Button(button_frame, text="Xong", fg="black" )  
		done_button.place(x=180, y=4, width=100, height=32)
		

        
		noteWindow.mainloop()

	def enter_label(self, label, bgc):
		label.config(bg=bgc)
            
			
	def leave_label(self, label, bgc):
		label.config(bg=bgc)
	
	def hover(self, label):
		label.bind("<Enter>", lambda event : self.enter_label(label, "#FBF6F6"))
		label.bind("<Leave>", lambda event: self.leave_label(label, "#d9d9d9"))
    

if __name__ == '__main__':
    trang_chu = GhiChuGUI()