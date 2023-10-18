from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import AuthUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import login



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create_user(username=username, password=password, email=email)

        # You can set other attributes if needed, for example:
        user.first_name = "First Name"
        user.last_name = "Last Name"
        user.is_superuser = False  # Set as needed
        user.is_staff = False  # Set as needed

        # Save the user
        user.save()
        # Đăng nhập người dùng sau khi tạo
        login(request, user)
        request.session['is_logged_in'] = True
        user_name = user.first_name + ' ' + user.last_name
        request.session['first_name'] = user.first_name
        request.session['last_name'] = user.last_name
        request.session['username'] = user_name
        print(user_name)
        user_id = request.user.id
        request.session['user_id'] = user_id
        return redirect('index')

    return render(request, "../templates/signup.html")