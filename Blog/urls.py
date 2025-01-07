from django.urls import path
from .views import *


urlpatterns = [
    path('home/',home_page,name='home_page'),
    path('addblog/',add_blog,name='add_blog'),
    path('profile/<int:id>/',profile,name='profile'),
    path('fullblog/<int:id>/',full_blog, name='fullblog'),
    path('delete/<int:id>/', delete_blog, name='delete_blog'),

]