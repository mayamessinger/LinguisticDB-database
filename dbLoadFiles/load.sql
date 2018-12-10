-- COPY Authors
-- FROM '/home/database/dbLoadFiles/authors.csv'
-- WITH
-- (
--     DELIMITER '|',  --CSV field delimiter
--     NULL 'NULL'
-- );
--
-- COPY Books
-- FROM '/home/database/dbLoadFiles/books.csv'
-- WITH
-- (
-- 	DELIMITER '|',
-- 	NULL 'NULL'
-- );
--
-- COPY Writes
-- FROM '/home/database/dbLoadFiles/writes.csv'
-- WITH
-- (
-- 	DELIMITER '|',
-- 	NULL 'NULL'
-- );
--
-- COPY BookWordAggregates
-- FROM '/home/database/dbLoadFiles/bookword.csv'
-- WITH
-- (
-- 		DELIMITER '|',
-- 		NULL 'NULL'
-- );

COPY CosineSimilarity
FROM '/home/database/dbLoadFiles/cosinesimilarity.csv'
WITH
(
		DELIMITER '|',
		NULL 'NULL'
);
