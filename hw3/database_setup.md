sudo apt install mariadb-server -y
printf "[mysqld]\nport = 6002\nbind-address = 0.0.0.0\n" | sudo tee /etc/mysql/mariadb.conf.d/99-comp370.cnf
sudo systemctl restart mariadb
sudo mariadb
CREATE DATABASE comp370_test;
CREATE USER 'comp370'@'%' IDENTIFIED BY '$ungl@ss3s';
GRANT ALL PRIVILEGES ON comp370_test.* TO 'comp370'@'%';