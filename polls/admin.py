from tabnanny import verbose
from django.contrib import admin

from .models import Question, Choice
# Register your models here.

class ChoiceInline(admin.StackedInline):
  model = Choice
  verbose_name_plurar = 'Choices'
  can_delete = False

class QuestionAdmin(admin.ModelAdmin):
  inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)