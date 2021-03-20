from django.shortcuts import render
from django.views.generic import View
# Create your views here.


class Home(View):
    def get(self, *args, **kwargs):
        context = {"pageName":"Home"}
        return render(self.request, "mainSite/home.html",context)