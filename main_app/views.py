from django.shortcuts import render
from .models import Finch

# dummy data
##### Delete #####
# class Finch:
#     def __init__(self, name, species, description, age):
#         self.name = name
#         self.species = species
#         self.description = description
#         self.age = age

# finches = [
#     Finch("Beak", "House", "Well Studied", 4),
#     Finch("Claw", "Cassin", "Long Head", 7),
# ]
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
