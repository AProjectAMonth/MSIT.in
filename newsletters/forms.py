from django import forms
from .models import NewsletterUser

class NewsletterUserSignUpForm(forms.ModelForm):
	email = forms.CharField()

	class Meta:
		model = NewsletterUser
		fields = ['email']

		def clean_email(self):
			email = self.cleaned_data.get('email')
			try:
				match = NewsletterUser.objects.get(email=email)
			except NewsletterUser.DoesNotExist:
				return email

			raise forms.ValidationError('this email is alredy subscribed')