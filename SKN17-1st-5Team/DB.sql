create database cardb;

grant all privileges on cardb.* to ohgiraffers@'%';





CREATE TABLE registed_car (
  region_id INT primary key AUTO_INCREMENT,
  added_year VARCHAR(4) NULL,
  added_month VARCHAR(2) NULL,
  type VARCHAR(40) NOT NULL,
  city VARCHAR(40) NOT NULL,
  town VARCHAR(40) NOT NULL,
  total INT NOT NULL,
  local_regist VARCHAR(2) NOT NULL CHECK (local_regist in ('Y','N'))
  );

CREATE TABLE IF NOT EXISTS FAQ (
	question_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content VARCHAR(510) NOT NULL
);

commit;
