from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.


class Home(View):
    def get(self, *args, **kwargs):
        context = {"pageName":"Home"}
        return render(self.request, "mainSite/home.html",context)

class Football(View):
    def get(self, *args, **kwargs):
        context = {"pageName":"Home"}
        return render(self.request,"mainSite/footballmanager.html")
    def post(self, *args, **kwargs):
        print(self.request.POST)

        

        return render(self.request,"mainSite/footballmanager.html", context={'post_req': True, 'position': self.request.POST['modal']})