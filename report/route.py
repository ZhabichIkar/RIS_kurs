from flask import render_template, Flask, request, redirect, url_for, flash, Blueprint, current_app
from access import login_required
import os
from database.select import select_proc, select_list, select_dict
from database.sql_provider import SQLProvider
from access import login_required, group_required

report_blueprint = Blueprint('report_bp', __name__, template_folder='templates')

sql_provider = SQLProvider(os.path.join(os.path.dirname(__file__),'sql'))

@report_blueprint.route('/report',  methods = ['GET','POST'])
@group_required
@login_required
def watch_report():
    if request.method == 'GET':
        return render_template('report.html')
    else:
        user_input_data = request.form
        result = select_dict(current_app.config['db_config'], sql_provider.get('watch_rep.sql', input_month = user_input_data['month'], input_year=user_input_data['year']))
        prod_title = "Result of your request"
        print(request)
        print(result)
        if result is None:
            return 'Неправильный вход в базу данных'
        else:
            return render_template ('show_rep.html' , prod_title=prod_title, results = result)

@report_blueprint.route('/report_create',  methods = ['GET','POST'])
@group_required
@login_required
def cr_report():
    if request.method == 'GET':
        return render_template('create_rep.html')
    else:
        input_month = request.form.get('month')
        input_year = request.form.get('year')
        result = select_proc(current_app.config['db_config'], sql_provider.get('create_report.sql', input_month = input_month, input_year = input_year))
        print(result)
        if result is None:
            flash('error')
            return render_template ('create_rep.html')
        if result == []:
            flash('Вы успешно создали отчёт')
            return render_template ('create_rep.html')
        else:
            flash('вы успешно создали отчёт')
            return render_template ('create_rep.html')
            