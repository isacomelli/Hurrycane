import pygame, sys
import Constants, Score, Hurrycane, SceneManager, Player, Ranking, Menu, RankingMenu, ControlsScreen, CharacterMenu, StreetOne, Market, StreetTwo, WinnerScreen, DefeatScreen

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.sceneManager = SceneManager.SceneManager('menu')
        self.score = Score.Score()
        self.sound_on = True
        # Atributos definidos depois
        self.hurrycane = None
        self.clock = None
        self.player = None

        self.states = {
            'menu': Menu.Menu(self),
            'rankingMenu': RankingMenu.RankingMenu(self), 
            'controlsScreen': ControlsScreen.ControlsScreen(self), 
            'characterMenu': CharacterMenu.CharacterMenu(self),
            # Atributos definidos depois 
            'streetOne': None,
            'market': None, 
            'streetTwo': None,
            'winnerScreen': None,
            'defeatScreen': None
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
                'size': (48, 18)
            },
            'water': {
                'name': 'water',
                'type': 'good',
                'speed': 0,
                'score': Constants.BIG_ITEM_SCORE,
                'size': (30, 80)
            },
            'food': {
                'name': 'food',
                'type': 'good',
                'speed': 0,
                'score': Constants.BIG_ITEM_SCORE,
                'size': (40, 72)
            },
            'med_kit': {
                'name': 'med_kit',
                'type': 'good',
                'speed': 0,
                'score': Constants.BIG_ITEM_SCORE,
                'size': (54, 58)
            },

            ##### BAD ITEMS
            'black_car': {
                'name': 'black_car',
                'type': 'bad',
                'speed': 0,
                'score': -Constants.BIG_ITEM_SCORE,
                'size': (Constants.CAR_WIDTH, Constants.CAR_HEIGHT)
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
                'size': (109, 105)
            },
            'alcool': {
                'name': 'alcool',
                'type': 'bad',
                'speed': 0,
                'score': -Constants.SMALL_ITEM_SCORE,
                'size': (20, 80)
            },
            'videogame': {
                'name': 'videogame',
                'type': 'bad',
                'speed': 0,
                'score': -Constants.SMALL_ITEM_SCORE,
                'size': (30, 48)
            },
            'cigarette': {
                'name': 'cigarette',
                'type': 'bad',
                'speed': 0,
                'score': -Constants.SMALL_ITEM_SCORE,
                'size': (30, 50)
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
                self.states['streetOne'] = StreetOne.StreetOne(self)
                self.states['market'] = Market.Market(self)
                self.states['streetTwo'] = StreetTwo.StreetTwo(self)
                self.hurrycane = Hurrycane.Hurrycane()

            if self.sceneManager.get_state() == 'menu':
                self.score = Score.Score()
            elif self.sceneManager.get_state() == 'winnerScreen':
                self.states['winnerScreen'] = WinnerScreen.WinnerScreen(self)
            elif self.sceneManager.get_state() == 'defeatScreen':
                self.states['defeatScreen'] = DefeatScreen.DefeatScreen(self)

