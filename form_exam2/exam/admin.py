from django.contrib import admin

from exam import models

# Register your models here.

admin.site.register(models.Code)
admin.site.register(models.User)
admin.site.register(models.InterestLanguage)

