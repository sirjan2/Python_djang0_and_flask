from django.contrib import admin
from . import models
class ChoiceInline(admin.StackedInline):
    model = models.Choice
    extra = 2
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fields=['pub_date','question_text']
    inlines=[ChoiceInline]
    list_display=['pub_date','question_text']
    list_editable=['question_text']
    list_filter=['pub_date']
# Changing admin fields.
class ChoiceAdmin(admin.ModelAdmin):
    fields=['votes','question','choice_text']
admin.site.register(models.Question,QuestionAdmin)
admin.site.register(models.Choice,ChoiceAdmin)