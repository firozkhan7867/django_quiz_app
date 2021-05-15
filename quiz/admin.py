from django.contrib import admin
from .models import Question,Quiz,History
# Register your models here.

admin.site.register([Question,Quiz,History])