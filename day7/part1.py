card_vals = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

class Hand:
    def __init__(self, string: str, bid: int) -> None:
        self.string = string
        self.bid = bid
        self.arr = [card_vals[c] for c in string]

        table = {}
        for card in self.arr:
            if card in table.keys():
                table[card] += 1
            else:
                table.update({card: 1})
        table = list(table.values())

        # finding the type
        match len(table):
            case 1:
                # five of a kind
                self.type = 6
            case 2:
                if table == [4, 1] or table == [1, 4]:
                    # four of a kind
                    self.type = 5
                elif table == [3, 2] or table == [2, 3]:
                    # full house
                    self.type = 4
                else: assert False
            case 3:
                if table == [3, 1, 1] or table == [1, 3, 1] or table == [1, 1, 3]:
                    # three of a kind
                    self.type = 3
                elif table == [2, 2, 1] or table == [2, 1, 2] or table == [1, 2, 2]:
                    # two pair
                    self.type = 2
                else: assert False
            case 4:
                # one pair
                self.type = 1
            case 5:
                # nothin :(
                self.type = 0
            case _:
                assert False

    def __str__(self) -> str:
        return self.string

hands = []
with open("day7/input", "r") as f:
    for line in f.readlines():
        hand, bid = line.split(" ")
        new_hand = Hand(hand, int(bid))
        hands.append(new_hand)

# selection sort
for i in range(len(hands)):
    lowest_hand_index = i
    for j in range(i + 1, len(hands)):
        if hands[j].type < hands[lowest_hand_index].type:
            lowest_hand_index = j
        elif hands[j].type == hands[lowest_hand_index].type:
            # resolving ties
            k = 0
            while hands[j].arr[k] == hands[lowest_hand_index].arr[k]:
                k += 1
            if hands[j].arr[k] < hands[lowest_hand_index].arr[k]:
                lowest_hand_index = j
    # swapping
    tmp = hands[i]
    hands[i] = hands[lowest_hand_index]
    hands[lowest_hand_index] = tmp

winnings = 0
for rank, hand in zip(range(1, len(hands) + 1), hands):
    print(hand, hand.bid)
    winnings += hand.bid * rank
print("\ntotal winnings:", winnings)
