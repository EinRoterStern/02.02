# -*- coding: utf-8 -*-
from bottle import post, request,response, template
from datetime import datetime
import re
import pdb
import json


questions = {} #������ �������

@post('/home', method='post')

def my_form():

    mail = request.forms.get('ADRESS')
    username = request.forms.get('USERNAME')
    question = request.forms.get('QUEST')

    pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$" #r - �������� ���� �� ����� ��� ���� �������(������� ��������� ��������), ^
                                                   #- ������ ������,-\w\. - ����� ���� ���� - ��������� �������� ����������� �������� ������ ��������, 
                                                   #����� ������� ������������� � �����, @ - ������ ���� ������,[-\w]{2,4} - 2-4 ������� ����������� ��������, $ - ����� ������
    #��������� ������������ �����
    if not username or not mail or not question or len(question) <= 3 or question.isdigit():     
        return template('index.tpl', message='fields are not filled or question <= 3 cymbol or all text is number!', year=datetime.now().year)
      #��������� ������������ �����
    if not re.match(pattern, mail):
        #print(f"Invalid email: {mail}") # �������� ������ � �������
        response.status = 400
        return template('index.tpl', message='dont corect email', year=datetime.now().year)
    access_date = datetime.now().strftime("%Y-%m-%d")
    if mail in questions:
        questions[mail][0]= username
        if question not in questions[mail][1:]:
            questions[mail].append(question)
        else:
             return template('index.tpl', message="ERROR: duplicate question!", year=datetime.now().year)
    else:   
        questions[mail] = [username,question]
    with open('quest.json', 'w') as json_file:
        json.dump(questions, json_file, indent=4)
    #pdb.set_trace()
    #���������� �������������� �����
    return "Thanks! {}! The answer will be sent to the mail {}, access Date: {}".format(username, mail, access_date)
