
from django.shortcuts import render,redirect
from courses.models import Course,Video,UserCourse
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.utils.decorators import method_decorator

#Create your Views here:
@method_decorator(login_required(login_url='login'),name='dispatch')
class MyCoursesList(ListView):
    template_name = "courses/my_courses.html"
    context_object_name = 'user_courses'

    def get_queryset(self):
        return UserCourse.objects.filter(user=self.request.user)


#if u login then u can see my_course:
'''
@login_required(login_url='login')
def my_courses(request):
    user = request.user
    user_course = UserCourse.objects.filter(user=user)
    context = {
        'user_courses':user_course
    }
    return render(request,template_name="courses/my_courses.html",context=context)

'''
def coursePage(request,slug):

    course = Course.objects.get(slug=slug)
    #getting serial number of lecture from course_page.html
    serial_number = request.GET.get('lecture')
    #sort all the videos
    videos = course.video_set.all().order_by('serial_number')
    if serial_number is None:
        serial_number = 1
    # print(serial_number)

    video = Video.objects.get(serial_number = serial_number,course = course)
    #condition if u login than u can watch preview video if not then:

    if (video.is_preview is False):
        if (request.user.is_authenticated is False):
            return redirect('login')
        else:
            user = request.user
            try:
                user_course = UserCourse.objects.get(user=user, course=course)

            except:
                return redirect('check-out',slug=course.slug)

    context = {
        'course': course,
        'video': video,
        'videos':videos
    }
    return render(request,template_name='courses/course_page.html',context=context)
