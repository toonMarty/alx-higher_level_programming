-- a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities
(
        id INTEGER AUTO_INCREMENT NOT NULL UNIQUE,
        name VARCHAR(256) NOT NULL,
        state_id INTEGER NOT NULL,
        CONSTRAINT prim_cities PRIMARY KEY(id),
        CONSTRAINT cities_ibfk_1 FOREIGN KEY(state_id) REFERENCES states(id)
)ENGINE = InnoDB;
