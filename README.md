# LingusticDB-database
Database is running locally on a VM, database is called "ldb"

Instructions to manage Postgres database:
sudo /etc/init.d/postgresql restart (status)
sudo su - postgres
/usr/lib/postgresql/11/bin/pg_ctl -D /etc/postgresql/11/main -l ~/logfile start

/etc/postgresql/11/main/postgresql.conf
/etc/postgresql/11/main/pg_ident.conf

To use a python load file:
File should print to std out once per table row
for file in glob.glob("/home/books/[0-9]*.txt"):
	print "var1|var2" %(var1, var2)

python -c 'import books_loader; books_loader.populate()' > books.csv
(CSV file might need to be sanitized if database doesn't like an entry)

In load.sql:
COPY <TableName>
FROM '/home/database/dbLoadFiles/<file>.csv'
WITH
(
		DELIMITER '|',
		NULL 'NULL'
);

sudo su - postgres
dropdb ldb; createdb ldb; psql ldb -af /home/repo/create.sql
psql ldb -af /home/repo/load.sql

to open db, psql ldb