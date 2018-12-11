# LingusticDB-database
Database is running locally on a VM, database is called "ldb"

Instructions to manage Postgres database:
``` bash
sudo /etc/init.d/postgresql restart (status)  
sudo su - postgres  
/usr/lib/postgresql/11/bin/pg_ctl -D /etc/postgresql/11/main -l ~/logfile start   
```
Files that configure database permissions:  
* /etc/postgresql/11/main/postgresql.conf
* /etc/postgresql/11/main/pg_ident.conf

Book text files stored at: /home/books/

For python files that generate CSVs to load into database:  
* File should print to std out once per table row  
``` python
for file in glob.glob("/home/books/[0-9]*.txt"):  
	bookid = file.split("/")[3].split(".")[0] # identifying key of book
	print "var1|var2" %(var1, var2) # format for CSV
```
``` bash
sudo python -c 'import <table>_loader; <table>_loader.populate()' > /home/database/dbLoadFiles/<table>.csv
# (CSV file might need to be sanitized if database doesn't like a line's formatting (mostly strings))
```

In load.sql, to mass load a CSV into database:  
``` sql
COPY <table>
FROM '/home/database/dbLoadFiles/<table>.csv'
WITH
(
		DELIMITER '|',
		NULL 'NULL'
);
```
To load database and then interact with it
``` bash
sudo su - postgres
dropdb ldb; createdb ldb; psql ldb -af /home/database/dbLoadFiles/create.sql
psql ldb -af /home/database/dbLoadFiles/load.sql
psql ldb
```
