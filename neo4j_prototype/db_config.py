from app import app
from flask.ext.neo4j import Neo4j

mysql = MySQL()

# Neo4j config

app.config['PY2NEO_HTTP_PORT'] = 'localmachine'
app.config['PY2NEO_HTTPS_PORT'] = ''
app.config['PY2NEO_BOLT_PORT'] = 'cs411_prototype'
app.config['PY2NEO_USER'] = 'localhost'
app.config['PY2NEO_PASSWORD'] = 'localhost'

mysql.init_app(app)