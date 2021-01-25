0:
	cat 0-privileges.sql | sudo mysql -hlocalhost -uroot -proot
	echo "CREATE USER 'user_0d_1'@'localhost';" |  sudo mysql -hlocalhost -uroot -proot
	echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" |  sudo mysql -hlocalhost -uroot -proot
	cat 0-privileges.sql | sudo mysql -hlocalhost -uroot -proot
1:
	cat 1-create_user.sql | sudo mysql -hlocalhost -uroot -proot
	cat 0-privileges.sql | sudo mysql -hlocalhost -uroot -proot
2:
	cat 2-create_read_user.sql | sudo mysql -hlocalhost -uroot -proot
	cat 0-privileges.sql | sudo mysql -hlocalhost -uroot -proot
3:
	cat 3-force_name.sql | sudo mysql -hlocalhost -uroot -proot hbtn_0d_2
	echo 'INSERT INTO force_name (id, name) VALUES (89, "Holberton School");' | sudo mysql -hlocalhost -uroot -proot hbtn_0d_2
	echo 'SELECT * FROM force_name;' | sudo mysql -hlocalhost -uroot -proot hbtn_0d_2
	echo 'INSERT INTO force_name (id) VALUES (333);' | sudo mysql -hlocalhost -uroot -proot hbtn_0d_2
	echo 'SELECT * FROM force_name;' | sudo mysql -hlocalhost -uroot -proot hbtn_0d_2
4:
	cat 4-never_empty.sql | sudo mysql -hlocalhost -uroot -proot hbtn_0d_2
	echo 'INSERT INTO id_not_null (id, name) VALUES (89, "Holberton School");' | sudo mysql -hlocalhost -uroot -proot hbtn_0d_2
	echo 'SELECT * FROM id_not_null;' | sudo mysql -hlocalhost -uroot -proot hbtn_0d_2
	echo 'INSERT INTO id_not_null (name) VALUES ("Holberton");' | sudo mysql -hlocalhost -uroot -proot hbtn_0d_2
	echo 'SELECT * FROM id_not_null;' | sudo mysql -hlocalhost -uroot -proot hbtn_0d_2
5:
	cat 5-unique_id.sql | sudo mysql -hlocalhost -uroot -proot hbtn_0d_2
	echo 'INSERT INTO unique_id (id, name) VALUES (89, "Holberton School");' | sudo mysql -hlocalhost -uroot -proot hbtn_0d_2  
	echo 'SELECT * FROM unique_id;' |  sudo mysql -hlocalhost -uroot -proot hbtn_0d_2
	echo 'INSERT INTO unique_id (id, name) VALUES (89, "Holberton");' | sudo mysql -hlocalhost -uroot -proot hbtn_0d_2
	echo 'SELECT * FROM unique_id;' | sudo mysql -hlocalhost -uroot -proot hbtn_0d_2 
6:
	cat 6-states.sql | sudo mysql -hlocalhost -uroot -proot
	echo 'INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas");' | sudo mysql -hlocalhost -uroot -proot hbtn_0d_usa
	echo 'SELECT * FROM states;' | sudo mysql -hlocalhost -uroot -proot hbtn_0d_usa
7:
	cat 7-cities.sql | sudo mysql -hlocalhost -uroot -proot 
	echo 'INSERT INTO cities (state_id, name) VALUES (1, "San Francisco");' | sudo mysql -hlocalhost -uroot -proot hbtn_0d_usa
	echo 'SELECT * FROM cities;' | sudo mysql -hlocalhost -uroot -proot hbtn_0d_usa
	echo 'INSERT INTO cities (state_id, name) VALUES (10, "Paris");' | sudo mysql -hlocalhost -uroot -proot hbtn_0d_usa
8:
	echo 'SELECT * FROM states;' |echo 'SELECT * FROM states;' | sudo mysql -hlocalhost -uroot -proot hbtn_0d_usa
	echo 'SELECT * FROM cities;' | sudo mysql -hlocalhost -uroot -proot hbtn_0d_usa
	 cat 8-cities_of_california_subquery.sql | sudo mysql -hlocalhost -uroot -proot hbtn_0d_usa

