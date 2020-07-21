from django.shortcuts import render
from django.views import View

# Create your views here.


class ListJobViewFull(View):
    def get(self, request):
        context={'type_page':2}
        return render(request, 'job_detail/job_full.html',context)


class ListJobViewMana(View):
    def get(self, request):
        context={'type_page':1}

        return render(request, 'job_detail/job_mana.html',context)


class ListJobViewFree(View):
    def get(self, request):
        context={'type_page':3}

        return render(request, 'job_detail/job_free.html',context)


class ListJobViewPart(View):
    def get(self, request):
        context={'type_page':4}

        return render(request, 'job_detail/job_part.html',context)


class HoSoView(View):
    def get(self, request):
        return render(request, 'job_detail/hoso.html')
