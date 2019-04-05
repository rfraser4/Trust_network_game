from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Banks and Fraser'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Trust_Network_Game'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    endowment = models.IntegerField()
    cp = models.IntegerField()
    promise = models.IntegerField()

    investment1 = models.IntegerField()
    investment2 = models.IntegerField()
    investment3 = models.IntegerField()
    investment4 = models.IntegerField()

    return1 = models.IntegerField()
    return2 = models.IntegerField()
    return3 = models.IntegerField()
    return4 = models.IntegerField()

    def role(self):
        if self.id_in_group == 1:
            return 'player1'
        if self.id_in_group == 2:
            return 'player2'
        if self.id_in_group == 3:
            return 'player3'
        if self.id_in_group == 4:
            return 'player4'





