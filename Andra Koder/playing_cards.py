from enum import Enum
from typing import Literal
import random


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
        return f"Card(rank={self.rank}, suit={self.suit}, visible={self.visible})"

    def __str__(self) -> str:
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
            self.cards = [Card(r, s) for r in Rank for s in Suit]
        elif isinstance(cards, list):
            if all([isinstance(e, Card) for e in cards]):
                self.cards = cards
            else:
                types_in_list = []

                for e in cards:
                    if type(e).__name__ not in types_in_list:
                        types_in_list.append(type(e).__name__)

                raise TypeError(f"'cards' is of type '{type(cards).__name__}[{", ".join([t for t in types_in_list])}]'; must be of type 'list[Card]' or 'None'")
        else:
            raise TypeError(f"'cards' is of type '{type(cards).__name__}'; must be of type 'list['Card']' or 'None'")
    
    def __repr__(self) -> str:
        return f"Deck(cards={self.cards})"
    
    def __str__(self) -> str:
        if len(self) > 0:
            return f"[{'['*(len(self.cards)//10)}{self.cards[-1]}]"
        else:
            return "[empty]"
    
    def __len__(self) -> int:
        return len(self.cards)

    def sort(self, sort_by : Literal["rank", "suit"], high_ace : bool) -> None:
        if isinstance(sort_by, str):
            
            if len(self) > 1:
                if sort_by == "rank":
                    pass                        # TODO Make this sort the deck.
                elif sort_by == "suit":
                    pass
                else:
                    raise ValueError(f"'sort_by' contains the value '{sort_by}'; must contain 'rank' or 'suit'")
        else:
            raise TypeError(f"'sort_by' is of type '{type(sort_by).__name__}'; must be 'str'")

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def reverse(self) -> None:
        self.cards.reverse()
    
    def flip(self) -> None:
        self.reverse()
        for card in self.cards:
            if card.visible:
                card.hide()
            else:
                card.show()

    def set_cards_show(self) -> None:
        for card in self.cards:
            card.show()

    def set_cards_hide(self) -> None:
        for card in self.cards:
            card.show()

    def take_card(self, index : int) -> Card | None:
        if len(self) > 0:
            if -len(self) <= index < len(self):
                return self.cards.pop(index)
            else:
                raise IndexError(f"'index' contains the value {index}; expected to be in range [{-len(self)}, {len(self) - 1}]")
        else:
            print("Deck is empty!")

    def take_top(self) -> Card | None:
        return self.take_card(-1)

    def take_bottom(self) -> Card | None:
        return self.take_card(0)

    def take_random(self) -> Card | None:
        return self.take_card(random.randint(0, len(self) - 1))

    def put_top(self, card : Card) -> None:
        if isinstance(card, Card):
            self.cards.append(card)
        else:
            raise TypeError(f"'card' is of type '{type(card).__name__}'; must be 'Card'")

    def put_bottom(self, card : Card) -> None:
        pass

    def put_random(self, card : Card) -> None:
        pass

spades_cards = [Card(r, Suit.SPADES) for r in list(Rank)] + [10]
spades_deck = Deck(spades_cards)
standard_deck = Deck()

print(spades_deck)
print(standard_deck)