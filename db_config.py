from app import app
from flaskext.mysql import MySQL
from neo4j import GraphDatabase

# MySQL config
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'localmachine'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'cs411_demo'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)

# Neo4j config
NEO4J_URL = "bolt://localhost:7687"
NEO4J_USERNAME = "neo4j"
NEO4J_PASSWORD = "test"
driver = GraphDatabase.driver(
    uri=NEO4J_URL,
    auth=(NEO4J_USERNAME,NEO4J_PASSWORD)
    )
neo = driver.session()