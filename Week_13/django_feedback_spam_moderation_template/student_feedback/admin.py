from django.contrib import admin
from .models import Feedback

# TODO create a filter to only display approved feedback 

admin.site.register(Feedback)
