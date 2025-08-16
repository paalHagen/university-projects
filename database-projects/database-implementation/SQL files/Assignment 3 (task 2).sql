DROP DATABASE IF EXISTS task2;
CREATE DATABASE task2;
USE task2;

DROP TABLE IF EXISTS HOTEL;
DROP TABLE IF EXISTS ROOM;
DROP TABLE IF EXISTS BOOKING;
DROP TABLE IF EXISTS GUEST;

CREATE TABLE HOTEL (
	hotelNO INT NOT NULL,
    hotelName VARCHAR(50),
    hotelType VARCHAR(50),
    hotelAddress VARCHAR(50),
    hotelCity VARCHAR(50),
    numRoom INT,
    PRIMARY KEY (hotelNO)
);

CREATE TABLE ROOM (
	roomNo INT NOT NULL,
    hotelNo INT NOT NULL,
    roomPrice INT,
    PRIMARY KEY (roomNo),
    FOREIGN KEY (hotelNo) REFERENCES HOTEL(hotelNo)
);

CREATE TABLE GUEST (
	guestNo INT NOT NULL,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    guestAddress VARCHAR(50),
    PRIMARY KEY (guestNo)
);

CREATE TABLE BOOKING (
	bookingNo INT NOT NULL,
    hotelNo INT NOT NULL,
    guestNo INT NOT NULL,
    checkIn DATE,
    checkOut DATE,
    totalGuest INT,
    roomNo INT NOT NULL,
    PRIMARY KEY (bookingNo),
    FOREIGN KEY (hotelNo) REFERENCES HOTEL(hotelNO),
    FOREIGN KEY (guestNo) REFERENCES GUEST(guestNo),
    FOREIGN KEY (roomNo) REFERENCES ROOM(roomNo)
);

-- Task 2.a)
SELECT *
FROM HOTEL
WHERE hotelCity = 'New York'
ORDER BY numRoom DESC;

-- Task 2.b)
SELECT *
FROM GUEST
WHERE firstName = 'Sara'
ORDER BY guestAddress ASC;