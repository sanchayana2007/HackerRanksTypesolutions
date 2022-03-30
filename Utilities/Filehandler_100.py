 
def handle_file(filename,choice):
 fd=open(filename)
 try:
   if choice == 'Normal':
    fd=open(filename,w)
   elif choice == 'NOBUF':
    '''0 means unbuffered, 1 means line buffered, any other positive value means use a buffer of (approximately
    that size. A negative buffering means to use the system default, which is usually line buffered for tty devices
    and fully buffered for other files. If omitted, the system default is used.'''
     fd=open(filename,w,buffering=0)
    elif choice == 'LNBUF':
     fd=open(filename,w,buffering=1)
    
   
   contetnts=fd.read()
   # Do something with contents
 except IOError: 
  sys.stderr.write(error)
 finally:
  fd.flush() ## Forcefully write whatever is present in your buffer 
  fd.close()
  
def read_from():
    with open('data.txt', 'r') as f:
    data = f.readlines()

    for line in data:
        words = line.split()
        print words



if __name__=="__main__":
 handle_file('test.txt')
