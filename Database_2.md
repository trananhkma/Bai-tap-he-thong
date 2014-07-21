#BTTL2_Tao_bang_va_insert_du_lieu_2

    create database thuc_hanh_2;
    use thuc_hanh_2;
#####
    create table DOISX
    (
    IDDOISX varchar(10) not null,
    TENDOI varchar(30),
    IDDOITRUONG varchar(10) not null,
    constraint doisx primary key (IDDOISX,IDDOITRUONG)
    );
#####
    create table TOSX
    (
    IDDOISX varchar(10) not null,
    STT int auto_increment not null,
    TEN varchar(30),
    IDTOTRUONG varchar(10) not null,
    constraint tosx primary key (STT,IDTOTRUONG),
    foreign key (IDDOISX) references DOISX(IDDOISX)
    );
#####
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
#####
    insert into DOISX(IDDOISX, TENDOI, IDDOITRUONG) values ('G1','DOI 1','DT1');
    insert into DOISX(IDDOISX, TENDOI, IDDOITRUONG) values ('G2','DOI 2','DT2');
