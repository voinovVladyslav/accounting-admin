from django.shortcuts import render
from django.views import View


class PhonesView(View):
    def get(self, request):
        return render(request, 'phones/main.html')

