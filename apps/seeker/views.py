from django.shortcuts import render
from django.views import View

# Create your views here.


class ListJobView(View):
    def get(self, request):
        return render(request, 'job_detail/job_detail.html')
