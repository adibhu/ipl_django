from django.db import models

# Create your models here.

class matches(models.Model):
    id = models.IntegerField(primary_key=True)
    season = models.IntegerField()
    city = models.CharField(max_length=200, null=True)
    date = models.DateField()
    team1 = models.CharField(max_length=200, null=True)
    team2 = models.CharField(max_length=200, null=True)
    toss_winner = models.CharField(max_length=200, null=True)
    toss_decision = models.CharField(max_length=200, null=True)
    result = models.CharField(max_length=200, null=True)
    dl_applied = models.CharField(max_length=200, null=True)
    winner = models.CharField(max_length=200, null=True)
    win_by_runs = models.IntegerField( null=True)
    win_by_wickets = models.IntegerField( null=True)
    player_of_match = models.CharField(max_length=200, null=True)
    venue = models.CharField(max_length=200, null=True)
    umpire1 = models.CharField(max_length=200, null=True)
    umpire2 = models.CharField(max_length=200, null=True)
    umpire3 = models.CharField(max_length=200, null=True)


class deliveries(models.Model):

    # match = models.ForeignKey(matches, on_delete=models.CASCADE, blank=True)

    match_id = models.IntegerField()
    inning = models.CharField(max_length=200)
    batting_team = models.CharField(max_length=100)
    bowling_team = models.CharField(max_length=100)
    over = models.IntegerField()
    ball = models.CharField(max_length=200)
    batsman = models.CharField(max_length=100)
    non_striker = models.CharField(max_length=100)
    bowler = models.CharField(max_length=100)
    is_super_over = models.IntegerField()
    wide_runs = models.IntegerField()
    bye_runs = models.IntegerField()
    legbye_runs = models.IntegerField()
    noball_runs = models.IntegerField()
    penalty_runs = models.IntegerField()
    batsman_runs = models.IntegerField()
    extra_runs = models.IntegerField()
    total_runs = models.IntegerField()
    player_dismissed = models.CharField(max_length=100)
    dismissal_kind = models.CharField(max_length=100)
    fielder =models.CharField(max_length=100, null=True, blank=True)
