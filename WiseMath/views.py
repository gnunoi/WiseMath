from django.http import HttpResponse
answer_form = """
<form method="POST" action="/test_html/">
    输入答案：<input type="text" name="user_answer"/>
    <input type="submit" value="提交"/>
</form>
"""
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

# def math_type(request, type):
#     html = "<center>"
#     html += f'<h1>数学试题，类型{{}}</h1>'.format(type)
#     html += "</center>"
#     return HttpResponse(html)

# def math_calc(request, a, op, b):
#     html = "<center>"
#     a = int(a)
#     b = int(b)
#     r = 0
#     if op == '+':
#         r = a + b
#     elif op == '-':
#         r = a - b
#     elif op == '*':
#         op = '×'
#         r = a * b
#     elif op == '/':
#         op = '÷'
#         r = a / b
#     elif op == '//':
#         r = a // b
#     elif op == '%':
#         r = a % b
#     elif op == '**':
#         r = a ** b
#     html += f'<h1>{{}} {{}} {{}} = {{}}</h1>'.format(a, op, b, r)
#     html += "</center>"
#     return HttpResponse(html)

# def test_request(request):
#     print(f'path_info:{request.path_info}')
#     print(f'method:{request.method}')
#     print(f'GET:{request.GET}')
#     print(f'POST:{request.POST}')
#     print(f'FILES:{request.FILES}')
#     print(f'PATH:{request.path}')
#     print(f'session:{request.session}')
#     print(f'full_path:{request.get_full_path()}')
#     print(f'body:{request.body}')
#     return HttpResponse('测试完毕')

# def test_post(request):
#     if request.method == 'GET':
#         return HttpResponse(answer_form)
#
#     if request.method == 'POST':
#         user_answer = request.POST.getlist('user_answer')
#         print(f'user_answer: {user_answer}')
#         return HttpResponse('POST测试完毕')
#
#     return HttpResponse('其它')

def test_html(request):
    from django.shortcuts import render
    if request.method == 'GET':
        return render(request,'test.html', {'user_answer': '1 + 2 = 3'})
    if request.method == 'POST':
        user_answer = request.POST.get('user_answer')
        question_type = request.POST.get('question_type')
        print(locals())
        print(f'user_answer: {user_answer}')
        print(request)
        return render(request,'test.html', locals())

def test_html2(request):
    from django.shortcuts import render
    context = {
        'option_list': list(range(16)),
    }
    if request.method == 'POST':
        selected_option = request.POST.get('selected_option', '未选择')
        context = {**context,
            'selected_option': selected_option
        }
    return render(request, 'test_html2.html', context)