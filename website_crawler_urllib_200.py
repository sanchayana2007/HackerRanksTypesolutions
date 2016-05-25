__author__ = 'Sanchayan'
import urllib.parse
import urllib.request
# Url to be Opened
def show_page_data(url):

    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

    # Values or fields of Data to be passed
    values = { }
    # header Will have your Machine and browser information of data
    headers = { 'User-Agent' : user_agent }

    # Lets Encode Every Thing
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')

    try:
        req = urllib.request.Request(url, data, headers)
        response = urllib.request.urlopen(req)
        the_page = response.read()
        return the_page
    except Exception as e:
        print(e)


if __name__== "__main__":
    url = 'http://google.com/search?=test'
    print( show_page_data(url))