from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class DashboardView(TemplateView):
	template_name = "dashboard.html"

	def get_context_data(self, *args, **kwargs):
		context = super(DashboardView, self).get_context_data(*args, **kwargs)
		
		return context
