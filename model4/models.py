from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'model4'
    players_per_group = None
    num_rounds = 1

    replicate_fee = c(1)
    replicate_finish = c(4)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    email = models.StringField(widget=widgets.TextInput, blank=True)
    replicate = models.StringField(choices=['Yes', 'No'], widget=widgets.RadioSelect, label="Do you want to continue? ")

    def set_payoff(self):
        self.payoff = self.participant.vars['n_correct_real_effort'] * 0.2
        self.payoff += self.participant.vars['words_found'] * 0.25

