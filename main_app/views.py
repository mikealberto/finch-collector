from django.shortcuts import render, redirect
#a python class that exist in Django
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Toy
from .forms import FeedingForm 

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
    # To get the toys that the finch does not have.
    #First, create a list of toy ids that the finch does have
    id_list = finch.toys.all().values_list("id")
    #Querying for toys whos ids are not in the list using exclude
    toys_finch_doesnt_have = Toy.objects.exclude(id__in=id_list)
    #not passing anything therefore it creates an empty form
    feeding_form = FeedingForm()
    return render(
        request, 
        "finches/detail.html", 
        {
            "finch": finch, 
            "feeding_form": feeding_form,
            "toys": toys_finch_doesnt_have #List of toys
        }
    )

#it will inherit from the CreateView Class
class FinchCreate(CreateView):
    model = Finch
    #So that form has input for the field in our models"
    fields = ["name", "species", "description", "age"]

class FinchUpdate(UpdateView):
    model = Finch
    #disallow renaming the species of a bird
    fields = ["name", "description", "age"]

class FinchDelete(DeleteView):
    model = Finch
    #can't use get method since there is no id available after you delete a bird 
    success_url = "/finches/"

def add_feeding(request, finch_id):
    #creating a feeding form instance with a post request
    #passing data from our detail form 
    form = FeedingForm(request.POST)
    if form.is_valid():
        #form.save will return a new instance of the feeding
        #commit=False prevents it from being saved in the database, it remains in memory

        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect("detail", finch_id=finch_id)

def assoc_toy(request, finch_id, toy_id):
    # You can pass a toy's id instead of the whole toy object
    Finch.objects.get(id=finch_id).toys.add(toy_id)
    return redirect("detail", finch_id=finch_id)

class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy

class ToyCreate(CreateView):
    model = Toy
    fields = "__all__"

class ToyUpdate(UpdateView):
    model = Toy
    fields = ["name", "color"]

class ToyDelete(DeleteView):
    model = Toy
    success_url = "/toys/"