import pygame
import Constants, Score, SceneManager, Player, StreetOne, Market, StreetTwo, Item

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.score = Score.Score()
        self.player = Player.Player(self, Constants.SCREEN_WIDTH // 2, Constants.SCREEN_HEIGHT - 100, 'img\\ariel.png') # vai ser definido dps do menu
        
        # self.sceneManager = SceneManager.SceneManager('StreetOne')
        #self.sceneManager = SceneManager.SceneManager('Market')
        # self.StreetOne = StreetOne.StreetOne(self)
        # self.Market = Market.Market(self)
        # self.StreetTwo = StreetTwo.StreetTwo(self)
    
        self.states = {
        #    'menu': self.menu, 
            'StreetOne': StreetOne.StreetOne(self),
            'Market': Market.Market(self), 
            'StreetTwo': StreetTwo.StreetTwo(self)
        #    'defeat': self.defeat, 
        #    'winner': self.winner
        }

    def run(self):
        #scene manager 
        #https://www.youtube.com/watch?v=r0ixaTQxsUI
        # self.states[self.sceneManager.get_state()].run()

        for state_name, state in self.states.items():
            state.run()
        # StreetOne.StreetOne(self).run()
        # Market.Market(self).run()
        # StreetTwo.StreetTwo(self).run()