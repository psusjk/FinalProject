from flask import Blueprint, render_template, url_for,request,redirect, flash, jsonify
from flask_login import login_required, current_user
from . import db
from .table import Books,User,Stock
from datetime import datetime
import json


homewindow = Blueprint('homewindow', __name__)



@homewindow.route('/', methods=['GET', 'POST'])
@login_required
def home():	
	return render_template("home.html")

@homewindow.route('/addbooks', methods=['GET', 'POST'])
def addbooks():
	if request.method == 'GET':
		return render_template('addbooks.html')
	elif request.method == 'POST':
		isbn = request.form.get('ISBN')
		title = request.form.get('Title')
		publisher = request.form.get('Publisher')
		auth = request.form.get('Author')
		pdate = request.form.get('PubDate')
		npages = request.form.get('NumPages')
		ncopies = request.form.get('NumCopies')
		price = request.form.get('Price')
		keys = request.form.get('Keywords')
		sbook = request.form.get('SubOfBook')
		temp = Books.query.filter_by(ISBN=isbn).first()

		if temp:
			flash('Book already exists.', category='error')
		else:
			new_book = Books(ISBN=isbn, Title=title, Publisher=publisher,PublicationDate=pdate,
				NumberOfPages=npages, NumberOfCopies=ncopies, Price=price, Keywords=keys,
				SubjectOfBook=sbook)
			new_author =Author(name=auth,ISBN=isbn)
			db.session.add(new_book)
			db.session.add(new_author)
			db.session.commit()
		return redirect(url_for('homewindow.addbooks'))
@homewindow.route('/update', methods=['GET', 'POST'])
def update():
	if request.method == 'GET':
		return render_template('update.html')
	elif request.method == 'POST':
		isbn = request.form.get('ISBN')
		ncopies=request.form.get('NumCopies')
		temp = Books.query.filter_by(ISBN=isbn).first()

		if not temp:
			flash('Book does not exists.', category='error')
		else:
			new_update=Books.query.filter(Books.ISBN == isbn).update({Books.NumberOfCopies: Books.NumberOfCopies + ncopies})
			#db.session.add(new_update)
			db.session.commit()
			return redirect(url_for('homewindow.update'))



@homewindow.route('/promote', methods=['GET', 'POST'])
def promote():
	if request.method == 'GET':
		result= User.query.with_entities(User.loginName).filter(User.role == "Customer").all()
		return render_template('promote.html', result=result)

	elif request.method == 'POST':
		isbn = request.form.get('post.loginName')
		print(isbn)
		return redirect(url_for('homewindow.home'))

@homewindow.route('/updatestock', methods=['GET', 'POST'])
def updatestock():
	if request.method == 'GET':
		return render_template('updatestock.html')

	elif request.method == 'POST':
		nbook = request.form.get('NoofBooks')
		new_stock=Stock(NumberOfBooks=nbook)
		db.session.add(new_stock)
		db.session.commit()
		return redirect(url_for('homewindow.home'))
		
		


@homewindow.route('/buy', methods=['GET', 'POST'])
def buy():
	if request.method == 'GET':
		result= Books.query.filter(Books.NumberOfCopies > 0)
		return render_template('buy.html',result=result)
	elif request.method == 'POST':
		book=request.form.getlist('BuyBook')
		print(book)

# @homewindow.route('/rent', methods=['GET', 'POST'])
# def rent():
# 	return render_template('rent.html')

# @homewindow.route('/reviews', methods=['GET', 'POST'])
# def reviews():
# 	return render_template('reviews.html')

# @homewindow.route('/rating', methods=['GET', 'POST'])
# def rating():
# 	return render_template('rating.html')