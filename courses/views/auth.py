

from django.shortcuts import render,redirect
from courses.forms import RegistrationForm,LoginForm
from django.views import View
from django.contrib.auth import logout
from django.shortcuts import HttpResponse

from django.views.generic.edit import FormView


class SignupView(FormView):
    template_name = 'courses/signup.html'
    form_class = RegistrationForm
    success_url = '/login'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)
#Create your Views here:
'''
class SignupView(View):
    def get(self,request):
        if request.method == 'GET':
            form = RegistrationForm()
            return render(request, template_name='courses/signup.html', context={'form': form})

    def post(self,request):
        form = RegistrationForm(request.POST)
        if (form.is_valid()):
            user = form.save()
            if (user is not None):
                return redirect('login')
        return render(request, template_name='courses/signup.html', context={'form': form})
'''

#Login class view
class LoginView(View):
    def get(self,request):
        form = LoginForm()
        context = {
            'form':form
        }
        return render(request, template_name="courses/login.html",context=context)


    def post(self,request):
        form = LoginForm(request=request,data=request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            return redirect('home')
        return render(request, template_name="courses/login.html", context=context)


def signout(request):
    logout(request)
    return redirect('home')





