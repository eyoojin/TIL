-- db.sqlite3 파일 생성 => Use Database => Run Query

-- create table
CREATE TABLE test (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT, 
    age INTEGER
);

-- rename tabel
ALTER TABLE test RENAME TO user;

-- add column
ALTER TABLE user ADD COLUMN email TEXT;

-- rename column
ALTER TABLE user RENAME COLUMN name TO username;

-- delete table
DROP TABLE user;