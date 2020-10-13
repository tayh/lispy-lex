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
    #keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    token_specification = [
        ('NAME', r"[a-zA-Z_][a-zA-Z_0-9]*"),
        ('LPAR', r'\('),
        ('RPAR', r'\)'),
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    print(tok_regex)
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        yield Token(kind, value)


# exemplos = [
#     "(max x y)"
# ]

# for ex in exemplos:
#     print(ex)
#     for tok in lex(ex):
#         print('    ', tok)
#     print()