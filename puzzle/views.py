from multiprocessing import context
from xml.dom.minidom import Element
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.sessions.models import Session
import random

from siteground.settings import SESSION_ENGINE
from .forms import HexForm, SquareForm, SubmitForm, Vertical1
# Create your views here.



def home_view(request):

    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            if form.cleaned_data == {'first_choice': '1'} :
                return redirect(reverse('puzzle:square'))
            else:
                return redirect(reverse('puzzle:hexagon'))
    else:
        form = SubmitForm()
    

    return render(request,'puzzle/index.html',context={'form':form})

def documentation_view(request):
    return render(request,'puzzle/documentation.html')

def congrats_view(request):
    return render(request,'puzzle/congrats.html')

def square_view(request):
    if request.method == 'POST':
        form = SquareForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            horizontal_data = form.cleaned_data['horizontal_rows']
            vertical_data = form.cleaned_data['vertical_rows']
            request.session["horizontal_task"] = horizontal_data
            request.session["vertical_task"] = vertical_data
            
            return redirect(reverse('puzzle:board'))
    else:
        form = SquareForm()
    return render(request,'puzzle/square.html',context={'form':form})

def hexagon_view(request):

    if request.method == 'POST':
        form = HexForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            horizontal_data = form.cleaned_data['horizontal_rows']
            vertical_data = form.cleaned_data['vertical_rows']
            request.session["horizontal_task"] = horizontal_data
            request.session["vertical_task"] = vertical_data
            return redirect(reverse('puzzle:hexboard'))
    else:
        form = HexForm()
    return render(request,'puzzle/hexagon.html',context={'form':form})

def board_view(request):
    horizontal_num = request.session["horizontal_task"]
    vertical_num = request.session["vertical_task"]
    horizontal_list = list(range(horizontal_num))
    vertical_list = list(range(vertical_num))
    if request.method == 'POST':
        form1 = Vertical1(request.POST)
        if form1.is_valid():
            print(form1.cleaned_data)
            return redirect(reverse('puzzle:congrats'))
    else:
        form1 = Vertical1()
    return render(request,'puzzle/board.html',context={'form1':form1,'horizontal_list':horizontal_list,'vertical_list':vertical_list})

def hexboard_view(request):
    horizontal_num = (request.session["horizontal_task"] -1) // 2
    vertical_num = request.session["vertical_task"]
    horizontal_list = list(range(horizontal_num))
    vertical_list = list(range(vertical_num))
    vertical_list_hex = list(range(vertical_num - horizontal_num))
    vertical_list_hex.append(1)
    x = horizontal_num
    y = vertical_num - horizontal_num
    my_list = {}
    for i in range(1, x + 1):
        my_list[i] = list(range(y))
        y += 1

    if request.method == 'POST':
        form = Vertical1(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = Vertical1()
    return render(request,'puzzle/hexboard.html',context={'form':form,'horizontal_list':horizontal_list,'vertical_list':vertical_list,'vertical_list_hex':vertical_list_hex,'my_list':my_list})