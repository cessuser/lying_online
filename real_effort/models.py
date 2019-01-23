from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Danlin Chen'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'real_effort'
    players_per_group = None
    num_rounds = 60

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            nums1 = [random.randint(10, 100) for i in range(0,Constants.num_rounds)]
            nums2 = [random.randint(10, 100) for i in range(0, Constants.num_rounds)]
            for p in self.get_players():
                p.participant.vars['nums1'] = nums1
                p.participant.vars['nums2'] = nums2


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    answer = models.IntegerField()
    correct = models.IntegerField()
    n_correct = models.IntegerField()
    test = models.IntegerField()

    def check_correct(self):

        if self.round_number == 1:
            self.participant.vars['n_correct_real_effort'] = 0
        correct_answer = self.participant.vars['nums1'][self.round_number-1] \
                         + self.participant.vars['nums2'][self.round_number-1]
        if self.answer == correct_answer:
            self.correct = 1
            self.participant.vars['n_correct_real_effort'] += 1
        else:
            self.correct = 0
        self.n_correct = self.participant.vars['n_correct_real_effort']


