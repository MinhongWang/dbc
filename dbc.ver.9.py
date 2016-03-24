# -*- coding: utf-8 -*-
import itertools, random, sys

class Card(object):
    def __init__(self, name, values=(0, 0), cost=1, clan=None):
        self.name = name
        self.cost = cost
        self.values = values
        self.clan = clan
    def __str__(self):
        return 'Name %s costing %s with attack %s and money %s' % (self.name, self.cost, self.values[0], self.values[1])
    def get_attack(self):
        return self.values[0]
    def get_money(self):
        return self.values[1]
#This function returns initial cards of main deck
def mainDeckCards():
    maindeckcards = [4 * [Card('Archer', (3, 0), 2)], 
                4 * [Card('Baker', (0, 3), 2)], 
                3 * [Card('Swordsman', (4, 0), 3)], 
                2 * [Card('Knight', (6, 0), 5)],
                3 * [Card('Tailor', (0, 4), 3)],
                3 * [Card('Crossbowman', (4, 0), 3)],
                3 * [Card('Merchant', (0, 5), 4)],
                4 * [Card('Thug', (2, 0), 1)],
                4 * [Card('Thief', (1, 1), 1)],
                2 * [Card('Catapault', (7, 0), 6)], 
                2 * [Card('Caravan', (1, 5), 5)],
                2 * [Card('Assassin', (5, 0), 4)]]
    return maindeckcards
#This function returns initial cards of player
def playerInitialCards():
    playercards = [8 * [Card('Serf', (0, 1), 0)],
                   2 * [Card('Squire', (1, 0), 0)]]
    return playercards
#Fucntion for player one's initiation
def playerOneInitial():
    global pO
    pO = {'name': 'player one', 'health': 30, 'deck': None, 'hand': None, 'active': None, 'handsize': 5, 'discard': None}
    playeronedeck = playerInitialCards()
    pod = list(itertools.chain.from_iterable(playeronedeck))
    pO['deck'] = pod
    pO['hand'] = []
    pO['discard'] = []
    pO['active'] = []
    for x in range(0, pO['handsize']):    #player draw the first new hand from their deck
        if len(pO['deck']) == 0:        #if player's deck is empty, then the discard pile is shuffled and moved to the deck
            random.shuffle(pO['discard']) #this if is not neccessary
            pO['deck'] = pO['discard']
            pO['discard'] = []
        card = pO['deck'].pop()
        pO['hand'].append(card)
#Function for computer's initiation
def playerComputerInitial():
    global pC
    pC = {'name': 'player computer', 'health': 30, 'deck': None, 'hand': None, 'active': None, 'handsize': 5, 'discard': None}
    playercomputerdeck = playerInitialCards()
    pcd = list(itertools.chain.from_iterable(playercomputerdeck))
    pC['deck'] = pcd
    pC['hand'] = []
    pC['discard'] = []
    pC['active'] = []
    for x in range(0, pO['handsize']):
        if len(pC['deck']) == 0:
            random.shuffle(pO['discard'])
            pC['deck'] = pC['discard']
            pC['discard'] = []
        card = pC['deck'].pop()
        pC['hand'].append(card)
#Function for initiating main deck and central line
def mainDeckCentralLineInitial():
    global central
    central = {'name': 'central', 'active': None, 'activeSize': 5, 'supplement': None, 'deck': None}
    mainDeck = mainDeckCards()
    
    supplement = 10 * [Card('Levy', (1, 2), 2)]
    deck = list(itertools.chain.from_iterable(mainDeck))
    random.shuffle(deck)
    central['deck'] = deck
    central['supplement'] = supplement
    central['active'] = []
    
    max = central['activeSize']          #move cards from main deck to central line
    count = 0
    while count < max:
        card = central['deck'].pop()
        central['active'].append(card)
        count = count + 1



if __name__ == '__main__':
    #Call the functions to initiate
    playerOneInitial()
    playerComputerInitial()
    mainDeckCentralLineInitial()
    #Start a game or not. And check the input. If player input N, then quit the program
    pG = raw_input('Do you want to play a game?(Y=Yes, N=No):').upper()
    while (pG!='Y' and pG!='N'):
        print("\nWrong input, please input again! (Y=Yes, N=No)")
        pG = raw_input('Do you want to play a game?(Y=Yes, N=No):').upper()    
    cG = (pG=='Y')
    nG = (pG=='N')
    while nG:
        print("Thank you!")
        sys.exit()
    #Aggressive opponent or acquisative. Check the input.
    oT = raw_input("Do you want an aggressive (A) opponent or an acquisative (Q) opponent?:").upper()
    while (oT!='A' and oT!='Q'):
        print("\nWrong input, please input again! (A=Aggressive, Q=Acquisative)")
        oT = raw_input("Do you want an aggressive (A) opponent or an acquisative (Q) opponent?:").upper()
    aggressive = (oT=='A')
    acquisative = (oT=='Q')

    print "---------------Game Start---------------"        
    while cG:
        money = 0
        attack = 0

        while True:
            if not cG:
                break
            #Print useful information for player
            print "\nPlayer Health %s" % pO['health']
            print "Computer Health %s" % pC['health']           

            print "\nAvailable Cards"
            for card in central['active']:
                print "\t%s" % card

            print "Supplement"
            if len(central['supplement']) > 0:
                print "\t%s" % central['supplement'][0]
            else:
                print "\tNo supplements any more."

            print "\nYour Hand"
            if len(pO['hand'])>0:
                index = 0
                for card in pO['hand']:
                    print "\t[%s] %s" % (index, card)
                    index = index + 1
            else:
                print "\tNo cards"

            print "\nYour Active Cards"
            if len(pO['active'])>0:
                for card in pO['active']:
                    print "\t%s" % card
            else:
                print "\tNo cards"
            
            print "\nYour Values"
            print "\tMoney %s, Attack %s" % (money, attack)
            
            print "\nChoose Action: (P = play all, [0-n] = play that card, B = Buy Card, A = Attack, E = end turn, Q = Quit)"
            #Get player's input and check
            act = raw_input("Enter Action: ").upper()
            while (act!='P' and act!='B'and act!='A'and act!='E'and act!='Q' and act.isdigit()==False):
                print("Wrong input, please input again! (P = play all, [0-n] = play that card, B = Buy Card, A = Attack, E = end turn, Q = Quit)")
                act = raw_input("Enter Action: ").upper()
            while(act.isdigit() and int(act)>=len(pO['hand'])):
                print("This card number is not valid, please input again!")
                act = raw_input("Enter Action: ").upper()            
            #If player input Q to quit the program
            if act == 'Q':
                print "---------------Your input is: quit the game---------------"
                print("\nThank you!")
                sys.exit()
            #If player input P to play all cards
            if act == 'P':
                if(len(pO['hand'])>0):
                    print "---------------Your input is: move all cards to active area---------------"
                    for x in range(0, len(pO['hand'])):
                        card = pO['hand'].pop()
                        pO['active'].append(card)
                        money = money + card.get_money()
                        attack = attack + card.get_attack()
                else:
                    print "---------------There is not card in hand!---------------"
            #If player input a number to play only one card
            if act.isdigit():
                if( int(act) < len(pO['hand'])):
                    print "---------------Your input is: move card ["+act+"] to active area---------------"
                    card = pO['hand'].pop(int(act))
                    pO['active'].append(card)
                    money = money + card.get_money()
                    attack = attack + card.get_attack()
            #If player input B to buy cards
            if (act == 'B'):
                print "---------------Your input is: start buying cards---------------"
                #If no money, end buying straightly
                if (money == 0):
                    print "Sorry! you cannot buy cards since your money value is 0."
                notending = True
                #This while loop until player input E to end buying or money reduce to zero
                while money > 0:
                    #Print useful information for player buying cards
                    print "Available Cards"
                    ind = 0
                    for card in central['active']:
                        print "\t[%s] %s" % (ind,card)
                        ind = ind + 1
                    print "Supplement"
                    if len(central['supplement']) > 0:
                        print "\t%s" % central['supplement'][0]
                    else:
                        print "\tNo supplements any more."
                    print "\nPresent money %s" % (money)
                    print "\nChoose a card to buy [0-n], S for supplement, E to end buying"
                    #Get player's input and check
                    bv = raw_input("Choose option: ").upper()
                    while (bv!='S' and bv!='E' and bv.isdigit()==False):
                        print "Wrong input! Please input again (Choose a card to buy [0-n], S for supplement, E to end buying):"
                        bv = raw_input("Choose option: ").upper()
                    while (bv.isdigit() and int(bv) >= len(central['active'])):
                        print "Your input number is invalid, please input again:"
                        bv = raw_input("Choose option: ").upper()
                    #If player buy a supplement
                    if bv == 'S':
                        if len(central['supplement']) > 0:
                            if money >= central['supplement'][0].cost:
                                money = money - central['supplement'][0].cost
                                pO['discard'].append(central['supplement'].pop())
                                print "Supplement Bought"
                            else:
                                print "\nInsufficient money to buy!\n"
                        else:
                            print "\nNo supplements left!\n"                                       
                    #If player end buying
                    elif bv == 'E':
                        notending = False
                        break;
                    #If player input a number to buy one card
                    elif bv.isdigit():
                        if int(bv) < len(central['active']):
                             if money >= central['active'][int(bv)].cost:
                                money = money - central['active'][int(bv)].cost
                                pO['discard'].append(central['active'].pop(int(bv)))
                                if( len(central['deck']) > 0):
                                    card = central['deck'].pop()
                                    central['active'].append(card)
                                else:
                                    central['activeSize'] = central['activeSize'] - 1
                                print "Card bought"
                             else:
                                print "\nInsufficient money to buy!\n"
                        else:
                             print "\nEnter a valid index number!\n"
                    #Check card exhausted. If no card anymore, end game
                    if central['activeSize'] == 0:
                        cG=False
                        print "No more cards available"
                        if pO['health'] > pC['health']:
                            print "Player One Wins on Health"
                        elif pC['health'] > pO['health']:
                            print "Computer Wins"
                        else:                                                 #？？？？？
                            pHT = 0
                            pCT = 0
                            if pHT > pCT:
                                print "Player One Wins on Card Strength"
                            elif pCT > pHT:
                                print "Computer Wins on Card Strength"
                            else:
                                print "Draw"
                        break                    
                print "---------------End buying cards---------------"
            #If player input A to attack
            if act == 'A':
                print "---------------Your input is: attack opponent---------------"
                if attack == 0:
                    print "Sorry! You cannot attack opponent since your attack value is zero."
                    print "---------------Attack end---------------"
                else: 
                    print "You attack with strength %s"%(attack)
                    pC['health'] = pC['health'] - attack
                    attack = 0
                    print "---------------Attack end---------------"
                    #Check computer's health. If died, end game
                    if pC['health'] <= 0:
                        cG = False
                        print 'Computer died'
                        print 'Player One Wins'
                        break
            #If player input E to end turn
            if act == 'E':
                print "---------------Your input is: end turn---------------"
                #If there are cards in hand, move to discard pile
                if (len(pO['hand']) >0 ):
                    for x in range(0, len(pO['hand'])):
                        pO['discard'].append(pO['hand'].pop())
                #If there are cards in active area, move to discard pile
                if (len(pO['active']) >0 ):
                    for x in range(0, len(pO['active'])):
                        pO['discard'].append(pO['active'].pop())
                #Player draws a new hand from his deck. If deck is empty, then shuffle discard pile and move to the deck
                for x in range(0, pO['handsize']):
                    if len(pO['deck']) == 0:
                        random.shuffle(pO['discard'])
                        pO['deck'] = pO['discard']
                        pO['discard'] = []
                    card = pO['deck'].pop()
                    pO['hand'].append(card)
                break
        
        if cG:
            print "---------------Computer Turn Start---------------"
            
            print "Available Cards" 
            for card in central['active']:
                print "\t%s" % card

            print "Supplement"
            if len(central['supplement']) > 0:
                print "\t%s" % central['supplement'][0]
            else:
                print "\tNo supplements any more."

            print "\nPlayer Health %s" % pO['health']
            print "Computer Health %s" % pC['health']

            print "\nComputer's hand"
            for card in pC['hand']:
                print "\t%s" % card
            money = 0
            attack = 0
            #Computer move all cards in hand to active area
            for x in range(0, len(pC['hand'])):
                            card = pC['hand'].pop()
                            pC['active'].append(card)
                            money = money + card.get_money()
                            attack = attack + card.get_attack()
            print "\nComputer move all cards to active area"
            print "\nComputer player values attack %s, money %s" % (attack, money)
            print "\nComputer attack! Computer attacking with strength %s" % attack
            pO['health'] = pO['health'] - attack
            attack = 0
            #Check player's health. If died, end game
            if pO['health'] <= 0:
                cG = False
                print "Player one died"
                print "Computer wins"
        
        if cG:    
            print "\nPlayer Health %s" % pO['health']
            print "Computer Health %s" % pC['health']
            print "\nComputer player values attack %s, money %s" % (attack, money)
            print "\nComputer buying"
            if money > 0:                
                templist = []
                print "Starting Money %s" % (money)                
                #Add all cards that computer can afford to templist
                if len(central['supplement']) > 0:
                    if central['supplement'][0].cost <= money:
                        templist.append("S")
                for intindex in range (0, central['activeSize']):
                    if central['active'][intindex].cost <= money:
                        templist.append(intindex)
                #Get all possible combinations of cards in templist that computer can afford.
                if len(templist) >0:
                    possibleCombinations = []
                    for l in range(0,len(templist)+1):
                        for subset in itertools.combinations(templist,l):
                            requireMoney = 0
                            for index in subset:
                                if index == "S":
                                    requireMoney = requireMoney + 2
                                if index in range(0,central['activeSize']):
                                    requireMoney = requireMoney + central['active'][int(index)].cost
                            if requireMoney <= money:
                                possibleCombinations.append(subset)
                highestAttack = 0
                highestMoney = 0
                #Get the best combination
                for combination in possibleCombinations:
                    newAttack = 0
                    newMoney = 0
                    for index in combination:
                        if index == "S":
                            newAttack = newAttack + 1
                            newMoney = newMoney + 2
                        if index in range(0,central['activeSize']):
                            newAttack = newAttack + central['active'][int(index)].get_attack()
                            newMoney = newMoney + central['active'][int(index)].get_money()
                        #If aggressive, get the combination with highest attack
                        #If more than one combinations have same attack value, get the one with higher money value
                        if aggressive:
                            if newAttack == highestAttack:
                                if newMoney > highestMoney:
                                    bestCombination = combination
                            elif newAttack > highestAttack:
                                highestAttack = newAttack
                                bestCombination = combination
                                if newMoney > highestMoney:
                                    highestMoney = newMoney  
                        #If acquisative, get the combination with highest money
                        #If more than one combinations have same money value, get the one with higher attack value
                        if acquisative:
                            if newMoney == highestMoney:
                                if newAttack > highestAttack:
                                    bestCombination = combination
                            elif newMoney > highestMoney:
                                highestMoney = newMoney
                                bestCombination = combination
                                if newAttack > highestAttack:
                                    highestAttack = newAttack
                #Computer buy cards
                for index in bestCombination:
                    if index in range(0,central['activeSize']):                        
                        money = money - central['active'][int(index)].cost
                        card = central['active'].pop(int(index))
                        print "Card bought %s" % card
                        pC['discard'].append(card)
                        if( len(central['deck']) > 0):
                            card = central['deck'].pop()
                            central['active'].append(card)
                        else:
                            central['activeSize'] = central['activeSize'] - 1
                    else:
                        money = money - central['supplement'][0].cost
                        card = central['supplement'].pop()
                        pC['discard'].append(card)
                        print "Supplement Bought %s" % card
            else:
                print "No Money to buy anything"                    
            #Check card exhausted. If no card anymore, end game
            if central['activeSize'] == 0:
                print "\nNo more cards available"
                if pO['health'] > pC['health']:
                    print "Player One Wins on Health!"
                elif pC['health'] > pO['health']:
                    print "Computer Wins on Health!"
                else:                                                 #？？？？？
                    pHT = 0
                    pCT = 0
                    if pHT > pCT:
                        print "Player One Wins on Card Strength!"
                    elif pCT > pHT:
                        print "Computer Wins on Card Strength!"
                    else:
                        print "Draw!"
                cG = False

        #If game did not end                 
        if cG:
            #Computer move cards in hand to discard pile
            if (len(pC['hand']) >0 ):
                for x in range(0, len(pC['hand'])):
                    pC['discard'].append(pC['hand'].pop())
            #Computer move cards in active area to discard pile
            if (len(pC['active']) >0 ):
                for x in range(0, len(pC['active'])):
                    pC['discard'].append(pC['active'].pop())
            #Computer draws a new hand from its deck. If deck is empty, then shuffle discard pile and move to the deck
            for x in range(0, pC['handsize']):
                        if len(pC['deck']) == 0:
                            random.shuffle(pC['discard'])
                            pC['deck'] = pC['discard']
                            pC['discard'] = []
                        card = pC['deck'].pop()
                        pC['hand'].append(card)
            print "---------------Computer Turn Ending---------------"
        #If game ended. Start a new game
        if not cG:
            pG = raw_input("\nDo you want to play another game?(Y=Yes, N=No):").upper()
            while (pG!='Y' and pG!='N'):
                print("\nWrong input, please input again! (Y=Yes, N=No)")
                pG = raw_input('Do you want to play a game?(Y=Yes, N=No):').upper()
            cG = (pG=='Y')
            nG = (pG=='N')
            while nG:
                print("Thank you!")
                sys.exit()
            if cG:
                oT = raw_input("Do you want an aggressive (A) opponent or an acquisative (Q) opponent?:").upper()
                while (oT!='A' and oT!='Q'):
                    print("\nWrong input, please input again! (A=Aggressive, Q=Acquisative)")
                    oT = raw_input("Do you want an aggressive (A) opponent or an acquisative (Q) opponent?:").upper()
                aggressive = (oT=='A')
                acquisative = (oT=='Q')
                #Call functions to initiate
                playerOneInitial()
                playerComputerInitial()
                mainDeckCentralLineInitial()

    exit()

