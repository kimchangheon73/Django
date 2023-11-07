from django.contrib import admin
from pybo.models import *

class QuestionSearch(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionSearch)
