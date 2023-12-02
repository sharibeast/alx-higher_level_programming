-- create the database hbtn_0d_usa and table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(id NOT NULL AUTOINCREMENT PRIMARY KEY UNIQUE, name VARCHAR(256));