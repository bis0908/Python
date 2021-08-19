from django.contrib import admin
from .models import Question, Answer

# Register your models here.

# admin.site.register(Question)
# admin.site.register(Answer)

class Search_subject_Admin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, Search_subject_Admin)
admin.site.register(Answer, Search_subject_Admin)