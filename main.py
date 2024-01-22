#Hello mr park this is my video presentaction for my computer final project. The assiment that I have chose is how to make a website using flask and I am making it on repplit because my school computer cant download flask so i am going to go throught the lines of code and explain their funtion and what they do. After I will explain the diffrences between the inital thougyt on what i was going to make and what I made.first inm gonig to talk about my main.py this is like the back bone of the website and contains anty type of funtuion or variable that it needs. It also contains the types of code need to inicalize a website using flask.

#Import Flask and if it is not downloaded it will download it.  Flask is a web framework for Python.
from flask import Flask, render_template, redirect, url_for
#This line is used to create or state that you are creating a web,it's like creating a class
app = Flask(__name__)

# This line is used to create a dictonary containg the name of the menu items and it's prices this will be used later in menu
menu_items = {
    'pizza_slice': {'name': 'Pizza Slice', 'price': 14.99},
    'hamburger': {'name': 'Hamburger', 'price': 12.99},
    'steak': {'name': 'Steak', 'price': 22.99},
    'french_fries': {'name': 'French Fries', 'price': 3.99},
    'meatball_sub': {'name': 'Meatball Sub', 'price': 10.99},
}

# This is used to store the items in the cart, this will be used in the cart template
cart = []

#This These are here to keep the urel at the top of the page so that you can keep chaning pages. They use somthing called the root url. The root url is the start or index page of a domain on a web server. It is essencially the name of the web page
@app.route('/')
def home():
    return render_template('home.html')

#This is the link to the menu page. @app.route is used to get the specific URL with the  function to get the desired out come. The last line is called a render and is used to get the url or the template for the web page menu and any relevent informaction that it might need.
@app.route('/menu')
def menu():
    return render_template('menu.html', menu_items=menu_items)

#This is the link to the cart page
@app.route('/add_to_cart/<item_name>')
def add_to_cart(item_name):
    item = menu_items.get(item_name)
    if item:
        cart.append(item)
    return redirect(url_for('menu'))

#This is the link to the History Page
@app.route('/history')
def history():
    return render_template('history.html')

#THis is the link to the contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# is used to get the template as well as calculate the total price of the items in the cart. Addotioanlly it determines the total price of items after tax.
@app.route('/cart')
def view_cart():
    sum = 0
    for item in cart:
        sum += item["price"]
    total_cost_before_tax = sum
    tax = total_cost_before_tax * 0.13  # 13% tax
    total_cost_after_tax = round(total_cost_before_tax + tax, 2)
    return render_template('cart.html', cart=cart, total_cost_before_tax=total_cost_before_tax, total_cost_after_tax=total_cost_after_tax)


# This is to start the page and host it. The 0.0.0.0 host means that the server should listen on all available network interfaces meaning from any ip adress of compyter yopu can get it so it is open to the public. For a long time I kept getting an error saying that the port was already in use so I changed it to 8080. this number is like a bar code for where the server should start and what it should be identifed as
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug = True) 