from analex import lexer

prox_simb = None

def parserError(simb):
    print("Erro sintático: token inesperado", simb)
    exit(1)

def rec_term(simb_type):
    global prox_simb
    if prox_simb.type == simb_type:
        val = prox_simb.value
        prox_simb = lexer.token()
        return val
    else:
        parserError(prox_simb)

def Factor():
    global prox_simb
    if prox_simb.type == 'NUM':
        val = int(rec_term('NUM'))
        return val
    elif prox_simb.type == 'LPAREN':
        rec_term('LPAREN')
        val = Expr()
        rec_term('RPAREN')
        return val
    else:
        parserError(prox_simb)

def Term_():
    global prox_simb
    if prox_simb and prox_simb.type == 'MUL':
        rec_term('MUL')
        val = Factor()
        return lambda acc: Term_()(acc * val)
    elif prox_simb and prox_simb.type == 'DIV':
        rec_term('DIV')
        val = Factor()
        return lambda acc: Term_()(acc // val)
    else:
        return lambda acc: acc

def Term():
    val = Factor()
    return Term_()(val)

def Expr_():
    global prox_simb
    if prox_simb and prox_simb.type == 'PLUS':
        rec_term('PLUS')
        val = Term()
        return lambda acc: Expr_()(acc + val)
    elif prox_simb and prox_simb.type == 'MINUS':
        rec_term('MINUS')
        val = Term()
        return lambda acc: Expr_()(acc - val)
    else:
        return lambda acc: acc

def Expr():
    val = Term()
    return Expr_()(val)

def rec_Parser(data):
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token()
    result = Expr()
    if prox_simb is not None:
        parserError(prox_simb)
    return result