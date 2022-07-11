from django.core.management.base import BaseCommand
import pandas as pd
from iplapp.models import deliveries


class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # Database connections here
        df = pd.read_csv('deliveries.csv')
        for match_id, inning, batting_team, bowling_team, over, ball, batsman, non_striker, bowler, is_super_over, wide_runs, bye_runs, legbye_runs, noball_runs, penalty_runs, batsman_runs, extra_runs, total_runs, player_dismissed, dismissal_kind, fielder in zip(df.match_id, df.inning, df.batting_team, df.bowling_team, df.over, df.ball, df.batsman, df.non_striker, df.bowler, df.is_super_over, df.wide_runs, df.bye_runs, df.legbye_runs, df.noball_runs, df.penalty_runs, df.batsman_runs, df.extra_runs, df.total_runs, df.player_dismissed, df.dismissal_kind, df.fielder):
            models = deliveries(match_id=match_id,
                                inning=inning,
                                batting_team=batting_team,
                                bowling_team=bowling_team,
                                over=over,
                                ball=ball,
                                batsman=batsman,
                                non_striker=non_striker,
                                bowler=bowler,
                                is_super_over=is_super_over,
                                wide_runs=wide_runs,
                                bye_runs=bye_runs,
                                legbye_runs=legbye_runs,
                                noball_runs=noball_runs,
                                penalty_runs=penalty_runs,
                                batsman_runs=batsman_runs,
                                extra_runs=extra_runs,
                                total_runs=total_runs,
                                player_dismissed=player_dismissed,
                                dismissal_kind=dismissal_kind,
                                fielder=fielder
                                )
            models.save()
