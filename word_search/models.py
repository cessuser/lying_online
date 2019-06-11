from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'David Klinowski Danlin Chen'

doc = """
Show word search puzzle and prompt for number of words found from given list (none of which actually appear on puzzle)
as measure of cheating proclivity

number of choices changed, puzzle picture changed
"""


class Constants(BaseConstants):
    name_in_url = 'word_search'
    players_per_group = None
    num_rounds = 1

    word_puzzle_seconds = 60
    prize = c(0.1)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def set_word_search_payoff(self):
        for p in self.get_players():
            p.payoff = p.words_found


class Player(BasePlayer):
    cows_found1 = models.IntegerField(min=0, max=100, label='How many cows did you find in the picture? You will get 100 ECUs times the number you select on the pull-down menu.')
    cows_found2 = models.IntegerField(
        label='How many cows did you find in the picture? You will get ' + str(Constants.prize) +  ' for each cow you find.',
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],
    )

    def set_payoff(self):
        if self.session.config['version'] == 1:
            self.payoff = self.cows_found1 * Constants.prize
        else:
            self.payoff = self.cows_found2 * Constants.prize
