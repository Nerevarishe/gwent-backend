from flask_mongoengine import Document
from mongoengine import field as fl
from datetime import datetime

class DefaultDocument(Document):
    date_created = fl.DateTimeField(default=datetime.utcnow)
    date_edited = fl.DateTimeField(default=datetime.utcnow)
    
    def refresh_date_edited(self):
        self.date_edited = datetime.utcnow()
    
    
class User(DefaultDocument):
    username = fl.StringField(min_length=2, max_length=20, required=True, unique=True, null=False)
    # password_hash = 
    email = fl.EmailField(required=True, unique=True, null=False)
    # user_decks = one to many
    # active_deck = one to one
    # games_history = on to many
    # win
    # loose

    
# Card types:
CARD_TYPE_WEATHER = 'CARD_TYPE_WEATHER'
CARD_TYPE_LEADER = 'CARD_TYPE_LEADER'
CARD_TYPE_PLAYABLE = 'CARD_TYPE_PLAYABLE'

# Card rows:


# Card abilities


class Card(DefaultDocument):
    card_type = fl.StringField(max_length=18, choices=[CARD_TYPE_WEATHER, CARD_TYPE_LEADER, CARD_TYPE_PLAYABLE], required=True, unique=True, null=False)
    name = fl.StringField(max_length=30, required=True, unique=True, null=False)
    # image = 
    description = fl.StringField(max_length=100, default='', null=False)
    strength = fl.IntField(min_value=0, default=0, require=True, null=False)
    # row = fl.StringField(choices=[])
    # ability =

    
class Deck(DefaultDocument):
    # user
    name = fl.StringField(max_length=20, require=True, null=False)
    # cards =
    # active


class GameSession(DefaultDocument):
#     session_stage= creating_game, waiting_opponent, playing, finished
#     player1= ref to user
#     player1_deck = get shuffled user's active deck
#     player1_rows
#     player1_retreat
#     player2= ref to user
#     player2_deck = get shuffled user's active deck
#     player2_rows
#     player2_retreat
#     who_win
#     who_loose
    pass
