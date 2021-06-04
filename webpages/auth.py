from flask import Blueprint, render_template, request, flash, redirect, url_for
from .table import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        loginName = request.form.get('loginName')
        password = request.form.get('password')

        customer = User.query.filter_by(loginName=loginName).first()
        if customer:
            # if customer:
            if check_password_hash(customer.password, password):
                flash('Logged in successfully!', category='success')
                login_user(customer, remember=True)
                #current_user=customer                    
                #authenticated_user.set_role("customer")
                #print(current_user)
                return redirect(url_for('homewindow.home'))
            else:
                flash('Incorrect password, try again.', category='error')
            # elif manager:
            #     # new_password = generate_password_hash(manager.password, method = 'sha256')
            #     if check_password_hash(manager.password, password):
            #         flash('Logged in successfully!', category='success')
            #         login_user(manager, remember=True)
            #         print(current_user)
            #         authenticated_user.set_role("manager")                    
            #         #current_user=manager
            #         return redirect(url_for('homewindow.home'))
	#final update

            #     else:
            #         flash('Incorrect password, try again.', category='error')
            # else:
            #     flash('Login Name does not exist.', category='error')
        else:
            flash('Login Name does not exist.', category='error')

    return render_template("login.html", user=current_user)


@ auth.route('/logout')
@ login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@ auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        loginName = request.form.get('loginName')
        fullName = request.form.get('fullName')
        phoneNumber = request.form.get('phoneNumber')
        address = request.form.get('address')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        customer = User.query.filter_by(loginName=loginName).first()
        if customer:
            flash('Login Name already exists.', category='error')
        elif len(loginName) < 4:
            flash('login Name must be greater than 3 characters.',
                  category='error')
        elif len(fullName) < 4:
            flash('Full name must be greater than 4 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 6:
            flash('Password must be at least 6 characters.', category='error')
        else:
            new_user = User(loginName=loginName, password=generate_password_hash(password1, method='sha256'),
                                fullName=fullName, phoneNumber=phoneNumber, address=address, role="Customer")
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('homewindow.home'))

    return render_template("sign_up.html", customer=current_user)
