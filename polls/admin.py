from django.contrib import admin

from .models import (Question,
                     Choice)


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):

    list_display = ('question_text', 'pub_date', 'was_published_recently')

    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)
