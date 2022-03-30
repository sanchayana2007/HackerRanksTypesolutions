__author__ = 'Sanchayan'
from sqlalchemy import *
engine = create_engine('sqlite:///tutorial.db', echo=True)

metadata = MetaData(engine)
users = Table('users', metadata,Column('users',Integer,primary_key=True),Column('name',String),
              Column('age',Integer),Column('password',String),)
try :
    users.create()
except Exception as e:
    print ('Exception',e)
    pass
#i = users.insert()
#i.execute(name='mary',age=30,password='secreat')
#i.execute({'name':'Jhon','age':'42'},{'name':'Santa','age':'4'},{'name':'carl','age':'55'})
s= users.select()
rs=s.execute()

row= rs.fetchone()
print('Id',row[0])
print('Name',row['name'])
print('Age',row.age)
print('Password',row[users.c.password])
for row in rs:
    print(row.age)





# The users table already exists, so no need to redefine it. Just
# load it from the database using the "autoload" feature.
users_table = Table('users', metadata, autoload=True)

def run(stmt):
    rs = stmt.execute()
    for row in rs:
        print ('Row',row)


s = users_table.select(users_table.c.name == 'John')
run(s)
s = users_table.select(users_table.c.age < 40)
run(s)

# Python keywords like "and", "or", and "not" can't be overloaded, so
# SQLAlchemy uses functions instead
s = users_table.select(and_(users_table.c.age < 40, users_table.c.name != 'mary'))
run(s)
s = users_table.select(or_(users_table.c.age < 40, users_table.c.name != 'mary'))
run(s)
s = users_table.select(not_(users_table.c.name == 'Susan'))
run(s)

# Or you could use &, | and ~ -- but watch out for priority!
s = users_table.select((users_table.c.age < 40) & (users_table.c.name != 'mary'))
run(s)
s = users_table.select((users_table.c.age < 40) | (users_table.c.name != 'mary'))
run(s)
s = users_table.select(~(users_table.c.name == 'Susan'))
run(s)

# There's other functions too, such as "like", "startswith", "endswith"
s = users_table.select(users_table.c.name.startswith('m'))
run(s)
s = users_table.select(users_table.c.name.like('%a%'))
run(s)
s = users_table.select(users_table.c.name.endswith('n'))
run(s)

# The "in" and "between" operations are also available
s = users_table.select(users_table.c.age.between(30,39))
run(s)


# If you want to call an SQL function, use "func"
s = users_table.select(func.substr(users_table.c.name, 2, 1) == 'a')
run(s)

# You don't have to call select() on a table; it's got a bare form
s = select([users_table], users_table.c.name != 'carl')
run(s)
s = select([users_table.c.name, users_table.c.age], users_table.c.name != 'carl')
run(s)

# This can be handy for things like count()
s = select([func.count(users_table.c.users)])
run(s)
# Here's how to do count(*)
s = select([func.count("*")], from_obj=[users])
run(s)


emails = Table('emails', metadata,
    Column('email_id', Integer, primary_key=True),
    Column('address', String),
    Column('user_id', Integer, ForeignKey('users.users')),
)
#emails.create()
#i = users.insert()
#i.execute(
    # There's a better way to do this, but we haven't gotten there yet
 #   {'address': 'mary@example.com', 'user_id': 1},
  #  {'address': 'john@nowhere.net', 'user_id': 2},
   # {'address': 'john@example.org', 'user_id': 2},
    #{'address': 'carl@nospam.net', 'user_id': 4},
#)
# This will return more results than you are probably expecting.
s = select([users, emails])
run(s)

# The reason is because you specified no WHERE clause, so a full join was
# performed, which returns every possible combination of records from
# tables A and B. With an appropriate WHERE clause, you'll get the
# restricted record set you really wanted.
s = select([users, emails], emails.c.user_id == users.c.users)
run(s)

# If you're interested in only a few columns, then specify them explicitly
s = select([users.c.name, emails.c.address],
           emails.c.user_id == users.c.users)
run(s)

# There are also "smart" join objects that can figure out the correct join
# conditions based on the tables' foreign keys
s = join(users, emails).select()
run(s)

# If you want all the users, whether or not they have an email address,
# then you want an "outer" join.
s = outerjoin(users, emails).select()
run(s)

# Order of outer joins is important! Default is a "left outer join", which
# means "all records from the left-hand table, plus their corresponding
# values from the right-hand table, if any". Notice how this time, Susan's
# name will *not* appear in the results.
s = outerjoin(emails, users).select()
run(s)

