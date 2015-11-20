__author__ = 'Sanchayan'
from datetime import date,datetime
'The Head Librarian at a library wants you to make a program that calculates the fine for returning the book after the return date.' \
'You are given the actual and the expected return dates'
fine = 2
def cal_fine(expected_ret,actual_ret):
    if expected_ret.year < actual_ret.year:
        yr_passed = expected_ret.year - actual_ret.year
        duration = actual_ret - expected_ret
        return duration * fine

if __name__ == '__main__':
    expected_date = (2012,1,1)
    actual_date = (2012,1,10)
    e = date(expected_date[0],expected_date[1],expected_date[2])
    a = date(actual_date[0],actual_date[1],actual_date[2])
    print('fine',cal_fine(e,a))
    date_object77 = datetime.strptime('May 1 2005', '%b %d %Y')
    print(date_object77)
    date_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

