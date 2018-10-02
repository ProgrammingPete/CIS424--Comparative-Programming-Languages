#!/usr/bin/python3
#Project 2
#Peter Parianos, Azam Ashrabkhujaev 
#Input is separated by spaces.
#
#type    id_list
#int   x , y , x ;
#real  f , g ;
#this pertains to the lexan() lexical analyzer
#
#variables  must be declared beofre being used. Also initialized to 0
#create symbol table mapping 'variable_name': val (dictionaries)
#

def lexan(): # lexical analyzer
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
        print('Syntax Error: missing', ch)
        exit()
        
def id_list(_type):
    global lookahead
    global symtab
    _id = lookahead
    if _id not in symtab:
        if _type == 'int':
            symtab[_id] = 0 # this makes more sense since 0 is int and 0.0 is float
        elif _type == 'real': #reals stored as float
            symtab[_id] = 0.0
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
        
def oprnd(_type,_oprnd):
    global symtab
    if _oprnd in symtab.keys():
        match(_oprnd)
        return check_type(symtab[_oprnd], _type) # value of id
    elif isNumber(_oprnd):
        match(_oprnd)
        return check_type(_oprnd,_type)
    else:
        print('Syntax Error: invalid operand: ', _oprnd)
        exit()

def cond(_type):
    global lookahead
    op1 = oprnd(_type,lookahead)
    if lookahead == '<':
        match('<')
        op2 = oprnd(_type,lookahead)
        return op1 < op2
    elif lookahead == '>':
        match('>')
        op2 = oprnd(_type,lookahead)
        return op1 > op2
    elif lookahead == '<=':
        match('<=')
        op2 = oprnd(_type,lookahead)
        return op1 <= op2
    elif lookahead == '>=':
        match('>=')
        op2 = oprnd(_type,lookahead)
        return op1 >= op2
    elif lookahead == '==':
        match('==')
        op2 = oprnd(_type,lookahead)
        return op1 == op2
    elif lookahead == '!=':
        match('!=')
        op2 = oprnd(_type,lookahead)
        return op1 != op2
    else:
        print('Syntax Error: invalid operator: ', lookahead)
        exit()
#term
def term(_type):
    global lookahead
    f = factor(_type)
    while True:
        if lookahead == '*':
            match('*')
            f *= factor(_type)
        elif lookahead == '/':
            match('/')
            f /= factor(_type)
        else:
            return f

def base(_type):
    global lookahead
    if lookahead == '(': #( <expr> )
        match('(')
        v = expr(_type)
        match(')')
        return check_type(v, _type)
    elif lookahead in symtab.keys(): #id
        _id = lookahead
        match(_id)
        return check_type(symtab[_id], _type)
    elif isNumber(lookahead): # intnum, realnum
        v = lookahead
        match(v)
        return check_type(v, _type)
    else:
        print('Syntax Error: Invalid Base, ', lookahead)
        exit()
            
    
    
def factor(_type):
    global lookahead
    op = base(_type)
    if lookahead == '^':
        match('^')
        return pow(op,factor(_type))
    else:
        return op
    
    
#expr
def expr(_type):
    global lookahead
    v = term(_type)
    while True:
        if lookahead == '+':
            match('+')
            v += term(_type)
        elif lookahead == '-':
            match('-')
            v -= term(_type)
        else:
            return v
        
def stmt():
    global lookahead
    global symtab
    if isId(lookahead):
        _id = lookahead
        if _id not in symtab.keys():
            print('Syntax Error: invalid Id')
            exit()
        else:
            _type = type(symtab[_id])
            _cond = bool
            match(_id)
            match('=')
            symtab[_id] = expr(_type)
            if lookahead == 'if':
                match('if')
                _cond = cond(_type)
                match('else')
                if _cond == False:
                    symtab[_id] = expr(_type)
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
        print('Syntax Error: Invalid Symbol: ', lookahead)
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
            continue
        elif lookahead != '':
            stmt_list()
            continue
        else:
            print('Pass')
            exit()
            
#######################
#peripheral functions
def isType(ch):
    types = ['int', 'real']
    if ch not in types:
        return False
    return True

def check_type(ch, _type):
    try:
        if _type == int:
            return int(ch)
        if _type == float:
            return float(ch)
    except ValueError:
        print('Syntax Error: Invalid Type: ', ch)
        exit()

def isId(ch):
    global reserved_words
    if isNumber(ch):
        return False
    elif ch in reserved_words:
        return False
    elif ch == '':
        return False
    return True

def isNumber(ch):
    try:
        float(ch)
        return True
    except ValueError:
        return False
    
#############################
    ##################
    
#start of the program
import sys
file = open(sys.argv[1], "r")
wlist = file.read().split()

symtab = dict()
reserved_words = ['printi', 'printr','int', 'real',',', ';','(',')','^','/', '=', '+', '-', '*', '<', '>', '<=', '>=', '==', '!=', 'if', 'else'] 
mitr = iter(wlist)
lookahead = lexan()

prog()
