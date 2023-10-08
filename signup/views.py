from django.shortcuts import render

# Create your views here.
def signup(request):
    signupcontext = "block"
    logincontext = "none"
    context = {"login":logincontext, "signup":signupcontext}
    return  render(request, "../templates/signup.html",context)