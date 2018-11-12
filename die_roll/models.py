from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
copy of Gahana experiment
"""

LEFT_RIGHT_CHOICES = [
    ('1', ''),
    ('2', ''),
    ('3', ''),
    ('4', ''),
    ('5', ''),
    ('6', ''),
    ('7', ''),
    ('8', ''),
    ('9', ''),
]

class Constants(BaseConstants):
    name_in_url = 'questionnaire'
    players_per_group = None
    num_rounds = 1
    show_app_name = "die_roll"
    die_conversion = c(1)


    cheat_tax_choices = tuple([('0', "Always justified")] + LEFT_RIGHT_CHOICES + [('10', "Never justified")])

    tax_democracy_choices = tuple([('0', "Absolutely essential")] + LEFT_RIGHT_CHOICES + [('10', "Not essential")])

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    die_roll = models.IntegerField(min = 0, max = 6)
    
    def set_payoff(self):
        self.payoff = self.die_roll * Constants.die_conversion
