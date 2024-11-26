CREATE DATABASE VIRTUALCLOSET;

USE VIRTUALCLOSET;

CREATE TABLE KIND_CLOTHES (
ID_KIND_CLOTHES INT PRIMARY KEY AUTO_INCREMENT,
NAME_KIND_CLOTHES VARCHAR(255)
);
drop table KIND_CLOTHES;

CREATE TABLE SEASON (
ID_SEASON INT PRIMARY KEY AUTO_INCREMENT,
NAME_SEASON VARCHAR (255)
);

DROP TABLE SEASON;

INSERT INTO SEASON (NAME_SEASON) VALUES ('PRIMAVERA');
INSERT INTO SEASON (NAME_SEASON) VALUES ('VERANO');
INSERT INTO SEASON (NAME_SEASON) VALUES ('OTOÑO');
INSERT INTO SEASON (NAME_SEASON) VALUES ('INVIERNO');


INSERT INTO KIND_CLOTHES (NAME_KIND_CLOTHES) VALUES ('CAMISETAS');
INSERT INTO KIND_CLOTHES (NAME_KIND_CLOTHES) VALUES ('CAMISAS');
INSERT INTO KIND_CLOTHES (NAME_KIND_CLOTHES) VALUES ('CHAQUETAS');
INSERT INTO KIND_CLOTHES (NAME_KIND_CLOTHES) VALUES ('ABRIGOS');
INSERT INTO KIND_CLOTHES (NAME_KIND_CLOTHES) VALUES ('PANTALONES');
INSERT INTO KIND_CLOTHES (NAME_KIND_CLOTHES) VALUES ('ZAPATOS');
INSERT INTO KIND_CLOTHES (NAME_KIND_CLOTHES) VALUES ('TENIS');
INSERT INTO KIND_CLOTHES (NAME_KIND_CLOTHES) VALUES ('BLUSAS');
INSERT INTO KIND_CLOTHES (NAME_KIND_CLOTHES) VALUES ('FALDAS');
INSERT INTO KIND_CLOTHES (NAME_KIND_CLOTHES) VALUES ('VESTIDOS');
INSERT INTO KIND_CLOTHES (NAME_KIND_CLOTHES) VALUES ('TACONES');
INSERT INTO KIND_CLOTHES (NAME_KIND_CLOTHES) VALUES ('TOPS');
INSERT INTO KIND_CLOTHES (NAME_KIND_CLOTHES) VALUES ('LEGGINS');
INSERT INTO KIND_CLOTHES (NAME_KIND_CLOTHES) VALUES ('PANTALONETA');
INSERT INTO KIND_CLOTHES (NAME_KIND_CLOTHES) VALUES ('TRAJE');
INSERT INTO KIND_CLOTHES (NAME_KIND_CLOTHES) VALUES ('BLAZZER');
INSERT INTO KIND_CLOTHES (NAME_KIND_CLOTHES) VALUES ('ACCESORIO');