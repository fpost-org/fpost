#PostgreSQL Automation Installer Script version 1
#Author - Shashank Srivastava
#set -x
echo "Checking availability of pre-required packages"
sleep 1s
sudo rpm -q readline-devel.x86_64
if [ $? != 0 ]
then
echo "Readline package not found. Installing it...."
sudo yum install readline-devel.x86_64 -y
fi
sudo rpm -q zlib-devel-1.2.3-29.el6.x86_64
if [ $? != 0 ]
then
echo "zlib package not found. Installing it...."
sudo yum install zlib-devel.x86_64 -y
fi
echo "Unpacking PostgreSQL tarball..."
sleep 2s
sudo tar -zxf /home/shashank/postgresql-9.3.5.tar.gz
echo ""
echo "Tarball unpacked. Creating destination directory for Postgre...."
sudo mkdir -p /opt/PostgreSQL/9.3
cd /home/shashank/postgresql-9.3.5/
echo ""
echo "Destination directory created. Building installer from source coude...."
sleep 1s
sudo ./configure --prefix=/opt/PostgreSQL/9.3
sudo make
sleep 2s
echo ""
echo "Installer built. Installing it now...."
sudo make install
sleep 1s
id -a postgres
if [ $? != 0 ]
then
echo "postgres user not found. Adding it...."
sudo useradd postgres
else
echo "postgres user already exists. Proceeding to next step...."
fi
echo ""
echo "Configuring PostgreSQL...."
sudo mkdir -p /opt/PostgreSQL/9.3/data
sudo chown postgres /opt/PostgreSQL/9.3/data
echo ""
echo "Defining data directory for Postgre & starting it...."
sudo su - postgres -c "/opt/PostgreSQL/9.3/bin/initdb /opt/PostgreSQL/9.3/data/; sleep 2s; /opt/PostgreSQL/9.3/bin/pg_ctl -D /opt/PostgreSQL/9.3/data/ -l logfile start"
echo ""
echo "Checking version...."
echo "-------------------------------------------"
/opt/PostgreSQL/9.3/bin/psql --version
/opt/PostgreSQL/9.3/bin/postgres --version
echo ""
echo "Script executed successfully!"