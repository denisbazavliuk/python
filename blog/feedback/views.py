from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .models import Email
from .forms import EmailForm
from django.contrib import auth

def email(request):
    context = {}
    if request.method == 'GET':
        form = EmailForm()
        context['form'] = form
        context['username'] = auth.get_user(request).username
    else:
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@djangoblog.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, "feedback/email.html", context)

def thanks(request):
    return render(request, 'feedback/thanks.html')
