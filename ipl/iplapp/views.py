from itertools import count
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
from .models import matches, deliveries
from django.db.models import Count

# Create your views here.
def matches_played_per_year(request):
    result = HttpResponse(matches.objects.values('season').annotate(no_of_matches=Count('id')).order_by('season'))
    return render(request, 'output.html',result = {result})