from urllib import request

from django.shortcuts import render

# Create your views here.
def login(request):
    signupcontext = "none"
    logincontext = "block"
    context = {"login":logincontext, "signup":signupcontext}
    return  render(request, "../templates/login.html",context)
