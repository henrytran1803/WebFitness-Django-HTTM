from urllib import request

from django.shortcuts import render
from .models import Bodymeasurements, UserPred, AuthUser
# Create your views here.


def index(request):
    islog = request.session.get('is_logged_in')
    username = request.session.get('username')
    context = {'is_logged_in': islog, 'username': username}
    return render(request, 'html/index.html', context)


from django.http import HttpResponse
from django.shortcuts import render, redirect


def user(request):
    islog = request.session.get('is_logged_in')
    fistname = request.session.get('first_name')
    lastname = request.session.get('last_name')
    user_id = request.session.get('user_id')

    if user_id is not None:
        user = AuthUser.objects.filter(id=user_id).first()

        if user is not None:
            username = user.username
        else:
            username = None  # Handle the case where the user with the specified ID is not found

        lastBodymeasurements = Bodymeasurements.objects.filter(userid=user_id).order_by('measurementdate').first()

        if lastBodymeasurements is not None:
            lastBodyUserPred = UserPred.objects.filter(body=lastBodymeasurements.id).order_by('date').first()
        else:
            lastBodyUserPred = None  # Handle the case where lastBodymeasurements is None
    else:
        # Handle the case where user_id is None
        username = None
        lastBodyUserPred = None
        lastBodymeasurements = None

    if request.method == 'POST':
        new_username = request.POST.get('inputUsername')
        new_firstname = request.POST.get('inputFirstName')
        new_lastname = request.POST.get('inputLastName')
        new_email = request.POST.get('inputEmailAddress')

        if (
                user_id is not None and new_username != username or new_firstname != fistname or new_lastname != lastname or new_email != user.email):
            user.username = new_username
            user.first_name = new_firstname
            user.last_name = new_lastname
            user.email = new_email
            user.save()

        username = new_username
        fistname = new_firstname
        lastname = new_lastname
        request.session['first_name'] = new_firstname
        request.session['last_name'] = new_lastname
        request.session['username'] = new_username

    context = {
        'is_logged_in': islog,
        'username': username,
        'first_name': fistname,
        'last_name': lastname,
        'bdf': round(lastBodyUserPred.bdf, 2) if lastBodyUserPred else None,
        'tdee': lastBodyUserPred.tdee if lastBodyUserPred else None,
        'email': user.email if user else None,
        'lastBodymeasurements': lastBodymeasurements,
    }
    return render(request, 'html/user_information.html', context)
