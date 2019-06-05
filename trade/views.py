from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Trade, Profile
from .forms import TradeForm
import requests
# Create your views here.



def listing(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    trade_list = Trade.objects.all()
    paginator = Paginator(trade_list, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    trades = paginator.get_page(page)
    return render(request, 'list.html', {'trades': trades, 'user': user, 'profile': profile})


def showtrade(request, id):
    user = request.user
    profile = Profile.objects.get(user=user)

    trade = get_object_or_404(Trade, pk=id)
    scamber = Profile.objects.get(id=trade.fk_profile.id)
    user = User.objects.get(id=scamber.user.id)

    return render(request, 'showtrade.html', {'trade': trade, 'user': user, 'scamber': scamber, 'profile': profile})


@login_required()
def mylist(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    trade = Trade.objects.filter(fk_profile=user.pk)

    if request.user.is_superuser:
        trade = Trade.objects.all()

    return render(request,'mylist.html', {'trade': trade, 'user': user, 'profile': profile})


@login_required()
def new_trade(request):       

    user = request.user
    profile = Profile.objects.get(user=user)
    form_trade = TradeForm(request.POST or None, request.FILES or None, initial={'fk_profile': profile})

    if form_trade.is_valid():

        form_trade.save()

        return redirect('mylist')

    return render(request, 'newtrade.html', {'form_trade': form_trade, 'user': user, 'profile': profile})


@login_required()
def boowl(request):

    #https://www.googleapis.com/books/v1/volumes?q=assassins+creed
    #user = {}
    #if 'username' in request.GET:
    #    username = request.GET['totalItems']
    #    url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:%s' % username
    #    response = requests.get(url)
    #    user = response.json() **/
    user = request.user
    profile = Profile.objects.get(user=user)
    
    if 'keyword' in request.GET:
        book = {}
        keyword = request.GET["keyword"]
        keyword = keyword.replace(' ', '+')
        url = 'https://www.googleapis.com/books/v1/volumes?q=:%s' % keyword
        response = requests.get(url)
        search = response.json()

        items = search["totalItems"]

        if items > 0:
            items = search["totalItems"]
            book = search["items"]
            #book = search["items"][0]["volumeInfo"]
            #authors = search["items"][0]["volumeInfo"]["authors"][0]
            
    else:
        items = 0
        book ='Digite um Valor'
        authors='Digite um Valor'
        pass

    return render(request, 'boowl.html', {'items': items, 'book': book, 'user': user, 'profile': profile})

@login_required()
def edit_trade(request, id):
    trade = get_object_or_404(Trade, pk=id)

    user = request.user
    profile = Profile.objects.get(user=user)

    if trade.fk_profile.id != request.user.id:
        return redirect('mylist')

    form = TradeForm(request.POST or None, request.FILES or None, instance=trade)

    if form.is_valid():
        form.save()
        return redirect('mylist')

    return render(request, 'newtrade.html', {'form_trade': form, 'user': user, 'profile': profile})


@login_required()
def delete_trade(request, id):
    
    user = request.user
    profile = Profile.objects.get(user=user)

    trade = get_object_or_404(Trade, pk=id)
    form = TradeForm(request.POST or None, request.FILES or None, instance=trade)

    if request.method=='POST':
        trade.delete()
        return redirect('mylist')

    return render(request,'deleteconfirm.html', {'trade': trade, 'user': user, 'profile': profile})