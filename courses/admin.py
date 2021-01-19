from django.contrib import admin
from courses.models import Course,Tag,Prerequisite,Learning
from courses.models import Video,UserCourse,Payment


# Register your models here.
class TagAdmin(admin.TabularInline):
    model = Tag

class VideoAdmin(admin.TabularInline):
    model = Video

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite


class LearningAdmin(admin.TabularInline):
    model = Learning

class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin,PrerequisiteAdmin,LearningAdmin,VideoAdmin]



admin.site.register(Course,CourseAdmin)
admin.site.register(Video)
admin.site.register(UserCourse)
admin.site.register(Payment)



