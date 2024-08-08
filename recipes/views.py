from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import RecipeModel
from .forms import RecipeForm
# Create your views here.
def home(req):
  data = RecipeModel.objects.all()
  context= {
    "data": data
  }
  return render(req, 'index.html', context=context)

def form_add(req):
  form = RecipeForm()
  return render(req, 'add_recipe.html', context={'form': form})
def add(req):
  if req.method == "POST":
    form = RecipeForm(req.POST, req.FILES)
    if form.is_valid:
      item = form.save()
      return redirect('/')
    else:
      print(form.errors)