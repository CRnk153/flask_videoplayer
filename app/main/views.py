from flask import request, render_template, flash, redirect, url_for, Blueprint
from flask_login import login_user
from app import login_manager, db
from app.models import User
from .forms import RegistrationForm, LoginForm

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/', methods=["GET"])
def index():
    return render_template('main/home.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.name.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('main.login'))
    return render_template('main/register.html', form=form)

@main.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.name.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('main.index'))
            next_page = request.args.get('next')
            return redirect(next_page or url_for('index'))
        else:
            flash('Invalid username or password.')
    return render_template('main/login.html', form=form)
