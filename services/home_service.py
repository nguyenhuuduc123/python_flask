from models.home_model import db, User
from utils import hash_password,check_password
def add_user(username, email,password):
    
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return f"User {username} already exists."
    password = hash_password(password)
    new_user = User(username=username, email=email,password=password)
    db.session.add(new_user)
    db.session.commit()
    return f"User {username} created successfully."


def check_user(email,password) :
    existing_user = User.query.filter_by(email=email,password=password).first()
    if existing_user:
        return True
    return False

def get_user(email,password)-> User:
    return User.query.filter_by(email=email,password=password).first()

def get_all_users():
    return User.query.filter_by(isAdmin = 0,deleteFlag = 0).all()

def update_username(username,email):
    user =  User.query.filter_by(email = email).first()
    if user:
        user.username = username
        db.session.commit()
    else:
        return False
    return True

def delete_user_by_email(email):
    user : User = User.query.filter_by(email=email).first()
    if not user:
        return 'error'
    user.deleteFlag = 1
    db.session.commit()
    return True


