from enum import Enum
from typing import Literal


class Rank(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

class Suit(Enum):
    SPADES = 1
    HEARTS = 2
    CLUBS = 3
    DIAMONDS = 4

class Card:
    def __init__(self, rank : Rank, suit : Suit, show : bool = False) -> None:
        if isinstance(rank, Rank):
            self.__rank = rank
        else:
            raise TypeError(f"'rank' is of type '{type(rank).__name__}'; must be of type 'Rank'")
        
        if isinstance(suit, Suit):
            self.__suit = suit
        else:
            raise TypeError(f"'suit' is of type '{type(suit).__name__}'; must be of type 'Suit'")
        
        if isinstance(show, bool):
            self.__visible = show
        else:
            raise TypeError(f"'show' is of type '{type(show).__name__}'; must be of type 'bool'")
            
        ranks_strs = {name: char for name, char in zip(list(Rank), ['A'] + [f'{n}' for n in range(2, 11)] + ['J', 'Q', 'K'])}
        suits_strs = {name: char for name, char in zip(list(Suit), ['♠', '♡', '♣', '♢'])}

        self.__rank_str = ranks_strs[rank]
        self.__suit_str = suits_strs[suit]

    @property
    def rank(self) -> Rank:
        return self.__rank

    @property
    def suit(self) -> Suit:
        return self.__suit
    
    @property
    def visible(self) -> bool:
        return self.__visible

    def __repr__(self) -> str:
        if self.visible:
            return f"{self.__suit_str}{self.__rank_str}"
        else:
            return "??"

    def show(self):
        self.__visible = True

    def hide(self):
        self.__visible = False

class Deck:
    def __init__(self, cards : list[Card] | None = None) -> None:
        if cards is None:
            pass
        elif isinstance(cards, list):
            if all([isinstance(e, Card) for e in cards]):
                pass
            else:
                types_in_list = []

                for e in cards:
                    if type(e).__name__ not in types_in_list:
                        types_in_list.append(type(e).__name__)

                raise TypeError(f"'cards' is of type '{type(cards).__name__}' containing '{types_in_list}'; must be of type 'list[Card]' or 'None'")
        else:
            raise TypeError(f"'cards' is of type '{type(cards).__name__}'; must be of type 'list[Card]' or 'None'")
        
    def sort(self, sort_by : Literal["rank", "suit"], hi_ace : bool) -> None:
        pass

cards = [Card(r, Suit.SPADES) for r in list(Rank)] + ["yo!"]
my_deck = Deck(cards)

print(my_deck)