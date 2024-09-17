from django.shortcuts import render, redirect
import datetime
import random
from django import forms


class ParticipantForm(forms.Form):
    name = forms.CharField(max_length=80)

    def name_parse(self):
        name = self.cleaned_data.get("name")
        return name


def create_list(request, players):
    form = ParticipantForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        players.append(name)
        request.session['players'] = players
        request.session.modified = True
        return redirect("santa")
    return render(request, 'hello/secret_santa.html',
                  {'form': form,
                   'players': players,
                   'pairs': None})


def clear(request):
    request.session['players'] = []
    request.session.modified = True
    return redirect("santa")


def create_pairs(request, players):
    form = ParticipantForm()
    if len(players) > 1:
        generated = pairing(players)
        return render(request, 'hello/secret_santa.html',
                      {'form': form,
                       'players': players,
                       'pairs': generated})
    else:
        return render(request, 'hello/secret_santa.html',
                  {'form': form,
                   'players': players,
                   'pairs': None,
                   "flag": 1})


def pairing(users):
    if len(users) < 2:
        return None
    santas = users.copy()
    random.shuffle(santas)
    receivers = santas[1:] + [santas[0]]
    pairs = {}
    for i in range(len(santas)):
        pairs[santas[i]] = receivers[i]
    return pairs


def date_checker():
    day = datetime.date.today().strftime("%d-%m")
    return day == "25-12"


def home(request):
    return render(request, 'hello/landing.html', {"date": date_checker()})


def secret_santa(request):
    players = request.session.get('players', [])

    if request.method == "POST":
        if "add" in request.POST:
            return create_list(request, players)
        elif "create" in request.POST:
            return create_pairs(request, players)
        elif "clear" in request.POST:
            return clear(request)

    form = ParticipantForm()
    return render(request, "hello/secret_santa.html",
                  {
                      "form": form,
                      "players": players,
                      "pairs": None})
