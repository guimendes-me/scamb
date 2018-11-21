from django.shortcuts import render, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.contrib.auth import logout
from django.contrib.auth.models import User




# Create your views here.
def home(request):
    return render(request,'home.html')

def logout_view(request):

    logout(request)
    return redirect('home')



