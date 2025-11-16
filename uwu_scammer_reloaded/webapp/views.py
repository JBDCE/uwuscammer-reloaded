from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import CreditCardForm

# Create your views here.
class CreditCardEntry(View):
    # form = CreditCardForm()
    def get(self, request):
        return HttpResponse('Not yet Implemented')
        return render(
            request=request,
            template_name='index.html',
            context={'form': self.form},
        )


    def post(self, request):
        form = CreditCardForm(request.POST)
        if not form.is_valid():
            return HttpResponse('Form invalid!')
        form.save()
        return HttpResponse('Success!')
