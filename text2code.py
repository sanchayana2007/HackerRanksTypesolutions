__author__ = 'Sanchayan'
import os
import re


def cre_wrte(filename,contents):
    directory = 'Pycodes'
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(directory+'\\'+filename,'w') as f:
        f.write(contents)

def create_codefiles(contents):
    pat1=' --------------------'
    pat2='-----------------------------'
    contents1=" --------------------rrrr.cloocetions_100.py----------------------------- ' \
             '__author__ = \'Sanchayan' \
             from collections.abc import Set as ColSet\
            import inspect\
            \
            class ListBasedSet(ColSet):\
                def __init__(self,val):\
                    self.elements = []\
                    if val is  not None:\
                        [self.elements.append(x) for x in val if not x in self.elements ]\
            if __name__ == '__main__':\
            \
                s1 = ListBasedSet('dedefftys')\
                s2 = ListBasedSet('deddsdff')\
            #    [print(i) for i in s1 & s2]\
                for z in (i for i in inspect.getmembers(list())):\
                    print(z)\
            "
    total = 0
    start = 0
    pat1_search = re.compile(pat1)
    pat2_search = re.compile(pat2)
    macthes= pat1_search.search(contents,0)
    start1 = macthes.start()
    while contents:

        if macthes:
            contents= contents[macthes.end():]

            macthes= pat2_search.search(contents,0)
            if macthes:
                print(macthes.span())
                start2=macthes.start()
                filename= contents[start1:start2]
                contents= contents[:macthes.end()]
                file_contents= contents[macthes.end():]
               # print(contents)
                print(filename)

                macthes= pat1_search.search(file_contents)
                if macthes:
                    print(file_contents[:macthes.start()])
                else:
                    print(file_contents)
               # cre_wrte(filename,contents)



if __name__=="__main__":
    Src ="All2text.txt"
    with open(Src) as f:
        contents = f.read()
        create_codefiles(contents)