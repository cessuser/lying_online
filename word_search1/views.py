from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.player.participant.vars['replicate'] == 'Yes'

class WordPuzzle(Page):
    timeout_seconds = Constants.word_puzzle_seconds + 1

    def is_displayed(self):
        return  self.player.participant.vars['replicate'] == 'Yes'


class WordsFound(Page):
    form_model = models.Player
    form_fields = ['words_found']

    def is_displayed(self):
        return self.player.participant.vars['replicate'] == 'Yes'

    def before_next_page(self):
        self.player.participant.vars['words_found'] = self.player.words_found


class PayInfo(Page):
    def vars_for_template(self):
        self.player.set_payoff()
        return{
            'part1': c(self.player.participant.vars['n_correct_real_effort'] * 0.2),
            'part3': c(self.player.participant.vars['words_found'] * 0.25),
            'second': c(1),
            'completion': c(4),
            'total': self.player.payoff
        }

page_sequence = [
    Introduction,
    WordPuzzle,
    WordsFound,
    PayInfo
]
