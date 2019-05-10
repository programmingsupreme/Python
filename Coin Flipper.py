from random import randint


def flipcoin(numtoflip):
    coin={'H':0,'T':0}
    for numtoflip in range(numtoflip):
        if randint(0,1)==0:
            coin['H']+=1
        else:
            coin['T']+=1
    print(f"The coin was flipped {numtoflip+1} times. The number of heads is {coin['H']}. The number of tails is {coin['T']}")

while True:
    try:
        print('Enter the number of times to flip the coin, enter \'exit\' to exit')
        ans=input()
        ans=ans.upper()
        if ans[0]=='E':
            print('Have a good day!')
            quit()
        else:
            ans=int(ans)
            flipcoin(ans)
    except KeyboardInterruptError:
        quit()
    except:
        print('A error occurred please try again!')
