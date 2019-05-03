from Card import Card

playerhand=[]
dealerhand=[]
money=1000

def intro():
    '''
    Checks whether the user wants to play and what they wish to bet
    '''
    global money

    print('Do you want to play blackjack?')
    try:
        ans = input()
        ans=ans.strip()
        ans = ans.upper()
    except KeyboardInterrupt:
        quit()
    except:
        print('An error occured try again')
        intro()
    if ans[0]=='Y':
        while True:     
            try:
                bet = int(input(f'How much do you want to bet you have ${money}?'))
                if bet<=0:
                    print('That\'s too low')
                    continue
                elif bet>money:
                    print('You can\'t bet that much it\'s too high')
                    continue
                else:
                    money-=bet
                    print(f'Money has been changed to {money}')
            except KeyboardInterrupt:
                exit()
            except:
                print('An error occured. Please try again')

            game()
    else:
        print('Have a good day!')
        exit()

def makecards():
    '''
    Initailizes the dealer and player\'s hands with cards at the begining of the game
    '''
    global playerhand,dealerhand,money
    
    playerhand.append(Card())
    playerhand.append(Card())
    dealerhand.append(Card())
    if(Card.sum(playerhand)>21):
        playerhand=[]
        dealerhand=[]
        makecards()
    elif Card.sum(playerhand)==21:
        print(f'You won!')
        showhands()
        money+=(1000-money)*2
        print(f'Money has been changed to {money}')
        intro()
    
    
def showhands():
    '''
    Shows the cards the dealer and player hold and the total value to the hands of both players
    '''
    for card in dealerhand:
        print(card)
    print(f'The sum of the dealer\'s hand is {Card.sum(dealerhand)}')

    for card in playerhand:
        print(card)

    print(f'The sum of the the player\'s hand is {Card.sum(playerhand)}')

def hitstay():
    '''
    Checks to see if the player wants to hit or stay and adds cards to the appropriate hand
    '''
    global playerhand,dealerhand

    print('Do you want to hit or stay?')
    try:
        ans = input()
        ans=ans.upper()
    except KeyboardInterrupt:
        quit()
    except:
        print('An error occured. Please try again')
        hitstay()
    if ans[0]=='H':
        playerhand.append(Card())
    elif ans[0]=='S':
        dealerhand.append(Card())
    else:
        print('That was not a option. Please enter \'Hit\' or \'Stay\'')
        hitstay()

def checkwin():
    '''
    Checks to see if someone has won or lost
    '''
    global playerhand,dealerhand,money
    
    if Card.sum(playerhand)==21:
        print('Congrats you won')
        money+=(1000-money)*2
        print(f'Money has been changed to {money}')
        dealerhand=[]
        playerhand=[]
        intro()
    elif Card.sum(dealerhand)==21:
        print('The dealer won!')
        dealerhand=[]
        playerhand=[]
        intro()
    elif Card.sum(playerhand)>21:
        print('You went over 21 and lost!')
        dealerhand=[]
        playerhand=[]
        intro()
    elif Card.sum(dealerhand)>21:
        print('Dealer Bust')
        money+=(1000-money)*2
        print(f'Money has been changed to {money}')
        dealerhand=[]
        playerhand=[]
        intro()


def game():
    '''
    Runs the main game loop
    '''
    makecards()
    while True:
        showhands()
        hitstay()
        checkwin()

if __name__ == '__main__':
    intro()
