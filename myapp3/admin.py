from django.contrib import admin

# Register your models here.
from .models import Book
from .models import Question
from .models import Choice
admin.site.register(Book)
admin.site.register(Question)
admin.site.register(Choice)

