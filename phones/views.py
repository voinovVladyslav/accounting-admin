from django.shortcuts import render
from django.views import View

from phones.models import Phone


class PhonesView(View):
    def get(self, request):
        phones = Phone.objects.all()
        context = {'phones': phones}
        return render(request, 'phones/main.html', context)
