# Projeto de Compilador vSL
**Processamento de Linguagens - LEI**

## 1. Introdução

Este projeto consiste na construção de um compilador para **Pascal Standard**. O compilador foi desenvolvido em Python utilizando a biblioteca `PLY` (Python Lex-Yacc) e cria código compatível com a máquina virtual fornecida **EWVM**.

---

## 2. Estrutura do Projeto

```bash
.
├── src/
│   ├── pascal_lex.py      # Analisador léxico
│   ├── pascal_sin.py      # Analisador sintático
│   ├── stack_generator.py # Gerador do código VM
│   └── tokenizer.py       # Ferramenta de debug dos tokens
├── tests/                 # Ficheiros de teste em Pascal (.pas)
├── outputs/               # Código VM gerado (.txt)
└── README.md              # Relatório
```

## 3. O Compilador

### 3.1 Gramática (Parser)

A gramática usada foi definida com recurso ao `PLY.yacc`, seguindo a notação BNF. A linguagem vSL aceita estruturas típicas como blocos `BEGIN...END`, ciclos `FOR` e `WHILE`, condicionais `IF`, declarações de variáveis, entre outras.

Exemplo de produções principais:

```bnf
program        → PROGRAM id ';' declarations block '.'
block          → BEGIN statements END terminator
declarations   → (VAR | CONST) declaration_list ';' | ε
declaration    → id_list ':' type
statements     → statement | statements statement
assignment     → id ASSIGN expression
expression     → term | expression opAdd term | num TWODOTS num
term           → factor | term opMul factor
factor         → const terminator | var terminator | '(' exprBool ')'
```
A gramática permite expressões compostas e booleanas, com operadores relacionais e aritméticos, e suporta chamadas de função, arrays e constantes.

### 3.2 Lexer (Tokens e Expressões Regulares)

O analisador léxico foi implementado com PLY.lex no ficheiro pascal_lex.py. Define tokens, literais e as respetivas expressões regulares para reconhecimento.

Literais:

```python
literals = ['+', '-', '*', '/', '%', '(', ')', ';', ':', '=', ',', '.', '<', '>', '[', ']', '{', '}']
```

Tokens definidos:
```python
tokens = [
    'id', 'num', 'text', 'comment',
    'MINOREQUALS', 'LARGEREQUALS', 'NOTEQUAL', 'TWODOTS', 'ASSIGN',
    'PROGRAM', 'BEGIN', 'END', 'VAR', 'INTEGER', 'REAL', 'STRING',
    'CHAR', 'BOOLEAN', 'ARRAY', 'IF', 'THEN', 'ELSE', 'WHILE', 'FOR', 'DO',
    'NOT', 'AND', 'OR', 'TRUE', 'FALSE', 'OF', 'TO', 'DOWNTO', 'DIV', 'MOD', 'CONST'
]
```
As palavras-chave são definidas individualmente. Exemplo:
```python
def t_PROGRAM(t): r'(?i)(program)'; return t
def t_BEGIN(t):   r'(?i)(begin)'; return t
# ... as restantes são iguais para cada palavra-chave
```
#### Expressões regulares dos terminais variáveis

**Identificadores:** começam por letra ou underscore, seguidos de letras, números ou ```_```.
```python
def t_id(t):
    r'[a-zA-Z_]\w*'
    return t
```
**Números:** inteiros ou reais com ponto decimal.
```python
def t_num(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t
```
**Textos(strings):** delimitados por aspas simples ```'texto'```, com suporte a escapes.
```python
def t_text(t):
    r'\'([^\\\n\']|\\.)*\''
    return t
```
**Comentários:** ```{...}```, ignorados no parsing.
```python
def t_comment(t):
    r'\{[^}]*\}'
    pass
```

#### Ignorar espaços
Estes caracteres não são tokens, mas aparecem no código-fonte. O lexer deve ignorá-los:

```python
t_ignore = ' \t'
```
#### Reconhecer novas linhas
O PLY precisa saber quando uma nova linha é encontrada para atualizar o número da linha:
```python
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
```

#### Tratamento de erros léxicos
Quando o lexer encontra um carácter ilegal, ele chama ``t_error``:
```python
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)
```
Esta função permite que a análise continue mesmo quando há erros e que estes possam ser vistos mais tarde.

## Conclusão

A implementação do compilador para a linguagem vSL permitiu aplicar os conceitos dados na unidade curricular de Processamento de Linguagens, percorrendo todas as fases de um compilador: análise léxica, análise sintática e geração de código.

A análise léxica foi realizada com expressões regulares usando `PLY.lex`, permitindo reconhecer tokens fixos e variáveis. A análise sintática, com `PLY.yacc`, seguiu a gramática por nós definida, capaz de reconhecer estruturas da linguagem, como blocos `BEGIN...END`, ciclos `FOR` e expressões booleanas. A geração de código produziu instruções compatíveis com a máquina virtual EWWM, ferramenta que usamos para a execução real dos programas compilados.

Este trabalho permitiu que, de uma maneira simples e a um a uma amplitude reduzida, pudessemos aplicar de forma prática os conhecimentos teóricos adquiridos na UC. A ligação entre teoria (autómatos, gramáticas, parsers) e prática (tokens, AST, código VM) permitiu exclarecer o que acontece entre alinguagem de programação de alto nível e linguagem assembly.
