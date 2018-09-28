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
    Id = lookahead
    if Id not in symtab:
        if _type == 'int':
            symtab[Id] = [int,0]
        elif _type == 'real':
            symtab[Id] = [float,0]
        else:
            print('Syntax Error: Invalid Type')
            exit()
        match(Id)
    if lookahead == ',':
        match(',')
        id_list(symtab, _type)
    return symtab
    
def decl(symtab):
    global lookahead
    _type = lookahead
    match(_type)
    if lookahead != 'int' or lookahead != 'real' or lookahead != ',' or lookahead != ';':
        symtab = id_list(symtab, _type)
    match(';')
    return symtab

def decl_list(symtab):
    global lookahead
    symtab = decl(symtab)
    while lookahead == 'int' or lookahead == 'real':
        symtab = decl(symtab)
    return symtab     
def prog():
    global lookahead
    symtab = dict()
    while True:
        if lookahead == 'int' or lookahead == 'real':
             symtab = decl_list(symtab)
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
