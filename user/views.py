import json
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from user.forms import ReqisterForm
from user.models import UserInfo
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
def loginIn_(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        username = body.get('username')
        password = body.get('password')

        if username == 'root' and password == '123':
            token = django.middleware.csrf.get_token(request)
            return JsonResponse({'status': 200, 'msg': '登录成功', 'data':{'token':token}})
    return JsonResponse({'status': 400, 'msg': '登录失败~','success':False})


@csrf_exempt
def register(req):
    if req.method=="POST":
        body = json.loads(req.body)
        form=ReqisterForm(body)
        if form.is_valid():
            data=form.cleaned_data #获取验证后的数据
            print(data)
            res=UserInfo.objects.create(**data)    #普通注册到数据库
            if res:
                return JsonResponse({"code":0,"msg":'注册成功'})
        return JsonResponse({"code":1,"msg":str(form._errors)})
    return JsonResponse({"code":1,"msg":'请使用post请求！！！'})


@csrf_exempt
def loginIn(req):
    if req.method=="GET":
        return JsonResponse({"code":1,"msg":'请使用post请求！！！'})
    username=req.POST.get("username","")
    password=req.POST.get("password","")

    #用户验证 验证成功返回user对象 否则返回none
    user= authenticate(req,username=username,password=password)
    print(user,'查找对象')
    if user:
        login(req,user)#记录用户登录状态，参数
        return JsonResponse({
            "code":0,
            "obj":{
                'username':user.username,
                'id':user.id
            },
            "msg":'登录成功'
            })
    return JsonResponse({"code":1,"msg":'登录失败'})