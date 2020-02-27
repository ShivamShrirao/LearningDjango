from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice,Question

# Create your views here.

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'q_list'

	def get_queryset(self):
		return Question.objects.order_by('-pub_date')

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