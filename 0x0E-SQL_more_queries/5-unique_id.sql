-- a script that creates the table unique_id on MySQL server.
CREATE TABLE IF NOT EXISTS unique_id
(
        id INTEGER DEFAULT(1) UNIQUE,
        name VARCHAR(256)
);
