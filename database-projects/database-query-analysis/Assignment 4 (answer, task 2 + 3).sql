-- INFO125 - Assignment 4

-- Create and use the database
CREATE DATABASE my_database;
USE my_database;

-- Task 2
-- a)
CREATE TABLE CAN_LAND (
Airport_code char(3),
Airplane_type_name varchar(13),
PRIMARY KEY (Airport_code, Airplane_type_name),
FOREIGN KEY (Airport_code) REFERENCES AIRPORT(Airport_code),
FOREIGN KEY (Airplane_type_name) REFERENCES AIRPLANE_TYPE(Airplane_type_name)
);

-- b)
SELECT Airport.City
FROM AIRPORT
JOIN CAN_LAND ON AIRPORT.Airport_code = CAN_LAND.Airport_code
WHERE CAN_LAND.Airplane_type_name = 'Boeing 747';

-- Task 3

CREATE TABLE DEPT_LOCATION (
    Loc_Code char(4),
    Address varchar(255),
    Post_Code varchar(10),
    City varchar(50),
    State varchar(50),
    Reg char(2),
    FOREIGN KEY (Reg) REFERENCES COUNTRY(Reg)
);

CREATE TABLE COUNTRY (
    Reg char(2),
    Country_name varchar(50),
    PRIMARY KEY (Reg)
);

CREATE TABLE WORKER (
    ID int,
    Fname varchar(50),
    Lname varchar(50),
    Hire_date date,
    Job_id varchar(50),
    Salary int,
    PRIMARY KEY (ID)
);

INSERT INTO DEPT_LOCATION (Loc_Code, Address, Post_Code, City, State, Reg) VALUES
('2700', 'Schwanthalerstr. 703', '80925', 'Munich', 'Bavaria', 'DE'),
('2800', 'Rua Frei Caneca 1360', '01307-002', 'Sao Paulo', 'Sao Paulo', 'BR'),
('2900', '20 Rue des Corps-Sai', '1730', 'Geneva', 'Geneva', 'CH'),
('3000', 'Murtenstrasse 921', '3095', 'Bern', 'BE', 'CH');

INSERT INTO COUNTRY (Reg, Country_name) VALUES
('AR', 'Argentina'),
('AU', 'Australia'),
('BE', 'Belgium'),
('BR', 'Brazil'),
('CA', 'Canada'),
('CH', 'Switzerland'),
('CN', 'China'),
('DE', 'Germany'),
('DK', 'Denmark');

INSERT INTO WORKER (ID, Fname, Lname, Hire_date, Job_id, Salary) VALUES
(100, 'Steven', 'King', '1987-06-17', 'AD_PRES', 24000.00),
(101, 'Neena', 'Kochhar', '1987-06-18', 'AD_VP', 17000.00),
(102, 'Lex', 'De Haan', '1987-06-19', 'AD_VP', 17000.00),
(103, 'Alexander', 'Hunold', '1987-06-20', 'IT_PROG', 9000.00),
(104, 'Bruce', 'Ernst', '1987-06-21', 'IT_PROG', 6000.00),
(105, 'David', 'Austin', '1987-06-22', 'IT_PROG', 4800.00),
(106, 'Valli', 'Pataballa', '1987-06-23', 'IT_PROG', 4800.00),
(107, 'Diana', 'Lorentz', '1987-06-24', 'IT_PROG', 4200.00);

-- 3 a)

SELECT DEPT_LOCATION.Loc_Code, DEPT_LOCATION.Address, DEPT_LOCATION.City, DEPT_LOCATION.State, COUNTRY.Country_name
FROM DEPT_LOCATION
JOIN COUNTRY ON DEPT_LOCATION.Reg = COUNTRY.Reg;

-- 3 b)

SELECT Job_id, COUNT(*) AS Count
FROM WORKER
GROUP BY Job_id
HAVING COUNT(*) > 1;

-- 3 c)

SELECT MAX(Salary)
FROM WORKER
WHERE Job_id = 'IT_PROG';