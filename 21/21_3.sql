CREATE TABLE dz_book (book_id int, book_title text, 
					  book_author text, publisher_id int)
SELECT * FROM dz_book
INSERT INTO dz_book VALUES (1, 'It', 'King', 3)
INSERT INTO dz_book VALUES
(2, 'Нос', 'Гоголь', 2),
(3, 'Война и мир', 'Толстой', 2),
(4, 'Carrie', 'King', 3),
(5, 'The Shining', 'King', 1),
(6, 'Тарас Бульба', 'Гоголь', 3)

SELECT book_title, book_author FROM dz_book

SELECT book_title, book_author FROM dz_book
WHERE book_title LIKE '% %'

SELECT book_title FROM dz_book WHERE publisher_id = 3

SELECT book_title FROM dz_book 
WHERE publisher_id = 3 and book_author = 'King'