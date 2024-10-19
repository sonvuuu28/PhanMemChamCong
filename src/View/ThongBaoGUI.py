import tkinter as tk
import utilView
import customtkinter as ctk
from time import strftime
from PIL import Image, ImageTk

class ThongBaoGUI:
	
	def __init__(self):
		self.myPath = "C:\\Users\\X\\HocPython\\PJ\\Test\\src\\"
		self.initUI()

	def initUI(self):
		notiWindow = tk.Tk()
		wWindow = 300
		hWindow = 380
		notiWindow.geometry(f"{wWindow}x{hWindow}")
		notiWindow.overrideredirect(True)
		frameNoti = utilView.frameUtil(notiWindow, wWindow, hWindow, 0, 0, bg = '#ffffff')

		headerNoti = utilView.frameUtil(frameNoti, wWindow, 40, 0, 0, bg='white')

		titleNoti = tk.Label(headerNoti, text="THÔNG BÁO", foreground="black", bg='white', font=("Arial", 12, "bold"))

		# titleNoti.pack(fill=tk.BOTH, expand=True, pady=(10))  # fill và expand   
		titleNoti.place(x=100, y=9)	


		close_icon = ImageTk.PhotoImage(file=self.myPath + "Icon\\close.png")  # Thay bằng đường dẫn đến ảnh của bạn

		# Tạo button với icon
		close_button = tk.Button(headerNoti, image=close_icon, width=40, height=40, bg="#fff", borderwidth=0, highlightthickness=0,cursor="hand2", command=lambda: notiWindow.destroy())
		close_button.place(x=260, y=0)

		
		# 
		bodyNoti = tk.Frame(notiWindow, width=300, height=340, bg="#fff")
		bodyNoti.pack_propagate(False)  # Không thay đổi kích thước của frame theo các widget con
		bodyNoti.pack()
		bodyNoti.place(x=0, y=40)

 		# Tạo canvas bên trong frame để thêm scrollbar
		canvas = tk.Canvas(bodyNoti, width=290, height=340)
		canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

		# Tạo scrollbar cho canvas 
		scrollbar = tk.Scrollbar(bodyNoti, orient="vertical", command=canvas.yview)
		scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    	# Kết nối canvas với scrollbar
		canvas.configure(yscrollcommand=scrollbar.set)
		
		# Tạo một frame bên trong canvas để chứa các mục
		list_frame = tk.Frame(canvas)

    	# Đặt frame này vào canvas
		canvas.create_window((0, 0), window=list_frame, anchor="nw")

    	# Thêm các mục vào list_frame
		for i in range(20):  # Ví dụ với 20 mục
			item_text = f"Nhân viên #001 đi trễ ca #012 -- 10p trước"
			item = tk.Label(list_frame,font=("Arial", 10), text=item_text, bg="#d9d9d9", width=290, height=3, anchor="w",wraplength=290, justify="left", padx=5)
			item.pack(fill=tk.X, pady=(5,5))
			self.hover(item)

   		# Điều chỉnh kích thước canvas theo nội dung
		list_frame.update_idletasks()
		canvas.config(scrollregion=canvas.bbox("all"))

		# Bắt sự kiện cuộn chuột
        # Cuộn canvas dựa trên sự kiện cuộn chuột
		canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))  # Windows và Mac
		canvas.bind_all("<Button-4>", lambda event: canvas.yview_scroll(-1, "units"))  # Linux
		canvas.bind_all("<Button-5>", lambda event: canvas.yview_scroll(1, "units"))  # Linux


		notiWindow.mainloop()

	def enter_label(self, label, bgc):
		label.config(bg=bgc)
            
			
	def leave_label(self, label, bgc):
		label.config(bg=bgc)
	
	def hover(self, label):
		label.bind("<Enter>", lambda event : self.enter_label(label, "#FBF6F6"))
		label.bind("<Leave>", lambda event: self.leave_label(label, "#d9d9d9"))
    

if __name__ == '__main__':
    trang_chu = ThongBaoGUI()