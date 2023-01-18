from django.db import models
from regionSelection import models as regionModel
#from location_field.models.spatial import LocationField

class user(models.Model):
        genderChoices = [
                ('M', "مرد"),
                ('F', "زن"),
        ]
        name = models.CharField(max_length=200, help_text="Users name")
        lastName = models.CharField(max_length=200,  help_text="Users lastname")
        meliCode = models.IntegerField(help_text="Users meli code(unique) ", primary_key=True, unique=True)
        gender = models.CharField(max_length=200, choices=genderChoices)
        phoneNumber1 = models.IntegerField(help_text="Users phone number(required)")
        phoneNumber2 = models.IntegerField(help_text="Users phone number(not required) for social purposes", blank=True)
        homeNumber1 = models.IntegerField(help_text="Users home number", blank=True)
        homeNumber1 = models.IntegerField(help_text="Users home number", blank=True)
        region = models.ManyToManyField(regionModel.region)
        #location = LocationField()

        def __str__(self) -> str:
                return f"{self.name} {self.lastName}"
