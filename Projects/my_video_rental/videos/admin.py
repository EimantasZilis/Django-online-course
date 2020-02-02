from django.contrib import admin
from videos import models

admin.site.register(models.Customer)
admin.site.register(models.Movie)