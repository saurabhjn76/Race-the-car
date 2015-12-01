import sys,pygame,random
from pygame.locals import *

BOARDHEIGHT=7
BOARDWIDTH=7
TILESIZE=92
WINDOWWIDTH=900
WINDOWHEIGHT=720
FENCEHEIGHT=5
FENCEWIDTH=2*(TILESIZE-2)
FPS=20
ANIMATIONSPEED=6
BLANK=None


# set of colors
#            R   G    B
GRAY    = (100, 100, 100)
NAVYBLUE= ( 60, 60, 100)
WHITE   = (255, 255, 255)
RED     = (255,  0,   0)
GREEN   = (0  ,190,0)
BLUE    = (0,    0 , 235)
YELLOW  = (255, 255,0)
ORANGE  = (255, 128,0)
PURPLE  = (255,0, 255)
CYAN    = ( 0, 255, 255)
DARKTURQUIOSE=(3,54,73)
BRIGHTBLUE=(0,50,255)
BLACK=(0,0,0)




BGCOLOR=DARKTURQUIOSE
TILECOLOR=GREEN
TEXTCOLOR=WHITE
BOARDCOLOR=NAVYBLUE
BASICFONTSIZE=20
BORDERCOLOR=BLACK
HIGHLIGHTCOLOR=BLUE
LIGHTBGCOLOR=BRIGHTBLUE

BUTTONTEXTCOLOR=BLACK
BUTTONCOLOR=WHITE
MESSAGECOLOR=WHITE


XMARGIN=int((WINDOWWIDTH-(TILESIZE*BOARDWIDTH+(BOARDWIDTH-1)))/2)
YMARGIN=int((WINDOWHEIGHT-(TILESIZE*BOARDHEIGHT-(BOARDHEIGHT-1)))/2)


UP='up'
DOWN='down'
LEFT='left'
RIGHT='right'
JUPUP='jumpupup'
JUPLEFT='jumpupleft'
JUPRIGHT='jumpupright'
JDOWNDOWN='jumpdowndown'
JDOWNLEFT='jumpdownleft'
JDOWNRIGHT='jumpdownright'
JLEFTLEFT='jumpleftleft'
JLEFTUP='jumpleftup'
JLEFTDOWN='jumpleftdown'
JRIGHTRIGHT='jumprightright'
JRIGHTUP='jumprightup'
JRIGHTDOWN='jumprightdown'

carImg=pygame.image.load('car_11.png')
carImg1=pygame.image.load('car_22.png')

player1Fence=[] # records the position of the fences by player1
player2Fence=[] # records the position of the fences by player2


def main():
	global FPSCLOCK,DISPLAYSURF,BASICFONT,FENCE_SURF,FENCE_RECT,MOVE_SURF,MOVE_RECT,SOLVE_SURF,SOLVE_RECT
	pygame.init()
	FPSCLOCK=pygame.time.Clock()
	mousex=0
	mousey=0 # co-ordinates of mouse events
	playerChance=1 #chance of the player by default=1
	DISPLAYSURF=pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
	pygame.display.set_caption('Race the Car')
	BASICFONT=pygame.font.Font('freesansbold.ttf',BASICFONTSIZE)
	textSurfaceObj=BASICFONT.render("Race the car....",True,BLACK,WHITE)
	textRectObj=textSurfaceObj.get_rect()
	textRectObj.center=(450,10)
	mainBoard=getStartingBoard()
	# Store the option button add their rectangle in Options
	FENCE_SURF,FENCE_RECT =makeText('FENCE',BUTTONTEXTCOLOR,BUTTONCOLOR,WINDOWWIDTH-120,WINDOWHEIGHT-450)
	MOVE_SURF,MOVE_RECT =makeText('MOVE',BUTTONTEXTCOLOR,BUTTONCOLOR,WINDOWWIDTH-120,WINDOWHEIGHT-410)
	checkForQuit()
	fenceClicked=False
	moveClicked=False
	slideTo=None # the direction to which any slide should slide
	while True:
		msg='Player turn-> ' + str(playerChance) 
		mouseClicked=False
		drawBoard(mainBoard,msg)
		hasWon(mainBoard)
		DISPLAYSURF.blit(textSurfaceObj,textRectObj)
		for event in pygame.event.get():
			if event.type==QUIT or(event.type==KEYUP and event.key==K_ESCAPE):
				terminate()
			elif event.type==MOUSEMOTION:
				mousex,mousey=event.pos
			elif event.type==MOUSEBUTTONUP:
				mousex,mousey=event.pos
				mouseClicked=True
			spotx,spoty=getSpotClicked(mainBoard,mousex,mousey)
		if(spotx,spoty)==(None,None):
			# check for the button pressed
			if FENCE_RECT.collidepoint((mousex,mousey)) and mouseClicked:
				# Fence Button pressed
				fenceClicked=True
				moveClicked=False
				mouseClicked=False
			if MOVE_RECT.collidepoint((mousex,mousey)):
				# MOVe button pressed
				fenceClicked=False
				moveClicked=True
				mouseClicked=False
		else:
			playerx,playery=getPlayerPosition(mainBoard,playerChance)
			if playerChance==1:
				onumber=2
			else:
				onumber=1
			oplayerx,oplayery=getPlayerPosition(mainBoard,onumber)
			if spotx!=oplayerx or spoty!=oplayery:
				if spotx==playerx+1 and spoty==playery :
					slideTo=LEFT
				elif spotx==playerx-1 and spoty==playery:
					slideTo=RIGHT
				elif spotx==playerx and spoty==playery-1:
					slideTo=DOWN
				elif spotx==playerx and spoty==playery+1:
					slideTo=UP

			if oplayerx==playerx+1 and oplayery==playery:
				if  spotx==playerx+2 and spoty==playery:
					slideTo=JLEFTLEFT
				if spotx==playerx+1 and spoty==playery-1:
					slideTo=JLEFTDOWN
				if spotx==playerx+1 and spoty==playery+1:
					slideTo=JLEFTUP

			elif oplayerx==playerx-1 and oplayery==playery:
				if  spotx==playerx-2 and spoty==playery:
					slideTo=JRIGHTRIGHT
				if spotx==playerx-1 and spoty==playery-1:
					slideTo=JRIGHTDOWN
				if spotx==playerx-1 and spoty==playery+1:
					slideTo=JRIGHTUP
				
			elif oplayerx==playerx and oplayery==playery-1:
				if spotx==playerx and spoty==playery-2:
					slideTo=JDOWNDOWN
				if spoty==playery-1 and spotx==playerx-1:
					slideTo=JDOWNRIGHT
				if spoty==playery-1 and spotx==playerx+1:
					slideTo=JDOWNLEFT	


			elif oplayerx==playerx and oplayery==playery+1:
				if (spotx==playerx and spoty==playery+2):
					slideTo=JUPUP
				if spoty==playery+1 and spotx==playerx-1:
					slideTo=JUPRIGHT
				if spoty==playery+1 and spotx==playerx+1:
					slideTo=JUPLEFT

			#print slideTo
			if  fenceClicked:
				drawBoard(mainBoard,'Player '+ str(playerChance)+' put the fence')
				drawFenceHighlight(spotx,spoty,HIGHLIGHTCOLOR,mousex,mousey)
				pygame.draw.rect(DISPLAYSURF,BLACK,FENCE_RECT,2)
				if mouseClicked:
					if fencePutting(spotx,spoty,playerChance,mousex,mousey): 
						if playerChance==1:
							playerChance=2
						elif playerChance==2:
							playerChance=1
						fenceClicked=False


				#tile pressed
			elif  moveClicked:
				drawBoard(mainBoard,'Player '+ str(playerChance)+' to move the car')
				pygame.draw.rect(DISPLAYSURF,BLACK,MOVE_RECT,2)
				if slideTo and not mouseClicked:
					drawHighlightTile(spotx,spoty,BLACK)
				if slideTo and mouseClicked:
					moveAnimation(mainBoard,slideTo,playerChance)
					makeMove(mainBoard,slideTo,playerChance)
					if playerChance==1:
						playerChance=2
					elif playerChance==2:
						playerChance=1
					moveClicked=False



		pygame.display.update()
		slideTo=None
		FPSCLOCK.tick(FPS)



def terminate():
	pygame.quit()
	sys.exit()
def checkForQuit():
	for event in pygame.event.get(QUIT):
		terminate()
	for event in pygame.event.get(KEYUP):
		if event.key==K_ESCAPE:
			terminate()
		pygame.event.post(event)

def getLeftTopOfTile(tileX,tileY):
	left=XMARGIN+(tileX*TILESIZE)+(tileX-1)
	top=YMARGIN+(tileY*TILESIZE)+(tileY-1)
	return(left,top)
def getStartingBoard():
	# Returns the board data structure with tiles in it
	state=3
	board=[]
	for x in range(BOARDWIDTH):
		column=[]
		for y in range(BOARDHEIGHT):
			column.append(state)
		board.append(column)
	board[BOARDWIDTH-int(BOARDWIDTH/2)-1][0]=2
	board[BOARDWIDTH-int(BOARDWIDTH/2)-1][BOARDHEIGHT-1]=1
	return board 
def hasWon(board):
	# checks for winning player
	color1=LIGHTBGCOLOR
	color2=BGCOLOR
	if board[BOARDWIDTH-int(BOARDWIDTH/2)-1][0]==1:
		#player 1 has won show it and exit
		for i in range(13):
			color1,color2=color2,color1
			drawBoard(board,'Player 1 has won',color1)
			pygame.display.update()
			pygame.time.wait(500)
		terminate()
	elif board[BOARDWIDTH-int(BOARDWIDTH/2)-1][BOARDHEIGHT-1]==2:
		#player 2 has won show it and exit
		#player 1 has won show it and exit
		for i in range(13):
			color1,color2=color2,color1
			drawBoard(board,'Player 2 has won',color1)
			pygame.display.update()
			pygame.time.wait(500)
		terminate()
def drawTile(tileX,tileY,number,adjx=0,adjy=0):
	# draw a tile at tileX ad tileY
	# pixels over determined by adjx and adjy
	left,top=getLeftTopOfTile(tileX,tileY)
	pygame.draw.rect(DISPLAYSURF,TILECOLOR,(left+adjx,top+adjy,TILESIZE,TILESIZE))
	if number==2 or number==1:
		
		textSurf=BASICFONT.render(str(number),True,TEXTCOLOR)
		textRect=textSurf.get_rect()
		textRect.center=left+adjx,top+adjy
		if number==2:
			adjx=11
			adjy=11
			textRect.center=left+adjx,top+adjy
			DISPLAYSURF.blit(carImg1,textRect)
		else:
			adjx=4
			adjy=6
			textRect.center=left+adjx,top+adjy
			DISPLAYSURF.blit(carImg,textRect)

	for position in player1Fence:
		drawFenceHighlight(position[0][0],position[0][1],BLACK,position[1][0],position[1][1],9)
	for position in player2Fence:
		drawFenceHighlight(position[0][0],position[0][1],BLACK,position[1][0],position[1][1],9)
	
def getPlayerPosition(board,number):
	# return the x,y co=ordinates of the blank box
	for x in range(BOARDWIDTH):
		for y in range(BOARDHEIGHT):
			if board[x][y]==number:
				return (x,y)
def makeMove(board,move,number):
	# just makes a move not checks if it's valid or not
	
	playerx,playery=getPlayerPosition(board,number)
	if move==UP :
		board[playerx][playery],board[playerx][playery+1]=board[playerx][playery+1],board[playerx][playery]
	elif move==DOWN:
		board[playerx][playery],board[playerx][playery-1]=board[playerx][playery-1],board[playerx][playery]
	elif move==RIGHT:
		board[playerx][playery],board[playerx-1][playery]=board[playerx-1][playery],board[playerx][playery]
	elif move==LEFT:
		board[playerx][playery],board[playerx+1][playery]=board[playerx+1][playery],board[playerx][playery]

	elif move==JUPUP:
		board[playerx][playery],board[playerx][playery+2]=board[playerx][playery+2],board[playerx][playery]
	elif move==JUPLEFT:
		board[playerx][playery],board[playerx+1][playery+1]=board[playerx+1][playery+1],board[playerx][playery]
	elif move==JUPRIGHT:
		board[playerx][playery],board[playerx-1][playery+1]=board[playerx-1][playery+1],board[playerx][playery]

	elif move==JDOWNDOWN:
		board[playerx][playery],board[playerx][playery-2]=board[playerx][playery-2],board[playerx][playery]
	elif move==JDOWNLEFT:
		board[playerx][playery],board[playerx+1][playery-1]=board[playerx+1][playery-1],board[playerx][playery]
	elif move==JDOWNRIGHT:
		board[playerx][playery],board[playerx-1][playery-1]=board[playerx-1][playery-1],board[playerx][playery]


	elif move==JRIGHTRIGHT:
		board[playerx][playery],board[playerx-2][playery]=board[playerx-2][playery],board[playerx][playery]
	elif move==JRIGHTUP:
		board[playerx][playery],board[playerx-1][playery+1]=board[playerx-1][playery+1],board[playerx][playery]
	elif move==JRIGHTDOWN:
		board[playerx][playery],board[playerx-1][playery-1]=board[playerx-1][playery-1],board[playerx][playery]

	elif move==JLEFTLEFT:
		board[playerx][playery],board[playerx+2][playery]=board[playerx+2][playery],board[playerx][playery]
	elif move==JLEFTUP:
		board[playerx][playery],board[playerx+1][playery+1]=board[playerx+1][playery+1],board[playerx][playery]
	elif move==JLEFTDOWN:
		board[playerx][playery],board[playerx+1][playery-1]=board[playerx+1][playery-1],board[playerx][playery]
	pygame.display.update()
	FPSCLOCK.tick(FPS)
		
	
def drawBoard(board,message,color1=BGCOLOR):
	DISPLAYSURF.fill(color1)
	if message:
	 	textSurf,textRect=makeText(message,MESSAGECOLOR,color1,5,5)
	 	DISPLAYSURF.blit(textSurf,textRect)
	for tilex in range(len(board)):
		for tiley in range(len(board[0])):
			if board[tilex][tiley]:
				drawTile(tilex,tiley,board[tilex][tiley])
	left,top=getLeftTopOfTile(0,0)
	width=BOARDWIDTH*TILESIZE
	height=BOARDHEIGHT*TILESIZE
	pygame.draw.rect(DISPLAYSURF,BORDERCOLOR,(left-5,top-5,width+11,height+11),6)
	DISPLAYSURF.blit(FENCE_SURF,FENCE_RECT)
	DISPLAYSURF.blit(MOVE_SURF,MOVE_RECT)
	#DISPLAYSURF.blit(SOLVE_SURF,SOLVE_RECT)
def getSpotClicked(board,x,y):
	# from x,and y pixel co-ordinates get x and y box co-odnate
	for tileX in range(len(board)):
		for tileY in range(len(board[0])):
			left,top=getLeftTopOfTile(tileX,tileY)
			tileRect=pygame.Rect(left,top,TILESIZE,TILESIZE)
			if tileRect.collidepoint(x,y):
				return (tileX,tileY)
	return (None,None)
def drawFenceHighlight(tileX,tileY,highLightColor,mousex,mousey,fence_thickness=4):
	left,top=getLeftTopOfTile(tileX,tileY)
	Ox,Oy=getLeftTopOfTile(0,0)
	if mousex>mousey and mousex+mousey<(top+left+TILESIZE):
		if left<=Ox+6*TILESIZE and top!=Oy:
			pygame.draw.line(DISPLAYSURF,highLightColor,(left,top),(left+2*TILESIZE,top),fence_thickness)
		elif left>Ox+6*TILESIZE and top!=Oy:
			pygame.draw.line(DISPLAYSURF,highLightColor,(Ox+5*TILESIZE+5,top),(Ox+7*TILESIZE+2,top),fence_thickness)

	elif mousex>mousey and mousex+mousey>(top+left+TILESIZE):
		if top<=Oy+6*TILESIZE and left<Ox+6*TILESIZE:
			pygame.draw.line(DISPLAYSURF,highLightColor,(left+TILESIZE,top),(left+TILESIZE,top+2*TILESIZE),fence_thickness)
		elif top>Oy+6*TILESIZE and left<Ox+6*TILESIZE:
			pygame.draw.line(DISPLAYSURF,highLightColor,(left+TILESIZE,Oy+5*TILESIZE+1),(left+TILESIZE,Oy+7*TILESIZE+1),fence_thickness)

	elif mousex<mousey and mousex+mousey<(top+left+TILESIZE):
		if top<=Oy+6*TILESIZE and left!=Ox:
			pygame.draw.line(DISPLAYSURF,highLightColor,(left,top),(left,top+2*TILESIZE),fence_thickness)
		elif top>Oy+6*TILESIZE and left!=Ox:
			pygame.draw.line(DISPLAYSURF,highLightColor,(left,Oy+5*TILESIZE+1),(left,Oy+7*TILESIZE+1),fence_thickness)

	elif mousex<mousey and mousex+mousey>(top+left+TILESIZE):
		if left<=Ox+6*TILESIZE and top<Oy+6*TILESIZE:
			pygame.draw.line(DISPLAYSURF,highLightColor,(left,top+TILESIZE),(left+2*TILESIZE,top+TILESIZE),fence_thickness)
		elif left>Ox+6*TILESIZE and top<Oy+6*TILESIZE:
			pygame.draw.line(DISPLAYSURF,highLightColor,(Ox+5*TILESIZE,top+TILESIZE),(Ox+7*TILESIZE+2,top+TILESIZE),fence_thickness)

def makeText(text,color,bgcolor,top,left):
	# create the surface and rect object for some text
	textSurf=BASICFONT.render(text,True,color,bgcolor)
	textRect=textSurf.get_rect()
	textRect.topleft=(top,left)
	return (textSurf,textRect)
def moveAnimation(board,direction,number,message='',jx=0,jy=0):
	playerx,playery=getPlayerPosition(board,number)
	drawBoard(board,message)
	baseSurf=DISPLAYSURF.copy() 
	# Drawing a base surface for temporary movement
	moveLeft,moveTop=getLeftTopOfTile(playerx,playery)
	pygame.draw.rect(baseSurf,TILECOLOR,(moveLeft,moveTop,TILESIZE-2,TILESIZE-4))
	# checking for jump conditions
	if direction==JUPUP:
		moveAnimation(board,UP,number)
		moveAnimation(board,UP,number,'',0,1)
	elif direction==JUPRIGHT:
		moveAnimation(board,UP,number)
		moveAnimation(board,RIGHT,number,'',0,1)
	elif direction==JUPLEFT:
		moveAnimation(board,UP,number)
		moveAnimation(board,LEFT,number,'',0,1)

	elif direction==JDOWNDOWN:
		moveAnimation(board,DOWN,number)
		moveAnimation(board,DOWN,number,'',0,-1)
	elif direction==JDOWNLEFT:
		moveAnimation(board,DOWN,number)
		moveAnimation(board,LEFT,number,'',0,-1)
	elif direction==JDOWNRIGHT:
		moveAnimation(board,DOWN,number)
		moveAnimation(board,RIGHT,number,'',0,-1)
		
	elif direction==JRIGHTRIGHT:
		moveAnimation(board,RIGHT,number)
		moveAnimation(board,RIGHT,number,'',-1,0)
	elif direction==JRIGHTUP:
		moveAnimation(board,RIGHT,number)
		moveAnimation(board,UP,number,'',-1,0)
	elif direction==JRIGHTDOWN:
		moveAnimation(board,RIGHT,number)
		moveAnimation(board,DOWN,number,'',-1,0)

	elif direction==JLEFTLEFT:
		moveAnimation(board,LEFT,number)
		moveAnimation(board,LEFT,number,'',1,0)
	elif direction==JLEFTUP:
		moveAnimation(board,LEFT,number)
		moveAnimation(board,UP,number,'',1,0)
	elif direction==JLEFTDOWN:
		moveAnimation(board,LEFT,number)
		moveAnimation(board,DOWN,number,'',1,0)

		drawBoard(board)
		# for double animation if required 
	moveLeft,moveTop=getLeftTopOfTile(playerx+jx,playery+jy)



	for i in range(0,TILESIZE,ANIMATIONSPEED):
		checkForQuit()
		DISPLAYSURF.blit(baseSurf,(0,0))
		if number==1:
			if direction==UP:
				#drawTile(movex,movey,board[movex][movey],0,-i)
				DISPLAYSURF.blit(carImg,(moveLeft,moveTop+i))
			elif direction==DOWN:
				#drawTile(movex,movey,board[movex][movey],0,i)
				DISPLAYSURF.blit(carImg,(moveLeft,moveTop-i))
			elif direction==RIGHT:
				#drawTile(movex,movey,board[movex][movey],i,0)
				DISPLAYSURF.blit(carImg,(moveLeft-i,moveTop))
			elif direction==LEFT:
				#drawTile(movex,movey,board[movex][movey],-i,0)
				DISPLAYSURF.blit(carImg,(moveLeft+i,moveTop))
		else:
			if direction==UP:
				#drawTile(movex,movey,board[movex][movey],0,-i)
				DISPLAYSURF.blit(carImg1,(moveLeft,moveTop+i))
			elif direction==DOWN:
				#drawTile(movex,movey,board[movex][movey],0,i)
				DISPLAYSURF.blit(carImg1,(moveLeft,moveTop-i))
			elif direction==RIGHT:
				#drawTile(movex,movey,board[movex][movey],i,0)
				DISPLAYSURF.blit(carImg1,(moveLeft-i,moveTop))
			elif direction==LEFT:
				#drawTile(movex,movey,board[movex][movey],-i,0)
				DISPLAYSURF.blit(carImg1,(moveLeft+i,moveTop))	
		pygame.display.update()
		FPSCLOCK.tick(FPS)

def fencePutting(tileX,tileY,playerChance,mousex,mousey):
	# puts the fence on the board and record it's positon in the array
	left,top=getLeftTopOfTile(tileX,tileY)
	Ox,Oy=getLeftTopOfTile(0,0)
	flag=0   # fence not on the border of the board then only append else return false
	if mousex>mousey and mousex+mousey<(top+left+TILESIZE) and top!=Oy:
		flag=1
	if mousex>mousey and mousex+mousey>(top+left+TILESIZE) and left<Ox+6*TILESIZE:
		flag=1
	if mousex<mousey and mousex+mousey<(top+left+TILESIZE) and left!=Ox:
		flag=1
	if mousex<mousey and mousex+mousey>(top+left+TILESIZE) and top<Oy+6*TILESIZE:
		flag=1

	if playerChance==1 and flag==1:
		player1Fence.append(((tileX,tileY),(mousex,mousey)))
		return True
	elif playerChance==2 and flag==1:
		player2Fence.append(((tileX,tileY),(mousex,mousey)))
		return True
	return False
def drawHighlightTile(tileX,tileY,highLightColor,tile_thickness=4):
	# highlight the box where car may move based on mouse hover
	left,top=getLeftTopOfTile(tileX,tileY)
	pygame.draw.rect(DISPLAYSURF,highLightColor,(left-4,top-4,TILESIZE+5,TILESIZE+5),tile_thickness)
def gameWonAnimation():
	color1=LIGHTBGCOLOR
	color2=BGCOLOR

	for i in range(13):
		color1,color2=color2,color1
		DISPLAYSURF.fill(color1)

if __name__=='__main__':
	main()

