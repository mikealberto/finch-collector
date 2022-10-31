from django.db import models
from django.urls import reverse

#2nd value is what django uses for forms 
MEALS = (
    ("B", "Breakfast"),
    ("L", "Lunch"),
    ("D", "Dinner")
)

#many to many model
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    #used by CBVs to redirect to the toy detail page
    # and pass in a specific toy id
    def get_absolute_url(self):
        return reverse("toys_detail", kwargs = {"pk": self.id})

# Create your models here.
class Finch(models.Model): 
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100) 
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.name

    #gets invoked by CBV
    def get_absolute_url(self): 
        return reverse("detail", kwargs = {"finch_id": self.id})

#inherit models.Model otherwise it is a python class and not a django model
class Feeding (models.Model): 
    date = models.DateField("Feeding Date")
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

    # #for any feeding set it wil make sure to have the dates in descending order 
    class Meta:
        ordering = ['-date']