#  基础镜像
FROM python:3.11.3

#  镜像作者
LABEL maintainer mep

 #  设置环境变量
ENV PYTHONUNBUFFERED 1

# 设置pip源为国内源
COPY pip.conf /root/.pip/pip.conf

 #  在容器内创建/var/mydjango 文件夹
RUN mkdir -p /var/mydjango                         

# 设置容器内工作目录为 /var/mydjango
WORKDIR /var/mydjango                                

# 将当前目录下所有文件添加至Docker容器内的工作目录中
ADD . /var/mydjango                                      

# 容器中安装pip依赖
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple      

# 对外暴露8000端口
EXPOSE 8000

# 容器启动时执行的命令
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]