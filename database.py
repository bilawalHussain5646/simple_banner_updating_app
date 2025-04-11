from flask import Flask,render_template,request,url_for,redirect,Response,flash
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from flask_sqlalchemy import SQLAlchemy




username = "lg_pq_test"
password = "1OFOIi5&ovD7"
host = "118.139.161.13" 
# lebanon_database = "lebanon_ramadan"
# lg_showcase = "oled_test_pq"
lg_showcase = "lg_pq_test"

# database_file = f'mysql://{username}:{password}@{host}/{lebanon_database}'
database_file = f'mysql://{username}:{password}@{host}/{lg_showcase}'


app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
app.config['JSON_SORT_KEYS'] = False
db = SQLAlchemy(app)
app.secret_key = "wtb_secret_key_bilawal"

# Secret Key

# token_key = URLSafeTimedSerializer("BraggingRights")
# File Extension
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
