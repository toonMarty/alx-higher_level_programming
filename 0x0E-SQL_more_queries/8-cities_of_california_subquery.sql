-- a script that lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT * FROM cities WHERE state_id =
(SELECT name FROM states WHERE name = 'California' ORDER BY id ASC);
