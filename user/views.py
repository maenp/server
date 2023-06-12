import json
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from user.forms import ReqisterForm
from user.models import UserInfo

def resolve(data, params={}): # params = dict(status?, msg?)
    return {
        'data': data,
        'status': params['status'] if params.get('status') else 200,
        'msg': params['msg'] if params.get('msg') else '成功',
        'success': True,
    }

def reject( data, params={}):
    return {
        'data': data,
        'status': params['status'] if params.get('status') else 400,
        'msg': params['msg'] if params.get('msg') else '失败',
        'success': False,
    }

# 退出登录
def logoutIn(req):
    is_login_status=req.user.is_authenticated # 判断用户是否登录
    if not is_login_status:
        return JsonResponse(reject(None, {'msg':'当前状态未登录'}))
    logout(req) # 退出登录
    return JsonResponse(resolve(None, {'msg':'退出登录成功'}))

# 获取当前的登录的用户信息
def current(request):
    is_login_status=request.user.is_authenticated # 判断用户是否登录
    if is_login_status:
        return JsonResponse(resolve({
            'status':is_login_status,
            'username': request.user.username,
            'id': request.user.id,
        }))
    else:
        return JsonResponse(reject(None, {'msg':'请先登录'}))

@csrf_exempt
def register(req):
    if req.method=="POST":
        body = json.loads(req.body)
        form=ReqisterForm(body)
        if form.is_valid():
            data=form.cleaned_data #获取验证后的数据
            print(data)
            # 判断账号是否已经注册过
            if UserInfo.objects.filter(username=data['username']).exists():
                return JsonResponse(reject(None, {'msg':'该账号已经注册过'}))

            # res=UserInfo.objects.create(**data)    #普通注册到数据库
            res=UserInfo.objects.create_user(**data) #使用django自带的用户注册到数据库
            if res:
                return JsonResponse(resolve(None, {'msg':'注册成功'}))
        return JsonResponse(reject(None, {'msg':str(form._errors)}))
    return JsonResponse(reject(None, {'msg':'请使用post请求！！！'}))


@csrf_exempt
def loginIn(req):
    if req.method=="GET":
        return JsonResponse(reject(None, {'msg':'请使用post请求！！！'}))
    
    body = json.loads(req.body)
    username = body.get('username')
    password = body.get('password')

    # authenticate 验证账号密码是否正确 返回用户对象 或者 None
    user= authenticate(req,username=username,password=password)
    # if not user:
    #     # 判断账号密码是否正确
    #     user = UserInfo.objects.filter(username=username, password=password).first()

    if user:
        login(req,user) # 登录 保存用户的登录状态 保存在session中 
        return JsonResponse(resolve({
            'username': user.username,
            'user_id': user.id,
        }, {'msg':'登录成功'}))
    return JsonResponse(reject(None, {'msg':'登录失败！！！'}))