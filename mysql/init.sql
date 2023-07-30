-- Создание пользователя
CREATE USER IF NOT EXISTS 'apiuser'@'%' IDENTIFIED BY 'apiuser';

-- Создание базы данных
CREATE DATABASE IF NOT EXISTS bazis;

-- Предоставление всех привилегий на базу данных пользователю
GRANT ALL ON bazis.* TO 'apiuser'@'%';

-- Создание таблицы (замените названия и поля таблицы на свои)
USE bazis;
CREATE TABLE users (
  id int NOT NULL AUTO_INCREMENT,
  info json DEFAULT NULL,
  created tinyint(1) DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;