-- a script that creates the table unique_id on MySQL server.
use hbtn_0d_2;
CREATE TABLE IF NOT EXISTS unique_id
(
        id INTEGER DEFAULT(1) UNIQUE,
        name VARCHAR(256)
);
