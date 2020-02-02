from django.contrib import admin
from videos import models

class MovieAdmin(admin.ModelAdmin):
    fields = ['release_year', 'title', 'length']
    search_fields = ['title', 'length']
    list_filter = ['release_year', 'title']
    list_display = ['title', 'release_year', 'length']

admin.site.register(models.Customer)
admin.site.register(models.Movie, MovieAdmin)