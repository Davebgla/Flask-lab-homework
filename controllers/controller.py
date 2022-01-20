from flask import render_template
from app import app
from models.shop_sales import *

@app.route('/orders')
def allorders():
    return render_template('index.html', title="Sal's Shop", openOrders=orders)

@app.route('/order/<number>')
def order_1(number):
    return render_template('order.html', title="Custom Order", order=orders[int(number)])