__author__ = 'Sanchayan'
'Louise and Richard play a game. They have a counter set to N. Louise gets the first turn and the turns alternate thereafter' \
'In the game, they perform the following operations.' \
'If N is not a power of 2, reduce the counter by the largest power of 2 less than N.' \
'If N is a power of 2, reduce the counter by half of N.' \
'The resultant value is the new N which is again used for subsequent operations.' \
'The game ends when the counter reduces to 1, i.e., N == 1, and the last person to make a valid move wins.' \
'Given N, your task is to find the winner of the game.'

def Power2_lesserN(N):
    num = N
    while(num>1):
        num = num -1
        if not num & num-1:
            print('Closet pow 2',num)
            return num

def whoiswinner(N):
    Turn = 1
    while N > 1:
        if not N & N-1:
            N= N - int(N/2)
        else:
            N = N - Power2_lesserN(N)
        Turn = Turn +1
    print('Number of Turns on my code ',Turn)
    if Turn % 2 ==0 :
        print('ricard')
    else:
        print('Louise')





def getClosestSmaller(x):
    x |= x >> 1
    x |= x >> 2
    x |= x >> 4
    x |= x >> 8
    x |= x >> 16
    x |= x >> 32
    x = x + 1
    x = x >> 1
    return x

def getNrReductions(x):
    reductions = 1

    while (x != 1):
        x = int(x)
        if x & x-1:
            #print "x is not power of two"
            x -= getClosestSmaller(x)
        else:
            #print "x is power of two"
            x /= 2
        reductions += 1

    return reductions





if __name__=='__main__':
    ## Calls my code
    N = 20
    whoiswinner(20)

    ## calls martin kysels code
    n = getNrReductions(N)
    print('Numebr of turns in Martin Kysels Code',n)
    if  n % 2 != 0:
        print ("Richard")
    else:
        print ("Louise")
