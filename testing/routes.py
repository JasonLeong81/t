from flask import Blueprint, render_template, flash
from testing.forms import RegistrationForm
from testing import db
from testing.models import User

user = Blueprint('user',__name__)


@user.route('/',methods=['GET','POST'])
def test():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        db.session.add(user)
        db.session.commit()
        flash('Done')
    return render_template('test.html',title='Home',form=form)
