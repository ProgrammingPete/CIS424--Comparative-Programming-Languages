#you need to put comments in your code
#example in the class
#this is a top-down recurive parser

import sys
file = open(sys.argv[1], "r")


wlist  = file.read().split()

mitr = iter(wlist)

#this will lok at the first letter, only one is needed
lookahead = lexan()
s()

if lookahead == "": #checks if empty
        print("pass")
    else:
        print("Syntax Erorr")
        exit()

    
def lexan(): #lexical analyzer
    global mitr
    try:
        return(next(mitr)) # this will advance the element by one
    except StopIteration:
        return('')
    
def match(ch):
    global lookahead

    if ch == lookahead:
        lookahead = lexan()
    else:
        print("Syntax Error")
        exit()

def s():
    global lookahead
    if lookahead == 'a':
        A()
        match('c') # different rules: add C()
    else if lookahead == 'b':
        B()
        match('c')
    else:
        print("Syntax Error")
        exit()
def A():
    global lookahead
    match('a') # no matter what we will have this because 
    if lookahead == 'a':
        A()
def B():
    global lookahead
    match('b')
    if lookahead == 'b':
        B()
    


