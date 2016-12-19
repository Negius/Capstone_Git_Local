from django.contrib import admin

from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 1
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question is :',               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine] # add them choice vao viec hien thi question 
    list_display = ('question_text', 'pub_date', 'was_published_recently') # thu tu hien thi trong question
    list_filter = ['pub_date'] # bo loc
    
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)