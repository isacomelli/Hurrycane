import pygame
import Constants, Score, SceneManager, Player, StreetOne, Market, StreetTwo, Menu, RankingMenu, CharacterMenu, WinnerScreen
import sys # SceneManager 02/11

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.score = Score.Score()
        self.player = None

        self.sceneManager = SceneManager.SceneManager('menu')

        self.states = {
                        'menu': Menu.Menu(self.sceneManager),
                        'rankingMenu': RankingMenu.RankingMenu(self.sceneManager, self.score),
                        'characterMenu': CharacterMenu.CharacterMenu(self.sceneManager), 
                        'streetOne': None,
                        'market': None, 
                        'streetTwo': None,
                        'winnerScreen': None
                       }

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.states[self.sceneManager.get_state()].run()

            if self.sceneManager.get_state() == 'streetOne':
                self.player = Player.Player(self, Constants.SCREEN_WIDTH // 2, Constants.SCREEN_HEIGHT - 100, self.states['characterMenu'].get_character())
                self.states['streetOne'] = StreetOne.StreetOne(self, self.sceneManager)
                self.states['market'] = Market.Market(self, self.sceneManager)
                self.states['streetTwo'] = StreetTwo.StreetTwo(self, self.sceneManager)
                self.states['winnerScreen'] = WinnerScreen.WinnerScreen(self.sceneManager, self.score, self, self.states['rankingMenu'])
                                                                      





        # https://www.youtube.com/watch?v=r0ixaTQxsUI
