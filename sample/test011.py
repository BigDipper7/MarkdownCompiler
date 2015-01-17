# -----------------------------------------------------------------------------
# @author globit
# This is template code of markdown generating by ply
# @update 2014-12-16
# @lience MIT
# -----------------------------------------------------------------------------
import sys

tokens = (
    'H1','H2','H3', 'CR', 'TEXT', 'STRONG', 'EM','HR','HH','CODE','HREF1','HREF2' ,'HREF3','UL','OL','COMMENT'

)
# Tokens
t_H1 = r'\# '
t_H2 = r'\#\# '
t_H3 = r'\#\#\# '
t_STRONG = r'\*\* |__ '
t_EM = r'\* |_ '
t_HR = r'(\-\-\-)'
t_HH = r'\=\=\= '
t_CODE = r'`'
t_HREF1= r'\[|\]'
t_HREF2= r'\(|\)'
t_HREF3= r'<|>'
t_UL= r'\+'
t_OL= r'\d\.'
t_COMMENT = r'\t'
def t_TEXT(t):
    r'[a-zA-Z,\/\.\':^-]+'
    t.value = str(t.value)
    return t

t_ignore = " "
#def t_ignore_COMMENT(t): r'\t+'
    


def t_CR(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lex.er
import ply.lex as lex
lex.lex()

# ------------------------------------
# definitions of parsing rules by yacc
# ------------------------------------
precedence = (
    )
names = {}

def p_body(p):
    '''body : statement'''
    print '<body>' + p[1] + '</body>'

def p_state(p):
    '''statement : expression
            | statement expression
            '''
    if (len(p) == 2):
        p[0] = p[1]
    elif (len(p) == 3):
        p[0] = str(p[1]) + str(p[2])

                     
def p_exp_cr(p):
    '''expression : H1 sentence CR
                | H2 sentence CR
                | H3 sentence CR  
                | sentence CR
                | sentence CR COMMENT CR
                | HR CR
                | HH CR
                | hr CR
                 '''
    if p[1] == '#':
        p[0] = '<h1>' + str(p[2]) + '</h1>'
    elif p[1] == '##':
        p[0] = '<h2>' + str(p[2]) + '</h2>'
    elif p[1] == '###': 
        p[0] = '<h3>' + str(p[2]) + '</h3>'
    elif p[1] == '===':
        p[0] = '<h1></h1>'
    elif p[1] == '---':
        p[0] = '<hr>'
    elif p[1] == '***':
        p[0] = '<hr>'
    else :
        p[0] = '<p>' + str(p[1]) + '</p>'

def p_hr_cr(p):
    ''' hr : EM EM
           | hr EM'''
    p[0] = str(p[1]) + str(p[2])
def p_sentence_ct(p):
    ''' expression : half CR 
                           '''
    p[0] = '<ul><li>' + str(p[1]) +'</li></ul>'

def p_sentence_cy(p):
    ''' expression : li CR  '''
    p[0] = '<ol><li>' + str(p[1]) +'</li></ol>'
def p_li_cr(p):
    ''' li : OL factor  
          | li factor'''          
    p[0] = str(p[1]) + ' ' + str(p[2])
def p_sentence_cr(p):
    ''' sentence : factor
               | half STRONG 
               | sentence sentence
               | half EM
               | half CODE
               | half HREF3
               | half HREF2
                                                        '''
    if (len(p) == 2):
        p[0] = p[1]
    elif p[2] == '**' or p[2] == '__':
        p[0] = '<strong>' + str(p[1]) + '</strong>'
    elif p[2] == '*' or p[2] == '_':
        p[0] = '<em>' + str(p[1]) + '</em>'
    elif p[2] == '`':
        p[0] = '<code>' + str(p[1]) + '</code>'
    elif p[2] == '\n':
        p[0] = '<ul><li>' + str(p[1]) +'</li><ul>'
    elif p[2] == '>':
        p[0] = '<a href="'+ str(p[1]) + '">' + str(p[1]) + '</a>'
    elif p[2] == ')':
        p[0] = str(p[1])
    else :
        p[0] = str(p[1]) + ' ' + str(p[2]) 


def p_half_cr(p):
    ''' half : STRONG factor
            | EM factor
            | CODE factor
            | HREF3 factor
            | half factor
            | name HREF2 factor
            | UL factor
             '''
    if p[1] == '**' or p[1] == '__':
        p[0] = p[2]
    elif p[1] == '*' or p[1] == '_' or p[1] == '+':
        p[0] = p[2]
    elif p[1] == '`' or p[1] == '<':
        p[0] = p[2]
    elif p[2] == '(':
        p[0] = '<a href="'+ str(p[3]) + '">' + str(p[1]) + '</a>'
    else :
        p[0] = str(p[1]) + ' ' + str(p[2]) 

def p_href_cr(p):
     ''' name : HREF1 factor HREF1  '''
     if p[1] == '[':
         p[0] = p[2]
      
#def p_comment_cr(p):
#     ''' comment : COMMENT '''
def p_factor_text(p):
    "factor : TEXT"
    p[0] = p[1]

def p_error(p):
    if p:
        print("error at '%s' line '%d'" % (p.value, p.lineno))
    else:
        print("error at EOF")

import ply.yacc as yacc
yacc.yacc()

if __name__ == '__main__':
    filename = 'test233.md'
    yacc.parse(open(filename).read())