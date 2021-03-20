from django.shortcuts import render

# Create your views here.


class Home(View):
    def get(self, *args, **kwargs):
        context = {"pageName":"Home"}
        return render(self.request, "mainSite/home.html",context)