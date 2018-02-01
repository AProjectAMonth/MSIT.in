from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import NewsletterUserSignUpForm
from .models import *

# Create your views here.

class NewsletterView(TemplateView):
	template_name = 'newsletters/signup.html'

	def get(self, request):
		form = NewsletterUserSignUpForm()
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = NewsletterUserSignUpForm(request.POST)
		if form.is_valid():
			created = NewsletterUser.objects.get_or_create(**form.cleaned_data)
			if created[1]:
				return HttpResponse('record successfully updated')	
			else:
				return HttpResponse('email id already subscribed')		

		args = {'form': form}
		return render(request, self.template_name, args)
