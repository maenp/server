import json
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import django

# 获取 csrftoken、用户信息
def current(request):
    token = django.middleware.csrf.get_token(request)
    return JsonResponse({
        'status': 200, 
        'msg': '登录成功', 
        'data':{
            'token':token,
            'username': 'root',
            'user_id': 1,
        }
    })

@csrf_exempt # 取消csrf验证
def login(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        username = body.get('username')
        password = body.get('password')

        if username == 'root' and password == '123':
            token = django.middleware.csrf.get_token(request)
            return JsonResponse({'status': 200, 'msg': '登录成功', 'data':{'token':token}})
    return JsonResponse({'status': 400, 'msg': '登录失败~','success':False})