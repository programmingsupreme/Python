
import random

class Card:


    def __init__(self):
        '''
        Constuctor
        '''
        list1=['\u2665','\u2600','\u2663','\u2666']
        random.shuffle(list1)
        self.suit=list1[0]
        thenum=random.randint(0,1)
        if thenum==0:
            self.number = random.randint(1,10)
        else:
            list2=['K','Q','J']
            random.shuffle(list2)
            self.number = list2[0]


    def __str__(self):
        return str(self.number)+self.suit

    
    def __len__(self):
        return len(str(self))

    def sum(arr):
        '''
        Returns the sum of all the cards in a given array
        '''
        tot=0
        for card in arr:
            tot+=card.getvalue()

        return tot

    def getvalue(self):
        '''
        Returns the numerical value of a card
        '''
        value=0
        if len(self)==2:
            
            if self.number=='K':
                value=13
            elif self.number=='Q':
                value=12
            elif self.number=='J':
                value=11
            else:
                value = self.number
        else:
            value = 10
        
        return value
