from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from courses.views import home,coursePage,SignupView,LoginView,signout,checkout,verifyPayment,MyCoursesList
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home,name='home'),
    path('logout',signout,name='logout'),
    path('my-courses',MyCoursesList.as_view(),name='my-courses'),
    path('course/<str:slug>', coursePage,name='coursepage'),
    path('signup', SignupView.as_view(),name='signup'),
    path('login', LoginView.as_view(),name='login'),
    path('check-out/<str:slug>', checkout,name='check-out'),
    path('varify_payment', verifyPayment,name='verify_payment'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)