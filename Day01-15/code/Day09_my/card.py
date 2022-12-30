import random


class Card(object):

    def __init__(self, suite, face):
        self._suite = suite
        self._face = face

    @property
    def suite(self):
        return self._suite

    @property
    def face(self):
        return self._face

    def __str__(self):
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return '%s%s' % (self._suite, face_str)

    def __repr__(self):
        return self.__str__()


class Poker(object):

    def __init__(self):
        self._cards = [Card(suite, face) for suite in '♠♥♣♦' for face in range(1, 14)]
        self._current = 0

    def shuffle(self):
        random.shuffle(self._cards)
        self._current = 0

    def deal(self):
        card = self._cards[self._current]
        self._current += 1
        return card

    def has_next(self):
        return self._current < len(self._cards)


class Player(object):

    def __init__(self, name):
        self._name = name
        self._cards_on_hands = []

    @property
    def name(self):
        return self._name

    @property
    def cards_on_hands(self):
        return self._cards_on_hands

    def get(self, card):
        self._cards_on_hands.append(card)

    def arrange(self, card_key):
        self._cards_on_hands.sort(key=card_key)


def get_key(card):
    return (card.suite, card.face)


def main():
    p = Poker()
    p.shuffle()
    players = [Player('xiaobei'), Player('tietie'), Player('pangpang')]
    while p.has_next():
        for player in players:
            if p.has_next():
                card = p.deal()
                player.get(card)

    for player in players:
        print(player.name + ':', end='  ')
        player.arrange(get_key)
        print(player.cards_on_hands, end=' ')
        print(len(player.cards_on_hands))


if __name__ == '__main__':
    main()
