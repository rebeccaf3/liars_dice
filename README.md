# Liar's Dice

A basic implementation of Liar's Dice.

- Players start with 5 dice and roll them all at the start of each round.
- Players should only be aware of what they rolled, but not what the other players rolled.
- Players each take turns bidding on the number of dice and the face value that were rolled for ALL players.
- To raise the bid, players must either increase the number of dice bid or make a bid with the same number of dice but with a higher face value.
- On each player's turn they can accuse the previous player's bid of being a lie or of being exact. At this point, the round ends and all dice are revealed.
- The bid is a lie if the previous player bid more than the amount of dice on the table (e.g. bidding five 2s is a lie if only three 2s were rolled between all players). In this case, the lying player loses one of their dice. If it is not a lie, the accusing player loses a dice.
- If it is exact (e.g. bid five 2s and there are EXACTLY fives 2s rolled between all players), then all players except the player who said 'exact' lose a dice. Otherwise, the player who incorrectly said 'exact' loses a dice.
- If a player runs out of dice, they are out.
- Rounds continue until only one player remains who is the winner.