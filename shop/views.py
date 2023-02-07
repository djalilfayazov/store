from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import User


def custom_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('home')

    form = AuthenticationForm() 
    
    return render(
	    request,'users/login.html',
		{
			'form':form
		}
	)


def home(request):
	return render(request, 'home.html', {})



def items(request):
	return render(
		request, 'shop/items.html',
		{
			'items': Product.objects.all()
		}
	)


def item(request, pk):
	return render(
		request, 'shop/item.html',
		{
			'item': Product.objects.get(id=pk)
		}
	)



class Registration(CreateView):
	template_name = 'users/register.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('register-success')


	def get_success_url(self):
		"""Return the URL to redirect to after processing a valid form."""
		if not self.success_url:
			raise ImproperlyConfigured("No URL to redirect to. Provide a success_url.")
		return str(self.success_url)  # success_url may be lazy

	def form_valid(self, form):
		"""If the form is valid, redirect to the supplied URL."""
		form.save()
		return HttpResponseRedirect(self.success_url)
	

def success(request):
	return render(request, 'users/success.html', {})