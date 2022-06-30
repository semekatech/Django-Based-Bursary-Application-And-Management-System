from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from accounts.forms import RegistrationForm


def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			return redirect('dashboard')
		else:
			context['registration_form'] = form
	else: #GET request
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'accounts/register.html', context)
def login_view(request):
	if request.POST:
	
			email = request.POST['email']
			raw_password = request.POST['password']
			user = authenticate(email=email, password=raw_password)
			login(request,user)
			return redirect('dashboard')
	else:
			return render(request, 'accounts/register.html', context)	
	