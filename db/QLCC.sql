--Create database QLCC;

use QLCC
GO
CREATE TABLE [NhanVien] (
  [MaNhanVien] nvarchar(255) PRIMARY KEY,
  [Ten] nvarchar(255) not null,
  [NgaySinh] DATE not null,
  [GioiTinh] nvarchar(10) not null,
  [DiaChi] nvarchar(255) not null,
  [SDT] nvarchar(15) not null,
  [ChucVu] nvarchar(100),
  [HinhAnh] nvarchar(100),
  [Status] bit not null
)
CREATE TABLE [PhanQuyen] (
  [MaQuyen] nvarchar(255) PRIMARY KEY,
  [TenQuyen] nvarchar(255),
  [QuyenChamCong] bit not null,
  [QuyenAdmin] bit not null,
  [QuyenNhanVien] bit not null
)
GO
CREATE TABLE [TaiKhoan] (
  [MaTK] nvarchar(255) PRIMARY KEY,
  [TenDangNhap] nvarchar(255) not null,
  [MatKhau] nvarchar(255) not null,
  [MaQuyen] nvarchar(255) not null,
  [MaNhanVien] nvarchar(255) unique,
  [Status] bit not null,
  FOREIGN KEY ([MaNhanVien]) REFERENCES [NhanVien] ([MaNhanVien]),
  FOREIGN KEY ([MaQuyen]) REFERENCES [PhanQuyen] ([MaQuyen])
)
GO
CREATE TABLE [CaLam] (
  [MaCa] nvarchar(255) PRIMARY KEY,
  [TenCa] nvarchar(50) not null,
  [ThoiGianVao] TIME not null,
  [ThoiGianRa] TIME not null,
  [Status] bit not null
)
GO
CREATE TABLE [LichLam] (
  [MaLich] nvarchar(255) PRIMARY KEY,
  [MaNhanVien] nvarchar(255),
  [MaCa] nvarchar(255),
  [Ngay] DATE not null,
  [Status] bit not null,
  FOREIGN KEY ([MaNhanVien]) REFERENCES [NhanVien] ([MaNhanVien]),
  FOREIGN KEY ([MaCa]) REFERENCES [CaLam] ([MaCa])
)	
GO
CREATE TABLE [BangChamCong] (
  [MaBCC] nvarchar(255) PRIMARY KEY,
  [ThoiGianVao] time not null,
  [ThoiGianRa] time not null,
  [Ngay] DATE not null,
  [TinhTrang] nvarchar(50) not null,
  [MaNhanVien] nvarchar(255),
  [Status] bit not null,
  FOREIGN KEY ([MaNhanVien]) REFERENCES [NhanVien] ([MaNhanVien])
)
GO
CREATE TABLE [BangLuong] (
  [MaBangLuong] nvarchar(255) PRIMARY KEY,
  [Thang] INT not null,
  [Nam] INT not null,
  [PhuCap] DECIMAL(10, 2) not null,
  [KhauTru] DECIMAL(10, 2) not null,
  [HeSoLuong] DECIMAL(10, 2) not null,
  [TongTien] DECIMAL(10, 2) not null,
  [MaNhanVien] nvarchar(255),
  [Status] bit not null,
  [sogiolam] DECIMAL(10, 2) not null,
  FOREIGN KEY ([MaNhanVien]) REFERENCES [NhanVien] ([MaNhanVien])
)
GO
CREATE TABLE [GhiChu] (
  [MaGC] nvarchar(255) PRIMARY KEY,
  [Ngay] DATE not null,
  [NoiDung] nvarchar(MAX) not null
)
GO

/*
drop table IF EXISTS GhiChu
drop table IF EXISTS BangLuong
drop table IF EXISTS LichLam
drop table IF EXISTS CaLam
drop table IF EXISTS TaiKhoan
drop table IF EXISTS PhanQuyen
drop table IF EXISTS BangChamCong
drop table IF EXISTS NhanVien
*/

