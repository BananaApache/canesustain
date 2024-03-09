from django.contrib import admin



# Register your models here.
from . import models

admin.site.register(models.UserDataModel)
admin.site.register(models.UserBlogModel)