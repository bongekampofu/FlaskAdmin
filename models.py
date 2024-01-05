from sqlalchemy.orm import relationship

from extension import db
from flask_login import UserMixin

from datetime import datetime as dt
from sqlalchemy import Column, Integer, DateTime




class User(db.Model, UserMixin):
 id = db.Column(db.Integer, primary_key=True)
 username = db.Column(db.String(50))
 email = db.Column(db.String(120), unique=True, nullable=False)
 password = db.Column(db.String(100), nullable=False)
 #hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
 #password=hashed_password

 posts = db.relationship("Post", back_populates="user")

 def __str__(self):
    return self.username
    #return f'<User {self.username}>'

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100))
  body = db.Column(db.Text)
  user_id = db.Column(db.ForeignKey("user.id"), nullable=False)
  user = db.relationship("User", back_populates="posts")

class Restaurant(db.Model):
 id = db.Column(db.Integer, primary_key=True)
 restname = db.Column(db.String(50))

 resttables = db.relationship("RestTable", back_populates="restaurant")

 def __str__(self):
    return self.restname
    #return f'<User {self.username}>'

class RestTable(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  tablename = db.Column(db.String(100))
  body = db.Column(db.Text)
  rest_id = db.Column(db.ForeignKey("restaurant.id"), nullable=False)
  restaurant = db.relationship("Restaurant", back_populates="resttables")


class Food(db.Model):
    __tablename__ = "food"
    food_id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(20), unique=True, nullable=False)
    food_price = db.Column(db.Numeric(10,2), nullable=False)
    # food_image = db.Column(db.LargeBinary)
    food_type = db.Column(db.String(30), nullable=False)


def __repr__(self):
    return f'<Food {self.food_name}>'

class Order(db.Model):
    __tablename__ = "order"
    order_no = db.Column(db.Integer, primary_key=True, autoincrement=True)
    food_id = db.Column(db.Integer, db.ForeignKey('food.food_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    trans_option = db.Column(db.String(30), nullable=False)
    status = db.Column(db.String(30), nullable=False)
    food = relationship(Food, backref='foods')


def __repr__(self):
    return f'<Order {self.order_no}>'


class Pay(db.Model):
    __tablename__ = "pay"
    pay_no = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_no = db.Column(db.Integer, db.ForeignKey('order.order_no'), nullable=False)
    total_price = db.Column(db.Integer, nullable=False)
    cust_name = db.Column(db.String(30), nullable=False)
    cust_address = db.Column(db.String(30), nullable=False)
    cust_postcode = db.Column(db.String(30), nullable=False)
    cust_email = db.Column(db.String(30), nullable=False)
    cust_cardno = db.Column(db.String(30), nullable=False)
    card_expirydate = db.Column(db.String(30), nullable=False)
    card_cvv = db.Column(db.String(30), nullable=False)
    pay_datetime = db.Column(db.DateTime, default=dt.now)
    # pay_datetime = db.Column(db.DateTime, default=datetime.datetime.utcnow)

def __repr__(self):
    return f'<Pay {self.pay_no}>'


