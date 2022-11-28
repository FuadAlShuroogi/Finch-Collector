from django.shortcuts import render
from django.http import HttpResponse
from .models import Finch
from django.views.generic.edit import CreateView,UpdateView,DeleteView

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
        finches = Finch.objects.all()
        return render(request, 'finches/index.html', { 'finches':finches })

def finches_show(request, finch_id):
        finch = Finch.objects.get(id=finch_id)
        return render(request, 'finches/show.html', {'finch': finch})
      
class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'
  success_url = '/finches'
  
class FinchUpdate(UpdateView):
  model = Finch
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = '__all__'
  success_url = '/finches'


class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches/'
  