import pygame, sys
import Constants, Score, Hurrycane, SceneManager, Player, Ranking, Menu, RankingMenu, CharacterMenu, StreetOne, Market, StreetTwo, WinnerScreen
 # SceneManager 02/11

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.score = Score.Score()
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

        self.items = {
            ##### GOOD ITEMS
            'radio': {
                'name': 'radio',
                'type': 'good',
                'speed': 0,
                'score': Constants.SMALL_ITEM_SCORE,
                'size': (24, 53)
            },
            'lantern': {
                'name': 'lantern',
                'type': 'good',
                'speed': 0,
                'score': Constants.SMALL_ITEM_SCORE,
                'size': (48, 18) # / 8
            },
            'water': {
                'name': 'water',
                'type': 'good',
                'speed': 0,
                'score': Constants.BIG_ITEM_SCORE,
                'size': (30, 80) #proporcao = 3
            },
            'food': {
                'name': 'food',
                'type': 'good',
                'speed': 0,
                'score': Constants.BIG_ITEM_SCORE,
                'size': (40, 72) # proporcao = 1.80
            },
            'med_kit': {
                'name': 'med_kit',
                'type': 'good',
                'speed': 0,
                'score': Constants.BIG_ITEM_SCORE,
                'size': (54, 58) # 6.5
            },

            ##### BAD ITEMS
            'black_car': {
                'name': 'black_car',
                'type': 'bad',
                'speed': 0,
                'score': -Constants.BIG_ITEM_SCORE,
                'size': (Constants.CAR_WIDTH, Constants.CAR_HEIGHT) #proporcao = 2.20
            },
            'purple_car': {
                'name': 'purple_car',
                'type': 'bad',
                'speed': 0,
                'score': -Constants.BIG_ITEM_SCORE,
                'size': (Constants.CAR_WIDTH, Constants.CAR_HEIGHT)
            },
            'green_car': {
                'name': 'green_car',
                'type': 'bad',
                'speed': 0,
                'score': -Constants.BIG_ITEM_SCORE,
                'size': (Constants.CAR_WIDTH, Constants.CAR_HEIGHT)
            },
            'gray_car': {
                'name': 'gray_car',
                'type': 'bad',
                'speed': 0,
                'score': -Constants.BIG_ITEM_SCORE,
                'size': (Constants.CAR_WIDTH, Constants.CAR_HEIGHT)
            },
            'red_car': {
                'name': 'red_car',
                'type': 'bad',
                'speed': 0,
                'score': -Constants.BIG_ITEM_SCORE,
                'size': (Constants.CAR_WIDTH, Constants.CAR_HEIGHT)
            },
            'market_cart': {
                'name': 'market_cart',
                'type': 'bad',
                'speed': 0,
                'score': -Constants.BIG_ITEM_SCORE,
                'size': (95, 73)
            },
            'alcool': {
                'name': 'alcool',
                'type': 'bad',
                'speed': 0,
                'score': -Constants.SMALL_ITEM_SCORE,
                'size': (20, 80) #3
            },
            'videogame': {
                'name': 'videogame',
                'type': 'bad',
                'speed': 0,
                'score': -Constants.SMALL_ITEM_SCORE,
                'size': (30, 48) #1.54
            },
            'cigarette': {
                'name': 'cigarette',
                'type': 'bad',
                'speed': 0,
                'score': -Constants.SMALL_ITEM_SCORE,
                'size': (30, 50) #1.64
            },
            'city_hole': {
                'name': 'city_hole',
                'type': 'bad',
                'speed': 0,
                'score': -Constants.SMALL_ITEM_SCORE,
                'size': (60, 25)
            },
            'forest_hole': {
                'name': 'forest_hole',
                'type': 'bad',
                'speed': 0,
                'score': -Constants.SMALL_ITEM_SCORE,
                'size': (75, 50)
            }
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

            if self.sceneManager.get_previous_state() == 'streetTwo':
                self.states['winnerScreen'] = WinnerScreen.WinnerScreen(self.sceneManager, self.states['characterMenu'].get_character(), self.score.get_score())

            if self.sceneManager.get_state() == 'menu':
                self.score = Score.Score()
