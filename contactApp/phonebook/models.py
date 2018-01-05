from django.db import models

class People(models.Model):
    firstName = models.CharField(max_length = 20)
    secondName = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.firstName + ' ' + self.secondName

class Address(models.Model):
    Number = models.IntegerField()
    email = models.CharField(max_length = 40)
    people = models.ForeignKey(People)
    
    def __str__(self):
        return self.Number + 'and ' + self.email
