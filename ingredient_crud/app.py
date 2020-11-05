from flask import Flask


app = Flask(__name__)
# TODO: change secret key (?) 
app.secret_key = "cs411-demo"
