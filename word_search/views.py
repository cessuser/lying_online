from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class WordPuzzle(Page):
    timeout_seconds = Constants.word_puzzle_seconds + 1


class WordsFound(Page):
    form_model = models.Player

    def get_form_fields(self):
        if self.session.config['version'] == 1:
            return ['cows_found1']
        else:
            return ['cows_found2']

    def before_next_page(self):
        if self.session.config['version'] == 1:
            self.player.participant.vars['words_found'] = self.player.cows_found1
        else:
            self.player.participant.vars['words_found'] = self.player.cows_found2
        self.player.set_payoff()



page_sequence = [
    Introduction,
    WordPuzzle,
    WordsFound
]
