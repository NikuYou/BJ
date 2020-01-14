#-----------------------------------------------------
#python 3.7.2
#Date: March 2019
#Project: BlackJack
#-----------------------------------------------------



import pygame
from pygame.locals import *
import random
import copy
import sys
import os



#Loading images for every card
cBack = pygame.image.load('images/cardback.png')

spade2 = pygame.image.load('images/2s.png')
spade3 = pygame.image.load('images/3s.png')
spade4 = pygame.image.load('images/4s.png')
spade5 = pygame.image.load('images/5s.png')
spade6 = pygame.image.load('images/6s.png')
spade7 = pygame.image.load('images/7s.png')
spade8 = pygame.image.load('images/8s.png')
spade9 = pygame.image.load('images/9s.png')
spade10 = pygame.image.load('images/10s.png')
spadeJ = pygame.image.load('images/js.png')
spadeQ = pygame.image.load('images/qs.png')
spadeA = pygame.image.load('images/as.png')
spadeK = pygame.image.load('images/ks.png')

heart2 = pygame.image.load('images/2h.png')
heart3 = pygame.image.load('images/3h.png')
heart4 = pygame.image.load('images/4h.png')
heart5 = pygame.image.load('images/5h.png')
heart6 = pygame.image.load('images/6h.png')
heart7 = pygame.image.load('images/7h.png')
heart8 = pygame.image.load('images/8h.png')
heart9 = pygame.image.load('images/9h.png')
heart10 = pygame.image.load('images/10h.png')
heartJ = pygame.image.load('images/jh.png')
heartQ = pygame.image.load('images/qh.png')
heartK = pygame.image.load('images/kh.png')
heartA = pygame.image.load('images/ah.png')

club2 = pygame.image.load('images/2c.png')
club3 = pygame.image.load('images/3c.png')
club4 = pygame.image.load('images/4c.png')
club5 = pygame.image.load('images/5c.png')
club6 = pygame.image.load('images/6c.png')
club7 = pygame.image.load('images/7c.png')
club8 = pygame.image.load('images/8c.png')
club9 = pygame.image.load('images/9c.png')
club10 = pygame.image.load('images/10c.png')
clubJ = pygame.image.load('images/jc.png')
clubQ = pygame.image.load('images/qc.png')
clubK = pygame.image.load('images/kc.png')
clubA = pygame.image.load('images/ac.png')

diamond2 = pygame.image.load('images/2d.png')
diamond3 = pygame.image.load('images/3d.png')
diamond4 = pygame.image.load('images/4d.png')
diamond5 = pygame.image.load('images/5d.png')
diamond6 = pygame.image.load('images/6d.png')
diamond7 = pygame.image.load('images/7d.png')
diamond8 = pygame.image.load('images/8d.png')
diamond9 = pygame.image.load('images/9d.png')
diamond10 = pygame.image.load('images/10d.png')
diamondJ = pygame.image.load('images/jd.png')
diamondQ = pygame.image.load('images/qd.png')
diamondK = pygame.image.load('images/kd.png')
diamondA = pygame.image.load('images/ad.png')

cards = [ diamondA, clubA, heartA, spadeA, diamond2, club2, heart2, spade2, diamond3, club3, heart3, spade3,
          diamond4, club4, heart4, spade4, diamond5, club5, heart5, spade5, diamond6, club6, heart6, spade6,
          diamond7, club7, heart7, spade7, diamond8, club8, heart8, spade8, diamond9, club9, heart9, spade9,
          diamond10, club10, heart10, spade10, diamondJ, clubJ, heartJ, spadeJ, diamondQ, clubQ, heartQ, spadeQ,
          diamondK, clubK, heartK, spadeK ]

cardA = [ diamondA, clubA, heartA, spadeA ]
card2 = [ diamond2, club2, heart2, spade2 ]
card3 = [ diamond3, club3, heart3, spade3 ]
card4 = [ diamond4, club4, heart4, spade4 ]
card5 = [ diamond5, club5, heart5, spade5 ]
card6 = [ diamond6, club6, heart6, spade6 ]
card7 = [ diamond7, club7, heart7, spade7 ]
card8 = [ diamond8, club8, heart8, spade8 ]
card9 = [ diamond9, club9, heart9, spade9 ]

card10 = [ diamond10, club10, heart10, spade10, diamondJ, clubJ, heartJ, spadeJ, diamondQ, clubQ, heartQ,
           spadeQ, diamondK, clubK, heartK, spadeK ]

'''
#create a deck, can be used when there's no more cards in cards and people still want to play
def newdeck():
    return [ diamondA, clubA, heartA, spadeA, diamond2, club2, heart2, spade2, diamond3, club3, heart3, spade3,
          diamond4, club4, heart4, spade4, diamond5, club5, heart5, spade5, diamond6, club6, heart6, spade6,
          diamond7, club7, heart7, spade7, diamond8, club8, heart8, spade8, diamond9, club9, heart9, spade9,
          diamond10, club10, heart10, spade10, diamondJ, clubJ, heartJ, spadeJ, diamondQ, clubQ, heartQ, spadeQ,
          diamondK, clubK, heartK, spadeK ]'''

def getCard(cards, list1):
    if cards == []:
        print("STOP! You cannot spend such a long time playing game. Go back to study OB!")
        sys.exit(0)
    #or we can use random.shuffle(cards) and cards.pop()
    cA = 0
    card = random.choice(cards)
    cards.remove(card)
    list1.append(card)
    if card in cardA:
        cA = 1
    return card, cA

def gameBeginning(cards, uCards, dCards):
    userAce = 0
    dealAce = 0
    card1, cA = getCard(cards, uCards)
    userAce += cA
    card2, cA = getCard(cards, dCards)
    dealAce += cA
    card3, cA = getCard(cards, uCards)
    userAce += cA
    card4, cA = getCard(cards, dCards)
    dealAce += cA
    return getPoints(card1) + getPoints(card3), userAce, getPoints(card2) + getPoints(card4), dealAce

def getPoints(card):
    if card in cardA:
        #Ace is default 11
        return 11
    elif card in card2:
        return 2
    elif card in card3:
        return 3
    elif card in card4:
        return 4
    elif card in card5:
        return 5
    elif card in card6:
        return 6
    elif card in card7:
        return 7
    elif card in card8:
        return 8
    elif card in card9:
        return 9
    elif card in card10:
        return 10
    else:
        print('Wrong Card!')
        sys.exit(0)
        
def basicRules(bets,accounts):
    '''basicRules: a beginner mode where it only has the basic rules of Black Jack
    where you are attempting to create a hand that is close to but without going over
    the value of 21. If neither the user or the computer dealer has 21, the winner is
    the one with the higher value. Face cards are treated as a value of 10 while aces
    are treated as either a 1 or 11. '''
    
    stand = False
    uCards = []
    dCards = []
    wins = float(bets)
    #wins is a float because it is possible for wins to be 1.5
    
    fails = 0
    #different from wins, it represents the times of lose, but won't be recorded in the account detail file
    accounts = accounts
    
    #Initialize Game
    pygame.init()
    
    #control the display window and screen
    #https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode
    screen = pygame.display.set_mode((640, 380))
    pygame.display.set_caption('BlackJack')
    font = pygame.font.SysFont('arial', 15)

    #draw font
    #https://www.pygame.org/docs/ref/font.html
    hitLabel = font.render('Hit', 1, (255, 140, 0))
    standLabel = font.render('Stand', 1, (255, 140, 0))
    restartLabel = font.render('Restart', 1, (255, 140, 0))
    gameoverLabel = font.render('GAME OVER!', 1, (255, 0, 0))

    #set background
    #https://www.pygame.org/docs/ref/surface.html#pygame.Surface.fill
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((123, 104, 238))

    #draw buttons
    #https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect
    hitButton = pygame.draw.rect(background, (28, 28, 28), (25, 345, 75, 25))
    standButton = pygame.draw.rect(background, (28, 28, 28), (120, 345, 75, 25))
    
    userSum, userA, dealSum, dealA = gameBeginning(cards, uCards, dCards)
    restartButton = pygame.draw.rect(background, (123, 104, 238), (480, 345, 75, 25))

    #Event Loop
    while True:
        #checks if game is over
        gameover = False
        if userSum >= 21 and userA == 0:
            gameover = True
        elif len(uCards) == 5:
            gameover = True
        elif len(uCards) == 2 and userSum == 21:
            gameover = True
        elif len(dCards) == 2 and dealSum == 21:
            gameover = True

        winLabel = font.render('Wins: %i' % wins, 1, (255, 140, 0))
        loseLabel = font.render('Losses: %i' % fails, 1, (255, 140, 0))
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                #quit event in pygame means closing the window
                accounts[user][1]=str(wins)
                with open("accounts.txt", 'w') as f:
                    for k in accounts.keys():
                        f.write('%s %s %s\n'%(k, accounts[k][0], accounts[k][1]))
                sys.exit(0)
                
            elif event.type == pygame.MOUSEBUTTONDOWN and not (gameover or stand) and hitButton.collidepoint(pygame.mouse.get_pos()):
                card, cA = getCard(cards, uCards)
                userA += cA
                userSum += getPoints(card)
                while userSum > 21 and userA > 0:
                    # check if there's A in hand, if there is, change the value to 1(default is 11)
                    userA -= 1
                    userSum -= 10
                    
            elif event.type == pygame.MOUSEBUTTONDOWN and not gameover and standButton.collidepoint(pygame.mouse.get_pos()):
                stand = True
                while dealSum <= userSum and dealSum < 17:
                    card, cA = getCard(cards, dCards)
                    dealA += cA
                    dealSum += getPoints(card)
                    while dealSum > 21 and dealA > 0:
                        #check As in dealer's hand
                        dealA -= 1
                        dealSum -= 10
                        
            elif event.type == pygame.MOUSEBUTTONDOWN and (gameover or stand) and restartButton.collidepoint(pygame.mouse.get_pos()):
                if userSum == dealSum:
                    print("Draw!")
                elif userSum <= 21 and dealSum < userSum or dealSum > 21:
                    if userSum==21 and len(uCards)==2:
                        wins += 1.5
                    else:
                        wins += 1
                else:
                    fails += 1
                    wins -= 1 
                gameover = False
                stand = False
                uCards = []
                dCards = []
                userSum, userA, dealSum, dealA = gameBeginning(cards, uCards, dCards)

        #https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit
        screen.blit(background, (0, 0))
        screen.blit(hitLabel, (54, 348))
        screen.blit(standLabel, (136, 348))
        screen.blit(winLabel, (500, 10))
        screen.blit(loseLabel, (565, 10))

        for card in dCards:
            x = 10 + dCards.index(card) * 110
            screen.blit(card, (x, 10))
        screen.blit(cBack, (120, 10))

        for card in uCards:
            x = 10 + uCards.index(card) * 110
            screen.blit(card, (x, 180))

        if gameover or stand:
            screen.blit(gameoverLabel, (510, 200))
            restartButton = pygame.draw.rect(background, (28,28,28), (480, 345, 75, 25))
            screen.blit(restartLabel, (497, 346))
            screen.blit(dCards[1], (120, 10))
        else:
            restartButton = pygame.draw.rect(background, (123,104,238), (480, 345, 75, 25))

        pygame.display.update()

def splitRules(bets,accounts):
    '''allow the user to split their cards. Splitting is when the two initial cards you are dealt in
    BlackJack have the same value. You are then able to add a bet equal to the initial bet to play a second hand. '''
    stand = False
    stand2 = False
    split = False
    uCards = []
    uCards2 = []
    dCards = []
    wins = float(bets)
    fails = 0
    accounts = accounts
   
    #Initialize Game
    #the same as what we did in basic rules, the only change is that there are more buttons for the second hand
    pygame.init()
    screen = pygame.display.set_mode((640, 380))
    pygame.display.set_caption('Black Jack')
    font = pygame.font.SysFont('arial', 15)
    
    hitLabel = font.render('Hit', 1, (255, 140, 0))
    standLabel = font.render('Stand', 1, (255, 140, 0))
    hitLabel2 = font.render('Hit2', 1, (255, 140, 0))
    standLabel2 = font.render('Stand2', 1, (255, 140, 0))
    restartLabel = font.render('Restart', 1, (255, 140, 0))
    gameoverLabel = font.render('GAME OVER!', 1, (255, 140, 0))
    splitLabel = font.render('Split', 1, (255, 0, 0))
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((123, 104, 238))
    
    hitButton = pygame.draw.rect(background, (28, 28, 28), (25, 345, 75, 25))
    standButton = pygame.draw.rect(background, (28, 28, 28), (120, 345, 75, 25))
    hitButton2 = pygame.draw.rect(background, (28, 28, 28), (310, 345, 75, 25))
    standButton2 = pygame.draw.rect(background, (28, 28, 28), (405, 345, 75, 25))
    splitButton = pygame.draw.rect(background, (28, 28, 28), (215, 345, 75, 25))
    
    userSum, userA, dealSum, dealA = gameBeginning(cards, uCards, dCards)
    userSum2 = 0
    userA2 = 0
    restartButton = pygame.draw.rect(background, (123, 104, 238), (500, 345, 75, 25))
    
    
    uCards = [heart5, club5]
    #initialize the first game's player's hand in this mode to help player easier to understand split rules.
    userSum = 10
    userA = 0
    
    #Event Loop
    while True:
        #check if game is over
        gameover = False
        gameover2 = False
        if userSum >= 21 and userA == 0:
            gameover = True
        elif len(uCards) == 5:
            gameover = True
        elif len(uCards) == 2 and userSum == 21:
            gameover = True
        if userSum2 >= 21 and userA2 == 0:
            gameover2 = True
        elif len(uCards2) == 5:
            gameover2 = True
        elif len(uCards2) == 2 and userSum2 == 21:
            gameover2 = True
        if len(dCards) == 2 and dealSum == 21 :
            gameover = True
            gameover2 = True

        winLabel = font.render('Wins: %i' % wins, 1, (255, 140, 0))
        loseLabel = font.render('Losses: %i' % fails, 1, (255, 140, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                accounts[user][1]=str(wins)
                with open("accounts.txt", 'w') as f:
                    for k in accounts.keys():
                        f.write('%s %s %s\n'%(k, accounts[k][0], accounts[k][1]))
                sys.exit(0)
                
            elif event.type == pygame.MOUSEBUTTONDOWN and not (gameover or stand) and hitButton.collidepoint(pygame.mouse.get_pos()):
                card, cA = getCard(cards, uCards)
                userA += cA
                userSum += getPoints(card)
                while userSum > 21 and userA > 0:
                    userA -= 1
                    userSum -= 10
                    
            elif event.type == pygame.MOUSEBUTTONDOWN and not gameover and standButton.collidepoint(pygame.mouse.get_pos()):
                stand = True
                while dealSum <= userSum and dealSum < 17:
                    card, cA = getCard(cards, dCards)
                    dealA += cA
                    dealSum += getPoints(card)
                    while dealSum > 21 and dealA > 0:
                        dealA -= 1
                        dealSum -= 10
                        
            elif event.type == pygame.MOUSEBUTTONDOWN and not (gameover2 or stand2) and hitButton2.collidepoint(pygame.mouse.get_pos()):
                if split:
                    card, cA = getCard(cards, uCards2)
                    userA2 += cA
                    userSum2 += getPoints(card)
                    while userSum2 > 21 and userA2 > 0:
                        userA2 -= 1
                        userSum2 -= 10
                        
            elif event.type == pygame.MOUSEBUTTONDOWN and not gameover2 and standButton2.collidepoint(pygame.mouse.get_pos()):
                if split:
                    stand2 = True
                    while dealSum <= userSum2 and dealSum < 17:
                        card, cA = getCard(cards, dCards)
                        dealA += cA
                        dealSum += getPoints(card)
                        while dealSum > 21 and dealA > 0:
                            dealA -= 1
                            dealSum -= 10
                            
            elif event.type == pygame.MOUSEBUTTONDOWN and not (gameover or stand) and splitButton.collidepoint(pygame.mouse.get_pos()):
                if len(uCards)== 2:
                    if getPoints(uCards[0])== getPoints(uCards[1]):
                        split = True
                        uCards2.append(uCards[1])
                        del uCards[1]
                        userSum2=getPoints(uCards2[0])
                        if uCards2[0] in cardA:
                            userA2 = 1
                            
            elif event.type == pygame.MOUSEBUTTONDOWN and (gameover or stand) and restartButton.collidepoint(pygame.mouse.get_pos()):
                if split:
                    if stand2 or gameover2:
                        if userSum == dealSum:
                            print("Draw!")
                        elif userSum <= 21 and dealSum < userSum or dealSum > 21:
                            if userSum == 21 and len(uCards) == 2:
                                wins += 1.5
                            else:
                                wins += 1
                        elif userSum2 <= 21 and dealSum < userSum2 or dealSum > 21:
                            if userSum2==21 and len(uCards2)==2:
                                wins += 1.5
                            else:
                                wins += 1
                        else:
                            fails += 1
                            wins -= 1
                        gameover = False
                        stand = False
                        stand2 = False
                        uCards = []
                        dCards = []
                        uCards2 = []
                        split = False
                        userA2 = 0
                        userSum2 = 0
                        userSum, userA, dealSum, dealA = gameBeginning(cards, uCards, dCards)
                        
                else:
                    if userSum == dealSum:
                        print("Draw!")
                    elif userSum <= 21 and dealSum < userSum or dealSum > 21:
                        if userSum == 21 and len(uCards) == 2:
                            wins += 1.5
                        else:
                            wins += 1
                    else:
                        fails += 1
                        wins -= 1
                    gameover = False
                    gameover2=False
                    stand = False
                    stand2=False
                    uCards = []
                    dCards = []
                    uCards2 = []
                    split = False
                    userA2 = 0
                    userSum2 = 0
                    userSum, userA, dealSum, dealA = gameBeginning(cards, uCards, dCards)

        screen.blit(background, (0, 0))
        screen.blit(hitLabel, (54, 348))
        screen.blit(standLabel, (136, 348))
        screen.blit(hitLabel2, (338, 348))
        screen.blit(standLabel2, (420, 348))
        screen.blit(splitLabel, (238, 348))
        screen.blit(winLabel, (500, 10))
        screen.blit(loseLabel, (565, 10))

        for card in dCards:
            x = 10 + dCards.index(card) * 110
            screen.blit(card, (x, 10))
        screen.blit(cBack, (120, 10))

        for card in uCards:
            x = 10 + uCards.index(card) * 40
            screen.blit(card, (x, 180))
        for card in uCards2:
            x = 300 + uCards2.index(card) * 40
            screen.blit(card, (x, 180))

        if gameover or stand:
            if split:
                    if stand2 or gameover2:
                        screen.blit(gameoverLabel, (510, 200))
                        restartButton = pygame.draw.rect(background, (28,28,28), (500, 345, 75, 25))
                        screen.blit(restartLabel, (520, 346))
                        screen.blit(dCards[1], (120, 10))
                        
            else:
                screen.blit(gameoverLabel, (510, 200))
                restartButton = pygame.draw.rect(background, (28,28,28), (500, 345, 75, 25))
                screen.blit(restartLabel, (520, 346))
                screen.blit(dCards[1], (120, 10))
                
        else:
            restartButton = pygame.draw.rect(background, (123,104,238), (500, 345, 75, 25))

        pygame.display.update()
            
if __name__ == '__main__':
    #accounts
    accounts={}
    if os.path.exists("accounts.txt"):
        data=open("accounts.txt", 'r')
        for line in data.readlines():
            name, pwd, bets = line.strip().split(" ")
            accounts[name] = [pwd, bets]
        
    user = input("Enter your name: ")
    pwd = input("Enter your password: ")
    bets = 10
    # default to 10
    
    if user in accounts.keys():
        cnt = 0
        while(pwd != accounts[user][0]):
            if cnt >= 2:
                print("You entered wrong passwords too many times, exit!")
                sys.exit(0)
            print("Wrong password~")
            pwd = input("Enter your password: ")
            cnt += 1
        print("Account is loaded!")
        bets = accounts[user][1]
    else:
        accounts[user] = [pwd, bets]
        print("New account created~")
    
    #rules
    advanceRules=False
    rule=input("Select game rules: 1 for basic rules, 2 for advanced rules(allowing split cards) .\n")
    if rule=='1':
        print("basic rules.")
        basicRules(bets, accounts)
    elif rule=='2':
        print("split rules")
        splitRules(bets, accounts)
    else:
        print('Wrong selection!')
    #Local Variable
    
