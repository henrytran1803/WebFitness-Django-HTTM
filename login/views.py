from django.urls import reverse
from urllib import request
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import  AuthUser

from django.contrib.auth import authenticate, login


def login_f(request):
    if request.method == 'POST':
        email = request.POST.get('login-email')
        password = request.POST.get('login-password')
        print(email,password)
        user = authenticate(request, username=email, password=password)
        print(user)
        if user is not None:
            login(request, user)  # Đăng nhập người dùng
            request.session['is_logged_in'] = True
            user_name = user.first_name + ' ' + user.last_name
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            request.session['username'] = user_name

            user_id = request.user.id
            print(user_id)
            request.session['user_id'] = user_id
            return HttpResponseRedirect(reverse('index'))

        else:
            return render(request, 'login.html', {'error_message': 'Tên người dùng hoặc mật khẩu không đúng.'})
    else:
        return render(request, 'login.html')



def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('index'))


