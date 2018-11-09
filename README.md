# LingusticDB-database
Database is running locally on a VM, database is called "ldb"

Instructions to manage Postgres database:
sudo /etc/init.d/postgresql restart (status)
sudo su - postgres
/usr/lib/postgresql/11/bin/pg_ctl -D /etc/postgresql/11/main -l ~/logfile start

/etc/postgresql/11/main/postgresql.conf
/etc/postgresql/11/main/pg_ident.conf

dropdb ldb; createdb ldb; psql ldb -af /home/repo/create.sql
psql ldb -af /home/repo/load.sql
