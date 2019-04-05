from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class MyPage(Page):
    form_model = 'player'
    form_fields = ['promise']

class MyPageWaitPage(Page):
    timeout_seconds = 1
    def before_next_page(self):
        self.player.cp = random.randint(1,10)
        self.player.endowment = random.randint(50, 500)

class MyPageWaitPage2(WaitPage):
    def after_all_players_arrive(self):
        pass

class Final_Page(Page):
    def vars_for_template(self):
        player1 = self.group.get_player_by_role('player1')
        player2 = self.group.get_player_by_role('player2')
        player3 = self.group.get_player_by_role('player3')
        player4 = self.group.get_player_by_role('player4')

        promise1 = player1.promise
        promise2 = player2.promise
        promise3 = player3.promise
        promise4 = player4.promise

        player1_return2 = player1.return2
        player1_return3 = player1.return3
        player1_return4 = player1.return4

        player2_return1 = player2.return1
        player2_return3 = player2.return3
        player2_return4 = player2.return4

        player3_return1 = player3.return1
        player3_return2 = player3.return2
        player3_return4 = player3.return4

        player4_return1 = player4.return1
        player4_return2 = player4.return2
        player4_return3 = player4.return3

        return {
            'promise1': promise1, 
            'promise2': promise2, 
            'promise3': promise3, 
            'promise4': promise4,
            'player1_return2': player1.return2, 
            'player1_return3': player1.return3, 
            'player1_return4': player1.return4,
            'player2_return1': player2.return1, 
            'player2_return3': player2.return3,
            'player2_return4': player3.return4, 
            'player3_return1': player3.return1, 
            'player3_return2': player3.return2,
            'player3_return4': player3.return4,
            'player4_return1': player4.return1,
            'player4_return2': player4.return2,
            'player4_return3': player4.return3
        }

class PrintingResult(Page):
    def vars_for_template(self):
        player1 = self.group.get_player_by_role('player1')
        player2 = self.group.get_player_by_role('player2')
        player3 = self.group.get_player_by_role('player3')
        player4 = self.group.get_player_by_role('player4')

        promise1 = player1.promise
        promise2 = player2.promise
        promise3 = player3.promise
        promise4 = player4.promise

        player1cp = player1.cp
        player2cp = player2.cp
        player3cp = player3.cp
        player4cp = player4.cp


        return {
            'promise1': promise1, 
            'promise2': promise2, 
            'promise3': promise3, 
            'promise4': promise4,
            'player2cp' : player2.cp, 
            'player1cp' : player1.cp,
            'player3cp' : player3.cp,
            'player4cp' : player4.cp
        }

    form_model = 'player'
    form_fields = ['investment1', 'investment2', 'investment3', 'investment4']

class investment_return(Page):

    form_model = 'player'
    form_fields = ['return1', 'return2', 'return3', 'return4']

    def vars_for_template(self):
        player1 = self.group.get_player_by_role('player1')
        player2 = self.group.get_player_by_role('player2')
        player3 = self.group.get_player_by_role('player3')
        player4 = self.group.get_player_by_role('player4')

        player1_investment2 = player1.investment2
        player1_investment3 = player1.investment3
        player1_investment4 = player1.investment4

        player2_investment1 = player2.investment1
        player2_investment3 = player2.investment3
        player2_investment4 = player2.investment4

        player3_investment1 = player3.investment1
        player3_investment2 = player3.investment2
        player3_investment4 = player3.investment4

        player4_investment1 = player4.investment1
        player4_investment2 = player4.investment2
        player4_investment3 = player4.investment3

        return {
            'player1_investment2': player1_investment2, 
            'player1_investment3': player1_investment3, 
            'player1_investment4': player1_investment4,
            'player2_investment1': player2_investment1, 
            'player2_investment3': player2_investment3, 
            'player2_investment4': player2_investment4,
            'player3_investment1': player3_investment1, 
            'player3_investment2': player3_investment2,
            'player3_investment4': player3_investment4,
            'player4_investment1': player4_investment1,
            'player4_investment2': player4_investment2,
            'player4_investment3': player4_investment3
        }

class Results(Page):
    pass


page_sequence = [
    MyPageWaitPage,
    MyPage,
    Results,
    PrintingResult,
    MyPageWaitPage2,
    investment_return,
    Final_Page
]
