from django.urls import path
from .views import *

urlpatterns = [
    path('', reder_index, name="render"),
    path('save/inventory', save_inventory, name="saveinventory"),
    path('about/', about, name="about"),
   # path('delete-todo/<int:id>/', deleteTodo, name="deleteTodo"),
   # path('login/', login, name="login"),
   # path('register/', register, name="register"),
   # path('logout/', logout, name="logout"),
]