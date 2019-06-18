class AnagramClue:
    def __init__(self, text, sol, ch, loc):
        self.clue_text = text
        self.solution = sol
        self.challenge = ch
        self.location = loc

class CoordClue:
    def __init__(self, num, text, loc):
        self.id = num
        self.clue_text = text
        self.location = loc

class CrypticClue:
    def __init__(self, text, short, loc, key):
        self.clue_text = text
        self.short_ver = short
        self.location = loc
        self.key = key
