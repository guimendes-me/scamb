from django.urls import path
from .views import mylist, listing, showtrade
from .views import new_trade
from .views import edit_trade
from .views import delete_trade

urlpatterns = [
    path('list/<int:id>/', showtrade, name='showtrade'),
    path('trades/', listing, name='trades'),
    path('mylist/', mylist,name='mylist'),
    path('new/',new_trade, name='new_trade'),
    path('update/<int:id>/',edit_trade, name= 'edit_trade'),
    path('delete/<int:id>/',delete_trade, name= 'delete_trade')
]