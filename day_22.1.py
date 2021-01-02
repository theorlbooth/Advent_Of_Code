player_1 = [41, 48, 12, 6, 1, 25, 47, 43, 4, 35, 10, 13, 23, 39, 22, 28, 44, 42, 32, 31, 24, 50, 34, 29, 14]

player_2 = [36, 49, 11, 16, 20, 17, 26, 30, 18, 5, 2, 38, 7, 27, 21, 9, 19, 15, 8, 45, 37, 40, 33, 46, 3]


def find_winning_cards(player_1, player_2):
  while len(player_1) > 0 and len(player_2) > 0:
    player_1_card = player_1[0]
    # print(player_1_card)
    player_2_card = player_2[0]
    # print(player_2_card)
    if player_1_card > player_2_card:
      player_1 = player_1[1:]
      player_1 = player_1 + [player_1_card] + [player_2_card]
      player_2 = player_2[1:]  
    else:
      player_2 = player_2[1:]
      player_2 = player_2 + [player_2_card] + [player_1_card]
      player_1 = player_1[1:]  
  if len(player_1) == 0:
    return ['Player 2', player_2]
  else:
    return ['Player 1', player_1]

# print(find_winning_cards(player_1, player_2))


winning_cards = [46, 24, 49, 22, 38, 15, 42, 13, 14, 4, 45, 5, 34, 3, 31, 25, 44, 30, 21, 16, 37, 7, 18, 2, 47, 23, 43, 19, 29, 26, 35, 33, 11, 9, 36, 20, 12, 10, 27, 17, 50, 41, 40, 6, 8, 1, 48, 39, 32, 28]

winning_cards_reversed = winning_cards[::-1]

print(winning_cards_reversed)

def find_total(cards):
  card = 0
  number = 1
  running_total = 0
  while card < 50:
    num = cards[card] * number
    running_total += num
    card += 1
    number += 1
  return running_total

print(find_total(winning_cards_reversed))