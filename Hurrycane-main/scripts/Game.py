import pygame
import Constants, Score, SceneManager, Player, StreetOne, Market, StreetTwo, Menu
import sys # SceneManager 02/11

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.score = Score.Score()
        self.player = Player.Player(self, Constants.SCREEN_WIDTH // 2, Constants.SCREEN_HEIGHT - 100, 'ariel') # vai ser definido dps do menu

        self.sceneManager = SceneManager.SceneManager('menu')
        self.menu = Menu.Menu(self.sceneManager)
        self.streetOne = StreetOne.StreetOne(self, self.sceneManager)
        self.market = Market.Market(self, self.sceneManager)
        self.streetTwo = StreetTwo.StreetTwo(self, self.sceneManager)

        self.states = {
                        'menu': self.menu,
                        'streetOne': self.streetOne,
                        'market': self.market, 
                        'streetTwo': self.streetTwo,
                        # 'defeat': self.defeat, 
                        # 'winner': self.winner
                       }
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            print(self.sceneManager.get_state())
            self.states[self.sceneManager.get_state()].run()
            # pygame.display.update()
            # self.clock.tick(Constants.FPS)
    

        # https://www.youtube.com/watch?v=r0ixaTQxsUI
