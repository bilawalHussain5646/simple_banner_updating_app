
from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime



# Users of the website
class countries(db.Model):
    id = db.Column(db.INTEGER, primary_key=True,nullable=False)
    sort_field = db.Column(db.INTEGER,nullable=False)
    name = db.Column(db.String(250),nullable=False)
    icon = db.Column(db.Text,nullable=False)
    banner = db.Column(db.Text,nullable=False)
    is_published = db.Column(db.INTEGER,nullable=False)
    created_at = db.Column(db.DateTime(),nullable=True)    
    updated_at = db.Column(db.DateTime(),nullable=True)    
    deleted_at = db.Column(db.DateTime(),nullable=True)    
    currency = db.Column(db.Text,nullable=False)
    

class products(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    sort_field = db.Column(db.Integer, default=0)
    priority = db.Column(db.Enum('high', 'mid'), default='mid')
    mpn = db.Column(db.String(255))
    cover = db.Column(db.Text)
    price = db.Column(db.Float(precision=8, asdecimal=True))
    price_old = db.Column(db.Float(precision=8, asdecimal=True))
    name_en = db.Column(db.String(255))
    name_ar = db.Column(db.String(255))
    description_en = db.Column(db.Text)
    description_ar = db.Column(db.Text)
    rating = db.Column(db.Integer)
    reviews_count = db.Column(db.Integer)
    link = db.Column(db.Text)
    link_buy = db.Column(db.Text)
    show_discount = db.Column(db.Boolean, default=False)
    discount_percent = db.Column(db.Integer, default=0)
    show_percent = db.Column(db.Boolean, default=False)
    is_published = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.TIMESTAMP, nullable=True)
    updated_at = db.Column(db.TIMESTAMP, nullable=True)
    deleted_at = db.Column(db.TIMESTAMP, nullable=True)
    category_id = db.Column(db.BigInteger)
    link_ar = db.Column(db.String(255))
    link_buy_ar = db.Column(db.String(255))
    add_pop_up = db.Column(db.Boolean, default=False)
    retailer_link1_logo = db.Column(db.Text)
    retailer_link2_logo = db.Column(db.Text)
    retailer_link3_logo = db.Column(db.Text)
    retailer_link4_logo = db.Column(db.Text)
    retailer_link5_logo = db.Column(db.Text)
    retailer_link6_logo = db.Column(db.Text)
    retailer_link7_logo = db.Column(db.Text)
    retailer_link8_logo = db.Column(db.Text)
    retailer_link1 = db.Column(db.Text)
    retailer_link2 = db.Column(db.Text)
    retailer_link3 = db.Column(db.Text)
    retailer_link4 = db.Column(db.Text)
    retailer_link5 = db.Column(db.Text)
    retailer_link6 = db.Column(db.Text)
    retailer_link7 = db.Column(db.Text)
    retailer_link8 = db.Column(db.Text)
    retailer_link1_title = db.Column(db.Text)
    retailer_link2_title = db.Column(db.Text)
    retailer_link3_title = db.Column(db.Text)
    retailer_link4_title = db.Column(db.Text)
    retailer_link5_title = db.Column(db.Text)
    retailer_link6_title = db.Column(db.Text)
    retailer_link7_title = db.Column(db.Text)
    retailer_link8_title = db.Column(db.Text)
        

class countries_products(db.Model):
    id = db.Column(db.INTEGER, primary_key=True,nullable=False)
    product_id = db.Column(db.INTEGER, nullable=False)
    country_id = db.Column(db.INTEGER, nullable=False)
