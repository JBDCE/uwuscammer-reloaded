from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm

# Create your views here.
def hello_world(request):
    return HttpResponse('Hello World!')


class HelloGermany(View):
    def get(self, request):
        return HttpResponse('Hello from Germany!')


class ReservationView(View):
    form = ReservationForm
    def get(self, request):
        return render(
            request=request,
            template_name='index.html',
            context={'form': self.form},
        )


    def post(self, request):
        form = ReservationForm(request.POST)
        if not form.is_valid():
            return HttpResponse('Form invalid!')
        form.save()
        return HttpResponse('Success!')
