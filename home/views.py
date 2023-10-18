from urllib import request

from django.shortcuts import render

# Create your views here.


def index(request):
    islog = request.session.get('is_logged_in')
    username = request.session.get('username')
    context = {'is_logged_in': islog, 'username': username}
    return render(request, 'html/index.html', context)


def user(request):
    islog = request.session.get('is_logged_in')
    username = request.session.get('username')
    fistname = request.session.get('first_name')
    lastname = request.session.get('last_name')
    context = {'is_logged_in': islog, 'username': username,'first_name': fistname,'last_name': lastname}
    print(islog,username)
    return render(request, 'html/user_information.html',context)  # Trả về trang chủ mặc định