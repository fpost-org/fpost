from app.DB import DB

flask_db = DB()
print (flask_db.check())

print (flask_db.host, flask_db.user, flask_db.pas, flask_db.db)
