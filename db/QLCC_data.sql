use QLCC 

INSERT INTO [NhanVien] ([MaNhanVien], [Ten], [NgaySinh], [GioiTinh], [DiaChi], [SDT], [ChucVu], [deleteStatus])
VALUES 
('NV001', N'Nguyen Van A', '1990-01-01', N'Nam', N'Hanoi', '0909123456', N'Nhan vien', 0),
('NV002', N'Tran Thi B', '1992-05-10', N'Nu', N'Ho Chi Minh', '0919123456', N'Ke toan', 0);


INSERT INTO [CaLam] ([MaCa], [TenCa], [ThoiGianVao], [ThoiGianRa], [deleteStatus])
VALUES 
('CA001', N'Ca sang', '08:00:00', '12:00:00', 1),
('CA002', N'Ca chieu', '13:00:00', '17:00:00', 1);

INSERT INTO [LichLam] ([MaLich], [MaNhanVien], [MaCa], [Ngay], [deleteStatus])
VALUES 
('LL001', 'NV001', 'CA001', '2024-10-11', 0),
('LL002', 'NV002', 'CA002', '2024-10-11', 0);

INSERT INTO [BangChamCong] ([MaBCC], [ThoiGianVao], [ThoiGianRa], [Ngay], [TinhTrang], [MaNhanVien], [deleteStatus])
VALUES 
('BCC001', '08:05:00', '12:00:00', '2024-10-11', N'Dung gio', 'NV001', 0),
('BCC002', '13:10:00', '17:00:00', '2024-10-11', N'Dung gio', 'NV002', 0);

INSERT INTO [BangLuong] ([MaBangLuong], [Thang], [Nam], [PhuCap], [HeSoLuong], [MaNhanVien], [deleteStatus])
VALUES 
('BL001', 10, 2024, 500.00, 23.000, 'NV001', 0),
('BL002', 10, 2024, 300.00, 23.00, 'NV002', 0);

INSERT INTO [GhiChu] ([MaGC], [Ngay], [NoiDung])
VALUES 
('GC001', '2024-10-11', N'Hoan thanh cong viec trong ngay.'),
('GC002', '2024-10-11', N'Ve som 30 phut vi ly do ca nhan.');

INSERT INTO [PhanQuyen] ([MaQuyen], [TenQuyen], [QuyenChamCong], [QuyenAdmin], [QuyenNhanVien] )
VALUES 
('Q001', N'Quyền chấm công', 1, 0, 0),  -- Quyền chấm công dùng ở các máy chấm công
('Q002', N'Quyền admin', 1, 1, 0),  -- Quyền quản lý nhân viên cả admin 
('Q003', N'Quyền nhân viên', 0, 1, 0)       -- Quyền nhân viên

INSERT INTO [TaiKhoan] ([MaTK], [TenDangNhap], [MatKhau], [MaQuyen], [MaNhanVien], [deleteStatus])
VALUES 
('TK001', N'nguyenvana', N'password123', 'Q001', 'NV001', 0),
('TK002', N'tranthib', N'password456', 'Q002', 'NV002', 0);

select * from NhanVien
select * from [GhiChu]
select * from [BangLuong]
select * from CaLam
select * from LichLam
select * from BangChamCong
select * from PhanQuyen
select * from TaiKhoan