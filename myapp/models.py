from django.db import models
from django.contrib.auth.models import User

class terminals(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Number = models.IntegerField()

    def __str__(self):
        return self.Name

class counter(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Terminal = models.CharField(max_length=100)

    def __str__(self):
        return self.Name


class Bus(models.Model):
    terminal = models.CharField(max_length=30, default = None)
    bus_name = models.CharField(max_length=30)
    coach_number = models.IntegerField()
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    rem = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
    arrival_time = models.TimeField()

    def __str__(self):
        return self.bus_name


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, default= 'username')
    type = models.CharField(max_length=10, default='None')

    def __str__(self):
        return self.name


class Book(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid =models.DecimalField(decimal_places=0, max_digits=2)
    busid=models.DecimalField(decimal_places=0, max_digits=2)
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=10, default='No')

    def __str__(self):
        return self.email
