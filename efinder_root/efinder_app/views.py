from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, Http404
from django.views import View
from .forms import InputForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class SearchView(View):

	def get(self, request, *args, **kwargs):
		
		template = "efinder_app/search.html"
		form = InputForm()
		context = {
			'form': form,
		}

		return render(request, template, context)


	def post(self, request, *args, **kwargs):

		template = "efinder_app/search.html"
		form = InputForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)

		context = {
			'form': form,
		}
		return render(request, template, context)




# class UserView(View):

# def user_auth(request):
# 	if request.user.is_authenticated():
# 		context = {

# 		}
# 		template = 
# 	else:
# 		context = {

# 		}
# 		template = 
# 	return render(request, context)