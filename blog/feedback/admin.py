from django.contrib import admin
from .models import Email

class EmailAdmin(admin.ModelAdmin):
	list_display = ['from_email', 'subject', 'timesend']
	search_fields = ['from_email', 'subject']
	class Meta:
		model = Email


admin.site.register(Email, EmailAdmin)


