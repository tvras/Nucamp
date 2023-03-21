


''' 
Goal of the game is to have a hand higher than the dealer 
but doens't total higher than 21
if higher than 21 = "Bust"

Cards 2-10 (face value)
Cards J, Q, K = 10
Card A can be 1 or 11 / You can change the value throuough the round



Game starts: 

1 - dealer deals 1st face up card for each player
2- dealer take 1st face up card
3- dealer deals 2nd face up card for each player
4- dealer take 2nd face down card

- if player cards total 21, automatically wins 1.5 x your bet from the dealer 
and you are done for that round.

- Otherwise dealer asks if you want another card from the top of the deck.
    - if you do want say "Hit".
        - No limit to how many cards you can get but if sum of your cards > 21 = "Bust"
        dealer gets your bet.

    - If you don't want another card say "Stay"

- dealer finishes going around the table, dealer flips the card face up
    - If dealer_hand_total <= 16, dealer has "Hit"
    - If is dealer_hand_total >= 17, dealer has to "Stay"

- If dealer "Bust", every player gets 2 x their bet
- If the dealer doesn't "Bust" only the player with hand higher than the dealers win 2x bet
everyone else loses their initial bet


- Round over, all players place a new bet.


'''

