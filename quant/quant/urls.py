from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('',views.index),
    path('search/',views.search,name='search'),
    path('stock/',views.stock),
    path('etf/',views.etf),
    path('news/',views.news),
    path('news/cnn/',views.cnn_news),
    path('news/bbc/',views.bbc_news),
    path('news/yahoo/',views.yahoo_news),
    path('admin/', admin.site.urls),
]