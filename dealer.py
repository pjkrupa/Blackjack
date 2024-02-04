deck_score = {'A\u2665': 11, '2\u2665': 2, '3\u2665': 3, '4\u2665': 4, '5\u2665': 5, '6\u2665': 6, '7\u2665': 7, '8\u2665': 8, '9\u2665': 9,
              '10\u2665': 10, 'J\u2665': 10, 'Q\u2665': 10, 'K\u2665': 10,
              'A\u2666': 11, '2\u2666': 2, '3\u2666': 3, '4\u2666': 4, '5\u2666': 5, '6\u2666': 6, '7\u2666': 7, '8\u2666': 8,
              '9\u2666': 9, '10\u2666': 10, 'J\u2666': 10, 'Q\u2666': 10, 'K\u2666': 10,
              'A\u2663': 11, '2\u2663': 2, '3\u2663': 3, '4\u2663': 4, '5\u2663': 5, '6\u2663': 6, '7\u2663': 7, '8\u2663': 8,
              '9\u2663': 9, '10\u2663': 10, 'J\u2663': 10, 'Q\u2663': 10, 'K\u2663': 10,
              'A\u2660': 11, '2\u2660': 2, '3\u2660': 3, '4\u2660': 4, '5\u2660': 5, '6\u2660': 6, '7\u2660': 7, '8\u2660': 8,
              '9\u2660': 9, '10\u2660': 10, 'J\u2660': 10, 'Q\u2660': 10, 'K\u2660': 10}

ace_list = ['A\u2665', 'A\u2666', 'A\u2663', 'A\u2660']

class Hand:
    def __init__(self, card1, card2):
        self.hand = [card1, card2]
        self.score = 0
        self.bust = False

    def hit_me(self, new_card):
        self.hand.append(new_card)

    def calculate_score(self):
        ace_counter = 0
        self.score = 0
        for i in self.hand:
            if i in ace_list:
                ace_counter = ace_counter + 1
        for card in self.hand:
            self.score = self.score + deck_score[card]
        if self.score > 21 and ace_counter > 0:
            while self.score > 21 and ace_counter > 0:
                self.score = self.score - 10
                ace_counter = ace_counter - 1
