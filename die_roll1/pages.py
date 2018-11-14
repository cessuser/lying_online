from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    def vars_for_template(self):
        return {"example_4": Constants.die_conversion * 4,
                "example_1": Constants.die_conversion * 1}

class DiceRolling(Page):
    form_model = 'player'
    form_fields = ['die_roll']




class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


class Introduction(Page):
    pass

page_sequence = [
    Introduction,
    Instructions,
    DiceRolling,
]
