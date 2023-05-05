from django.http import JsonResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
#  
def index(request):
    return HttpResponse('hello world')

# 渲染模板
def user_list(request):
    return render(
        request, 
        # 模板名字 在templates目录下 
        # 会在所有的app下面去找 优先在当前应用下寻找 
        'user_list.html', 
        # 传递的参数 
        {'users':[{'name':'jack','pwd':'abc'},{'name':'tom','pwd':'123'}]}
    )

# 请求
def something(request):
    # request是请求对象，包含请求信息
    # request.method 请求方法
    # request.GET 请求参数
    # request.POST 请求参数
    print(request.method)
    print(request.GET)
    # 返回json数据
    return JsonResponse({'name': 'zhangsan'})
    return HttpResponse('something')