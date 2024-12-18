from flask import Blueprint, render_template,request,redirect, url_for
from services.home_service import add_user, check_user, get_all_users, get_user,update_username,delete_user_by_email
bp = Blueprint('home', __name__)

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/add_user', methods=['GET'])
def create_user():
    return render_template('add_user.html')

@bp.route('/create_user', methods=['POST'])
def create_user_post():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    
    if not username or not email:
        return "Missing username or email!", 400

    result = add_user(username, email,password)
    if result: 
       return render_template('home.html')
    return None



@bp.route('/login_user', methods=['POST'])
def login_user():
    password = request.form.get('password')
    email = request.form.get('email')
    
    if not password or not email:
        return "Missing username or email!", 400
    
    result = check_user(email, password)
    if result:
        if get_user(email,password).isAdmin == 1:
            return redirect(url_for('home.admin'))
        return redirect(url_for('home.chat'))
    
    return redirect(url_for('home.notfound',email=email))


@bp.route('/chatapp')
def chat():
    return render_template('chatbox.html')

@bp.route('/notfound/<string:email>')
def notfound(email):
    return render_template('_404.html',email=email)

@bp.route('/admin')
def admin():
    users = get_all_users()
    return render_template('admin_panel.html',users=users)

# create new user


@bp.route('/create/newUser', methods=['POST'])
def create_new_user():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    result = add_user(username, email,password)
    
    if result: 
       return redirect(url_for('home.admin'))
    return None


@bp.route('/update-user', methods=['POST'])
def update_user():
    username = request.form.get('username')
    email = request.form.get('email')   
    result = update_username(username, email)
    if result: 
       return redirect(url_for('home.admin'))
    return None

@bp.route('/delete_user', methods=['POST'])
def delete_user():
    email = request.form.get('email')  # Lấy email từ form gửi lên
    if not email:
        return render_template('home.html')
    result = delete_user_by_email(email)
    if result:
     return redirect(url_for('home.admin'))