from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, Http404
from django.views import View

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class HomeView(View):

	def get(self, request, *args, **kwargs):
		
		template = "efinder_app/index.html"
		
		return render(request, template)