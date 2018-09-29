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

def match(ch):
    global lookahead
    if ch == lookahead:
        lookahead = lexan()
    else:
        print('Syntax Error')
        exit()
        
def id_list(_type):
    global lookahead
    global symtab
    _id = lookahead
    if _id not in symtab:
        if _type == 'int':
            symtab[_id] = [int,0]
        elif _type == 'real': #reals stored as float
            symtab[_id] = [float,0]
        match(_id)
    if lookahead == ',':
        match(',')
        if isId(lookahead):
            id_list(_type) #recursion
    
def decl():
    global lookahead
    _type = lookahead
    match(_type)
    if isId(lookahead): 
        id_list(_type)
    match(';')
    
def decl_list():
    global lookahead
    decl()
    while isType(lookahead):
        decl()
        
def oprnd(_oprnd):
    global symtab
    if _oprnd in symtab.keys():
        match(_oprnd)
        return symtab[_oprnd][1] # value of id
    elif isNumber(_oprnd):
        match(_oprnd)
        return _oprnd
    else:
        print('Syntax Error: invalid operand')
        exit()

def cond():
    global lookahead
    op1 = oprnd(lookahead)
    if lookahead == '<':
        match('<')
        op2 = oprnd(lookahead)
        return op1 < op2
    elif lookahead == '>':
        match('>')
        op2 = oprnd(lookahead)
        return op1 > op2
    elif lookahead == '<=':
        match('<=')
        op2 = oprnd(lookahead)
        return op1 <= op2
    elif lookahead == '>=':
        match('>=')
        op2 = oprnd(lookahead)
        return op1 >= op2
    elif lookahead == '==':
        match('==')
        op2 = oprnd(lookahead)
        return op1 == op2
    elif lookahead == '!=':
        match('!=')
        op2 = oprnd(lookahead)
        return op1 != op2
    
def stmt():
    global lookahead
    global symtab
    if isId(lookahead):
        _id = lookahead
        if _id not in symtab.keys():
            print('Syntax Error: invalid Id')
            exit()
        else:
            _type = symtab[_id][0]
            _cond = bool
            match(_id)
            match('=')
            symtab[_id][1] = expr(_type)
            if lookahead == 'if':
                match('if')
                _cond = cond()
                match('else')
                if _cond == False:
                    symtab[_id][1] = expr(_type)
                else:
                    expr(_type)                    
                match(';')
            else:
                match(';')         
    elif lookahead == 'printi':
        match('printi')
        print(expr(int))
        match(';')
    elif lookahead == 'printr':
        match('printr')
        print(expr(float))
        match(';')
    else:
        print('Syntax Error: Invalid Symbol')
        exit()

def stmt_list():
    global lookahead
    stmt()
    while isId(lookahead) or lookahead == 'printf' or lookahead == 'printi':
        stmt()
        
def prog():
    global lookahead
    while True:
        if isType(lookahead):
            decl_list()
        else:
            stmt_list()
        if lookahead == '':
            print('Pass')
            break

def isType(ch):
    types = ['int', 'real']
    if ch not in types:
        return False
    return True

def getType(ch):
    return type(ch)

def isId(ch):
    global reserved_words
    if isNumber(ch):
        return False
    elif ch in reserved_words:
        return False
    return True

def isNumber(ch):
    try:
        float(ch)
        return True
    except ValueError:
        return False

    
#start of the program
import sys
file = open(sys.argv[1], "r")
wlist = file.read().split()

symtab = dict()
reserved_words = ['printi', 'printr','int', 'real',',', ';','(',')','^','/', '=', '+', '-', '*', '<', '>', '<=', '>=', '==', '!=', 'if', 'else'] 
mitr = iter(wlist)
lookahead = lexan()

prog() 
