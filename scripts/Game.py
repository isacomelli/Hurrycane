import pygame
from scripts import Constants, Score, SceneManager, Player, StreetOne, Market, StreetTwo

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.score = Score.Score()
        self.player = Player.Player(self, Constants.SCREEN_WIDTH // 2, Constants.SCREEN_HEIGHT - 100, "img\\ariel.png") # vai ser definido dps do menu
        
        # self.sceneManager = SceneManager.SceneManager('streetOne')
        # self.sceneManager = SceneManager.SceneManager('market')
        # self.streetOne = StreetOne.StreetOne(self)
        # self.market = Market.Market(self)
        # self.market = Market.Market(self.screen, self.sceneManager)
    
        # self.states = {
        #             #   'menu': self.menu, 
        #               'streetOne': self.streetOne, 
        #               'market': self.market, 
        #             #   'street2': self.street2, 
        #             #   'defeat': self.defeat, 
        #             #   'winner': self.winner
        #               }

    def run(self):
        #scene manager 
        #https://www.youtube.com/watch?v=r0ixaTQxsUI
        # self.states[self.sceneManager.get_state()].run()
        # self.streetOne.run()
        # self.market.run()

        StreetOne.StreetOne(self).run()
        Market.Market(self).run()
        StreetTwo.StreetTwo(self).run()