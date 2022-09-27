from django.contrib import admin
from .models import Question, Choice

# class PBMConsentAdmin(admin.ModelAdmin):
#     list_display =('question_number', 'question_text')

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question')

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice, ChoiceAdmin)
