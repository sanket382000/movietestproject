from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200)
    poster = models.ImageField(upload_to='movieimages')
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# CRUD OPERATION MODEL

class student(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    age = models.IntegerField()
    courses = models.CharField(max_length=200,null=True,blank=True)
    city = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return '{}{}{}'.format(self.name, self.age, self.city)

class Slides(models.Model):
    name = models.CharField(max_length=255)
    image= models.ImageField(upload_to="images")

    def _str_(self):
        return self.name

