import re
from typing import NamedTuple, Iterable


class Token(NamedTuple):
    kind: str
    value: str

def tokenize(chars: str) -> list:
    "Convert a string of characters into a list of tokens."
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()

def lex(code: str) -> Iterable[Token]:
    """
    Retorna sequência de objetos do tipo token correspondendo à análise léxica
    da string de código fornecida.
    """
    #keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    token_specification = [
        ('NAME', r"[a-zA-Z_][a-zA-Z_0-9]*"),
        ('LPAR', r'\('),
        ('RPAR', r'\)'),
        ('NUMBER', r'\+?\-?\d+(\.\d*)?([eE][+-]?\d+)?'),
        ('BOOL', r'\#[t|f]'),
        ('CHAR', r'\#\\[\w]+')
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        yield Token(kind, value)

# exemplos = [
#     r"#\a #\Backspace"
# ]

# for ex in exemplos:
#     print(ex.split())
#     for tok in lex(ex):
#         print('    ', tok)
#     print()