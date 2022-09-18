from cmath import log
from django.shortcuts import render
from .models import Inventoryoff
from django.http import HttpResponse
import logging

# Create your views here.
def index(request):
  return render(request, 'inventoryapp/index.html')

def reder_index(request):
  return render(request, 'inventoryapp/index.html')

def save_inventory(request):
    name = request.POST.get('name')
    designation = request.POST.get('designation')
    grade = request.POST.get('grade')
    mobile = request.POST.get('mobile')   
    logging.Logger.error("called")
    en=Inventoryoff(name=name, designation=designation, grade=grade, mobile=mobile)
    en.create()

#@login_required
"""""
def deleteTodo(request, id):
    Todo.objects.get(id=id).delete()
    #get_object_or_404(Todo, id=id, user=request.user).delete()
    return redirect('/')
"""""

def about(request):
    return render(request, 'inventoryapp/about.html')
