import pygame, sys
import Constants, Score, Hurrycane, SceneManager, Player, Ranking, Menu, RankingMenu, CharacterMenu, StreetOne, Market, StreetTwo, WinnerScreen
 # SceneManager 02/11

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.score = Score.Score()
        # self.hurrycane = Hurrycane.Hurrycane()
        self.hurrycane = None
        self.clock = None
        self.player = None

        self.sceneManager = SceneManager.SceneManager('menu')

        self.states = {
                        'menu': Menu.Menu(self.sceneManager),
                        'rankingMenu': RankingMenu.RankingMenu(self.sceneManager),
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

            if self.sceneManager.get_previous_state() == 'characterMenu':
                self.player = Player.Player(self, self.states['characterMenu'].get_character())
                self.states['streetOne'] = StreetOne.StreetOne(self, self.sceneManager)
                self.states['market'] = Market.Market(self, self.sceneManager)
                self.states['streetTwo'] = StreetTwo.StreetTwo(self, self.sceneManager)
                self.hurrycane = Hurrycane.Hurrycane()

            elif self.sceneManager.get_previous_state() == 'streetTwo':
                self.states['winnerScreen'] = WinnerScreen.WinnerScreen(self.sceneManager, self.score.get_score())

            if self.sceneManager.get_state() == 'menu':
                self.score = Score.Score()
                
        # https://www.youtube.com/watch?v=r0ixaTQxsUI
