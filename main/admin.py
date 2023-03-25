from django.contrib import admin
from .models import *
# Register your models here.


class ResourceInlineAdmin(admin.TabularInline):
    model = Resource
    list_display = ["title", "url", "image"]


class QuestionInlineAdmin(admin.TabularInline):
    model = ControlQuestion
    list_display = ["question"]


class LectureAdmin(admin.ModelAdmin):
    model = Lecture
    inlines = [QuestionInlineAdmin, ResourceInlineAdmin]


admin.site.register(Lecture, LectureAdmin)