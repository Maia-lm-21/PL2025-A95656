import ply.lex as lex

tokens = ('NUM', 'PLUS', 'MINUS', 'MUL', 'DIV', 'LPAREN', 'RPAREN')

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_MUL     = r'\*'
t_DIV     = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_NUM     = r'\d+'

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()