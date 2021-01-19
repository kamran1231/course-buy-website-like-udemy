
from django.db import models
from courses.models.course import Course

#Create your models here:

class Video(models.Model):
    title = models.CharField(max_length=100,null=False)
    course = models.ForeignKey(Course,null=False,on_delete=models.CASCADE)
    serial_number = models.IntegerField(null=False)
    video_id = models.CharField(max_length=30,null=False)
    is_preview = models.BooleanField(default=False)

    #visible name in admin
    def __str__(self):
        return self.title
