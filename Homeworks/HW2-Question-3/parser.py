#this is a top-down recursive parser
#Peter Parianos CIS424

def lexan(): #lexical analyzer that basically uses an global iterator 
    global mitr

    #we will test the iteration and if an exception occurs, lexan() will return NULL
    try:
        return(next(mitr)) # this will advance the element by one, the next item in the list
    except StopIteration:
        return ''
    
def match(ch):
    global lookahead

    if ch == lookahead:
            #we will check if the passed character is equal to the current lookaead character
            #if this is true then iterate to the next letter
        lookahead = lexan()
    else:
        print("Syntax Error")
        exit()

def S():
        #this is a start definition: <S> -> <X> z <Y> | <Y> z <X> 
    global lookahead
    
    #this make use of recursion embedded in the python language itself
    if lookahead == 'x':
        X()
        match('z')
        Y()
    elif lookahead == 'y':
        Y()
        match('z')
        X()
    else:
        print("Syntax Error")
        exit()
        
def X(): #this is for the grammar definition <X> -> x <X> | x 
    global lookahead
    match('x')  #always make sure first letter is x
    if lookahead == 'x':
        X()
        
def Y(): #this is for the grammar definition <Y> -> y <Y> | y
    global lookahead
    match('y')
    if lookahead == 'y':
        Y()

#open the file, read the file, and place in wlist delimited with default char  
import sys
file = open(sys.argv[1], "r")
wlist  = file.read().split()

#we will attach an iterator to this list
mitr = iter(wlist)

#this will look at the next letter, only one is needed. Tis is to give us hits
lookahead = lexan()

S()

if lookahead == "": #checks if empty, if true then there are no invalid caracters
        print("pass")
else:
        print("Syntax Error")
        exit()

    

    


