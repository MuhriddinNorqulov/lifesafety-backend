from django.contrib import admin
from .models import *
from exams.models import *


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


# class ResultAdmin(admin.ModelAdmin):
#     model = Result
#     list_display = ["first_name", 'last_name', 'group', "task1", "task2", "task3", "task4", "task5", "task6",
#                     "task7", 'total']
#
#     def group(self, obj):
#         return obj.student.group.name
#
#     def first_name(self, obj):
#         return obj.student.first_name
#
#     def last_name(self, obj):
#         return obj.student.last_name
#
#     def group(self, obj):
#         return obj.student.group.name
#
#     def task1(self, obj):
#         exam_items_all = ExamItem.objects.filter(group=obj.student.group)
#         student_result = StudentResult.objects.filter(exam_item=exam_items_all[0])
#         if len(student_result) == 0:
#             return 0
#         return min([i.ball for i in student_result])
#
#     def task2(self, obj):
#         exam_items_all = ExamItem.objects.filter(group=obj.student.group)
#         student_result = StudentResult.objects.filter(exam_item=exam_items_all[1])
#         return student_result.ball
#
#     def task3(self, obj):
#         exam_items_all = ExamItem.objects.filter(group=obj.student.group)
#         student_result = StudentResult.objects.filter(exam_item=exam_items_all[2])
#         return student_result.ball
#
#     def task4(self, obj):
#         exam_items_all = ExamItem.objects.filter(group=obj.student.group)
#         student_result = StudentResult.objects.filter(exam_item=exam_items_all[3])
#         return student_result.ball
#
#     def task5(self, obj):
#         exam_items_all = ExamItem.objects.filter(group=obj.student.group)
#         student_result = StudentResult.objects.filter(exam_item=exam_items_all[4])
#         return student_result.ball
#
#     def task6(self, obj):
#         exam_items_all = ExamItem.objects.filter(group=obj.student.group)
#         student_result = StudentResult.objects.filter(exam_item=exam_items_all[5])
#         return student_result.ball
#
#     def task7(self, obj):
#         exam_items_all = ExamItem.objects.filter(group=obj.student.group)
#
#         student_result = StudentResult.objects.filter(exam_item=exam_items_all[6])
#         return student_result.ball
#
#     def total(self, obj):
#         exam_items_all = ExamItem.objects.filter(group=obj.student.group)
#         total = 0
#         for i in range(0, 6):
#             total += StudentResult.objects.filter(exam_item=exam_items_all[6]).ball
#         return total
#
#
# admin.site.register(Result, ResultAdmin)