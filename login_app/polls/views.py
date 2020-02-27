from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Choice,Question

# Create your views here.

def index(request):
	q_list = Question.objects.order_by('-pub_date')[:5]
	ctx = {'q_list': q_list}
	return render(request,'polls/index.html',ctx)

def detail(request, question_id):
	que = get_object_or_404(Question, pk=question_id)
	return render(request,'polls/detail.html',{'que':que})

def results(request, question_id):
	que = get_object_or_404(Question, pk=question_id)
	return render(request,'polls/results.html',{'que':que})

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