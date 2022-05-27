from django.shortcuts import render, redirect
from djangoProject1.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'recommendation/front.html')

# def contact(request):
#     return render(request, 'recommendation/contact.html')

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
			return render(request, 'recommendation/front.html')

	form = ContactForm()
	return render(request, "recommendation/contact.html", {'form':form})

