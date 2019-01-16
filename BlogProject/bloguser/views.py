from django.shortcuts import render,redirect,HttpResponse
from .models import UserInfo
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
import gvcode


def home(request):
    return render(request,'user/index.html')

def get_code(request):
    # """
    # 返回一个base64编码的随机验证码
    # """
    base64_code,str_code = gvcode.base64()
    request.session['verify_code'] = str_code      ###!!!!!!!!!!!!!!!
    # return  render(request,'user/login.html',{'base64_code':base64_code})
    return HttpResponse(base64_code)

def myinfo(request):
    user = request.user
    return render(request,'user/myinfo.html',{'user':user})

def updateinfo(request):
    if request.method =='GET':
        user = request.user
        return render(request, 'user/updateinfo.html', {'user': user})
    elif request.method == 'POST':
        user = request.user
        data = request.POST
        user.email = data.get('email')
        user.age = data.get('age')
        user.phone = data.get('phone')
        user.save()
        return redirect(myinfo)

def updatepasswd(request):
    if request.method == 'GET':
        return render(request,'user/updatepasswd.html')
    elif request.method == 'POST':
        error={}
        oldpassword = request.POST.get('oldpassword')
        newpassword = request.POST.get('newpassword')
        newpassword2 = request.POST.get('newpassword2')
        user = request.user
        if not check_password(oldpassword,user.password):
            error['password'] = '旧密码不正确!'
        elif len(newpassword) == 0:
            error['password2'] = '密码不能为空!'
        elif newpassword != newpassword2:
            error['password3'] = '两次新密码输入不一致!'
        if not error:
            user.password = make_password(newpassword)
            user.save()
            logout(request)
            return render(request,'user/login.html',{'msg':'修改成功!'})
        else:
            return render(request,'user/updatepasswd.html',error)



def user_login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        error = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = UserInfo.objects.filter(username=username).first()
        if not user:
            error['username'] = '用户名不存在!'
        # if user is not None:
        #     error['username']='用户名不能为空!'
        elif not check_password(password, user.password):
            error['password'] = '密码输入错误!'

        if not error:
            login(request,user)
            return redirect('/myblog/index/')
        else:
            return render(request, 'user/login.html', error)

def register(request):
    error = {}
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        data = request.POST
        username = data.get('username')
        name = data.get('name')
        password = data.get('password')
        password2 = data.get('password2')
        email = data.get('email')
        age = data.get('age', 18)
        phone = data.get('phone')

        data = request.POST.get('verify_code')
        str_code = request.session.get('verify_code')

        user = UserInfo.objects.filter(username=username).first()
        if user is not None:
            error['username'] = '用户名已存在！！！'
        if not username:
            error['username'] = '用户名不能为空！！！'
        if password != password2:
            error['password'] = '两次密码输入不一致！！！'
        if str_code != data:
            error['code'] = '验证码输入错误!'
        if not error:
            user = UserInfo()
            user.username = username
            user.name = name
            user.password = make_password(password)
            user.email=email
            user.age = age
            user.phone=phone
            user.save()
            return render(request,'user/login.html',{'msg':'注册成功!'})
        # User.objects.create()
        else:
            # return HttpResponse(str(error))
            return render(request, 'user/register.html', error)


def user_logout(request):
    logout(request)
    return redirect(user_login)


