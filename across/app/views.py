from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from pprint import pprint
from app.models import Game, Team

def index(request):
    context = {

    }
    return render(request, "index.html", context)
def team(request):
    context = {

    }
    return render(request, "team.html", context)
def staff(request):
    context = {

    }
    return render(request, "staff.html", context)
def affiliate(request):

    context = {

    }
    return render(request, "affiliate.html", context)
def profil(request):
    # Récuperer les donées
    # donées -> mettre a jour la db
    context = {

    }
    return render(request, "profil.html", context)
def contact(request):
    context = {

    }
    return render(request, "contact.html", context)
def auth_logout(request):
    logout(request)
    context = {

    }
    return render(request, "index.html", context)
def admin(request):
    allGame = Game.objects.all()
    allTeam = Team.objects.all()
    context = {
        "allGame": allGame,
        "allTeam": allTeam,
    }
    return render(request, "admin.html", context)
def add_game(request):

    if request.POST.get('gameName'):
        gameName = request.POST.get('gameName')
        game = Game(name=gameName)
        game.save()
    else:
        print("error: Game was not created")

    return redirect('/admin')

def delete_game(request):

    if request.GET.get('gamePk'):
        gamePk = request.GET.get('gamePk')
        Game.objects.get(id=gamePk).delete()
    else:
        print("error: Game was not deleted")

    return redirect('/admin')
def add_team(request):
    print("gg")
    if request.POST.get('teamName'):
        teamName = request.POST.get('teamName')
        teamStructure = request.POST.get('teamStructure')
        teamGame = Game.objects.get(pk=request.POST.get('teamGame'))
        team = Team(name=teamName, structure=teamStructure, game=teamGame)
        team.save()
    else:
        print("error: Team was not created")

    return redirect('/admin')

def delete_team(request):

    if request.GET.get('teamPk'):
        teamPk = request.GET.get('teamPk')
        Team.objects.get(id=teamPk).delete()
    else:
        print("error: Team was not deleted")

    return redirect('/admin')