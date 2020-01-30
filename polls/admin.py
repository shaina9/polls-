from django.contrib import admin

# Register your models here.
from.models import Question,Choice
class QuestionAdmin(admin.ModelAdmin):

    list_display = ('question_text', 'pub_date')
admin.site.register(Question,QuestionAdmin)

class ChoiceAdmin(admin.ModelAdmin):

    list_display = ('question', 'choice_text','votes')

admin.site.register(Choice,ChoiceAdmin)
