-- a script that creates the table id_not_null on MySQL server
use hbtn_0d_2;
CREATE TABLE IF NOT EXISTS id_not_null
(
        id INTEGER DEFAULT (1),
        name VARCHAR(256)
);
