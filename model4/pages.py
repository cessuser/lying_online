from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models



class Results(Page):
    form_model = models.Player
    form_fields = ['replicate']

    def is_displayed(self):
        return self.session.config['test'] == 0

    def before_next_page(self):
        self.player.participant.vars['replicate'] = self.player.replicate


class EmailCollect(Page):
    form_fields = ['email']
    form_model = models.Player

    def is_displayed(self):
        return self.session.config['test'] == 0


class PayInfo(Page):
    def vars_for_template(self):
        self.player.set_payoff()
        msg = ''
        if self.player.replicate == 'Yes':
            msg = 'Because you agree to participate the second round of the survey, we add $1 to your account now.'
        return {
            'msg': msg,
            'part1': c(self.player.participant.vars['n_correct_real_effort'] * 0.2),
            'part2': self.player.participant.vars['module2_payoff'],
            'part3': c(self.player.participant.vars['words_found'] * 0.25),
            'total': self.player.final_payoff
        }
page_sequence = [
    Results,
    EmailCollect,
    PayInfo
]
