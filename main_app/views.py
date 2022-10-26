from django.shortcuts import render
from django.http import HttpResponse

# dummy data
class Finch:
    def __init__(self, name, species, description, age):
        self.name = name
        self.species = species
        self.description = description
        self.age = age

finches = [
    Finch("Beak", "House", "Well Studied", 4),
    Finch("Claw", "Cassin", "Long Head", 7),
    Finch("Chippy", "Cassia Crossbill", "Doesn't Migrate", 2),
    Finch("Falcon", "Shaft-tail", "Found in abudance", 0),
]


def home(request):
    return HttpResponse("<h1>Hello Finch</h1>")

def about(request):
    return render(request, "about.html")

def finches_index(request):
    return render(request, "finches/index.html", {"finches": finches})
