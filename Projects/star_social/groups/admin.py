from django.contrib import admin
from groups import models

class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.regisrter(models.Group)

