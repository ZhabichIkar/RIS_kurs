
import json
import os
from flask import render_template, Flask, request, redirect, url_for, flash, Blueprint
from access import group_required
from database.sql_provider import SQLProvider
from database.select import select_dict
from database.DBcm import db_config
from database.sql_provider import SQLProvider

blueprint_query = Blueprint('query_bp', __name__, template_folder='templates')

""" @blueprint_query.route('/')
@group_required
def query_index():
    # Указываем путь к папке 'sql'
    sql_provider = SQLProvider(file_path='./sql')
    
    # Получаем SQL-запрос
    sql = sql_provider.get(file='session.sql', name={'cinema_hall.name%'})
    
    # Выполняем запрос и получаем результат
    result = select_dict(current_app.config['db_config'], sql)
    if result:
        session = 'Результаты из БД'
        return render_template("dynamic.html", session=session, sessions=result)
    else:
        return "не достали из бд" """


sql_provider = SQLProvider(os.path.join(os.path.dirname(__file__),'sql'))



@blueprint_query.route('/')
@group_required
#@login_required
def get_category():
    product = select_dict(db_config, 'SELECT product_category  FROM products2')
    if product is None:
        return 'Неправильный вход в базу данных'
    else:
        return render_template ('dynamic.html', products= product)

@blueprint_query.route('/',  methods = ['POST'])
# @login_required
def request_result():
    user_input = request.form
    product = select_dict(db_config, sql_provider.get('session.sql', cinema_hall_name = user_input['cinema_hall_name']))
    prod_title = "Result of your request"
    if product is None:
        return 'Неправильный вход в базу данных'
    else:
        return render_template ('dynamic.html',prod_title = prod_title , products = product)
    
@blueprint_query.route('/aaa')
@group_required
# @login_required
def aaa():
    product = select_dict(db_config, 'SELECT product_category  FROM products2')
    if product is None:
        return 'Неправильный вход в базу данных'
    else:
        return render_template ('dynamic.html', products= product)
    
@blueprint_query.route('/ooo')
@group_required
# @login_required
def ooo():
    product = select_dict(db_config, 'SELECT product_category  FROM products2')
    if product is None:
        return 'Неправильный вход в базу данных'
    else:
        return render_template ('dynamic.html', products= product)