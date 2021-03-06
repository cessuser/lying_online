from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    def vars_for_template(self):
        return {"example_4": Constants.die_conversion * 4,
                "example_1": Constants.die_conversion * 1}

class DiceRolling(Page):
    form_model = 'player'
    form_fields = ['die_roll','virtual_dice']

    def before_next_page(self):
        self.player.set_payoff()
        print("Payoff set" + str(self.player.payoff))


page_sequence = [
    Instructions,
    DiceRolling,
]
