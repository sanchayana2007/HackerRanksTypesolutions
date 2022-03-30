__author__ = 'Sanchayan'
#this string of integers will be coneverted into individual characters list
l = list("314159123456908345")


def Is_song_py(song):
    for idx,i in enumerate(song):
        if  int(l[idx]) != len(i):
            return  False
    return True

if __name__ =='__main__':
    song = ['you','r','this','a','reste','wqwqdder']
    if Is_song_py(song):
        print('Song of PI')
    else:
        print('Not Song of PI')