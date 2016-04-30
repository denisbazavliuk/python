from django.shortcuts import render
from .forms import SignUpForm
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def home(request):
	title = 'Welcome'
	form = SignUpForm(request.POST or None)
	if form.is_valid():
		registration = form.save(commit = False)
		registration.save()
	context = {
        'title': title,
        'form': form,
	}
	return render(request, 'register/home.html', context)
