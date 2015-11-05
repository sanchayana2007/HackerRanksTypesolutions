__author__ = 'Sanchayan'
'Louise and Richard play a game. They have a counter set to N. Louise gets the first turn and the turns alternate thereafter' \
'In the game, they perform the following operations.' \
'If N is not a power of 2, reduce the counter by the largest power of 2 less than N.' \
'If N is a power of 2, reduce the counter by half of N.' \
'The resultant value is the new N which is again used for subsequent operations.' \
'The game ends when the counter reduces to 1, i.e., N == 1, and the last person to make a valid move wins.' \
'Given N, your task is to find the winner of the game.'


def power2(N):

    while N%2==0 and N > 1:
        N=N/2
    return N==1

def counter_winner(N):
   pass

if __name__=='__main__':
   print( powerof2(128))
   print(power2(128))