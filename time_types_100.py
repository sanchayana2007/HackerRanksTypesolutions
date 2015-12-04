__author__ = 'Sanchayan'
from datetime import date,datetime,timedelta

'The Head Librarian at a library wants you to make a program that calculates the fine for returning the book after the return date.' \
'You are given the actual and the expected return dates'\
'Calculate the Expected return date by the Price'
fine = 2
def cal_fine(expected_ret,actual_ret):
    if expected_ret > actual_ret:
        duration =  expected_ret - actual_ret
        #Duration is a time delta object
        return int(duration.days * fine)
    return "No Fine"
def Expected_Ret_date(price):
    today = datetime.now()
    days = price/2
    #convert the int into timedelta to get the arithmatic stuffs working
    expected_ret=today + timedelta(days)
    print(expected_ret.strftime('%d/%m/%Y'))

if __name__ == '__main__':

    #Entry in a int in a Tuple
    expected_date = (2013,1,1)
    actual_date = (2012,1,10)
    e = date(expected_date[0],expected_date[1],expected_date[2])
    a = date(actual_date[0],actual_date[1],actual_date[2])
    print('fine',cal_fine(e,a))
    #Entry in String formats Taken
    a = datetime.strptime('May 1 2005', '%b %d %Y')
    e = datetime.strptime('21/06/2005', '%d/%m/%Y')
    print('fine',cal_fine(e,a))

    #Expected Day calculation based on the Price
    Expected_Ret_date(20)