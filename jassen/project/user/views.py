from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegisterForm

# Create your views here.
class RegisterView(CreateView):
	form_class = RegisterForm
	template_name = 'registration/register.html'
	success_url = '/'

	def dispatch(self, *args, **kwargs):
		if self.request.user.is_authenticated():
			return redirect("/logout")
		return super(RegisterView, self).dispatch(*args, **kwargs)