from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models



class Results(Page):
    form_model = models.Player
    form_fields = ['email', 'replicate']

    def before_next_page(self):
        self.player.participant.vars['replicate'] = self.player.replicate


class PayInfo(Page):
    def is_displayed(self):
        return self.player.participant.vars['replicate'] == 'No'

    def vars_for_template(self):
        self.player.set_payoff()
        return {
            'part1': c(self.player.participant.vars['n_correct_real_effort'] * 0.2),
            'part3': c(self.player.participant.vars['words_found'] * 0.2),
            'total': self.player.payoff
        }
page_sequence = [
    Results,
    PayInfo
]
