from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import Club

class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')


class ClubsView(View):
    def get(self, request):
        clubs = Club.objects.all()
        context = {
            'clubs': clubs
        }
        return render(request, 'clubs.html', context)


class ClubDetailsView(View):
    def get(self,request,pk):
        club = get_object_or_404(Club,id=pk)
        players = club.player_set.order_by('-price')
        context = {
            'club':club,
            'players':players,
        }
        return render(request,'club-details.html',context)

class AboutView(View):
    def get(self, request):
        return render(request,'about.html')