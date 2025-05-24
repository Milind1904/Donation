from flask import Blueprint, render_template
from flask_login import current_user
from app.models import NGO, Donation, Request

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    # Get some statistics for the homepage
    total_donations = Donation.query.count()
    active_ngos = NGO.query.filter_by(verified=True).count()
    urgent_requests = Request.query.filter_by(status='urgent').limit(5).all()
    
    return render_template('main/home.html', 
                         title='Home',
                         total_donations=total_donations,
                         active_ngos=active_ngos,
                         urgent_requests=urgent_requests)

@main.route('/about')
def about():
    return render_template('main/about.html', title='About Us')

@main.route('/contact')
def contact():
    return render_template('main/contact.html', title='Contact Us')

@main.route('/how-it-works')
def how_it_works():
    return render_template('main/how_it_works.html', title='How It Works')

@main.route('/ngos')
def ngo_list():
    ngos = NGO.query.filter_by(verified=True).all()
    return render_template('main/ngo_list.html', title='NGO Partners', ngos=ngos)

@main.context_processor
def utility_processor():
    def is_admin():
        return current_user.is_authenticated and current_user.role == 'admin'
    return dict(is_admin=is_admin) 
