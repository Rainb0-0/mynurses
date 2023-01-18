from django.db import models

class country(models.Model):
        countryName = models.CharField(max_length=200, help_text="The country name", unique=True)

        def __str__(self) -> str:
                return self.countryName

class city(models.Model):
        cityName = models.CharField(max_length=200, help_text="The city name", unique=True)
        countryName = models.ManyToManyField(country)
        def __str__(self) -> str:
                print(type(self.countryName.all()))
                return f"{self.cityName} - {self.countryName.all()[0]}"

class region(models.Model):
        regionName = models.CharField(max_length=200, help_text="The region name")
        cityName = models.ManyToManyField(city)
        
        def __str__(self) -> str:
                return f"{self.regionName} - {self.cityName.all()[0]}"
