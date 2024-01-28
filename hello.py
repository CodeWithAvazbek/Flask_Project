from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# create a Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "my super secret key that no one is supposed to know"


# Create A form Class
class NamerForm(FlaskForm):
    name = StringField("What's Your name", validators=[DataRequired()])
    submit = SubmitField("Submit")

    # BooleanField
    # DateField
    # DateTimeField
    # DecimalField
    # FileField
    # HiddenField
    # MultipleField
    # FieldList
    # FloatField
    # FormField
    # IntegerField
    # PasswordField
    # RadioField
    # SelectField
    # SelectMultipleField
    # SubmitField
    # StringField
    # TextAreaField

    # Validators
    # DataRequired
    # Email
    # EqualTo
    # InputRequired
    # IPAddress
    # Length
    # MacAddress
    # NumberRange
    # Optional
    # Regexp
    # URL
    # UUID
    # AnyOf
    # NoneOf


# Create a route decorator
# @app.route('/')
# def index():
#     return f"<h1>Hello World!</h1>"

# safe
# capitalize
# lower
# upper
# title
# trim
# striptags
@app.route('/')
def index():
    first_name = "Avazbek"
    last_name = "Hazratov"
    flash("Welcome To Our Website! ")
    favorite_pizza = ['Pepperoni', 'cheese', 'Mushrooms', 41]
    return render_template(
        'index.html',
        first_name=first_name,
        last_name=last_name,
        favorite_pizza=favorite_pizza
    )


# localhost:5000/user/avazbek
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)


# Create Custom Error Pages
# Invalid URL
@app.errorhandler(404)
def pages_not_found(e):
    return render_template('404.html'), 404


# Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# create Name page
@app.route('/name', methods=['GET', 'POSt'])
def name():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
        flash("Form Submitted Successfully ")

    return render_template(
        "name.html",
        name=name,
        form=form
    )
