class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        if not secret or not guess:
            return "0A0B"
        bulls, cows = 0, 0
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bulls += 1
        tmps, tmpg = collections.Counter(secret), collections.Counter(guess)
        cows = sum((tmps & tmpg).values()) - bulls
        return str(bulls) + "A" + str(cows) + "B"
        