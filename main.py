from player import Player
from bid import Bid
import random
NUMPLAYERS = 4

###FUNCTION FOR TESTING###
def printPlayerDetails(inPlayers):
    for p in inPlayers:
        print(p.ID,p.diceRolls)
##########################

def bid(player, oldBid):
    """Take a bid from a specific player

    Args:
        player (Player): The player to make a bid
        oldBid (Bid): The previous bid made. None if this is the first turn.

    Returns:
        tuple[Bid, bool]: (The highest bid made, whether the bid is updated or not)
    """
    numDice = int(input("Num dice: "))
    numFace = int(input("Num face: "))
    currentBid = Bid(numDice, numFace, player)
    if (currentBid.validBid(oldBid)):
        return currentBid, True
    else:
        print("Invalid bid")
        return oldBid, False

def getAllDiceRolls(inPlayers):
    """Get all dice rolls from all current players

    Args:
        inPlayers (list[Player]): The list of all players currently in the round.

    Returns:
        list[int]: A list containing all the dice rolls across all players in the round.
    """
    allDiceRolls = []
    for p in inPlayers:
        allDiceRolls = allDiceRolls + p.diceRolls
    return allDiceRolls

def round(inPlayers):
    """Play a round with the list of players `inPlayers`.

    Args:
        inPlayers (list[Player]): List of players have have >=1 dice to play.
    """

    for p in inPlayers:
        p.rollDice()

    ##FUNCTION FOR TESTING##
    printPlayerDetails(inPlayers)
    ########################

    playerIndex = random.randint(0, len(inPlayers)-1)
    startPlayer = inPlayers[playerIndex]
    print(f"Player {startPlayer.ID} starts")
    currentBid = None

    validBid = False
    while not validBid:
        currentBid, validBid = bid(startPlayer,None)

    while True:
        playerIndex = (playerIndex + 1) % len(inPlayers)
        currentPlayer = inPlayers[playerIndex]
        print(f"Player {currentPlayer.ID}'s turn")

        option = input("Enter 'b' to bid, 'l' to accuse lie, 'e' to say exact: ")
        if option == 'b':
            validBid = False
            while not validBid:
                currentBid, validBid = bid(currentPlayer, currentBid)

        elif option == 'l':
            allDiceRolls = getAllDiceRolls(inPlayers)
            if currentBid.isTruthful(allDiceRolls):
                # The current player loses a dice as they incorrectly accused the previous player of lying.
                print("They were not lying")
                currentPlayer.numDice -= 1
            else:
                # The accused player who made the latest bid was lying so they lose a dice.
                print("They were lying")
                currentBid.player.numDice -= 1
            break

        elif option == 'e':
            allDiceRolls = getAllDiceRolls(inPlayers)
            if currentBid.isExact(allDiceRolls):
                print("Previous bid exactly correct!")
                # All other players lose 1 dice
                for p in inPlayers:
                    if p.ID != currentPlayer.ID:
                        p.numDice -= 1
            else:
                print("Incorrect!")
                # The current player loses a dice as they were incorrect in guessing that this number is exact.
                currentPlayer.numDice -= 1
            break

def getInPlayers(players):
    """Get all players taking part in the round who have at least one dice to play.

    Args:
        players (list[Player]): List of all players.

    Returns:
        list[Player]: List of all players who still have at least one dice to play.
    """
    return [p for p in players if p.numDice >= 1]


def main():
    players = [Player(i) for i in range(NUMPLAYERS)]
    while True:
        inPlayers = getInPlayers(players)
        if len(inPlayers) > 1:
            # There is no winner yet so play another round
            round(inPlayers)
        else:
            print(f"Player {inPlayers[0].ID} wins")
            break

main()
