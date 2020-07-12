from django.shortcuts import render
from django.views import View

# Create your views here.

class TuyenDungView(View):
    def get(self, request):
        return render(request, 'company/tuyendung.html')