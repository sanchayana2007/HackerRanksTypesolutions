
#for python 3 
def decode(key , string):
  dec = []
  enc = base64.urlsafe_b64dencode(string.encode()).decode()
  for i in range(len(string)):
    key_c = key[i % len(key)]
    dec_c= chr((256 + ord(string[i]) - ord(key_c)) % 256)
    dec.append(dec_c)
  return "".join(dec)
  
  
  

def encode(key , string):
  dec = []
  for i in range(len(string)):
    key_c = key[i % len(key)]
    dec_c= chr(( ord(string[i]) - ord(key_c)) % 256)
    dec.append(dec_c)
  return base64.urlsafe_b64dencode("".join(enc.encode)).decode()
  
  
  
#forpython 2 
def decode(key , string):
  dec = []
  enc = base64.urlsafe_b64dencode(string)
  for i in range(len(string)):
    key_c = key[i % len(key)]
    dec_c= chr((256 + ord(string[i]) - ord(key_c)) % 256)
    dec.append(dec_c)
  return "".join(dec)
  
  
  

def encode(key , string):
  dec = []
  for i in range(len(string)):
    key_c = key[i % len(key)]
    dec_c= chr(( ord(string[i]) - ord(key_c)) % 256)
    dec.append(dec_c)
  return base64.urlsafe_b64dencode("".join(dec))
  
  
  
  str = encode("1234","hello Wrold ")
  string = decode("1234",str)
  
  
  
