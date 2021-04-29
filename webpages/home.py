from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json

homewindow = Blueprint('homewindow', __name__)


@homewindow.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html")


    