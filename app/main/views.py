from flask import render_template, flash, redirect, url_for, Blueprint
from app import login_manager, db
from app.models import User
from .forms import RegistrationForm

main = Blueprint('main', __name__, 
                 static_folder='static',
                 static_url_path='/static',
                 template_folder='templates')

@main.route('/', methods=["GET"])
def index():
    return render_template('main/home.html')

@main.route('/login', methods=["GET", "POST"])
def login():
    pass

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('main.login'))
    return render_template('main/register.html', form=form)
