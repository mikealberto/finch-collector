from django.shortcuts import render
#a python class that exist in Django
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch

# dummy data
##### Delete #####
# class Finch:
#     def __init__(self, name, species, description, age):
#         self.name = name
#         self.species = species
#         self.description = description
#         self.age = age
###############

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, "finches/index.html", {"finches": finches})

#anticipating an incoming argument
def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, "finches/detail.html", {"finch": finch})

#it will inherit from the CreateView Class
class FinchCreate(CreateView):
    model = Finch
    fields = "__all__" #So that form has input for the field in our models
    # success_url = "/finches/"

class FinchUpdate(UpdateView):
    model = Finch
    #disallow renaming the species of a bird
    fields = ["name", "description", "age"]

class FinchDelete(DeleteView):
    model = Finch
    #can't use get method since there is no id available after you delete a bird 
    success_url = "/finches/"