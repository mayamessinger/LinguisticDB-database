COPY Authors
FROM '/home/repo/authors.csv'
WITH
(
    DELIMITER '|',  --CSV field delimiter
    NULL 'NULL'
);

COPY Books
FROM '/home/repo/books.csv'
WITH
(
	DELIMITER '|',
	NULL 'NULL'
);

COPY Writes
FROM '/home/repo/writes.csv'
WITH
(
	DELIMITER '|',
	NULL 'NULL'
);

COPY BookWordAggregates
FROM '/home/repo/bookword.csv'
WITH
(
		DELIMITER '|',
		NULL 'NULL'
);