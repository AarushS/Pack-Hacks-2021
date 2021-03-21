from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.
import pickle
import pandas as pd

x = {}
# pickle.load('./ipynb-analysis/player.pkl')
with open('./ipynb-analysis/profiles.pkl','rb') as f:
    x = pickle.load(f)

# df = pd.read_csv('./static/data/player.csv')
n = 0
player_profiles = {}
# for i in x.keys():
#     # x[i].update({:df[df['Player Code']==int(float(i))]})
#     # print(df[df['Player Code']==int(float(i))]['First Name'].values)
#     # print(df[df['Player Code']==int(float(i))]['Last Name'].values)
#     key = df[df['Player Code']==int(float(i))]['First Name'].values + " " + df[df['Player Code']==int(float(i))]['Last Name'].values
#     # print(list(key)[0])
#     try:
#         player_profiles[list(key)[0]] = x[i]
#     except Exception as e:
#         print(e)
#         pass
#     print(player_profiles)

# print(player_profiles)
# with open('prof.pkl', 'wb') as handle:
#     print('written')
#     pickle.dump(player_profiles, handle)

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
        context = {}     
        try:
            data = x[self.request.POST['name']]
            context = {
                'name':self.request.POST['name'],
                'post_req': True,
                'position': self.request.POST['modal'],
                'games': data['games'],
                'year': data['year'],
                'rush_yards': data['rush yards'],
                'pass_yards': data['pass yards'],
                'rush_att': data['rush att'],
                'rush_td': data['rush td'],
                'pass_att': data['pass att'],
                'pass_comp': data['pass comp'],
                'pass_td': data['pass td'],
                'pass_int': data['pass int'],
            }
        except:
            print("error")
        return render(self.request,"mainSite/footballmanager.html", context=context)