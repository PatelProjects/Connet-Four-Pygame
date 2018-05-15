import sys, pygame
import random
from pygame.locals import *
from WinFunction1 import *
from WinFunction2 import *
from WinFunction3 import *
from WinFunction4 import *
from ai import *


pygame.init()

Xscreen, Yscreen = 640, 480  #Make the screen size
windowSize = (Xscreen, Yscreen) 
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption('Connect Four')


#The following line define a few colors that I am going to be using throughout this program
RED = (255 , 0 , 0)
PURPLE = (230 , 60 , 250)
BLACK = ('black')
LIGHTBLUE = (0, 50, 255)
WHITE = (255, 255, 255)

screen.fill(LIGHTBLUE) #Makes the background of the screen lightblue

BOXSIZE = 50 #Size of each box in the game board

StartImg = pygame.image.load("connectfourimg.jpg") #Loads the image the appears on the starting menu
StartImg = pygame.transform.scale(StartImg ,(300, 300)) #Resizes the image to an approprite size

TwoPeopleIMG = pygame.image.load("TwoPeople.png")
TwoPeopleIMG = pygame.transform.scale(TwoPeopleIMG , (200 , 200))

ComputerIMG = pygame.image.load("Computer.jpg")
ComputerIMG = pygame.transform.scale(ComputerIMG, (200 , 200))

REDTOKENIMG = pygame.image.load('4row_red.png') #Loads image for red token 
REDTOKENIMG = pygame.transform.smoothscale(REDTOKENIMG, (BOXSIZE, BOXSIZE)) #Scales the token image to appropriate size

#Next two lines are the same as above 2 lines but for the black token 
BLACKTOKENIMG = pygame.image.load('4row_black.png') 
BLACKTOKENIMG = pygame.transform.smoothscale(BLACKTOKENIMG, (BOXSIZE, BOXSIZE))

#Loads the boxes that the board is going to be made out of and scales them to size
BOARDIMG = pygame.image.load('4row_board.png')
BOARDIMG = pygame.transform.smoothscale(BOARDIMG, (BOXSIZE, BOXSIZE))

#The following variables keep track of how many token are in each collum
colOne = 0
colTwo = 0
colThree = 0
colFour = 0
colFive = 0
colSix = 0
colSeven = 0

#The follwing list will keep track of the player that plays a token in each of the collums 
colOneMoves = []
colTwoMoves = []
colThreeMoves = [] 
colFourMoves = []
colFiveMoves = []
colSixMoves = []
colSevenMoves = []

#allMoves is a list of all the moves done by eaither player
allMoves = [colOneMoves , colTwoMoves , colThreeMoves , colFourMoves , colFiveMoves , colSixMoves , colSevenMoves]

#repeat variables are used in special cases when a turn is to be repeated because of an illegal move
repeatBlack = False

FirstGame = True

#Keeps track of red's score
RedScore = 0

#Keeps track of black's score
BlackScore = 0

#The following two functions are used to determine of if the mouses current position intersects with a button on the screen
def intersectsX(x , a , b):
    if x >= a and x <= b:
        return True
    return False
    
def intersectsY(y , a , b):
    if y >= a and y <= b:
        return True
    return False

#The following are four possible menus that the code can go through. Each part can only be viewed under certain circumstances.
FirstWindow = True
SecondWindow = True 
ThirdWindow = True
FourthWindow = True

clock = pygame.time.Clock()

#variable that is used to check if it is the first game played in a session. 
FirstGame = True

#when the variable win is set to true, it would mean that a player has won and so the code will exit. 
win = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    
    while FirstWindow == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
                
        screen.blit(StartImg , (175 , 30)) #Places the image in the center of the first menu
        pygame.draw.rect(screen , RED , (270 , 350 , 100, 50))#Draws the "start" button
        myriadProFont = pygame.font.SysFont("Myriadcl Pro", 48) 
        PlayText = myriadProFont.render("Play!" , 1 , (255, 255, 255), (255, 0, 0)) #Print "start" in the button
        screen.blit(PlayText , (280 , 355)) #Location if the start button

        mousePosition = pygame.mouse.get_pos() #gets mouse position

        x = mousePosition[0]
        y = mousePosition[1]

        intX = intersectsX(x , 270 , 370) #checks is x coordinate of the mouse is in the range of the x values of he button
        intY = intersectsY(y , 350 , 400) #does the same as above except for the y values

        #If both of the intersections are true than the following lines basicallly make it so that if you mouse over the button it changes color
        if intX == True and intY == True:
            pygame.draw.rect(screen , PURPLE , (270 , 350 , 100, 50))
            PlayText = myriadProFont.render("Play!" , 1 , (255, 255, 255), (230, 60, 250))
            screen.blit(PlayText , (280 , 355))
            if event.type == MOUSEBUTTONDOWN:
                #If the button is pressed then the current window will be set to false and the code will move on to the next window
                screen.fill(LIGHTBLUE)
                FirstWindow = False

        pygame.display.update()
        clock.tick(30)

    while SecondWindow == True and FirstWindow == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        
        # Places 2 images on the screen, similar to how the last image on the previous image was placed
        screen.blit(TwoPeopleIMG , (100 , 100))
        screen.blit(ComputerIMG , (350 , 100))
        
        #Draws 2 more buttons. 1 that says "vs. player" and one that says "vs. comp"
        pygame.draw.rect(screen , RED , (120 , 350 , 150 , 70))
        pygame.draw.rect(screen , RED , (370 , 350 , 150 , 70))
        myriadProFont = pygame.font.SysFont("Myriadcl Pro", 38)
        PlayerText = myriadProFont.render("vs. Player" , 1 , (255 , 255 , 255), (255 , 0 , 0))
        screen.blit(PlayerText , (130 , 370))
        AiText = myriadProFont.render("vs. Comp" , 1 , (255 , 255 , 255), (255 , 0 , 0))
        screen.blit(AiText , (390 , 370))

        #The following lines are the same concept as from the previous button in the other window. If you mouse over the button it will change color
        mousePosition = pygame.mouse.get_pos()

        x = mousePosition[0]
        y = mousePosition[1]
            
        intXOne = intersectsX(x , 120 , 270)   
        intYOne = intersectsY(y , 350 , 410)
        
        if intXOne == True and intYOne == True:
            pygame.draw.rect(screen , PURPLE , (120 , 350 , 150 , 70))
            PlayerText = myriadProFont.render("vs. Player" , 1 , (255 , 255 , 255), (230, 60, 250))
            screen.blit(PlayerText , (130 , 370))
            if event.type == MOUSEBUTTONDOWN:
                screen.fill(LIGHTBLUE)
                SecondWindow = False
            
        intXTwo = intersectsX(x , 370 , 520)  
        intYTwo = intersectsY(y , 350 , 410)        
            
        if intXTwo == True and intYTwo == True:
            pygame.draw.rect(screen , PURPLE , (370 , 350 , 150 , 70))
            PlayerText = myriadProFont.render("vs. Comp" , 1 , (255 , 255 , 255), (230, 60, 250))
            screen.blit(PlayerText , (390 , 370))
            if event.type == MOUSEBUTTONDOWN:
                screen.fill(LIGHTBLUE)
                SecondWindow = False
                ThirdWindow = False
                
                
        pygame.display.update()
        clock.tick(30)

    #Hold is a variable that is true only when the player picks up a token. This concept will be explained later. 
    hold = False
                    
    while ThirdWindow ==  True and SecondWindow == False: 
        
        turn = "playerOne" #Makes it the first players turn
        
        if repeatBlack == True: #If for some reason blacks turn has to be repeated this line makes it so that red's turn will be skipped.
            turn = "playerTwo"
            
        
        while turn == "playerOne" and repeatBlack == False:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                    
            if FirstGame == True:
                screen.fill(LIGHTBLUE)
                
                FirstGame = False
            
            
            #Fills every section of the screen will light blue, except the playing board
            screen.fill(LIGHTBLUE , (0 , 0 , 140 , 480))
            screen.fill(LIGHTBLUE , (0 , 0 , 640 , 70))
            screen.fill(LIGHTBLUE , (500 , 0 , 140 , 480))
            screen.fill(LIGHTBLUE , (0 , 380 , 640 , 480 ))
            
            #Presents the current score of the two players
            ScoreRedText = myriadProFont.render("Red Score: " + str(RedScore) , 1 , (255 , 255 , 255), (230, 60, 250))
            screen.blit(ScoreRedText , (10 , 10))
                
            ScoreBlackText = myriadProFont.render("Black Score: " + str(BlackScore) , 1 , (255 , 255 , 255), (230, 60, 250))
            screen.blit(ScoreBlackText , (450 , 10))
            
            #Provides explainations on how to play the game
            RedMoveText = myriadProFont.render("Player One click on the RED token", 1 , (255 , 255 , 255), (230, 60, 250))
            screen.blit(RedMoveText , (110 , 410))
            
            #Draws a 7x6 playing board
            for k in range(6):
                for i in range(7):
                    screen.blit(BOARDIMG , (145 + i*50 , 70 + k*50 ))
            screen.blit(REDTOKENIMG , (50, 400))
            screen.blit(BLACKTOKENIMG, (550, 400))  
                
                
            #The following lines get the mouse position and and blink the token to a new location directly above the board in the collumn the mouse position is closest to.
            #There are also instructions that tell the player of this concept (Extra spaces are for formatting)
            mousePosition = pygame.mouse.get_pos()
            x , y = mousePosition[0] , mousePosition[1]
            
            
            #When the play has decided to pick up his token hold will be set to true (see line 285)
            if x >= 40 and x <= 94 and y >= 350 and y <= 450:
                if event.type == MOUSEBUTTONDOWN: 
                    hold = True
            
            if hold == True:
                RedMoveTextTwo = myriadProFont.render("          Move token over board.          ", 1 , (255 , 255 , 255), (230, 60, 250))
                screen.blit(RedMoveTextTwo , (110, 390))
                
                RedMoveTextTwo = myriadProFont.render("                 Click to place.                    ", 1 , (255 , 255 , 255), (230, 60, 250))
                screen.blit(RedMoveTextTwo , (110, 420))
                
                mousePosition = pygame.mouse.get_pos()
                a , b = mousePosition[0] , mousePosition[1]
        
                
                if a >= 95 and a < 195:
                    a = 165
                    b = 40
                    
                elif a >= 195 and a < 249:
                    a = 215
                    b = 40
                    
                elif a >= 249 and a < 299:
                    a = 265
                    b = 40
                    
                elif a >= 299 and a < 349:
                    a = 315
                    b = 40
                
                elif a >= 349 and a < 399:
                    a = 365
                    b = 40
                    
                elif a >= 399 and a < 449:
                    a = 415
                    b = 40
                
                elif a >= 449 and a < 549:
                    a = 465
                    b = 40
                
                screen.blit(REDTOKENIMG , (a - 20 , b -20))
      
                    
            #While the variable hold is equal to true the token will be continuously blited at the mouse position, so the player is free to move it
            if event.type == MOUSEBUTTONDOWN and hold == True and a >= 95 and a <= 549:
                
                #If the mouse button is pressed a second time then the token will be dropped into the column of the players choice.
                #First time is only true the first frame token is dropped
                FirstTime = True
                
                #Dropped is only true the last frame after the token is dropped (so when it reaches the bottom)
                dropped = False
                
                
                #The following lines drop the token. The column and position number in the column is noted and added to the allMoves list. The amount of token in each column is also noted so we on;t exceed the maximum of seven tokens in one column. 
                while hold == True:
                    
                    if a == 165 and colOne != 7:
                        b += 5
                        if FirstTime == True:
                            colOne += 1
                            n = str(colOne) + "R"
                            colOneMoves.append(n)
                            
                        screen.fill(LIGHTBLUE , (140 , 0 , 60 , 400 - (50 * colOne)))
                        screen.blit(REDTOKENIMG , (a - 20 , b - 50 * colOne + 50))
                        
                    elif a == 215 and colTwo != 7:
                        b += 5
                        if FirstTime == True:
                            colTwo += 1 
                            n = str(colTwo) + "R"
                            colTwoMoves.append(n)
                            
                        screen.fill(LIGHTBLUE , (190 , 0 , 60 , 400 - (50 * colTwo)))
                        screen.blit(REDTOKENIMG , (a - 20 , b - 50 * colTwo + 50))
                        
                    elif a == 265 and colThree != 7:
                        b += 5
                        if FirstTime == True:
                            colThree += 1 
                            n = str(colThree) + "R"
                            colThreeMoves.append(n)
                            
                        screen.fill(LIGHTBLUE , (240 , 0 , 60 , 400 - (50 * colThree)))
                        screen.blit(REDTOKENIMG , (a - 20 , b - 50 * colThree + 50))
    
                    elif a == 315 and colFour != 7:
                        b += 5
                        if FirstTime == True:
                            
                            colFour += 1 
                            n = str(colFour) + "R"
                            colFourMoves.append(n)
                            
                        screen.fill(LIGHTBLUE , (290 , 0 , 60 , 400 - (50 * colFour)))
                        screen.blit(REDTOKENIMG , (a - 20 , b - 50 * colFour + 50))
                        
                    elif a == 365 and colFive != 7:
                        b += 5
                        if FirstTime == True:
                            
                            colFive += 1
                            n = str(colFive) + "R"
                            colFiveMoves.append(n) 
                            
                        screen.fill(LIGHTBLUE , (340 , 0 , 60 , 400 - (50 * colFive)))
                        screen.blit(REDTOKENIMG , (a - 20 , b - 50 * colFive + 50))
                        
                    elif a == 415 and colSix != 7:
                        b += 5
                        if FirstTime == True:
                            
                            colSix += 1 
                            n = str(colSix) + "R"
                            colSixMoves.append(n)
                            
                        screen.fill(LIGHTBLUE , (390 , 0 , 60 , 400 - (50 * colSix)))
                        screen.blit(REDTOKENIMG , (a - 20 , b - 50 * colSix + 50))
    
                    elif a == 465  and colSeven != 7:
                        b += 5
                        if FirstTime == True:
                            
                            colSeven += 1 
                            n = str(colSeven) + "R"
                            colSevenMoves.append(n)
                            
                        screen.fill(LIGHTBLUE , (440 , 0 , 60 , 400 - (50 * colSeven)))
                        screen.blit(REDTOKENIMG , (a - 20 , b - 50 * colSeven + 50))
                    
                    else:
                        repeatRed = True
                        break
                        
                    #The following 2 lines call upon my win functions and detect if red has won. If he/she has then win is set to true and another condition will be entered shortly (Line 402)
                    if FirstTime == True:
                        if WinFunctionOneRED(allMoves) == "win" or WinFunctionTwoRED(allMoves) == "win" or WinFunctionThreeRED(allMoves) == "win" or WinFunctionFourRED(allMoves) == "win":
                            win = True 
                            print "Red wins"
                       
                    #When the token is dropped the appropriate amount this sets dropped to True and so the token stops falling 
                    if b == 320:
                        hold = False
                        dropped = True
                        
                    #This reprint the playing board so that the board image always stays on top of the token and not the other way around
                    for k in range(6):
                        for i in range(7):
                            screen.blit(BOARDIMG , (145 + i*50 , 70 + k*50 ))
                    screen.blit(REDTOKENIMG , (50, 400))
                    screen.blit(BLACKTOKENIMG, (550, 400))
                    
                    FirstTime = False 
                    
                    turn = "playerTwo"
                    
                    repeatRed = False
                    
                    #The following lines stop the program when red has won. It then tells the players to click anywhere to play again. If the players choose to play again then the following lines also reset the board by clearing all the moves and emptying all the lists
                    while dropped == True and win == True:

                        screen.fill(LIGHTBLUE , (0 , 380 , 640 , 480 ))                 
                               
                        RedWinText = myriadProFont.render("RED WINS!" , 1 , (255 , 255 , 255), (230, 60, 250))
                        screen.blit(RedWinText, (250 , 380))
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT: 
                                sys.exit()
                                
                                
                        PlayAgainText = myriadProFont.render("Click Anywhere to Play Again!" , 1 , (255 , 255 , 255), (230, 60, 250))
                        screen.blit(PlayAgainText, (140 , 420))
                        
                        if event.type == MOUSEBUTTONDOWN:

                            repeatRed = True
                            FirstGame = True
                            win = False
                            RedScore += 1
                            colOne = 0
                            colTwo = 0
                            colThree = 0
                            colFour = 0
                            colFive = 0
                            colSix = 0
                            colSeven = 0
                            colOneMoves = []
                            colTwoMoves = []
                            colThreeMoves = [] 
                            colFourMoves = []
                            colFiveMoves = []
                            colSixMoves = []
                            colSevenMoves = []
                            allMoves = [colOneMoves , colTwoMoves , colThreeMoves , colFourMoves , colFiveMoves , colSixMoves , colSevenMoves]
                            break
                    
                        
                        pygame.display.update()
                        clock.tick(30) 
                        
                    dropped = False
                    
                    pygame.display.update()
                    clock.tick(30) 

                
            pygame.display.update()
            clock.tick(30)
            
        if repeatRed == True:
            turn = "playerOne"
            
        #The next 250 lines or so is the same thing as 187 - 464 but for the black token
        while turn == "playerTwo" and repeatRed == False:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                    
                
            screen.fill(LIGHTBLUE , (0 , 0 , 140 , 480))
            screen.fill(LIGHTBLUE , (0 , 0 , 640 , 70))
            screen.fill(LIGHTBLUE , (500 , 0 , 140 , 480))
            screen.fill(LIGHTBLUE , (0 , 380 , 640 , 480 ))
            
            ScoreRedText = myriadProFont.render("Red Score: " + str(RedScore) , 1 , (255 , 255 , 255), (230, 60, 250))
            screen.blit(ScoreRedText , (10 , 10))
                
            ScoreBlackText = myriadProFont.render("Black Score: " + str(BlackScore) , 1 , (255 , 255 , 255), (230, 60, 250))
            screen.blit(ScoreBlackText , (450 , 10))
            
            BlackMoveText = myriadProFont.render("  Player Two click on  ", 1 , (255 , 255 , 255), (230, 60, 250))
            screen.blit(BlackMoveText , (180 , 390))
            
            BlackMoveText = myriadProFont.render("     the BLACK token   ", 1 , (255 , 255 , 255), (230, 60, 250))
            screen.blit(BlackMoveText , (180 , 420))
                
            for k in range(6):
                for i in range(7):
                    screen.blit(BOARDIMG , (145 + i*50 , 70 + k*50 ))
            screen.blit(REDTOKENIMG , (50, 400))
            screen.blit(BLACKTOKENIMG, (550, 400))  
                
            mousePosition = pygame.mouse.get_pos()
            x , y = mousePosition[0] , mousePosition[1]
            
            
            
            if x >= 550 and x <= 605 and y >= 350 and y <= 450:
                if event.type == MOUSEBUTTONDOWN: 
                    hold = True
            
            if hold == True:
                
                RedMoveTextTwo = myriadProFont.render("          Move token over board.          ", 1 , (255 , 255 , 255), (230, 60, 250))
                screen.blit(RedMoveTextTwo , (110, 390))
                
                RedMoveTextTwo = myriadProFont.render("                 Click to place.                    ", 1 , (255 , 255 , 255), (230, 60, 250))
                screen.blit(RedMoveTextTwo , (110, 420))
                
                mousePosition = pygame.mouse.get_pos()
                a , b = mousePosition[0] , mousePosition[1]
                
                
                
                if a >= 95 and a < 195:
                    a = 165
                    b = 40
                    
                elif a >= 195 and a < 249:
                    a = 215
                    b = 40
                    
                elif a >= 249 and a < 299:
                    a = 265
                    b = 40
                    
                elif a >= 299 and a < 349:
                    a = 315
                    b = 40
                
                elif a >= 349 and a < 399:
                    a = 365
                    b = 40
                    
                elif a >= 399 and a < 449:
                    a = 415
                    b = 40
                
                elif a >= 449 and a < 549:
                    a = 465
                    b = 40
                
                screen.blit(BLACKTOKENIMG , (a - 20 , b -20))
      
                    
        
            if event.type == MOUSEBUTTONDOWN and hold == True and a >= 95 and a <= 549:
                
                
                FirstTime = True
                
                while hold == True:
                    
                    if a == 165 and colOne != 7:
                        b += 5
                        if FirstTime == True:
                            
                            colOne += 1
                            n = str(colOne) + "B"
                            colOneMoves.append(n)
                            
                        screen.fill(LIGHTBLUE , (140 , 0 , 60 , 400 - (50 * colOne)))
                        screen.blit(BLACKTOKENIMG , (a - 20 , b - 50 * colOne + 50))
                        
                    elif a == 215 and colTwo != 7:
                        b += 5
                        if FirstTime == True:
                            
                            colTwo += 1 
                            n = str(colTwo) + "B"
                            colTwoMoves.append(n)
                            
                        screen.fill(LIGHTBLUE , (190 , 0 , 60 , 400 - (50 * colTwo)))
                        screen.blit(BLACKTOKENIMG , (a - 20 , b - 50 * colTwo + 50))
                        
                    elif a == 265 and colThree != 7:
                        b += 5
                        if FirstTime == True:
                            
                            colThree += 1
                            n = str(colThree) + "B"
                            colThreeMoves.append(n) 
                            
                        screen.fill(LIGHTBLUE , (240 , 0 , 60 , 400 - (50 * colThree)))
                        screen.blit(BLACKTOKENIMG , (a - 20 , b - 50 * colThree + 50))
    
                    elif a == 315 and colFour != 7:
                        b += 5
                        if FirstTime == True:
                            
                            colFour += 1 
                            n = str(colFour) + "B"
                            colFourMoves.append(n)
                            
                        screen.fill(LIGHTBLUE , (290 , 0 , 60 , 400 - (50 * colFour)))
                        screen.blit(BLACKTOKENIMG , (a - 20 , b - 50 * colFour + 50))
                        
                    elif a == 365 and colFive != 7:
                        b += 5
                        if FirstTime == True:
                            
                            colFive += 1 
                            n = str(colFive) + "B"
                            colFiveMoves.append(n)
                            
                        screen.fill(LIGHTBLUE , (340 , 0 , 60 , 400 - (50 * colFive)))
                        screen.blit(BLACKTOKENIMG , (a - 20 , b - 50 * colFive + 50))
                        
                    elif a == 415 and colSix != 7:
                        b += 5
                        if FirstTime == True:
                            
                            colSix += 1 
                            n = str(colSix) + "B"
                            colSixMoves.append(n)
                            
                        screen.fill(LIGHTBLUE , (390 , 0 , 60 , 400 - (50 * colSix)))
                        screen.blit(BLACKTOKENIMG , (a - 20 , b - 50 * colSix + 50))
    
                    elif a == 465  and colSeven != 7:
                        b += 5
                        if FirstTime == True:
                            
                            colSeven += 1 
                            n = str(colSeven) + "B"
                            colSevenMoves.append(n)
                            
                        screen.fill(LIGHTBLUE , (440 , 0 , 60 , 400 - (50 * colSeven)))
                        screen.blit(BLACKTOKENIMG , (a - 20 , b - 50 * colSeven + 50))
                    
                    else:
                        repeatBlack = True
                        break
                    
                    if  FirstTime == True:

                        if WinFunctionOneBLACK(allMoves) == "win" or WinFunctionTwoBLACK(allMoves) == "win" or WinFunctionThreeBLACK(allMoves) == "win" or WinFunctionFourBLACK(allMoves) == "win":
                            win = True 
                            print "Black wins"
                        
                        
                    if b == 320:
                        hold = False
                        dropped = True
                        
                         
                    for k in range(6):
                        for i in range(7):
                            screen.blit(BOARDIMG , (145 + i*50 , 70 + k*50 ))
                    screen.blit(REDTOKENIMG , (50, 400))
                    screen.blit(BLACKTOKENIMG, (550, 400))
                    
                    while colOne + colTwo + colThree + colFour + colFive + colSix + colSeven == 42 and dropped == True:
                        
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT: 
                                sys.exit()
                        
                        RedScore += 1
                        BlackScore += 1

                        BlackWinText = myriadProFont.render("It's a TIE!" , 1 , (255 , 255 , 255), (230, 60, 250))
                        screen.blit(BlackWinText, (250 , 380))
                        
                        PlayAgainText = myriadProFont.render("Click Anywhere to Play Again!" , 1 , (255 , 255 , 255), (230, 60, 250))
                        screen.blit(PlayAgainText, (140 , 420))
                        
                        if event.type == MOUSEBUTTONDOWN:

                            repeatRed = True
                            FirstGame = True
                            win = False
                            BlackScore += 1
                            colOne = 0
                            colTwo = 0
                            colThree = 0
                            colFour = 0
                            colFive = 0
                            colSix = 0
                            colSeven = 0
                            colOneMoves = []
                            colTwoMoves = []
                            colThreeMoves = [] 
                            colFourMoves = []
                            colFiveMoves = []
                            colSixMoves = []
                            colSevenMoves = []
                            allMoves = [colOneMoves , colTwoMoves , colThreeMoves , colFourMoves , colFiveMoves , colSixMoves , colSevenMoves]
                            break
                        
                        
                        
                    
                    FirstTime = False 
                    
                    turn = "playerOne"
                    
                    repeatBlack = False
                    
                    while dropped == True and win == True:
                        
                        screen.fill(LIGHTBLUE , (0 , 380 , 640 , 480 ))
                        
                        BlackWinText = myriadProFont.render("BLACK WINS!" , 1 , (255 , 255 , 255), (230, 60, 250))
                        screen.blit(BlackWinText, (250 , 380))
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT: 
                                sys.exit()
                                
                                
                        PlayAgainText = myriadProFont.render("Click Anywhere to Play Again!" , 1 , (255 , 255 , 255), (230, 60, 250))
                        screen.blit(PlayAgainText, (140 , 420))
                        
                        if event.type == MOUSEBUTTONDOWN:

                            repeatRed = True
                            FirstGame = True
                            win = False
                            BlackScore += 1
                            colOne = 0
                            colTwo = 0
                            colThree = 0
                            colFour = 0
                            colFive = 0
                            colSix = 0
                            colSeven = 0
                            colOneMoves = []
                            colTwoMoves = []
                            colThreeMoves = [] 
                            colFourMoves = []
                            colFiveMoves = []
                            colSixMoves = []
                            colSevenMoves = []
                            allMoves = [colOneMoves , colTwoMoves , colThreeMoves , colFourMoves , colFiveMoves , colSixMoves , colSevenMoves]
                            break
                    
                        
                        pygame.display.update()
                        clock.tick(30) 
                        
                    dropped = False
                    
                    pygame.display.update()
                    clock.tick(30)
                     
            pygame.display.update()
            clock.tick(30) 
                    
                    
        pygame.display.update()
        clock.tick(90) 
        
        
    
    #This loop is only entered if the player has chosen the vs. Comp option. The rest of the code is generally the same as the above 550 line except for black turn (CPU's Turn). At that time the best move is taken from my AI program and that is placed onto the board. 
    while FourthWindow == True and SecondWindow == False and FirstWindow == False and ThirdWindow == False:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        
        
        turn = "playerOne"
        
        if repeatBlack == True:
            turn = "playerTwo"
            
        
        while turn == "playerOne" and repeatBlack == False:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                    
            if FirstGame == True:
                screen.fill(LIGHTBLUE)
                
                FirstGame = False
            
                
            screen.fill(LIGHTBLUE , (0 , 0 , 140 , 480))
            screen.fill(LIGHTBLUE , (0 , 0 , 640 , 70))
            screen.fill(LIGHTBLUE , (500 , 0 , 140 , 480))
            screen.fill(LIGHTBLUE , (0 , 380 , 640 , 480 ))
            
            
            ScoreRedText = myriadProFont.render("Red Score: " + str(RedScore) , 1 , (255 , 255 , 255), (230, 60, 250))
            screen.blit(ScoreRedText , (10 , 10))
                
            ScoreBlackText = myriadProFont.render("Black Score: " + str(BlackScore) , 1 , (255 , 255 , 255), (230, 60, 250))
            screen.blit(ScoreBlackText , (450 , 10))
            
            RedMoveText = myriadProFont.render("Player One click on the RED token", 1 , (255 , 255 , 255), (230, 60, 250))
            screen.blit(RedMoveText , (110 , 410))
            
            for k in range(6):
                for i in range(7):
                    screen.blit(BOARDIMG , (145 + i*50 , 70 + k*50 ))
            screen.blit(REDTOKENIMG , (50, 400))
            screen.blit(BLACKTOKENIMG, (550, 400))  
                
            mousePosition = pygame.mouse.get_pos()
            x , y = mousePosition[0] , mousePosition[1]
            
            
            
            if x >= 40 and x <= 94 and y >= 350 and y <= 450:
                if event.type == MOUSEBUTTONDOWN: 
                    hold = True
            
            if hold == True:
                
                RedMoveTextTwo = myriadProFont.render("          Move token over board.          ", 1 , (255 , 255 , 255), (230, 60, 250))
                screen.blit(RedMoveTextTwo , (110, 390))
                
                RedMoveTextTwo = myriadProFont.render("                 Click to place.                    ", 1 , (255 , 255 , 255), (230, 60, 250))
                screen.blit(RedMoveTextTwo , (110, 420))
                
                mousePosition = pygame.mouse.get_pos()
                a , b = mousePosition[0] , mousePosition[1]
                
                
                
                if a >= 95 and a < 195:
                    a = 165
                    b = 40
                    
                elif a >= 195 and a < 249:
                    a = 215
                    b = 40
                    
                elif a >= 249 and a < 299:
                    a = 265
                    b = 40
                    
                elif a >= 299 and a < 349:
                    a = 315
                    b = 40
                
                elif a >= 349 and a < 399:
                    a = 365
                    b = 40
                    
                elif a >= 399 and a < 449:
                    a = 415
                    b = 40
                
                elif a >= 449 and a < 549:
                    a = 465
                    b = 40
                
                screen.blit(REDTOKENIMG , (a - 20 , b -20))
      
                    
        
            if event.type == MOUSEBUTTONDOWN and hold == True and a >= 95 and a <= 549:
                
                FirstTime = True
                
                dropped = False
                
                while hold == True:
                    
                    if a == 165 and colOne != 7:
                        b += 5
                        if FirstTime == True:
                            colOne += 1
                            n = str(colOne) + "R"
                            colOneMoves.append(n)
                            
                        screen.fill(LIGHTBLUE , (140 , 0 , 60 , 400 - (50 * colOne)))
                        screen.blit(REDTOKENIMG , (a - 20 , b - 50 * colOne + 50))
                        
                    elif a == 215 and colTwo != 7:
                        b += 5
                        if FirstTime == True:
                            colTwo += 1 
                            n = str(colTwo) + "R"
                            colTwoMoves.append(n)
                            
                        screen.fill(LIGHTBLUE , (190 , 0 , 60 , 400 - (50 * colTwo)))
                        screen.blit(REDTOKENIMG , (a - 20 , b - 50 * colTwo + 50))
                        
                    elif a == 265 and colThree != 7:
                        b += 5
                        if FirstTime == True:
                            colThree += 1 
                            n = str(colThree) + "R"
                            colThreeMoves.append(n)
                            
                        screen.fill(LIGHTBLUE , (240 , 0 , 60 , 400 - (50 * colThree)))
                        screen.blit(REDTOKENIMG , (a - 20 , b - 50 * colThree + 50))
    
                    elif a == 315 and colFour != 7:
                        b += 5
                        if FirstTime == True:
                            
                            colFour += 1 
                            n = str(colFour) + "R"
                            colFourMoves.append(n)
                            
                        screen.fill(LIGHTBLUE , (290 , 0 , 60 , 400 - (50 * colFour)))
                        screen.blit(REDTOKENIMG , (a - 20 , b - 50 * colFour + 50))
                        
                    elif a == 365 and colFive != 7:
                        b += 5
                        if FirstTime == True:
                            
                            colFive += 1
                            n = str(colFive) + "R"
                            colFiveMoves.append(n) 
                            
                        screen.fill(LIGHTBLUE , (340 , 0 , 60 , 400 - (50 * colFive)))
                        screen.blit(REDTOKENIMG , (a - 20 , b - 50 * colFive + 50))
                        
                    elif a == 415 and colSix != 7:
                        b += 5
                        if FirstTime == True:
                            
                            colSix += 1 
                            n = str(colSix) + "R"
                            colSixMoves.append(n)
                            
                        screen.fill(LIGHTBLUE , (390 , 0 , 60 , 400 - (50 * colSix)))
                        screen.blit(REDTOKENIMG , (a - 20 , b - 50 * colSix + 50))
    
                    elif a == 465  and colSeven != 7:
                        b += 5
                        if FirstTime == True:
                            
                            colSeven += 1 
                            n = str(colSeven) + "R"
                            colSevenMoves.append(n)
                            
                        screen.fill(LIGHTBLUE , (440 , 0 , 60 , 400 - (50 * colSeven)))
                        screen.blit(REDTOKENIMG , (a - 20 , b - 50 * colSeven + 50))
                    
                    else:
                        repeatRed = True
                        break
                        
                    if FirstTime == True:
                        if WinFunctionOneRED(allMoves) == "win" or WinFunctionTwoRED(allMoves) == "win" or WinFunctionThreeRED(allMoves) == "win" or WinFunctionFourRED(allMoves) == "win":
                            win = True 
                            print "Red wins"
                        
                    if b == 320:
                        hold = False
                        dropped = True
                        
                         
                    for k in range(6):
                        for i in range(7):
                            screen.blit(BOARDIMG , (145 + i*50 , 70 + k*50 ))
                    screen.blit(REDTOKENIMG , (50, 400))
                    screen.blit(BLACKTOKENIMG, (550, 400))
                    
                    FirstTime = False 
                    
                    if b == 320:
                        FirstTime = True
                    
                    turn = "playerTwo"
                    
                    repeatRed = False
                    
                        
                    while dropped == True and win == True:
                        
                        screen.fill(LIGHTBLUE , (0 , 380 , 640 , 480 ))
                        
                        RedWinText = myriadProFont.render("RED WINS!" , 1 , (255 , 255 , 255), (230, 60, 250))
                        screen.blit(RedWinText, (250 , 380))
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT: 
                                sys.exit()
                                
                                
                        PlayAgainText = myriadProFont.render("Click Anywhere to Play Again!" , 1 , (255 , 255 , 255), (230, 60, 250))
                        screen.blit(PlayAgainText, (140 , 420))
                        
                        if event.type == MOUSEBUTTONDOWN:

                            repeatRed = True
                            FirstGame = True
                            win = False
                            RedScore += 1
                            colOne = 0
                            colTwo = 0
                            colThree = 0
                            colFour = 0
                            colFive = 0
                            colSix = 0
                            colSeven = 0
                            colOneMoves = []
                            colTwoMoves = []
                            colThreeMoves = [] 
                            colFourMoves = []
                            colFiveMoves = []
                            colSixMoves = []
                            colSevenMoves = []
                            allMoves = [colOneMoves , colTwoMoves , colThreeMoves , colFourMoves , colFiveMoves , colSixMoves , colSevenMoves]
                            break
                    
                        
                        pygame.display.update()
                        clock.tick(30) 
                        
                    dropped = False
                    
                    pygame.display.update()
                    clock.tick(30) 

                
            pygame.display.update()
            clock.tick(30)
            
        if repeatRed == True:
            turn = "playerOne"
            
            
            
        while turn == "playerTwo" and repeatRed == False:
            
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                    
                
            screen.fill(LIGHTBLUE , (0 , 0 , 140 , 480))
            screen.fill(LIGHTBLUE , (0 , 0 , 640 , 70))
            screen.fill(LIGHTBLUE , (500 , 0 , 140 , 480))
            
            ScoreRedText = myriadProFont.render("Red Score: " + str(RedScore) , 1 , (255 , 255 , 255), (230, 60, 250))
            screen.blit(ScoreRedText , (10 , 10))
                
            ScoreBlackText = myriadProFont.render("Black Score: " + str(BlackScore) , 1 , (255 , 255 , 255), (230, 60, 250))
            screen.blit(ScoreBlackText , (450 , 10))
                
            for k in range(6):
                for i in range(7):
                    screen.blit(BOARDIMG , (145 + i*50 , 70 + k*50 ))
            screen.blit(REDTOKENIMG , (50, 400))
            screen.blit(BLACKTOKENIMG, (550, 400))  
      
      
            BestMove = ai(allMoves)
            
            finished = False

            b = 40
            while finished == False:
                
                
                if BestMove == 1 and colOne != 7:
                    a = 165
                    b += 5
                    if FirstTime == True:
                        
                        colOne += 1
                        n = str(colOne) + "B"
                        colOneMoves.append(n)
                        
                    screen.fill(LIGHTBLUE , (140 , 0 , 60 , 400 - (50 * colOne)))
                    screen.blit(BLACKTOKENIMG , (a - 20 , b - 50 * colOne + 50))
                    
                elif BestMove == 2 and colTwo != 7:
                    a = 215
                    b += 5
                    if FirstTime == True:
                        
                        colTwo += 1 
                        n = str(colTwo) + "B"
                        colTwoMoves.append(n)
                        
                    screen.fill(LIGHTBLUE , (190 , 0 , 60 , 400 - (50 * colTwo)))
                    screen.blit(BLACKTOKENIMG , (a - 20 , b - 50 * colTwo + 50))
                    
                elif BestMove == 3 and colThree != 7:
                    a = 265
                    b += 5
                    if FirstTime == True:
                        
                        colThree += 1
                        n = str(colThree) + "B"
                        colThreeMoves.append(n) 
                        
                    screen.fill(LIGHTBLUE , (240 , 0 , 60 , 400 - (50 * colThree)))
                    screen.blit(BLACKTOKENIMG , (a - 20 , b - 50 * colThree + 50))

                elif BestMove == 4 and colFour != 7:
                    a = 315
                    b += 5
                    if FirstTime == True:
                        
                        colFour += 1 
                        n = str(colFour) + "B"
                        colFourMoves.append(n)
                        
                    screen.fill(LIGHTBLUE , (290 , 0 , 60 , 400 - (50 * colFour)))
                    screen.blit(BLACKTOKENIMG , (a - 20 , b - 50 * colFour + 50))
                    
                elif BestMove == 5 and colFive != 7:
                    a = 365
                    b += 5
                    if FirstTime == True:
                        
                        colFive += 1 
                        n = str(colFive) + "B"
                        colFiveMoves.append(n)
                        
                    screen.fill(LIGHTBLUE , (340 , 0 , 60 , 400 - (50 * colFive)))
                    screen.blit(BLACKTOKENIMG , (a - 20 , b - 50 * colFive + 50))
                    
                elif BestMove == 6 and colSix != 7:
                    a = 415
                    b += 5
                    if FirstTime == True:
                        
                        colSix += 1 
                        n = str(colSix) + "B"
                        colSixMoves.append(n)
                        
                    screen.fill(LIGHTBLUE , (390 , 0 , 60 , 400 - (50 * colSix)))
                    screen.blit(BLACKTOKENIMG , (a - 20 , b - 50 * colSix + 50))

                elif BestMove == 7 and colSeven != 7:
                    a = 465
                    b += 5
                    if FirstTime == True:
                        
                        colSeven += 1 
                        n = str(colSeven) + "B"
                        colSevenMoves.append(n)
                        
                    screen.fill(LIGHTBLUE , (440 , 0 , 60 , 400 - (50 * colSeven)))
                    screen.blit(BLACKTOKENIMG , (a - 20 , b - 50 * colSeven + 50))
                
                else:
                    BestMove = random.randint(1,7)
                    
                if  FirstTime == True:
                    if WinFunctionOneBLACK(allMoves) == "win" or WinFunctionTwoBLACK(allMoves) == "win" or WinFunctionThreeBLACK(allMoves) == "win" or WinFunctionFourBLACK(allMoves) == "win":
                        win = True 
                        print "Black wins"
                    
                      
                if b == 320:
                    finished = True
                    dropped = True
                    
                     
                for k in range(6):
                    for i in range(7):
                        screen.blit(BOARDIMG , (145 + i*50 , 70 + k*50 ))
                screen.blit(REDTOKENIMG , (50, 400))
                screen.blit(BLACKTOKENIMG, (550, 400))
                
                while colOne + colTwo + colThree + colFour + colFive + colSix + colSeven == 42 and dropped == True:
                        
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT: 
                                sys.exit()
                                
                        RedScore += 1
                        BlackScore += 1
                        
                        BlackWinText = myriadProFont.render("It's a TIE!" , 1 , (255 , 255 , 255), (230, 60, 250))
                        screen.blit(BlackWinText, (250 , 380))
                        
                        PlayAgainText = myriadProFont.render("Click Anywhere to Play Again!" , 1 , (255 , 255 , 255), (230, 60, 250))
                        screen.blit(PlayAgainText, (140 , 420))
                        
                        if event.type == MOUSEBUTTONDOWN:

                            repeatRed = True
                            FirstGame = True
                            win = False
                            BlackScore += 1
                            colOne = 0
                            colTwo = 0
                            colThree = 0
                            colFour = 0
                            colFive = 0
                            colSix = 0
                            colSeven = 0
                            colOneMoves = []
                            colTwoMoves = []
                            colThreeMoves = [] 
                            colFourMoves = []
                            colFiveMoves = []
                            colSixMoves = []
                            colSevenMoves = []
                            allMoves = [colOneMoves , colTwoMoves , colThreeMoves , colFourMoves , colFiveMoves , colSixMoves , colSevenMoves]
                            break
                        
                FirstTime = False 
                
                turn = "playerOne"
                
                repeatBlack = False
                
                while dropped == True and win == True:

                    screen.fill(LIGHTBLUE , (0 , 380 , 640 , 480 ))
                    
                    BlackWinText = myriadProFont.render("BLACK WINS!" , 1 , (255 , 255 , 255), (230, 60, 250))
                    screen.blit(BlackWinText, (250 , 380))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT: 
                            sys.exit()
                            
                            
                    PlayAgainText = myriadProFont.render("Click Anywhere to Play Again!" , 1 , (255 , 255 , 255), (230, 60, 250))
                    screen.blit(PlayAgainText, (140 , 420))
                    
                    if event.type == MOUSEBUTTONDOWN:

                        repeatRed = True
                        FirstGame = True
                        win = False
                        BlackScore += 1
                        colOne = 0
                        colTwo = 0
                        colThree = 0
                        colFour = 0
                        colFive = 0
                        colSix = 0
                        colSeven = 0
                        colOneMoves = []
                        colTwoMoves = []
                        colThreeMoves = [] 
                        colFourMoves = []
                        colFiveMoves = []
                        colSixMoves = []
                        colSevenMoves = []
                        allMoves = [colOneMoves , colTwoMoves , colThreeMoves , colFourMoves , colFiveMoves , colSixMoves , colSevenMoves]
                        break
                
                    
                    pygame.display.update()
                    clock.tick(30) 
                    
                dropped = False
                
                pygame.display.update()
                clock.tick(30)
                 
        pygame.display.update()
        clock.tick(90) 
