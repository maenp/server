# 1.创建项目
django-admin startproject [project_name]

server # 项目的根目录
- manage.py  # 项目的管理文件 【不用动】
- server     
    - __init__.py   # 项目的初始化文件
    - settings.py   # 项目的配置文件
    - urls.py       # 项目的URL声明 url和函数的对应关系    【经常操作】
    - asgi.py       # ASGI是ASGI是异步服务器网关接口【异步】【不用动】
    - wsgi.py       # WSGI是Web服务器网关接口      【同步】【不用动】



# 2.创建App
python manage.py startapp [app_name]

app1 # 应用的根目录
- migrations        # 数据库迁移文件      【不用动】
- __init__.py       # 应用的初始化文件
- admin.py          # 应用的后台管理文件   【不用动】
- apps.py           # 应用的配置文件      【不用动】
- tests.py          # 应用的测试文件      【不用动】
- models.py         # 应用的模型文件      【经常操作】
- views.py          # 应用的视图文件      【经常操作】


# 3.快速开始
- 注册应用
    - server/settings.py
        - INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',

            'app1.apps.App1Config', # 注册应用
        ]
- 编写url和视图函数对应的关系
    - server/urls.py
        - from django.contrib import admin
        - from django.urls import path,include
        - urlpatterns = [
            path('admin/', admin.site.urls),
            path('app1/', include('app1.urls')), # 注册应用的url
        ]
    - app1/urls.py
        - from django.urls import path
        - from . import views
        - urlpatterns = [
            path('index/', views.index), # 注册url和视图函数的对应关系
        ]
- 编写视图函数
    - app1/views.py
        - from django.shortcuts import render
        - from django.http import HttpResponse
        - def index(request):
            - return HttpResponse('Hello World!')

- 启动项目
    - python manage.py runserver [port:默认8000]
    - http://localhost:8000/index

# 4.templates 模板
- 作用：将数据和html页面进行分离
- 使用：
    - 在应用的根目录下创建templates文件夹
    - 在templates文件夹下创建html文件
    - 在视图函数中使用render函数渲染html页面
        - render(request, 'index.html', {'name': 'zhangsan'})
    - 在html页面中使用{{ name }}获取数据

# 5.静态文件
- 作用：存放css、js、img等静态文件
- 使用：
    - 在应用的根目录下创建static文件夹
    - 在static文件夹下创建css、js、img等文件夹
    - 在html页面中使用{% load static %}加载静态文件
    - 在html页面中使用{% static 'css/index.css' %}获取静态文件
    - 图片：
        - <img src="{% static 'img/1.jpg' %}" alt="">
        无法显示图片：
            - 在settings.py中配置STATICFILES_DIRS
                - STATICFILES_DIRS = [
                    os.path.join(BASE_DIR, 'static'),
                ]
            - 在html页面中使用{% static 'img/1.jpg' %}获取静态文件

# 6.请求和响应
- 请求：
    - request.GET # 获取get请求的参数
    - request.POST # 获取post请求的参数
    - request.method # 获取请求的方式
    - request.path # 获取请求的路径
    - request.get_full_path() # 获取请求的完整路径
    - request.META # 获取请求的元数据
    - request.COOKIES # 获取请求的cookie
    - request.session # 获取请求的session
- 响应：
    - HttpResponse('Hello World!') # 返回字符串
    - render(request, 'index.html', {'name': 'zhangsan'}) # 返回html页面
    - HttpResponseRedirect('/index/') # 重定向
    - JsonResponse({'name': 'zhangsan'}) # 返回json数据
    - FileResponse(open('1.jpg', 'rb')) # 返回文件
    - StreamingHttpResponse(open('1.jpg', 'rb')) # 返回流文件