

from django.shortcuts import render,redirect
from courses.models import Course,Video,Payment,UserCourse
from django.shortcuts import HttpResponse
from code_with_kamran.settings import *
from time import time
from django.views.decorators.csrf import csrf_exempt




import razorpay
client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))

#Create your Views here:

def checkout(request,slug):

    course = Course.objects.get(slug=slug)

    user = None

    if not request.user.is_authenticated:
        return redirect('login')
    #user name object
    user = request.user
    action = request.GET.get('action')
    order = None
    payment = None

    error = None
    if action == 'create_payment':
        #In this we will check ye user pehle se enroll hua h ki nhi:
        try:
            user_course = UserCourse.objects.get(user=user,course=course)
            error = 'You already enrolled in this course'
        except:
            pass

        if error is None:
            amount = int((course.price - (course.price * course.discount * 0.01))*100)
            currency = "INR"
            notes = {
                'email':user.email,
                'name': f'{user.first_name} {user.last_name}'

            }
            receipt = f'code_with_kamran - {int(time())}'
            #order
            order = client.order.create({'receipt':receipt,
                                         'notes':notes,
                                         'amount':amount,
                                         'currency':currency,
                                         })

            #payment object
            payment = Payment()
            payment.user = user
            payment.course = course
            payment.order_id = order.get('id')
            payment.save()

    context = {
        'course': course,
        'order':order,
        'payment':payment,
        'user':user,
        'error':error

    }
    return render(request,template_name='courses/check-out.html',context=context)

@csrf_exempt
def verifyPayment(request):
    if request.method == 'POST':
        data = request.POST
        context = {}
        print(data)
        try:
           client.utility.verify_payment_signature(data)

           razorpay_order_id = data['razorpay_order_id']
           razorpay_payment_id = data['razorpay_payment_id']
           #now we will search payment id with the help of this razorpay_order_id:
           payment = Payment.objects.get(order_id=razorpay_order_id)
           #we got the payment id from uper code so now we will update payment id:
           payment.payment_id = razorpay_payment_id
           #Now we need to update status also
           payment.status = True

           #Now we will update the Usercourse:
           userCourse = UserCourse(user=payment.user,course=payment.course)
           userCourse.save()

           #Now we will update this userCourse on payment:
           payment.user_course = userCourse
           payment.save()


           return redirect('my-courses')
        except:
            return HttpResponse('Invalid payment details')
