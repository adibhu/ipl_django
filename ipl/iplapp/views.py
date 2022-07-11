
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
from .models import matches, deliveries
from django.db.models import Count, Sum

# Create your views here.
def matches_played_per_year(request):
    result =matches.objects.values('season').annotate(no_of_matches=Count('id')).order_by('season')
    return render(request, 'output.html', {'result' : result})

def number_of_matches_won_per_team(request):
    result = matches.objects.values('season','winner').annotate(no_of_wins=Count('winner')).order_by('season')
    return render(request, 'output2.html', {'result' : result})

def extra_runs_conceded(request):
    result = deliveries.objects.values('bowling_team').annotate(extra_runs_con=Sum('extra_runs')).order_by('bowling_team')
    return render(request, 'output3.html', {'result' : result})

def 