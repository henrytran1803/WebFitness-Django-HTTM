from urllib import request

from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'html/index.html')  # Trả về trang chủ mặc định

def index(request, username=None, islog=None):
    context = {'is_logged_in': islog, 'username': username}
    return render(request, 'html/index.html', context)

def user(request):

    return render(request, 'html/user_information.html')  # Trả về trang chủ mặc định