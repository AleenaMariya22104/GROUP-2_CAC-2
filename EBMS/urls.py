
from django.contrib import admin
from django.contrib.auth import login
from django.urls import path

from ADMIN import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name='login'),
    path('',views.signup,name='signup'),

]
