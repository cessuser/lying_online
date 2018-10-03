from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models



class Results(Page):
    form_model = models.Player
    form_fields = ['email']


page_sequence = [
    Results
]
