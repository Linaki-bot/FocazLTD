
from django.contrib import admin
from django.urls import path,include
from FocazLTDapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
]
