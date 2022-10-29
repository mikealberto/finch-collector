from django.db import models
from django.urls import reverse

#2nd value is what django uses for forms 
MEALS = (
    ("B", "Breakfast"),
    ("L", "Lunch"),
    ("D", "Dinner")
)

# Create your models here.
class Finch(models.Model): 
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100) 
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    #gets invoked by CBV
    def get_absolute_url(self): 
        return reverse("detail", kwargs = {"finch_id": self.id})

#inherit models.Model otherwise it is a python class and not a django model
class Feeding (models.Model): 
    date = models.DateField()
    meal = models.CharField(
        max_length=1,
        # choices field option
        # choices is built into django
        choices=MEALS,
        #default value for meal is "B"
        default=MEALS[0][0]
    )
    # create a finch_id FK
    #on delete when a Finch record is deleted it will make sure that there are no orphan record 
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        #method for obtaining value of Field.choice
        #django creates this method out of which object attribute has choice
        #returns the 2nd values of meals tuple
        return f"{self.get_meal_display()} on {self.date}"