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
    name_in_url = 'questionnaire1'
    players_per_group = None
    num_rounds = 1
    show_app_name = "die_roll1"
    die_conversion = c(1)


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    die_roll = models.IntegerField(min = 0, max = 6)
    
