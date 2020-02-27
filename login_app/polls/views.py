from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request):
	q_list = Question.objects.order_by('-pub_date')[:5]
	output = ',<br>'.join([q.question_text for q in q_list])
	return HttpResponse(output)

def detail(request, question_id):
	return HttpResponse("You're looking at question %s" % question_id)

def results(request, question_id):
	return HttpResponse("You're looking at results of question %s" % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s" % question_id)
