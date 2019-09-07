from django.shortcuts import render
from emailApp.forms import ContactForm
from django.core.mail import BadHeaderError,EmailMessage
from django.http import HttpResponse

# Create your views here.

def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():

            subject = form.cleaned_data['subject']

            from_email = form.cleaned_data['to']

            message = form.cleaned_data['message']

            recipient_list = []
            recipient_list.append(from_email)
            try:
                emailobj = EmailMessage(subject,message,to=recipient_list)
                emailobj.send()

                return HttpResponse("BooM!!! Your Email Has been sent!!!!!!!")

            except BadHeaderError:
                return HttpResponse('Invalid Header Found.')
            #return redirect('/') #note: if you want to redirect it to anywhere else please declare the path
    return render(request,'email.html',{'form':form})
