/*
    Title: whatabook_program_queries.sql
    Author: Brendan Spurlock
    Date: 08/10/2023
    Description: WhatABook program queries
*/

-- DISPLAY USER WISHLIST
SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author
FROM wishlist
    INNER JOIN user ON wishlist.user_id = user.user_id
    INNER JOIN book ON wishlist.book_id = book.book_id
WHERE user.user_id = 1;

-- VIEW THE STORES LOCATION
SELECT store_id, locale from store;

-- ALL WHATABOOK BOOKS
SELECT book_id, book_name, details, author from book;

-- VIEW LISTING OF BOOKS THAT ARE NOT IN USERS WISHLIST
SELECT book_id, book_name, details, author
FROM book
WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = 2);

-- ADDING A NEW BOOK WITH INSERT STATEMENT
INSERT INTO wishlist(user_id, book_id)
    VALUES(2, 5)

-- REMOVING A BOOK FROM WISHLIST 
DELETE FROM wishlist WHERE user_id = 2 AND book_id = 5;