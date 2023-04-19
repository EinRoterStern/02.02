# -*- coding: utf-8 -*-
from bottle import post, request,response, template
from datetime import datetime
import re

@post('/home', method='post')

def my_form():

    mail = request.forms.get('ADRESS')
    username = request.forms.get('USERNAME')
    question = request.forms.get('QUEST')

    pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
    #проверяем заполненость полей
    if not username or not mail or not question:     
        return template('index.tpl', message='fields are not filled!', year=datetime.now().year)
    #проверяем правильность почты
    if not re.match(pattern, mail):
        #print(f"Invalid email: {mail}")  # логируем ошибку в консоль
        response.status = 400
        return template('index.tpl', message='dont corect email', year=datetime.now().year)
    access_date = datetime.now().strftime("%Y-%m-%d")
    #используме форматирование строк
    return "Thanks! {}! The answer will be sent to the mail {}, access Date: {}".format(username, mail, access_date)
