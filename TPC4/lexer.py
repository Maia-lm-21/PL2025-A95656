import ply.lex as lex

# Lista de literais
literals = ['.', '{', '}', 'a']
# Lista de tokens
tokens = [
    'VAR',
    'PREFIX',
    'STRING',
    'LANGTAG',
    'NUMBER',
    'SELECT',
    'WHERE',
    'LIMIT',
]

t_ignore = ' \t'

def t_VAR(t):
    r'\?[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_PREFIX(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*:[a-zA-Z0-9_]+'
    return t

def t_LANGTAG(t):
    r'@[a-zA-Z\-]+'
    return t

def t_STRING(t):
    r'"[^"]*"'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_SELECT(t):
    r'(?i)SELECT'
    return t

def t_WHERE(t):
    r'(?i)WHERE'
    return t

def t_LIMIT(t):
    r'(?i)LIMIT'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'\#.*'
    pass  # Ignora comentários

def t_error(t):
    print(f"Caracter ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Criação do analisador léxico
lexer = lex.lex()

import sys

data = sys.stdin.read()
lexer.input(data)

print("Tokens reconhecidos:")
for tok in lexer:
    print(tok)
