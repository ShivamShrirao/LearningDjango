from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .models import Choice,Question

# Create your views here.

def index(request):
	return render(request,'polls/index.html',{})

class HomepageView(generic.ListView):
	template_name = 'polls/homepage.html'
	context_object_name = 'q_list'
	model = Question

	# def get_queryset(self):
	# 	return Question.objects.order_by('-pub_date')

def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request=request,data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				messages.success(request, f"Logged in as {username}.")
				return HttpResponseRedirect(reverse('polls:homepage'))
		messages.error(request, "Invalid username or password!")

	return render(request,'polls/login.html')

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'
	context_object_name = 'que'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'
	context_object_name = 'que'

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

		return HttpResponseRedirect(reverse('polls:results', args=(que.id,)))