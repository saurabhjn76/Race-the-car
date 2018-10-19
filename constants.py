BOARDHEIGHT = 7
BOARDWIDTH = 7
TILESIZE = 92
WINDOWWIDTH = 900
WINDOWHEIGHT = 720
FENCEHEIGHT = 5
FENCEWIDTH = 2 * (TILESIZE - 2)
FPS = 20
ANIMATIONSPEED = 6
BLANK = None


# set of colors
#            R   G    B
GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE = (255, 255, 255)
DARKGREEN = (0, 155, 0)
RED = (255, 0, 0)
GREEN = (0, 190, 0)
BLUE = (0, 0, 235)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
DARKTURQUIOSE = (3, 54, 73)
BRIGHTBLUE = (0, 50, 255)
DARKGRAY = (40, 40, 40)
BLACK = (0, 0, 0)


BGCOLOR = DARKTURQUIOSE
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BOARDCOLOR = NAVYBLUE
BASICFONTSIZE = 30
BORDERCOLOR = BLACK
HIGHLIGHTCOLOR = BLUE
LIGHTBGCOLOR = BRIGHTBLUE

BUTTONTEXTCOLOR = BLACK
BUTTONCOLOR = WHITE
MESSAGECOLOR = WHITE


XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT - (BOARDHEIGHT - 1))) / 2)


UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"
JUPUP = "jumpupup"
JUPLEFT = "jumpupleft"
JUPRIGHT = "jumpupright"
JDOWNDOWN = "jumpdowndown"
JDOWNLEFT = "jumpdownleft"
JDOWNRIGHT = "jumpdownright"
JLEFTLEFT = "jumpleftleft"
JLEFTUP = "jumpleftup"
JLEFTDOWN = "jumpleftdown"
JRIGHTRIGHT = "jumprightright"
JRIGHTUP = "jumprightup"
JRIGHTDOWN = "jumprightdown"

carImg = pygame.image.load("car_11.png")
carImg1 = pygame.image.load("car_22.png")
flagImg = pygame.image.load("blue2.jpg")
flagImg1 = pygame.image.load("red2.jpg")
hmImg1 = pygame.image.load("hm2.jpg")

FENCELIMIT = 8  # The maximum numbr of fences a player can use