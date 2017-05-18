apt-get install postgresql-9.2


/etc/postgresql/9.2/main
postgresql.conf:
data_directory = '/var/lib/postgresql/9.2/main' 
listen_addresses = '*'

pg_hba.conf:
host    all             all             0.0.0.0/0               md5

su postgres
/usr/bin/psql -d template1
\c postgres
\password postgres


/etc/init.d/postgresql restart