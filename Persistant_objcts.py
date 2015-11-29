__author__ = 'Sanchayan'

from collections import defaultdict

class Posts(object):
    def __init__(self,date,title,rst_text,tags):
        self.date = date
        self.title = title
        self.rst_text = rst_text
        self.tags = tags

    def as_dict(self):
        return dict(date = str(self.date),title = self.title,underline = '_'*len(self.title),rst_text = self.rst_text,
                    tag=''.join(tags))




class Blog:
    def __init__( self, title, posts=None ):
        self.title= title
        self.entries= posts if posts is not None else []
    def append( self, post ):
        self.entries.append(post)

    def by_tag(self):
        tag_index= defaultdict(list)
        for post in self.entries:
            for tag in post.tags:
                tag_index[tag].append( post.as_dict() )
        return tag_index

    def as_dict( self ):
        return dict(
            title= self.title,
            underline= "="*len(self.title),
            entries= [p.as_dict() for p in self.entries],)


if __name__== '__main()':

    travel = Blog( "Travel" )
    travel.append(
        Posts( date=datetime.datetime(2013,11,14,17,25),
              title="Hard Aground",
              rst_text="""Some embarrassing revelation.Including ? and ?""",
              tags=("#RedRanger", "#Whitby42", "#ICW"),)
    )

    travel.append(
        Posts( date=datetime.datetime(2013,11,18,15,30),
        title="Anchor Follies",
        rst_text="""Some witty epigram. Including < & >characters.""",
        tags=("#RedRanger", "#Whitby42", "#Mistakes"),)
    )