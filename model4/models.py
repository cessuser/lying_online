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
    final_payoff = models.CurrencyField()
    email = models.StringField(widget=widgets.TextInput)
    replicate = models.StringField(choices=['Yes', 'No'], widget=widgets.RadioSelect, label="Do you want to participate the second round of the survey? ")

    def set_payoff(self):
        self.final_payoff = self.participant.vars['n_correct_real_effort'] * 0.2
        self.final_payoff += self.participant.vars['words_found'] * 0.25
        self.final_payoff += self.participant.vars['module2_payoff']

        if self.replicate == 'Yes' and self.session.config['retake'] == 0:
            self.payoff = 1
            self.final_payoff += 1
        if self.session.config['retake'] == 1:
            self.payoff = 4

