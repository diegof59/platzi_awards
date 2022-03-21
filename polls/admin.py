from tabnanny import verbose
from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
  model = Choice
  verbose_name_plurar = 'Choices'
  extra = 0

class QuestionAdmin(admin.ModelAdmin):
  inlines = [ChoiceInline]
  list_display = ["statement", "publication_date"]  
  list_filter = ["publication_date"]
  search_fields = ["statement"]

admin.site.register(Question, QuestionAdmin)