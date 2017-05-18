sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | sudo apt-key add -
sudo apt-get update
sudo apt-get install postgresql-9.5 libpq-dev

# edit /etc/postgresql/9.3/main/pg_hba.conf manualy
sudo sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/g" /etc/postgresql/9.5/main/postgresql.conf
# alter password 
sudo passwd postgres 
su postgres 
psql -c "ALTER USER postgres WITH PASSWORD 'postgres'" -d template1 
exit
sudo /etc/init.d/postgresql restart