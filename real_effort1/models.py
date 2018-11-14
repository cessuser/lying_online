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
    num_rounds = 60

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            nums1 = [69, 22, 10, 22, 31, 83, 65, 16, 21, 91, 63, 70, 24, 87, 84, 10, 52, 29, 56, 98, 84, 92, 88, 72, 78, 17, 94, 55, 89, 45, 22, 35, 84, 36, 26, 79, 100, 33, 94, 89, 42, 32, 23, 67, 72, 59, 31, 11, 69, 67, 72, 19, 86, 80, 22, 89, 61, 30, 72, 65]
            nums2 = [47, 80, 37, 76, 26, 16, 12, 47, 54, 66, 11, 74, 74, 43, 47, 48, 48, 63, 69, 96, 50, 21, 44, 72, 60, 30, 43, 11, 79, 65, 10, 54, 92, 77, 39, 63, 68, 56, 61, 100, 40, 67, 79, 15, 24, 82, 48, 34, 14, 20, 36, 65, 69, 78, 21, 91, 92, 99, 93, 73]
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
            self.participant.vars['n_correct_real_effort1'] = 0
        correct_answer = self.participant.vars['nums1'][self.round_number-1] \
                         + self.participant.vars['nums2'][self.round_number-1]
        if self.answer == correct_answer:
            self.correct = 1
            self.participant.vars['n_correct_real_effort1'] += 1
        else:
            self.correct = 0
        self.n_correct = self.participant.vars['n_correct_real_effort1']

