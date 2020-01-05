from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def indexPageView(request):
	# latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('management/index.html')
	context = {
		# 'latest_question_list': latest_question_list,
	}
	return HttpResponse(template.render(context, request))
	# return HttpResponse("Employee Space")

def pageNotFoundView(request):
	return HttpResponse("Error 404! Page not found")