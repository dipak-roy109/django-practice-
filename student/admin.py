from django.contrib import admin

# Register your models here.
from . import models

@admin.register(models.Student)
class Studentadmin(admin.ModelAdmin):
    list_display = ['name','roll','department','phone']