from flask import render_template, request
from FlaskProject2.BusinessLayer import amazon_displayer
from FlaskProject2.BusinessLayer import tapaz_displayer
from FlaskProject2 import app

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        item = request.form["search"]
        min_price = request.form["min"]
        max_price = request.form["max"]
        sort_style = request.form["sort"]
        currency = request.form["currency"]
        amazon = request.form.getlist('amazon')
        tapaz = request.form.getlist('tapaz')
        #aliexpress = request.form.getlist('aliexpress')
        amazon_products = amazon_displayer.display(item, sort_style, amazon, currency, min_price, max_price)
        tapaz_products = tapaz_displayer.display(item, sort_style, tapaz, currency, min_price, max_price)
        #aliexpress_products = displayAliexpress(item, sort_style, aliexpress, currency, min_price, max_price)
        return render_template('home.html', tapaz_products=tapaz_products, amazon_products=amazon_products)
    else:
        amazon_products = []
        tapaz_products = []
        #aliexpress_products = []
        return render_template('home.html', tapaz_products = tapaz_products, amazon_products = amazon_products)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/login')
def login():
    return render_template('login.html', title='Login')


@app.route('/register')
def register():
    return render_template('register.html', title='Registeration')
