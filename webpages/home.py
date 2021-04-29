from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json

homewindow = Blueprint('homewindow', __name__)


@homewindow.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html")

@homewindow.route('/mhome', methods=['GET', 'POST'])
def mhome():
	return render_template('mhome.html')

@homewindow.route('/buy', methods=['GET', 'POST'])
def buy():
	return render_template('buy.html')

@homewindow.route('/rent', methods=['GET', 'POST'])
def rent():
	return render_template('rent.html')

@homewindow.route('/reviews', methods=['GET', 'POST'])
def reviews():
	return render_template('reviews.html')

@homewindow.route('/rating', methods=['GET', 'POST'])
def rating():
	return render_template('rating.html')