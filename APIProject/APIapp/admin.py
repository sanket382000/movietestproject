from django.contrib import admin
from .models import Movie,student
from .models import *

# Register your models here.
admin.site.register(Movie)
admin.site.register(Slides)
admin.site.register(student)
