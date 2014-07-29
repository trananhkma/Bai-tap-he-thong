#Giải bài tập mysql 2 (bt2_mysql.pdf)

#####Tạo database:

    create database thuc_hanh_2;
    use thuc_hanh_2;
    
#####Tạo bảng:

    create table DOISX
    (
    IDDOISX varchar(10) not null,
    TENDOI varchar(30),
    IDDOITRUONG varchar(10) not null,
    constraint doisx primary key (IDDOISX,IDDOITRUONG)
    );
# 
    create table TOSX
    (
    IDDOISX varchar(10) not null,
    STT int auto_increment not null,
    TEN varchar(30),
    IDTOTRUONG varchar(10) not null,
    constraint tosx primary key (STT,IDTOTRUONG),
    foreign key (IDDOISX) references DOISX(IDDOISX)
    );
# 
    create table CONGNHAN 
    (
    IDDOISX varchar(10) not null,
    IDCONGNHAN varchar(10) not null,
    HOTEN varchar(30),
    NAMSINH int,
    STTTO int not null,
    IDNQL varchar(10),
    primary key (IDCONGNHAN),
    foreign key (STTTO) references TOSX(STT),
    foreign key (IDDOISX) references DOISX(IDDOISX)
    );
    
#####Nhập dữ liệu 

    insert into DOISX(IDDOISX, TENDOI, IDDOITRUONG) values ('G1','DOI 1','DT1');
    insert into DOISX(IDDOISX, TENDOI, IDDOITRUONG) values ('G2','DOI 2','DT2');
# 
    insert into TOSX(IDDOISX, TEN, IDTOTRUONG) values ('G1','TO 1','TT1');
    insert into TOSX(IDDOISX, TEN, IDTOTRUONG) values ('G1','TO 2','TT2');
    insert into TOSX(IDDOISX, TEN, IDTOTRUONG) values ('G2','TO 3','TT3');
    insert into TOSX(IDDOISX, TEN, IDTOTRUONG) values ('G2','TO 4','TT4');
# 
    insert into CONGNHAN(IDDOISX, IDCONGNHAN, HOTEN, NAMSINH, STTTO, IDNQL) values ('G1','CN1','Nguyen Van A', '1988', '1', 'QL1');
    insert into CONGNHAN(IDDOISX, IDCONGNHAN, HOTEN, NAMSINH, STTTO, IDNQL) values ('G1','CN2','Nguyen Van B', '1989', '1', 'QL1');
    insert into CONGNHAN(IDDOISX, IDCONGNHAN, HOTEN, NAMSINH, STTTO, IDNQL) values ('G1','CN3','Nguyen Van C', '1989', '2', 'QL1');
    insert into CONGNHAN(IDDOISX, IDCONGNHAN, HOTEN, NAMSINH, STTTO, IDNQL) values ('G1','CN4','Nguyen Van D', '1989', '2', 'QL1');
