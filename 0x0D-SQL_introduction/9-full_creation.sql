-- a script that creates a table second_table in the database hbtn_0c_0 in MySQL and add multiple rows
CREATE TABLE IF NOT EXISTS second_table
(
        id INTEGER,
        name VARCHAR(256),
        score INTEGER
);

INSERT INTO second_table(id, name, score) VALUES(1, "John", 10);
INSERT INTO second_table(id, name, score) VALUES(2, "Alex", 3);
INSERT INTO second_table(id, name, score) VALUES(3, "Bob", 14);
INSERT INTO second_table(id, name, score) VALUES(4, "George", 8);
