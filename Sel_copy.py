__author__ = 'Sanchayan'
import os

if __name__=='__main__':
    Src = 'D:\codes'
    Dest = 'D:\codesCopy'
    dir_list = []
    dir_list.append(Src)

    for dir in dir_list:
        l=	os.listdir(dir)
        for i in l:
            entity =dir + "\\" + i
            if os.path.isdir(entity) :

                print('Folder\  ',entity)
                dir_list.append(entity)
                Commnad = Dest + "\\" + entity.lstrip()[3:]
                if not os.path.isdir(Commnad):
                    create_dir = 'mkdir ' + Commnad
                    print(create_dir)
                    os.system(create_dir)

            else:
                print('File',entity)

