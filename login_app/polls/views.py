from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.utils.http import is_safe_url
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Choice,Question

# Create your views here.

def index(request):
	return render(request,'polls/index.html',{})

class HomepageView(LoginRequiredMixin,generic.ListView):
	login_url = '/polls/login/'
	template_name = 'polls/homepage.html'
	context_object_name = 'q_list'
	model = Question

	# def get_queryset(self):
	# 	return Question.objects.order_by('-pub_date')

def login_request(request):
	nextp = request.GET.get('next')
	if not is_safe_url(nextp,allowed_hosts=settings.ALLOWED_HOSTS,require_https=request.is_secure()):
		nextp = 'polls:index'
	if request.user.is_authenticated:
		return redirect(nextp)
	if request.method == 'POST':
		form = AuthenticationForm(request=request,data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				messages.success(request, f"Logged in as {username}.")
				return redirect(nextp)
		messages.error(request, "Invalid username or password!")

	return render(request,'polls/login.html')

class DetailView(LoginRequiredMixin,generic.DetailView):
	login_url = '/polls/login/'
	model = Question
	template_name = 'polls/detail.html'
	context_object_name = 'que'

class ResultsView(LoginRequiredMixin,generic.DetailView):
	login_url = '/polls/login/'
	model = Question
	template_name = 'polls/results.html'
	context_object_name = 'que'

@login_required(login_url = '/polls/login/')
def vote(request, question_id):
	que = get_object_or_404(Question, pk=question_id)
	try:
		selected_c = que.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request,'polls/detail.html',{
			'que':que,
			'error_message': "You didn't select a choice!",
			})
	else:
		selected_c.votes+=1
		selected_c.save()

		return redirect('polls:results', pk=que.id)

@login_required(login_url = '/polls/login/')
def logout_request(request):
	logout(request)
	messages.info(request,"Logged out successfully!")
	return redirect('polls:login')