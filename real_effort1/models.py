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
    name_in_url = 'real_effort1'
    players_per_group = None
    num_rounds = 80

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            nums1 = [36, 48, 42, 25, 63, 29, 64, 78, 16, 15, 54, 74, 20, 89, 49, 57, 46, 40, 17, 54, 31, 11, 36, 18, 95, 33, 88, 16, 59, 76, 67, 89, 43, 59, 78, 58, 88, 23, 91, 90, 50, 65, 22, 89, 42, 26, 26, 30, 37, 38, 58, 21, 82, 10, 12, 11, 45, 72, 88, 18, 22, 81, 61, 67, 84, 49, 30, 39, 89, 30, 78, 51, 32, 55, 46, 69, 25, 15, 47, 44]
            nums2 = [47, 80, 37, 76, 26, 16, 12, 47, 54, 66, 11, 74, 74, 43, 47, 48, 48, 63, 69, 96, 50, 21, 44, 72, 60, 30, 43, 11, 79, 65, 10, 54, 92, 77, 39, 63, 68, 56, 61, 100, 40, 67, 79, 15, 24, 82, 48, 34, 14, 20, 36, 65, 69, 78, 21, 91, 92, 99, 93, 73, 87, 86, 39, 93, 100, 93, 70, 100, 37, 10, 97, 58, 86, 76, 38, 20, 19, 89, 26, 33]
            for p in self.get_players():
                p.participant.vars['nums1'] = nums1
                p.participant.vars['nums2'] = nums2


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    answer = models.IntegerField()
    correct = models.IntegerField()
    n_correct = models.IntegerField()

    def check_correct(self):
        if self.round_number == 1:
            self.payoff = 0
            self.participant.vars['n_correct_real_effort1'] = 0
        correct_answer = self.participant.vars['nums1'][self.round_number-1] \
                         + self.participant.vars['nums2'][self.round_number-1]
        if self.answer == correct_answer:
            self.correct = 1
            self.participant.vars['n_correct_real_effort1'] += 1
            self.payoff += 0.2
        else:
            self.correct = 0
        self.n_correct = self.participant.vars['n_correct_real_effort1']

