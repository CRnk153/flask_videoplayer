from flask import request, render_template, flash, redirect, url_for, Blueprint, get_flashed_messages
from flask_login import login_user, login_required, logout_user
from app import db
from app.models import User
from .forms import RegistrationForm, LoginForm

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/', methods=["GET"])
def index():
    flash("Welcome!", "info")
    flash("Welcome!", "info")
    return render_template('main/home.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if db.session.query(User).filter(User.username == form.name.data).first(): 
            flash("Username is already taken", "form-error")
            return redirect(url_for('main.register'))
        if db.session.query(User).filter(User.email == form.email.data).first():
            flash("Email is already taken", "form-error")
            return redirect(url_for('main.register'))
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

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/videoplayer')
@login_required
def videoplayer():
    return render_template('main/videoplayer.html')
