from django.http import HttpResponse

def math(request):
    html = "<center>"
    html += "<h1>数学教程</h1>"
    html += "<h2>小学一年级</h2>"
    html += "<h2>小学二年级</h2>"
    html += "<h2>小学三年级</h2>"
    html += "<h2>小学四年级</h2>"
    html += "<h2>小学五年级</h2>"
    html += "<h2>小学六年级</h2>"
    html += "</center>"
    return HttpResponse(html)

def math_type(request, type):
    html = "<center>"
    html += f'<h1>数学试题，类型{{}}</h1>'.format(type)
    html += "</center>"
    return HttpResponse(html)

def math_calc(request, a, op, b):
    html = "<center>"
    a = int(a)
    b = int(b)
    r = 0
    if op == '+':
        r = a + b
    elif op == '-':
        r = a - b
    elif op == '*':
        r = a * b
    elif op == '/':
        r = a / b
    elif op == '//':
        r = a // b
    html += f'<h1>{{}} {{}} {{}} = {{}}</h1>'.format(a, op, b, r)
    html += "</center>"
    return HttpResponse(html)