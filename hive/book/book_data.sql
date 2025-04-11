CREATE EXTERNAL TABLE books_t
(
	isbn STRING,
	book_title STRING,
	book_author STRING,
	year_of_publication INT,
	publisher STRING, 
	image_url_s STRING,
	image_url_m STRING,
	image_url_l STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
	"separatorChar" = ";",
	"quoterChar" = "\""
)
STORED AS TEXTFILE
LOCATION '/TIL/input/book/books';

CREATE EXTERNAL TABLE ratings_t
(
	user_id INT,
	isbn STRING,
	book_rating INT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
	"separatorChar" = ";",
	"quoterChar" = "\""
)
STORED AS TEXTFILE
LOCATION '/TIL/input/book/ratings';

CREATE EXTERNAL TABLE users_t
(
	user_id INT,
	location STRING,
	age INT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
	"separatorChar" = ";",
	"quoterChar" = "\""
)
STORED AS TEXTFILE
LOCATION '/TIL/input/book/users';

CREATE VIEW books_view_t AS
SELECT
	isbn,
	book_title,
	book_author,
	CAST(year_of_publication AS INT) AS year_of_publication,
	publisher,
	image_url_s,
	image_url_m,
	image_url_l
FROM books_t;
	
CREATE VIEW ratings_view_t AS
SELECT
	CAST(user_id AS INT) AS user_id,
	isbn,
	CAST(book_rating AS INT) AS book_rating
FROM ratings_t;

CREATE VIEW users_view_t AS
SELECT
	CAST(user_id AS INT) AS user_id,
	location,
	CAST(age AS INT) AS age
FROM users_t;

SELECT * FROM books_t LIMIT 10;
SELECT * FROM ratings_t LIMIT 10;
SELECT * FROM users_t LIMIT 10;
SELECT * FROM books_view_t LIMIT 10;
SELECT * FROM ratings_view_t LIMIT 10;
SELECT * FROM users_view_t LIMIT 10;

DROP TABLE books_t;

-- Books 테이블에서 중복된 ISBN 확인
SELECT isbn, COUNT(*) FROM books_view_t
GROUP BY isbn
HAVING COUNT(*) > 1;

-- Users 테이블에서 Age의 결측값 확인
SELECT COUNT(*) FROM users_view_t
WHERE age is NULL;

-- 사용자 연령의 기초 통계(최소, 최대, 평균)를 확인합니다.
SELECT 
	MIN(age) AS min_age, 
	MAX(age) AS max_age, 
	AVG(age) AS avg_age 
FROM users_view_t;

-- 책의 출판 연도에 대한 기초 통계(최소, 최대, 평균)를 확인합니다.
SELECT 
	MIN(year_of_publication) AS min_year, 
	MAX(year_of_publication) AS max_year, 
	AVG(year_of_publication) AS avg_year
FROM books_view_t;

-- 평점의 분포 확인
SELECT book_rating, COUNT(*) AS rating_count 
FROM ratings_view_t
GROUP BY book_rating;

-- 출판사별로 얼마나 많은 책이 있는지, 그리고 그 책들의 평균 평점이 어떤지 확인합니다. 
-- 예시의 데이터는 book_count를 기준으로 정렬 후 상위 10개의 데이터를 출력했습니다.
SELECT b.publisher, COUNT(*) AS book_count, AVG(r.book_rating) AS avg_rating
FROM books_view_t b JOIN ratings_view_t r
ON b.isbn = r.isbn
GROUP BY b.publisher
ORDER BY book_count DESC
LIMIT 10;

-- 가장 많이 평가된 책과 그 평점
SELECT b.book_title, COUNT(*) AS rating_count, AVG(r.book_rating) AS avg_rating
FROM books_view_t b JOIN ratings_view_t r
ON b.isbn = r.isbn
GROUP BY b.book_title
ORDER BY book_count DESC
LIMIT 10;

-- 책의 출판 연도와 평점 간의 관계를 확인합니다.
SELECT b.year_of_publication, AVG(r.book_rating) AS avg_rating
FROM books_view_t b JOIN ratings_view_t r
ON b.isbn = r.isbn
GROUP BY b.year_of_publication;

-- 위치(location)에 따라 평균 평점을 출력합니다.
-- 적어도 10개 이상의 평가를 한 경우만 출력합니다.
SELECT location, AVG(r.book_rating) AS avg_rating, COUNT(*) AS rating_count
FROM users_view_t u JOIN ratings_view_t r
ON u.user_id = r.user_id
GROUP BY u.location
HAVING rating_count >= 10
ORDER BY avg_rating DESC
LIMIT 10;

-- 각 저자별로 평균 평점이 어떻게 다른지 확인합니다.
-- 적어도 10개 이상의 평가를 한 경우만 출력합니다.
SELECT b.book_author, AVG(r.book_rating) AS avg_rating, COUNT(*) AS rating_count
FROM books_view_t b JOIN ratings_view_t r
ON b.isbn = r.isbn
GROUP BY b.book_author
HAVING rating_count >= 10
ORDER BY avg_rating DESC
LIMIT 10;

