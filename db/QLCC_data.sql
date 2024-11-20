use QLCC 

INSERT INTO [NhanVien] ([MaNhanVien], [Ten], [NgaySinh], [GioiTinh], [DiaChi], [SDT], [ChucVu], [HinhAnh], Status)
VALUES 
('NV001', N'Nguyễn Văn A', '1990-01-01', N'Nam', N'123 An Dương Vương', '0909123456', N'Nhân Viên', 'NV001.png', 1),
('NV002', N'Trần Thị B', '1992-05-10', N'Nữ', N'123 Nguyễn Trãi', '0919123456', N'Quản Lý', 'NV002.png', 1),
('NV003', N'máy chấm công', '1992-05-10', N'no', N'no', 'no', N'Quản Lý', 'no', 0);

insert into PhanQuyen(MaQuyen, TenQuyen, QuyenAdmin, QuyenChamCong, QuyenNhanVien) values
('Q001', N'Quyền Nhân Viên', 0, 0, 1),-- Quyền nhân viên
('Q002', N'Quyền Quản Lý', 1, 0, 0),-- Quyền quản lý nhân viên cả admin 
('Q003', N'Quyền Máy Chấm Công', 0, 1, 0)-- Quyền chấm công dùng ở các máy chấm công

INSERT INTO [CaLam] ([MaCa], [TenCa], [ThoiGianVao], [ThoiGianRa], Status)
VALUES 
('CA001', N'Ca sáng', '08:00:00', '12:00:00', 1),
('CA002', N'Ca chiều', '13:00:00', '17:00:00', 1);

INSERT INTO [LichLam] ([MaLich], [MaNhanVien], [MaCa], [Ngay], [Status])
VALUES 
('LL001', 'NV001', 'CA001', '2024-10-11', 1),
('LL002', 'NV002', 'CA002', '2024-10-11', 1);

INSERT INTO [BangChamCong] ([MaBCC], [ThoiGianVao], [ThoiGianRa], [Ngay], [TinhTrang], [MaNhanVien], [Status])
VALUES 
('BCC001', '08:05:00', '12:00:00', '2024-10-11', N'Dung gio', 'NV001', 0),
('BCC002', '13:10:00', '17:00:00', '2024-10-11', N'Dung gio', 'NV002', 0);

INSERT INTO [BangLuong] ([MaBangLuong], [Thang], [Nam], [PhuCap], KhauTru, [HeSoLuong], TongTien, [MaNhanVien], [Status], sogiolam)
VALUES 
('BL001', 10, 2024, 500.00, 0.000, 23.000, 3000.000,'NV001', 1, 3000.000),
('BL002', 10, 2024, 500.00, 0.000, 23.000, 3000.000,'NV002', 1, 3000.000);

INSERT INTO [GhiChu] ([MaGC], [Ngay], [NoiDung])
VALUES 
('GC001', '2024-10-11', N'Hoàn thành công việc trong ngày.'),
('GC002', '2024-10-11', N'Nguyễn Văn A về sớm 30p vì lý do cá nhân.');

INSERT INTO [TaiKhoan] ([MaTK], [TenDangNhap], [MatKhau], [MaQuyen], [MaNhanVien], Status)
VALUES 
('TK001', N'nhanvien1', N'123', 'Q001', 'NV001', 1),
('TK002', N'nhanvien2', N'123', 'Q002', 'NV002', 1),
('TK003', N'chamcong1', N'123', 'Q003', 'NV003', 1);


select * from NhanVien
select * from [GhiChu]
select * from [BangLuong]
select * from CaLam
select * from LichLam
select * from BangChamCong
select * from PhanQuyen
select * from TaiKhoan