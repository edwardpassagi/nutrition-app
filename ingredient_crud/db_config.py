from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL config

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'cs411_demo'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'

mysql.init_app(app)