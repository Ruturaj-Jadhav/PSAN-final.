from django.shortcuts import render
from multiprocessing import context
from xmlrpc.client import DateTime
from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from datetime import datetime
from members.forms import userform , SignUpForm, EditProfileForm,LoginForm
from django.views import generic
from django.contrib import messages
from django.shortcuts import  render, redirect
from .forms import PasswordChangeingForm, userform
from django.contrib.auth import login
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login, authenticate,logout
from django.views.generic import ListView , DetailView
from django.contrib.auth.views import PasswordChangeView
# Create your views here.


class UserRegisterView(generic.CreateView) :
	form_class= SignUpForm
	template_name ='register.html'
	success_url =reverse_lazy('login')

class UserLoginView(generic.CreateView) :
	form_class= UserCreationForm
	template_name ='registration/login.html'
	success_url =reverse_lazy('login')

class UserEditView(generic.UpdateView):
	form_class=  EditProfileForm
	template_name ='registration/edit_profile.html'
	success_url =reverse_lazy('blogs')

	def get_object(self) :
		return self.request.user


class PasswordsChangeView(PasswordChangeView) :
	form_class= PasswordChangeingForm
	success_url =reverse_lazy('blogs')
