from django.db import models

class Users(models.Model):
    uid = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
