from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'David Klinowski'

doc = """
Show word search puzzle and prompt for number of words found from given list (none of which actually appear on puzzle)
as measure of cheating proclivity
"""


class Constants(BaseConstants):
    name_in_url = 'word_search1'
    players_per_group = None
    num_rounds = 1

    word_puzzle_seconds = 90


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def set_word_search_payoff(self):
        for p in self.get_players():
            p.payoff = p.words_found


class Player(BasePlayer):
    words_found = models.PositiveIntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelect()
    )
    def set_payoff(self):
        self.payoff = self.participant.vars['n_correct_real_effort'] * 0.2
        self.payoff += self.participant.vars['words_found'] * 0.25 + 5
        self.payoff += self.participant.vars['module2_payoff']