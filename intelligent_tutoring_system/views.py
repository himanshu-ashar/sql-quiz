from django.shortcuts import render
from .ques_gen import Ques_Gen_Book
import sqlite3
import sqlvalidator

def index(request):
    return render(request,'index.html')

def question_gen_1(request):
    ques_gen = Ques_Gen_Book()
    ques, query = ques_gen.lvl_1_ques()
    feedback = ''
    if request.GET.get('answer'):
        connection = sqlite3.connect("C:/Users/hhash/Desktop/FYP Implementation/books.db")
        crsr = connection.cursor()
        correct_answer = str(request.GET.get('correct_answer'))
        crsr.execute(correct_answer)
        ans = crsr.fetchall()
        user_ans = request.GET.get('answer')
        user_ans_check = sqlvalidator.parse(user_ans)
        if not user_ans_check.is_valid():
            feedback = 'Incorrect Syntax'
        # print(user_ans_check.errors)
        else:
            crsr.execute(user_ans)
            user_ans = crsr.fetchall()
            test_1 = set(ans) - set(user_ans)
            test_2 = set(user_ans) - set(ans)
            final = list(test_1) + list(test_2)
            if len(final)==0:
                feedback = 'Correct Answer'
            else:
                feedback = 'Incorrect Answer'
    context = {'ques':ques,'feedback':feedback,'query':query}

    return render(request,'question_gen.html',context=context)

def question_gen_2(request):
    ques_gen = Ques_Gen_Book()
    ques, query = ques_gen.lvl_2_ques()
    feedback = ''
    if request.GET.get('answer'):
        connection = sqlite3.connect("C:/Users/hhash/Desktop/FYP Implementation/books.db")
        crsr = connection.cursor()
        correct_answer = str(request.GET.get('correct_answer'))
        crsr.execute(correct_answer)
        ans = crsr.fetchall()
        user_ans = request.GET.get('answer')
        user_ans_check = sqlvalidator.parse(user_ans)
        if not user_ans_check.is_valid():
            feedback = 'Incorrect Syntax'
        # print(user_ans_check.errors)
        else:
            crsr.execute(user_ans)
            user_ans = crsr.fetchall()
            test_1 = set(ans) - set(user_ans)
            test_2 = set(user_ans) - set(ans)
            final = list(test_1) + list(test_2)
            if len(final)==0:
                feedback = 'Correct Answer'
            else:
                feedback = 'Incorrect Answer'
    context = {'ques':ques,'feedback':feedback,'query':query}

    return render(request,'question_gen.html',context=context)

def question_gen_3(request):
    ques_gen = Ques_Gen_Book()
    ques, query = ques_gen.lvl_3_ques()
    feedback = ''
    if request.GET.get('answer'):
        connection = sqlite3.connect("C:/Users/hhash/Desktop/FYP Implementation/books.db")
        crsr = connection.cursor()
        correct_answer = str(request.GET.get('correct_answer'))
        crsr.execute(correct_answer)
        ans = crsr.fetchall()
        user_ans = request.GET.get('answer')
        user_ans_check = sqlvalidator.parse(user_ans)
        if not user_ans_check.is_valid():
            feedback = 'Incorrect Syntax'
        # print(user_ans_check.errors)
        else:
            crsr.execute(user_ans)
            user_ans = crsr.fetchall()
            test_1 = set(ans) - set(user_ans)
            test_2 = set(user_ans) - set(ans)
            final = list(test_1) + list(test_2)
            if len(final)==0:
                feedback = 'Correct Answer'
            else:
                feedback = 'Incorrect Answer'
    context = {'ques':ques,'feedback':feedback,'query':query}

    return render(request,'question_gen.html',context=context)

def question_gen_4(request):
    ques_gen = Ques_Gen_Book()
    ques, query = ques_gen.lvl_4_ques()
    feedback = ''
    if request.GET.get('answer'):
        connection = sqlite3.connect("C:/Users/hhash/Desktop/FYP Implementation/books.db")
        crsr = connection.cursor()
        correct_answer = str(request.GET.get('correct_answer'))
        crsr.execute(correct_answer)
        ans = crsr.fetchall()
        user_ans = request.GET.get('answer')
        user_ans_check = sqlvalidator.parse(user_ans)
        if not user_ans_check.is_valid():
            feedback = 'Incorrect Syntax'
        # print(user_ans_check.errors)
        else:
            crsr.execute(user_ans)
            user_ans = crsr.fetchall()
            test_1 = set(ans) - set(user_ans)
            test_2 = set(user_ans) - set(ans)
            final = list(test_1) + list(test_2)
            if len(final)==0:
                feedback = 'Correct Answer'
            else:
                feedback = 'Incorrect Answer'
    context = {'ques':ques,'feedback':feedback,'query':query}

    return render(request,'question_gen.html',context=context)
