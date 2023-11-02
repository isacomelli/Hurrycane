import pygame

class Score:
    score = 0
    def regularScore(self):
        self.score = self.score + 0.1

    ## Vai variar com o item.. tem q mexer dps
    def addScore(self):
        self.score += 100