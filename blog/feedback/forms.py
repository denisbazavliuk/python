from .models import Email
from django import forms

class EmailForm(forms.ModelForm):
	class Meta:
		model = Email
		fields = [
			'from_email',
			'subject',
			'message',
		]
