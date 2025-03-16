class Bid():
    def __init__(self, numDice, numFace, player):
        self.numDice = numDice
        self.numFace = numFace
        self.player = player

    def validBid(self, oldBid):
        """Validate the latest bid such that it successfully raises the bid.
        To do this it must either:
        - Keep the number of dice the same and increase the face value (e.g. can raise 2 twos to 3 twos)
        - Increase the number of dice bid using any face value (e.g. can raise 2 twos to 3 ones)

        Args:
            oldBid (Bid): The last bid object that was made. None if no bid was made.

        Returns:
            bool: Returns True if the bid is valid and False otherwise.
        """
        if ((self.numFace <= 0) or (self.numFace > 6)):
            return False

        if (self.numDice < 1):
            return False

        if oldBid == None:
            # No previous bid
            return True
        else:
            if (self.numDice > oldBid.numDice):
                # Increase dice number so the bid has been raised.
                return True
            elif (self.numDice == oldBid.numDice) and (self.numFace > oldBid.numFace):
                # The dice number is the same using a greater face value, so the bid has been raised.
                return True
            else:
                # The bid has not been raised.
                return False

    def count(self, allDiceRolls):
        """Takes a list representing ALL dice for all players and returns the number of dice that match this bid's face value.

        Args:
            allDiceRolls (list[int]): A list of ALL dice rolls for all players.

        Returns:
            int: The number of dice that match this bid's face value.
        """
        count = 0
        for roll in allDiceRolls:
            if roll == self.numFace:
                count += 1
        return count

    def isExact(self, allDiceRolls):
        """Determine if the current bid matches the set of dice rolls exactly.

        Args:
            allDiceRolls (list[int]): A list of ALL dice rolls for all players.

        Returns:
            bool: Returns True if the bid matches the dice rolls exactly and False otherwise.
        """
        return self.count(allDiceRolls) == self.numDice

    def isTruthful(self, allDiceRolls): 
        """Determines if the current bid is truthful (correct) or a lie (have bid too high).

        Args:
            allDiceRolls (list[int]): A list containing ALL dice rolls for all players.

        Returns:
            bool: Returns True if the bid is accurate and False otherwise.
        """
        return self.count(allDiceRolls) >= self.numDice
