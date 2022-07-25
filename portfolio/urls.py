from django.contrib import admin
from django.urls import path
import portfolio_back
from portfolio_back import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
