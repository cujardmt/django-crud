from django.db import models   
    
class Traveler(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=200)
    country = models.CharField(max_length=125)
    
    travel_date = models.DateField(null=True);
    return_date = models.DateField(null=True);
    country_destination = models.CharField(max_length=125, null=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
