from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models


class MyPage(Page):
    form_fields = ['consent']
    form_model = models.Player

    def app_after_this_page(self, upcoming_apps):
        if self.player.consent == 'No':
            self.player.participant.vars['consent'] = False
            return upcoming_apps[-1]

    def before_next_page(self):
        self.player.participant.vars['consent'] = False


page_sequence = [
    MyPage,
]
