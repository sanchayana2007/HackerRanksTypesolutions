__author__ = 'Sanchayan'

from html.parser import *


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
  def __init__(self):
    self.tableParsingOngoing = False
    self.charref = False
    self.exclude = False
    self.row_started = False
    self.key_started = False
    self.value_started = False
    self.key = ''
    self.value = ''
    self.L = list()
    self.D = dict()
    HTMLParser.__init__(self)

  def handle_startendtag(self, tag, attrs):
    if tag == 'table':
      self.tableParsingOngoing = True

    #if self.tableParsingOngoing == True:
    #  print('tag: ', tag, attrs)


  def handle_charref(self, name):
    if self.tableParsingOngoing == True:
      #print(name)
      self.charref = True

  def handle_starttag(self, tag, attrs):
    if tag == 'table':
      self.tableParsingOngoing = True

    if tag == 'tr':
      self.row_started = True

    if tag == 'th' and self.row_started == True:
      self.key_started = True

    if tag == 'td' and self.row_started == True:
      self.value_started = True

    if self.tableParsingOngoing == True and tag != '':
      #self.L.append(tag.strip())
      pass

  def handle_endtag(self, tag):
    if tag == 'table':
      self.tableParsingOngoing = False

    if tag == 'tr':
      self.row_started = False

    if tag == 'th' and self.row_started == True:
      self.key_started = False

    if tag == 'td' and self.row_started == True:
      self.value_started = False
      self.D[self.key] = self.value
      self.key = ''
      self.value = ''

    if self.tableParsingOngoing == True and tag != '':
      #self.L.append(tag.strip())
      pass

  def handle_data(self, data):
    if self.tableParsingOngoing == True and data != '' and data != '\n':
      if self.charref == True and len(self.L) >= 1:
        self.charref = False
        item = self.L[len(self.L) - 1]
        item = item + ' ' + data
        self.L[len(self.L) - 1] = item
        if self.key_started == True:
          if self.key != '':
            self.key = self.key + ' ' + item
          else:
            self.key = item
        if self.value_started == True:
          if self.value != '':
            self.value = self.value + ' ' + item
          else:
            self.value = item
      else:
        data = data.replace('\n', '')
        data = data.replace(',', '')
        data = data.replace(';', '')
        data = data.replace(':', '')
        #if data not ' '
        if data.startswith(' '):
          data = data[1:]
        if data.endswith(' '):
          data = data[:len(data) - 1]

        if data == '[':
          self.exclude = True
        elif data == ']':
          self.exclude = False
        elif data != '' and self.exclude == False:
          self.L.append(data)
          if self.key_started == True:
            if self.key != '':
              self.key = self.key + ' ' + data
            else:
              self.key = data
          if self.value_started == True:
            if self.key != '':
              self.value = self.value + ' ' + data
            else:
              self.value = self.value
        else:
          pass

  def display(self):
    print(self.L)
    print('Dictionary:\n',self.D)

f = open('a.html')
X = MyHTMLParser()
X.feed(f.read().strip())
X.display()