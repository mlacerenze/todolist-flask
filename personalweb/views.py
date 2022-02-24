# from personalweb import app
from flask import render_template, Blueprint

bp = Blueprint('bp', __name__)

@bp.route('/')
@bp.route('/home')
def home():
  return render_template('home.html')

@bp.route('/portfolio')
def portfolio():
  return render_template('portfolio.html')

@bp.route('/contact')
def contact():
  return render_template('contact.html')
 