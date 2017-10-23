import getconf
config = getconf.ConfigGetter('fpost', ['./app/config.ini', './app/settings.ini'])
debug = config.getbool('debug', False)
db_host = config.get('db.host', 'localhost')
db_port = config.getint('db.port', 5432)
print(db_host)