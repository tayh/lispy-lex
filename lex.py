import re
from typing import NamedTuple, Iterable


class Token(NamedTuple):
    kind: str
    value: str

def lex(code: str) -> Iterable[Token]:
    """
    Retorna sequência de objetos do tipo token correspondendo à análise léxica
    da string de código fornecida.
    """
    token_specification = [
        ('NUMBER', r'\+?\-?\d+(\.\d*)?([eE][+-]?\d+)?'),
        ('NAME', r"([^()\"\n \#\;]+)"),
        ('LPAR', r'\('),
        ('RPAR', r'\)'),
        ('BOOL', r'\#[t|f]'),
        ('CHAR', r'\#\\[\w]+|\d+'),
        ('STRING', r'\"[^"\\]*(\\[^\n\t\r\f][^"\\]*)*\"'),
        ('COMMENT', r'\;([^\n\r]+)'),
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'COMMENT':
            continue
        yield Token(kind, value)