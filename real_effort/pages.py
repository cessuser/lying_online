from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import time


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


class TaskPage(Page):
    form_fields = ['answer']
    form_model = models.Player
    timeout_seconds = 60

    def is_displayed(self):
        if self.round_number == 1:
            self.player.participant.vars['remaining_time'] = 60
        self.player.participant.vars['time_onLoad'] = time.time()
        return self.player.participant.vars['remaining_time'] > 0 and 1 <= self.round_number <= Constants.num_rounds

    def get_timeout_seconds(self):
        print("remain time: ", self.participant.vars['remaining_time'])
        return self.player.participant.vars['remaining_time']

    def vars_for_template(self):
        return {
            'shown_num1': self.player.participant.vars['nums1'][self.round_number - 1],
            'shown_num2': self.player.participant.vars['nums2'][self.round_number - 1]
        }

    def before_next_page(self):
        self.player.check_correct()
        spent = time.time() - self.player.participant.vars['time_onLoad']
        self.player.participant.vars['remaining_time'] = self.player.participant.vars['remaining_time'] - spent
        if self.timeout_happened:
            self.player.participant.vars['remaining_time'] = 0


class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    def vars_for_template(self):
        self.player.payoff = self.player.participant.vars['n_correct_real_effort']*0.2

page_sequence = [
    Introduction,
    TaskPage,
    Results
]
