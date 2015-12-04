__author__ = 'Sanchayan'
import pickle

class SimpleBalclass(object):
    def __init__(self,text):
        self.text = text
    def as_dict(self):
        return dict(text = self.text)


class pickeltest:
    def __init__(self,text,*NOlisting):
        self.server_text = text
        self.sever_list = NOlisting
        #print(i.as_dict for i in self.sever_list)


    def as_dict(self):
        return dict(text = self.server_text,server_list = [i.as_dict() for i in self.sever_list])


if __name__== '__main__':
    p = pickeltest('complex bal', SimpleBalclass('Simple'),SimpleBalclass('Simple1'))
    print( p.as_dict())

    # The pickel object Load will produce the same as normal object
    with open('Balcomplex.p','wb') as target:
        pickle._dump(p,target)

    with open("Balcomplex.p","rb") as source:
        copy= pickle.load( source )
        print(copy.as_dict())

