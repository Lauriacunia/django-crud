from django.db import models

# Create your models here.
class adress(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}"


class User(models.Model): # extends models.Model
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    adress = models.ForeignKey(adress, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} {self.lastname} {self.email} {self.adress}"
