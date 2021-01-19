from django.db import models


#Create your models here:
class Course(models.Model):
    name = models.CharField(max_length=50,null=False)
    slug = models.CharField(max_length=50,null=False,unique=True)
    description = models.CharField(max_length=200,null=True)
    price = models.IntegerField(null=False)
    discount = models.IntegerField(default=0)
    active = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to='files/thumbnail')
    date = models.DateTimeField(auto_now_add=True)
    resource = models.FileField(upload_to='files/resource')
    length = models.IntegerField(null=False)

    #visible name in admin
    def __str__(self):
        return self.name


class CourseProperty(models.Model):
    description = models.CharField(max_length=30, null=False)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)

    #with the help of meta class CourseProperty doesn't create table in a database
    class Meta:
        abstract = True


class Tag(CourseProperty):
    pass

class Prerequisite(CourseProperty):
    pass

class Learning(CourseProperty):
    pass



