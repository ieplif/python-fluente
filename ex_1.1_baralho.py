import collections
from random import choice

# Representa as cartas individuais
# namedtuple cria classe de objetos que sejam apenas grupos de atributos
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]  # quebra de linha ordena
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self,position):
        return self._cards[position]

# representação das cartas   
beer_card = Card('7', 'diamonds')
beer_card

# número de cartas
deck = FrenchDeck()
len(deck)

# cartas específicas
deck[0], deck[-1]

# carta aleatória
choice(deck)

# slicing
deck[:3]

# selecionando ases, seleciona o 12 e avança 13 cartas
deck[12::13]

# __getitem__ iterável
#for card in deck: # doctest: +ELLIPSIS
    # print(card)

# de forma inversa
# for card in reversed(deck): #doctest: +ELLIPSIS
    #print(card)
 
 
# função para classificação de cartas
# Ás é maio e 2 a menor
# naipes ordem: spades, hearts, diamonds, clubs
# 0 para o 2 de paus e 51 para o Ás de espadas

suit_values = dict(spades= 3, hearts= 2, diamonds= 1, clubs= 0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

# listando em ordem crescente 

for card in sorted(deck, key=spades_high):
    print(card)
