from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

# view as a function
def main(request):
    context = {"name": "John"}
    return render(request, "sem3app/index.html", context)


# view as a class
class TemplateAbout(TemplateView):
    template_name = "sem3app/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Python'
        context['number'] = 'трех'
        return context
