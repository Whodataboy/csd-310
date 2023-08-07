/*
    Title: db_init.sql
    Author: Brendan Spurlock
    Date: 08/06/2023
    Description: whatabook db initialization script.
*/

-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

-- Create table(s)
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_id)
);

-- insert store record 
INSERT INTO store(locale) 
    VALUES('13800 N May Ave, Oklahoma City, OK, 73134');

-- insert book records 
INSERT INTO book(book_name, author, details) 
    VALUES ('Scar Tissue', 'Anthony Kiedis', 'Scar Tissue is the autobiography of Red Hot Chili Peppers vocalist Anthony Kiedis.');

INSERT INTO book(book_name, author, details) 
    VALUES ('Acid For The Children', 'Flea', 'Acid for the Children is the memoir of Red Hot Chili Peppers bassist Flea.');

INSERT INTO book(book_name, author, details) 
    VALUES ('The Storyteller', 'Dave Grohl', 'A collection of memories of a life lived loud.');

INSERT INTO book(book_name, author, details) 
    VALUES ('Beastie Boys Book', 'Michael Diamond', 'A panoramic experience that tells the story of Beastie Boys.');

INSERT INTO book(book_name, author, details) 
    VALUES ('Heaven Is A Playground', 'Rick Telander', 'Heaven Is a Playground was the first book on the uniquely American phenomenon of urban basketball.');

INSERT INTO book(book_name, author, details) 
    VALUES ('KRINK New York City', 'Craig Costello', 'Craig Costello, aka KR, grew up in Queens, New York, where graffiti was part of the landscape and a symbol of the city.');

INSERT INTO book(book_name, author, details) 
    VALUES ('I Put A Spell On You', 'Nina Simone', 'The 1992 autobiography by Nina Simone, written with Stephen Cleary.');

INSERT INTO book(book_name, author, details) 
    VALUES ('The Eye', 'Nathan Williams', 'In The Eye, we meet fashion designers like Claire Waight Keller and Thom Browne.');

INSERT INTO book(book_name, author, details) 
    VALUES ('Original Gangstas', 'Ben Westhoff', 'It’s the definitive history of L.A. gangsta rap, revealing how a cohort of then-unknown rappers.');

-- insert user
INSERT INTO user(first_name, last_name) 
    VALUES ('John', 'Frusciante');

INSERT INTO user (first_name, last_name) 
    VALUES ('Chad', 'Smith');

INSERT INTO user (first_name, last_name) 
    VALUES ('Anthony', 'Kiedis');

-- insert wishlist records 
INSERT INTO wishlist (user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'John'),
        (SELECT book_id FROM book WHERE book_name = 'Scar Tissue')
    );

INSERT INTO wishlist (user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Chad'),
        (SELECT book_id FROM book WHERE book_name = 'Acid For The Children')
    );

INSERT INTO wishlist (user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Anthony'),
        (SELECT book_id FROM book WHERE book_name = 'The Storyteller')
    );