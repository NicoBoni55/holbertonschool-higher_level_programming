-- listar todos los privilegios de los usuarios
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'password1';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'password2';

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';

SHOW GRANTS FOR 'user_0d_1'@'localhost';

SHOW GRANTS FOR 'user_0d_2'@'localhost';