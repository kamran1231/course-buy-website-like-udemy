from django.shortcuts import render
from django.shortcuts import HttpResponse
from courses.models import Course
from django.views.generic import ListView

#Create your Views here:

# class HomePageView(ListView):
#     template_name = 'courses/home.html'
#     queryset = Course.objects.all()
#     context_object_name = 'courses'



def home(request):
    courses = Course.objects.all()
    print(courses)
    return render(request,template_name='courses/home.html',
                  context={'courses':courses})
