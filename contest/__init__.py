from otree.api import *


doc = """
Implementation of contest games with selectable contest success function
"""


class C(BaseConstants):
    NAME_IN_URL = 'contest'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 3
    ENDOWMENT = Currency(10)
    COST_PER_TICKET = Currency(0.50)
    PRIZE = Currency(8)


class Subsession(BaseSubsession):
    is_paid = models.BooleanField()
    # Can take on the values True or False
    def setup_round(self):
        self.is_paid = True
        for group in self.get_groups():
            group.setup_round()

class Group(BaseGroup):
    prize=models.CurrencyField()

    def setup_round(self):
        self.prize = C.PRIZE
        self.csf = ...
        for player in self.get_players():
            player.setup_round()


class Player(BasePlayer):
    endowment = models.CurrencyField()
    cost_per_ticket = models.CurrencyField()
    tickets_purchased = models.IntegerField()

    def setup_round(self):
        self.endowment = C.ENDOWMENT
        self.cost_per_ticket = C.COST_PER_TICKET
    # Setup round is one operation we are going to do on one player by setting the endowment to the constant endowment


def creating_session(subsession):
    subsession.setup_round()
# This created sessions across all rounds

# PAGES
class SetupRound(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def after_all_players_arrive(subsession):
        subsession.setup_round()
# All functions on pages start with @staticmethod because pages are supposed to be very easy to follow and basic
class Intro(Page):
    pass

class Decision(Page):
    pass

class WaitForDecisions(WaitPage):
    pass

class Outcome(Page):
    pass

class EndBlock(Page):
    pass

class Results(Page):
    pass

# Standard format of writing lists in Python (to be noted)
page_sequence = [
    SetupRound,
    Intro,
    Decision,
    WaitForDecisions,
    Outcome,
    EndBlock,
    Results]
