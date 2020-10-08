from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Events.models import Event, Comments
from django.contrib.auth.models import User



def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account Created For {username}')
			return redirect('explore')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html',{'form':form, 'title':"Register"})

@login_required
def profile(request):
	if request.method == "POST":
		user_form = UserUpdateForm(request.POST, instance=request.user)
		profile_form = ProfileUpdateForm(request.POST, request.FILES,
										 instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, f'Your Account has been updated!')
			return redirect('profile')
	else:
		user_form = UserUpdateForm(instance=request.user)
		profile_form = ProfileUpdateForm(instance=request.user.profile)
	event = Event.objects.filter(host=request.user)
	context ={'user_form' :user_form, 'profile_form':profile_form, 'events':event, 'title':'Profile'}
	return render(request, 'users/profile.html', context, )

def user_events(request, username, pk):
	user = User.objects.filter(pk=pk).first()
	events = Event.objects.filter(host=user)
	comments = Comments.objects.filter(user_id=user.pk)
	return render(request, 'users/user_events.html', {'events':events, 'user':user, 'comments':comments, 'title':f'{user.username}'})