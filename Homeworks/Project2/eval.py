#!/usr/bin/python3
#
#Input is separated by spaces.
#
#type    id_list
#int   x , y , x ;
#real  f , g ;
#this pertains to the lexan() lexical analyzer
#
#variables  must be declared beofre being used. Also initialized to 0
#create symbol table mapping 'variable_name': [type, val] (dictionaries)
#
#use type() to return the type. can tell if it is an interger or a float
#"""

def lexan():
    global mitr
    #we will test the iteration and if an exception occurs, lexan() will return NULL
    try:
        return(next(mitr)) # this will advance the element by one, the next item in the list
    except StopIteration:
        return ''

def match(string):
    global lookahead
    if string == lookahead:
        lookahead = lexan()
    else:
        print('Syntax Error')
        exit()
def id_list(symtab, _type):
    global lookahead
    name = lookahead
    if name == ',':
        print('Syntax Error: Illegal Name')
        exit()
    elif name not in symtab:
        if _type == 'int':
            symtab[name] = [int, 0] #dictionary points to a list
        elif _type == 'real':
            symtab[name] = [float, 0]
        match(name)
        return
    elif name in symtab:
        print("Syntax Error: Name already Defined")
        exit()
        
def decl(symtab, _type):
    global lookahead
    
    while True: #user needs to remember to put the ';', else loop with be inf                                          
        id_list(symtab, _type)
        if lookahead == ',':
            match(',')
            continue
        elif lookahead == ';':
            match(';')
            return
        else:
            print("Syntax Error: forgot comma? ")
            exit()
                
def decl_list():
        """Creation of the dictionary (Symbol Table := 'name': [type, val])"""
        global lookahead        
        symtab = dict()
        while True:
            if lookahead == 'int':
                match('int')
                decl(symtab, 'int')
            elif lookahead == 'real':
                match('real')
                decl(symtab, 'real')
            else:
                return symtab #this is all variable declarations

def prog():
    global lookahead
    while True:
        if lookahead == 'int' or lookahead == 'real':
             symtab = decl_list()
        else:
            stmt_list()

#start of the program
import sys
file = open(sys.argv[1], "r")
wlist = file.read().split()

mitr = iter(wlist)
lookahead = lexan()

prog()

if lookahead == "":
    print("pass")
else:
    print("Syntax Error")
    exit()
