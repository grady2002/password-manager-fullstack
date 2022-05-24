-- initial database setup
-- import into PHPMyAdmin or your SQL Dashboard

create database passwordManager;
use passwordManager;
create table auth (
    id int auto_increment primary key,
    username varchar(255) unique,
    pass varchar(255),
    site varchar(255)
);
insert into auth (username, pass, site) values ("admin", "admin", "example.com")