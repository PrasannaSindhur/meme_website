from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from user_navigation.forms import UserDetailsForm
from .library import *
import requests, time


def index(request):
    isValidUser, username = authenticate_user(request)
    if isValidUser:
        request.session['username'] = username
        request.session['time'] = time.time()
        return render(request, 'cookie_popup.html', {'logged_in': True})
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        isValidUser, username = authenticate_user(request)
        if isValidUser:
            request.session['username'] = username
            request.session['time'] = time.time()
            return render(request, 'cookie_popup.html')
        else:
            if username is not None:
                messages.error(request, "Incorrect Password")
            else:
                messages.error(request, "User not Registered")
    return render(request, 'login.html')


def register(request):
    user_details = UserDetailsForm()
    return render(request, 'register.html', {'form': user_details})


def complete_registration(request):
    if request.method == 'POST':
        user_details_form = UserDetailsForm(request.POST)
        if user_details_form.is_valid():
            userdetails = user_details_form.save(commit=False)
            userdetails.password = make_password(userdetails.password)
            userdetails.confirm_password = make_password(userdetails.confirm_password)
            userdetails.save()
            request.session['username'] = userdetails.first_name
            return render(request, 'cookie_popup.html', {'logged_in': True})
    return render(request, 'register.html', {'form': user_details_form})



def display_meme(request):
    if 'username' not in request.session:
        return redirect('login')
    update_consent(request.session['username'])
    api_data = requests.get('https://api.imgflip.com/get_memes')
    if api_data.status_code == 200:
        memes_list = api_data.json().get("data").get("memes")
    memes_paginator = Paginator(memes_list, 5)

    page_number = request.GET.get('page')
    if page_number is None:
        page_number = 1
    meme_page = memes_paginator.get_page(int(page_number))
    messages.info(request, "Cookie : %s" % (request.COOKIES['last_visit']))
    return render(request, 'memes.html', {'logged_in': True, 'memes': meme_page})


def logout(request, username, flag):
    message = "Succesfully Logged Out"
    alert = {'alert_flag': "loggedout", 'message': message}
    if 'username' in request.session.keys():
        del request.session['username']
    if flag != 1:
        message = "Sorry %s, Couldn't display memes since cookies were not accepted" %(username)
        alert = {'alert_flag': "danger", 'message': message}
    return render(request, 'msg_box.html', alert)


def update_consent(username):
    user_details = UserDetails.objects.get(first_name=username)
    user_details.consent = 1
    user_details.save()

