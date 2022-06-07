from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "날씨정보 사이트 Contact email" 
			body = {
        'name': form.cleaned_data['name'], 
        'subject': form.cleaned_data['subject'],
        'message':form.cleaned_data['message'],
        'from_email':form.cleaned_data['from_email']
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'from_email', ['lee_yechan@hufs.ac.kr'])  
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return HttpResponse('Complete')

	form = ContactForm()
	return render(request, "contactform/contact.html", {'form':form})

def homepage(request):
	return render(request, "polls/index.html")