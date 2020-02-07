from django.contrib import admin

from exam.models import User, InterestLanguage, Code

# Register your models here.
admin.site.register(User)
admin.site.register(InterestLanguage)
admin.site.register(Code)