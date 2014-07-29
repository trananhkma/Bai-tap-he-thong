#Giải bài tập mysql 1 (bt1_mysql.pdf)

###I/Đăng nhập với quyền root và tạo cơ sở dữ liệu:
	
	mysql -u root -p1
	create database thuc_hanh_1;
	use thuc_hanh_1;

###II/Tạo các bảng biểu: <br>
####1. Bảng KHUVUC: <br>
Khóa chính là IDKhuVuc (Khu Vực)

	create table KHUVUC
	(
	IDKhuVuc varchar(10) not null,
	TenKhuVuc varchar(30),
	PhongQL varchar(10),
	primary key (IDKhuVuc)
	);
	
####2. Bảng DAY (dãy): <br>	
Khóa chính là STTDay, khóa ngoại là IDKhuVuc

	create table DAY
	(
	STTDay int not null auto_increment,
	IDKhuVuc varchar(10) not null,
	Ten varchar(30),
	PhongBV varchar(10),
	primary key (STTDay),
	FOREIGN KEY (IDKhuVuc) REFERENCES KHUVUC(IDKhuVuc)
	);

####3. Bảng PHONG (Phòng)<br>
Khóa ngoại là IDKhuVuc và STTDay

	create table PHONG
	(
	IDKhuVuc varchar(10) not null,
	IDPhong varchar(10) not null,
	STTDay int not null,
	SucChua int,
	PhongTB varchar(10),
	foreign key (IDKhuVuc) references KHUVUC(IDKhuVuc),
	foreign key (STTDay) references DAY(STTDay)
	);

###III/Nhập dữ liệu:

	insert into KHUVUC(IDKhuVuc, TenKhuVuc, PhongQL) values ('KV01','Khu Vuc 1','QL1');
	insert into KHUVUC(IDKhuVuc, TenKhuVuc, PhongQL) values ('KV02','Khu Vuc 2','QL2');
	insert into KHUVUC(IDKhuVuc, TenKhuVuc, PhongQL) values ('KV03','Khu Vuc 3','QL3');

#### 

	insert into DAY(IDKhuVuc, Ten, PhongBV) values ('KV01','DAY 1','BV1');
	insert into DAY(IDKhuVuc, Ten, PhongBV) values ('KV01','DAY 2','BV2');
	insert into DAY(IDKhuVuc, Ten, PhongBV) values ('KV02','DAY 3','BV3');
	insert into DAY(IDKhuVuc, Ten, PhongBV) values ('KV02','DAY 4','BV4');
	insert into DAY(IDKhuVuc, Ten, PhongBV) values ('KV03','DAY 5','BV5');
	insert into DAY(IDKhuVuc, Ten, PhongBV) values ('KV03','DAY 6','BV6');

#### 

	insert into PHONG(IDKhuVuc, STTDay, IDPhong, SucChua, PhongTB) values ('KV01','1','P1','10','TB1');
	insert into PHONG(IDKhuVuc, STTDay, IDPhong, SucChua, PhongTB) values ('KV01','1','P2','9','TB2');
	insert into PHONG(IDKhuVuc, STTDay, IDPhong, SucChua, PhongTB) values ('KV01','2','P3','10','TB3');
	insert into PHONG(IDKhuVuc, STTDay, IDPhong, SucChua, PhongTB) values ('KV01','2','P4','8','TB4');
	insert into PHONG(IDKhuVuc, STTDay, IDPhong, SucChua, PhongTB) values ('KV02','3','P5','8','TB5');
	insert into PHONG(IDKhuVuc, STTDay, IDPhong, SucChua, PhongTB) values ('KV02','4','P7','8','TB7');
	insert into PHONG(IDKhuVuc, STTDay, IDPhong, SucChua, PhongTB) values ('KV02','4','P8','8','TB8');
	insert into PHONG(IDKhuVuc, STTDay, IDPhong, SucChua, PhongTB) values ('KV03','5','P9','10','TB9');
	insert into PHONG(IDKhuVuc, STTDay, IDPhong, SucChua, PhongTB) values ('KV03','5','P10','10','TB10');
	insert into PHONG(IDKhuVuc, STTDay, IDPhong, SucChua, PhongTB) values ('KV03','6','P11','10','TB11');
	insert into PHONG(IDKhuVuc, STTDay, IDPhong, SucChua, PhongTB) values ('KV03','6','P12','10','TB12');
