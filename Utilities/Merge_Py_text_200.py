__author__ = 'Sanchayan'
import os

def read_file(file,Dst):
   print(file,Dst)

   with open(Src + file) as f:
       file_content = f.read()
       with open(Dst,'a') as w:
           file_seperation = '\n --------------------'+ file + '-----------------------------\n'

           w.write(file_seperation + file_content)

if __name__ =="__main__":
    Src = str('C:\\Users\Sanchayan\Documents\GitHub\HackerRanksTypesolutions\\')
    Dest = 'D:\All2text.txt'
    onlypyfiles = []
    files =os.listdir(Src)
    [read_file(file,Dest) for file in files if 'py' == file[-2:]]






